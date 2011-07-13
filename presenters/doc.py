#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Module
from flask import render_template, request, redirect
from flask.helpers import url_for

# models
from models.users import Users

doc = Module(__name__)

@doc.route('/policy')
def policy():
    return render_template('doc/policy.html', **locals())

@doc.route('/about')
def about():
    return render_template('doc/about.html', **locals())