from flask import render_template, redirect, url_for, abort, request



@main.route ('/')
def index():
    """
    Function that returns index page and data
    """
    category = PitchCategory.get_categories()
    return render_template('index.html', categories = category)