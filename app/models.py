from . import db 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#pitch categories
class PitchCategory(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = PitchCategory.query.all()
        return categories