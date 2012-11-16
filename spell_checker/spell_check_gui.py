from bottle import route, run, template, debug, request, redirect
import spell_check
@route('/')
def index():
	'''
	Show form to input spelling observation
	'''
	return template('index', corrections=[], suggestions={})

@route('/correct', method="post")
def correct():
	if request.POST.get('observation','').strip():
		obs = request.POST.get('observation', '').strip()
		#return spell_check.Spelling(obs).correct()
		a = spell_check.Spelling(obs)
		return template('index',corrections = a.correct(), suggestions=a.edit_distances())
	else:
		redirect('/')
debug(True)
run(reloader=True)
