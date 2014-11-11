#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import logging
import urllib2
import os
import random
import data

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

score = 0
word = ''

class PlayHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        currentword = random.choice(data.words) #gets a random word from list of words
        letterimages = ''
        answerlist = []
        for letter in currentword:
            #adds image to list
            thisletter = random.choice(data.letters[letter])
            letterimages = letterimages + '<img height=100 src="' + thisletter + '" />'
            answerlist.append(data.dictionary[thisletter])
        template_values['answerlist'] = answerlist
        template_values['word'] = letterimages
        template_values['currentword'] = currentword
        global word
        word = currentword

        template_values['currentscore'] = str(score)

        template = jinja_environment.get_template('views/play.html')
        self.response.out.write(template.render(template_values))

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        answer1 = self.request.get('answer1')
        template_values['answer1'] = answer1
        if answer1.lower()==word:
            global score
            score = score+1
        template_values['currentscore'] = str(score) #THIS IS THE PROBLEM NOW. CAN'T ACCESS GLOBAL VARIABLE

        template = jinja_environment.get_template('views/check.html')
        self.response.out.write(template.render(template_values))
        #self.redirect('/')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', PlayHandler),('/submit', CheckHandler)
], debug=True)
