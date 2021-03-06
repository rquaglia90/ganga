from __future__ import absolute_import

from GangaCore.testlib.GangaUnitTest import GangaUnitTest


class TestSavannah76973(GangaUnitTest):
    def test_Savannah76973(self):
        from GangaCore.GPI import Job, JobTemplate, JobError

        j = Job()
        t = JobTemplate(j)
        self.assertEqual(t.status, 'template')

        self.assertRaises(JobError, t.submit)
