Levenshtein Edit Distance Based Spell Checker
=============================================

A simple module that takes in a word and corrects a spelling mistake, if any, by linearly matching it to a predifined corpus

for gui version (depends on the bottle.py micro-framework):
<pre>
python spell_check_gui.py
</pre>
and visit http://127.0.0.1:8080/ in your browser

for api :
<pre>
from spell_check import Spelling
observation = Spelling("acress")
correct     = observation.correct() # will return a string or list
</pre>
