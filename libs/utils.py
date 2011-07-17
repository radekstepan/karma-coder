#!/usr/bin/python
# -*- coding: utf -*-

# time & date
import datetime
import time

def slugify(value):
    import unicodedata, re

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)

def timestamp_ago(years=None, months=None, days=None):
    return int(time.mktime((datetime.datetime.now() + datetime.timedelta(years=years, months=months, days=days)).timetuple()))