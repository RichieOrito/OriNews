from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

@main.route('/articles/<source_id>')
def source(source_id):
    '''
    View articles page function that returns articles from the specified sources.
    '''
    
