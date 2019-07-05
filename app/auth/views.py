from . import auth
from .. import db
from ..models import User
from .forms import RegistrationForm,LoginForm
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,login_required, logout_user, current_user
