import sys, time, stomp

SERVER = 'gridmsg001.cern.ch'
PORT = 6163
USERNAME = ''
PASSWD = ''

from Ganga.Utility.logging import getLogger
log = getLogger('MSGErrorLog')

# Simply log any incoming messages
class LoggerListener(object):
    def __init__(self):
        self.logger = getLogger( '~/MSGLoggerListener')
        self.f = file( 'Logger.log','w')
        self.streaming = {}
        
    def on_error(self, headers, message):
        self.logger.debug('received an error %s' % message)
        
    def on_disconnected(self):
        self.f.close()

    def on_message(self, headers, message):
        self.logger.debug('received a message %s' % message)
#========  IF  message were a dictionary   ==================================== 
#        message = {'2145': 'begin'})
#        r = message.split(':') #["{'2145'", " 'begin'}"]
#        id = r[-2][2:-1]
#        value = r[-1][2:-1]

        r = message.split(',')
        id = r[-2]
        value = r[-1]
        self.f.write('id is: ' + id)
        self.f.write('value is: '+value)
        if id not in self.streaming:
            """First order to start streaming"""
            self.streaming[id] = 'begin'
        elif value == 'begin':               
            """The id already exists in the dictionary and its value means begin streaming"""                          
            self.streaming[id] = 'begin'
        else :
            self.streaming[id] = 'stop'

        self.f.write(message)
        self.f.write(str(self.streaming))
        self.f.flush()



def createPublisher(T):
    # generic connection thread class; bring up connection if necessary
    class MSGAsynchPublisher(T):
        def __init__(self,name=None):
            T.__init__(self,name=name)
            from Queue import Queue
            self.msg_q = Queue()
            self.connection = stomp.Connection([(SERVER, PORT)], USERNAME, PASSWD)
            self.listener = LoggerListener()
            self.connection.add_listener(self.listener)
            self.__should_stop_flag = False

        def run(self):
            while not self.should_stop():
                while not self.msg_q.empty():
                    if not self.connection.is_connected():
                        self.connection.start()
                        self.connection.connect()
                    m = self.msg_q.get()
                    self.__send(m)
                time.sleep(0.3)
            self.connection.disconnect()

        def send(self, (dst, msg)):
            msg['_publisher_t'] = time.time()
            log.debug('Queueing message %s' % msg)
            self.msg_q.put((dst, msg))

        def __send(self, (dst, msg)):
            log.debug('Sending message %s' % msg)
            self.connection.send(destination=dst, message=repr(msg))

        def should_stop(self):
            return self.__should_stop_flag

        def stop(self):
            self.__should_stop_flag = True
    p = MSGAsynchPublisher(T)
    p.setDaemon(True)
    return p
    

# for testing purposes
if __name__ == '__main__':
    p = MSGAsynchPublisher()
    p.send(('/topic/lostman-test/status', 'Hello World 1!'))
    p.send(('/topic/lostman-test/status', 'Hello World 2!'))
    from threading import Thread
    t = Thread(target=p.run)
    t.start()