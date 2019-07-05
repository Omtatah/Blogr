from flask import render_template,redirect,url_for,request,abort,flash
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm,SubscribeForm
from .. import db,photos
from ..models import User,Blog,Comment,Subscriber
from flask_login import login_required,current_user
from .. import db,photos
import json