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
