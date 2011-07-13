#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Module
from flask import render_template, request, redirect
from flask.helpers import url_for

# models
from models.users import Users

listing = Module(__name__)

@listing.route('/')
def index():
    return render_template('listing/index.html', **locals())

@listing.route('/new')
def new():
    return render_template('listing/new.html', **locals())