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

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

score = 0
letters = {
    'a': ['img/a1.png','img/a2.png'], #AMC Theatres,Samsung
    'b': ['img/b1.png'],
    'c': ['img/c1.png'],
    'd': ['img/d1.png'], #Disney
    'e': ['img/e1.png'],
    'f': ['img/f1.png'], #Facebook
    'g': ['img/g1.png'], #General Mills
    'h': ['img/h1.png'], #Yahoo
    'i': ['img/i1.png'],
    'j': ['img/j1.png'],
    'k': ['img/k1.png'],
    'l': ['img/l1.png'],
    'm': ['img/m1.png'], #Motorola
    'n': ['img/n1.png'],
    'o': ['img/o1.png'], #Google
    'p': ['img/p1.png'],
    'q': ['img/q1.png'],
    'r': ['img/r1.png'],
    's': ['img/s1.png'],
    't': ['img/t1.png'],
    'u': ['img/u1.png','img/u2.png'], #United Airlines, Hulu
    'v': ['img/v1.png'],
    'w': ['img/w1.png'],
    'x': ['img/x1.png'], #Exon
    'y': ['img/y1.png'],
    'z': ['img/z1.png'],

}
words = ['ananya', 'calla', 'carrot', 'easter', 'fairy', 'fish', 'hello', 'macbook', 'rabbit', 'santa', 'world']

def hi():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #'b': ['img/b1.png'],
    for letter in alphabet:
        print '\'' + letter + '\': [\'img/' + letter + '1.png\'],'

class PlayHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        currentword = random.choice(words)
        letterimages = ''
        for letter in currentword:
            letterimages = letterimages + '<img height=100 src="' + random.choice(letters[letter]) + '" />'
        template_values['word'] = letterimages
        template_values['currentword'] = currentword
        template_values['currentscore'] = str(score)

        template = jinja_environment.get_template('views/play.html')
        self.response.out.write(template.render(template_values))

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        answer1 = self.request.get('answer1')
        template_values['answer1'] = answer1
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
