from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'NEWS HIGHLIGHT'
    return render_template('index.html',message = message)

@app.route('/sources/<int:articles_id>')
def articles(articles_id):
	'''
	view articles page
	'''
	# articles = get_articles(id)
	# title = f'NH | {id}'

	return render_template('articles.html',id = articles_id)