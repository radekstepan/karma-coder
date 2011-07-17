#!/usr/bin/python
# -*- coding: utf -*-

# db
from libs.db import Collection

class Jobs(Collection):

    table = 'jobs'

    def save(self, title, description, tags, location, email, expiry):

        # TODO: validate email

        # TODO: split tags

        # TODO: determine expiry from utils

        # TODO: throw on error

        dict = {'emo':'fdfd'}

        super(Jobs, self).save(dict)
        