from turtle import title
from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = 'Not Found | Orinews'
    return render_template('fourOwfour.html', error_msg = error, title=title),404


