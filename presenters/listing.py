#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Module
from flask import render_template, request, redirect
from flask.helpers import url_for

# models
from models.tags import Tags

listing = Module(__name__)

@listing.route('/')
def index():
    tags = Tags()

    return render_template('listing/index.html', **locals())

@listing.route('/new', methods=["GET", "POST"])
def new():
    if request.method == "POST":
        messages = []
        # validate form
        if 'title' in request.form and request.form['title']: title = request.form['title']
        else: messages.append({"category":"warning", "text":"Missing job title"})
        if 'description' in request.form and request.form['description']: description = request.form['description']
        else: messages.append({"category":"warning", "text":"Missing job description"})
        if 'tags' in request.form and request.form['tags']: tags = request.form['tags']
        else: messages.append({"category":"warning", "text":"Missing job tags"})
        if 'location' in request.form and request.form['location']: location = request.form['location']
        else: messages.append({"category":"warning", "text":"Missing job location"})
        if 'email' in request.form and request.form['email']: location = request.form['email']
        else: messages.append({"category":"warning", "text":"Missing your e-mail address"})
        if 'expiry' in request.form and request.form['expiry']: expiry = request.form['expiry']
        else: messages.append({"category":"warning", "text":"You need to set an expiry period"})

        if not messages:
            # GET after POST
            return redirect(url_for('new'))
    return render_template('listing/new.html', **locals())