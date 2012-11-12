from bottle import route, run, template, debug, request, redirect
import spell_check
@route('/')
def index():
	'''
	Show form to input spelling observation
	'''
	return template('index', corrections=[])

@route('/correct', method="post")
def correct():
	if request.POST.get('observation','').strip():
		obs = request.POST.get('observation', '').strip()
		#return spell_check.Spelling(obs).correct()
		return template('index',corrections = spell_check.Spelling(obs).correct())
	else:
		redirect('/')
debug(True)
run(reloader=True)