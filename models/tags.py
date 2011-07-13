#!/usr/bin/python
# -*- coding: utf -*-

import os
import yaml

class Tags():

    tags = None

    def __init__(self):
        f = open(os.path.join('models/tags.yaml'))
        self.tags = yaml.load(f)
        f.close()