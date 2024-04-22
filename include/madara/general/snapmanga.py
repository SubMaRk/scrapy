# CONFIG FILE FOR SNAP-MANGA.COM

CONFIGURATIONS = {
    "snap-manga.com": {
        "getsection": "div.site-content",
        "gettitle": "div.post-title h1",
        "gettype": "div.summary-heading h5:contains('Type')",
        "getgenre": "div.summary-heading h5:contains('Artist(s)')",
        "getstatus": "div.summary-heading h5:contains('Status')",
        "getchapterlist": "ul.main",
        "getcover": "div.summary_image a img",
        "getchaptertitle": "h1.chapter-heading",
        "readdiv": "div.reading-content",
        "delaylist": False,
        "readjson": False,
        "readencrypt": False
    }
}