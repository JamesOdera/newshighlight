from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_articles,search_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('category')
    print(sources)
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = 'NEWS HIGHLIGHT'

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html', title = title,sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources=entertainment_sources)
    
    

@app.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)



##############
@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)