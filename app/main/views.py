from flask import render_template, redirect, request, url_for, abort, flash
from . import main
from flask_login import login_required,current_user
from ..email import mail_message
from ..models import *
from . import main
from .. import db,photos
from .forms import *

#views
@main.route('/')
def index():
  '''
    View root page function that returns the index page and its data
  '''

  return render_template('index.html')

@main.route('/blogs')
def blogs():
    '''
    View categories page function that returns the pitch details page
    '''
    blogs = Blog.query.all()
    return render_template('blogs.html', blogs = blogs)

@main.route('/new_blog', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        blog = form.blog.data
        user_id = current_user
        
        new_blog_object = Blog(blog=blog,user_id=current_user._get_current_object().id)
        new_blog_object.save_blog()
        return redirect(url_for('main.blogs'))
        
    return render_template('new_blog.html', form = form)

