from flask import render_template, redirect, url_for, abort, request
from ..models import User, Pitch, Comments, PitchCategory, Votes
from flask_login import login_required, current_user 
from .forms import PitchForm, CommentForm, UpdateProfile, CategoryForm
from .. import db, photos


@main.route ('/')
def index():
    """
    Function that returns index page and data
    """
    category = PitchCategory.get_categories()
    return render_template('index.html', categories = category)

@main.route('/category/new-pitch/<int:id>', methods= ['GET', 'POST'])
@login_required
def new_pitch(id):
    """
    Function to fetch data 
    """
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)
        
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_pitch = Pitch(pitch = pitch, category_id = category.id, user_id= current_user.id)
        new_pitch.save_pitch()
        

        return redirect(url_for('.category', id= category.id))
    
    return render_template('new_pitch.html', pitch_form = form, category = category)    

@main.route ('/categories/<int:id>')
@login_required
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort (404)
        
    pitches = Pitch.get_pitches(id)
    
    return render_template ('category.html', pitches = pitches, category= category)


@main.route('/add/category', methods = ['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    
    if form.validate_on_submit():
        name = form.name.data
        new_category = PitchCategory(name=name)
        new_category.save_category()
        
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('.index'))
    title = 'New Category'   
    return render_template('post_comment.html', comment_form = form, title = title)    

@main.route('/view_pitch/<int:id>', methods = ['GET', 'POST'])
@login_required
def view_pitch(id):
    """
    Function that returns a single pitch with comments
    """
    print(id)
    pitches = Pitch.query.get(id)
    if pitches is None:
        abort(404)
           
    comment = Comments.get_comments(id)
    title = 'View Pitch'
    return render_template('view_pitch.html', pitches= pitches, comment = comment, category_= id, title= title)
