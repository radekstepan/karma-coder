#!/usr/bin/python
# -*- coding: utf -*-

import os
import yaml

class Tags():

    tags = []

    def __init__(self):
        if not self.tags:
            # load
            f = open(os.path.join('models/tags.yaml'))
            tags = yaml.load(f)
            f.close()

            # split
            tags = tags.split()

            # sort
            tags.sort()

            # dictize
            temp = {}
            for tag in tags:
                letter = tag[0]
                if letter not in temp:
                    temp[letter] = []
                temp[letter].append(tag)

            # listize
            for key, value in temp.iteritems():
                kv = [key, value]
                self.tags.append(kv)