from flask import render_template, redirect, url_for, abort, request
from ..models import User, Pitch, Comments, PitchCategory, Votes
from flask_login import login_required, current_user 


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