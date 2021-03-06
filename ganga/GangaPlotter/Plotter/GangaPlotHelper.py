#!/usr/bin/env python

import math

def floatRgb(mag, cmin, cmax):
    """
    These functions, when given a magnitude mag between cmin and cmax, return
    a colour tuple (red, green, blue). Light blue is cold (low magnitude)
    and yellow is hot (high magnitude).

    Return a tuple of floats between 0 and 1 for the red, green and
    blue amplitudes.
    """
    try:
        # normalize to [0,1]
        x = float(mag-cmin)/float(cmax-cmin)
    except:
        # cmax = cmin
        x = 0.5
    blue = min((max((4*(0.75-x), 0.)), 1.))
    red  = min((max((4*(x-0.25), 0.)), 1.))
    green= min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return (red, green, blue)

def rgb(mag, cmin, cmax):
    """
    Return a tuple of integers to be used in AWT/Java plots.
    """
    red, green, blue = floatRgb(mag, cmin, cmax)
    return (int(red*255), int(green*255), int(blue*255))

# function for mapping tld to country name
def tld_country(tld):
    tld_countries = {
       "af": "Afghanistan",
       "al": "Albania",
       "dz": "Algeria",
       "as": "American Samoa",
       "ad": "Andorra",
       "ao": "Angola",
       "ai": "Anguilla",
       "aq": "Antarctica",
       "ag": "Antigua and Barbuda",
       "ar": "Argentina",
       "am": "Armenia",
       "aw": "Aruba",
       "au": "Australia",
       "at": "Austria",
       "az": "Azerbaijan",
       "bs": "Bahamas",
       "bh": "Bahrain",
       "bd": "Bangladesh",
       "bb": "Barbados",
       "by": "Belarus",
       "be": "Belgium",
       "bz": "Belize",
       "bj": "Benin",
       "bm": "Bermuda",
       "bt": "Bhutan",
       "bo": "Bolivia",
       "ba": "Bosnia and Herzegowina",
       "bw": "Botswana",
       "bv": "Bouvet Island",
       "br": "Brazil",
       "io": "British Indian Ocean Territory",
       "bn": "Brunei Darussalam",
       "bg": "Bulgaria",
       "bf": "Burkina Faso",
       "bi": "Burundi",
       "kh": "Cambodia",
       "cm": "Cameroon",
       "ca": "Canada",
       "cv": "Cape Verde",
       "ky": "Cayman Islands",
       "cf": "Central African Republic",
       "td": "Chad",
       "cl": "Chile",
       "cn": "China",
       "cx": "Christmas Island",
       "cc": "Cocos (Keeling) Islands",
       "co": "Colombia",
       "km": "Comoros",
       "cg": "Congo",
       "cd": "Congo, The Democratic Republic of the",
       "ck": "Cook Islands",
       "cr": "Costa Rica",
       "ci": "Cote D'Ivoire",
       "hr": "Croatia",
       "cu": "Cuba",
       "cy": "Cyprus",
       "cz": "Czech Republic",
       "dk": "Denmark",
       "dj": "Djibouti",
       "dm": "Dominica",
       "do": "Dominican Republic",
       "tp": "East Timor",
       "ec": "Ecuador",
       "eg": "Egypt",
       "sv": "El Salvador",
       "gq": "Equatorial Guinea",
       "er": "Eritrea",
       "ee": "Estonia",
       "et": "Ethiopia",
       "fk": "Falkland Islands (Malvinas)",
       "fo": "Faroe Islands",
       "fj": "Fiji",
       "fi": "Finland",
       "fr": "France",
       "gf": "French Guiana",
       "pf": "French Polynesia",
       "tf": "French Southern Territories",
       "ga": "Gabon",
       "gm": "Gambia",
       "ge": "Georgia",
       "de": "Germany",
       "gh": "Ghana",
       "gi": "Gibraltar",
       "gr": "Greece",
       "gl": "Greenland",
       "gd": "Grenada",
       "gp": "Guadeloupe",
       "gu": "Guam",
       "gt": "Guatemala",
       "gn": "Guinea",
       "gw": "Guinea-Bissau",
       "gy": "Guyana",
       "ht": "Haiti",
       "hm": "Heard Island and Mcdonald Islands",
       "va": "Holy See (Vatican City State)",
       "hn": "Honduras",
       "hk": "Hong Kong",
       "hu": "Hungary",
       "is": "Iceland",
       "in": "India",
       "id": "Indonesia",
       "ir": "Iran, Islamic Republic of",
       "iq": "Iraq",
       "ie": "Ireland",
       "il": "Israel",
       "it": "Italy",
       "jm": "Jamaica",
       "jp": "Japan",
       "jo": "Jordan",
       "kz": "Kazakstan",
       "ke": "Kenya",
       "ki": "Kiribati",
       "kp": "Korea, Democratic People's Republic of",
       "kr": "Korea, Republic of",
       "kw": "Kuwait",
       "kg": "Kyrgyzstan",
       "la": "Lao People's Democratic Republic",
       "lv": "Latvia",
       "lb": "Lebanon",
       "ls": "Lesotho",
       "lr": "Liberia",
       "ly": "Libyan Arab Jamahiriya",
       "li": "Liechtenstein",
       "lt": "Lithuania",
       "lu": "Luxembourg",
       "mo": "Macau",
       "mk": "Macedonia",
       "mg": "Madagascar",
       "mw": "Malawi",
       "my": "Malaysia",
       "mv": "Maldives",
       "ml": "Mali",
       "mt": "Malta",
       "mh": "Marshall Islands",
       "mq": "Martinique",
       "mr": "Mauritania",
       "mu": "Mauritius",
       "yt": "Mayotte",
       "mx": "Mexico",
       "fm": "Micronesia",
       "md": "Moldova",
       "mc": "Monaco",
       "mn": "Mongolia",
       "ms": "Montserrat",
       "ma": "Morocco",
       "mz": "Mozambique",
       "mm": "Myanmar",
       "na": "Namibia",
       "nr": "Nauru",
       "np": "Nepal",
       "nl": "Netherlands",
       "an": "Netherlands Antilles",
       "nc": "New Caledonia",
       "nz": "New Zealand",
       "ni": "Nicaragua",
       "ne": "Niger",
       "ng": "Nigeria",
       "nu": "Niue",
       "nf": "Norfolk Island",
       "mp": "Northern Mariana Islands",
       "no": "Norway",
       "om": "Oman",
       "pk": "Pakistan",
       "pw": "Palau",
       "ps": "Palestinian Territory, Occupied",
       "pa": "Panama",
       "pg": "Papua New Guinea",
       "py": "Paraguay",
       "pe": "Peru",
       "ph": "Philippines",
       "pn": "Pitcairn",
       "pl": "Poland",
       "pt": "Portugal",
       "pr": "Puerto Rico",
       "qa": "Qatar",
       "re": "Reunion",
       "ro": "Romania",
       "ru": "Russian Federation",
       "rw": "Rwanda",
       "sh": "Saint Helena",
       "kn": "Saint Kitts and Nevis",
       "lc": "Saint Lucia",
       "pm": "Saint Pierre and Miquelon",
       "vc": "Saint Vincent and the Grenadines",
       "ws": "Samoa",
       "sm": "San Marino",
       "st": "Sao Tome and Principe",
       "sa": "Saudi Arabia",
       "sn": "Senegal",
       "sc": "Seychelles",
       "sl": "Sierra Leone",
       "sg": "Singapore",
       "sk": "Slovakia",
       "si": "Slovenia",
       "sb": "Solomon Islands",
       "so": "Somalia",
       "za": "South Africa",
       "gs": "South Georgia and the South Sandwich Islands",
       "es": "Spain",
       "lk": "Sri Lanka",
       "sd": "Sudan",
       "sr": "Suriname",
       "sj": "Svalbard and Jan Mayen",
       "sz": "Swaziland",
       "se": "Sweden",
       "ch": "Switzerland",
       "sy": "Syrian Arab Republic",
       "tw": "Taiwan",
       "tj": "Tajikistan",
       "tz": "Tanzania, United Republic of",
       "th": "Thailand",
       "tg": "Togo",
       "tk": "Tokelau",
       "to": "Tonga",
       "tt": "Trinidad and Tobago",
       "tn": "Tunisia",
       "tr": "Turkey",
       "tm": "Turkmenistan",
       "tc": "Turks and Caicos Islands",
       "tv": "Tuvalu",
       "ug": "Uganda",
       "ua": "Ukraine",
       "ae": "United Arab Emirates",
       "gb": "United Kingdom",
       "uk": "United Kingdom",
       "us": "United States",
       "um": "United States Minor Outlying Islands",
       "uy": "Uruguay",
       "uz": "Uzbekistan",
       "vu": "Vanuatu",
       "ve": "Venezuela",
       "vn": "Viet Nam",
       "vg": "Virgin Islands, British",
       "vi": "Virgin Islands, U.S.",
       "wf": "Wallis and Futuna",
       "eh": "Western Sahara",
       "ye": "Yemen",
       "yu": "Yugoslavia",
       "zm": "Zambia",
       "zw": "Zimbabwe",
    }
 
    country = None
    if tld in tld_countries:
        country = tld_countries[tld]
    return country
