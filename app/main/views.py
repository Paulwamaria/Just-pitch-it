from flask import render_template, request,redirect_url,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment
from db, import photos,db
import dateTime

@main.route('/')
def index():
    title = "Welcome to just pitch it"

    business_pitches = picth.get_pitches('business')
    screenplay_pitches = picth.get_pitches('screenplay')
    project_pitches = picth.get_pitches('project')
    return render_template('index.html',title = title,business=business,screenplay = screenplay)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))