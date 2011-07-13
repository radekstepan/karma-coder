#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Flask

# imports
import libs.utils as utils

app = None

def create_app(database):
    global app

    # create our little application :)
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(__name__)
    app.secret_key = '^]CUCqFL6;wVz-w4%#ZYKTIB]kWT+3rfAq@_}(p;r%Mjq6umt9\>8-.){.u!uA*'

    # db import
    from libs.db import init_connection

    # db setup
    init_connection(database)

    # presenters
    from presenters.listing import listing
    from presenters.doc import doc

    # register modules
    app.register_module(listing)
    app.register_module(doc)

    # template filters
    @app.template_filter('test_format')
    def test_format(input):
        return input[::-1]

    return app

if __name__ == '__main__':
    app = create_app(database='karmacoder')
    app.run(port=5006)
