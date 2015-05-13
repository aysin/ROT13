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
import cgi
import string
import cgitb


form ="""

<font size="3">ROT13 by Aysin Oruz</font>
<form method = "post">
	<br>
	<div alight = "left">
	<font size="15" color="Blue"><b>Enter a text!</b></font>
	<br>
	<textarea cols ="65" rows="20" name="text">%(fill)s</textarea>
	<br><br>
	<input type="Submit" value="Submit">
	</div>
</form>


"""

def escape_html(s):
    return cgi.escape(s, quote = True)

def rot_13(s):
    abc = string.ascii_lowercase
    abc_13 = abc[13:] + abc[:13]

    rot = '' 
    for c in s:
        if c in string.ascii_letters:
            rot += abc_13[abc.index(c.lower())]
        else:
            rot += c

    for i in range(0, len(s)):
        if s[i] in string.ascii_uppercase:
            rot = rot.replace(rot[i], rot[i].upper())

    return rot

class MainHandler(webapp2.RequestHandler):

    def write_form(self, fill = ""):
        self.response.out.write(form % {"fill" : escape_html(fill)})

    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get("text")
        convert = rot_13(user_input)

        if convert:
            self.write_form(convert)


app = webapp2.WSGIApplication([
    ('/', MainHandler)], debug=True)











