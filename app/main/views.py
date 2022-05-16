from flask import render_template, redirect, request, url_for, abort, flash
from . import main
from flask_login import login_required,current_user
from ..email import mail_message
from ..models import *
from . import main
from .. import db,photos
from .forms import *
from app.request import get_quote

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
    quote = get_quote()
    blogs = Blog.query.all()
    return render_template('blogs.html', blogs = blogs, quote=quote)

@main.route('/new_blog', methods = ['POST','GET'])
@login_required
def new_blog():
    subscribers = User.query.all()
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        blog = form.blog.data
        user_id = current_user._get_current_object().id
        
        new_blog_object = Blog(blog=blog,user_id=user_id,title=title,description=description)
        new_blog_object.save_blog()

        for subscriber in subscribers:
            mail_message("New Blog Post","email/blog_notification",subscriber.email,blog=blog)
        return redirect(url_for('main.blogs'))
        flash('You Posted a new Blog')

        
    return render_template('new_blog.html', form = form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_comment()

        return redirect(url_for('.blogs', blog_id = blog_id))

    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))


@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.filter_by(user=user).order_by(Blog.posted.desc()).paginate(page = page, per_page = 4)
    return render_template('userposts.html',blogs=blogs,user = user)

@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.description = form.description.data
        blog.blog = form.blog.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('main.blogs',id = blog.id)) 
    if request.method == 'GET':
        form.title.data = blog.title
        form.description.data = blog.description
        form.blog.data = blog.blog
    return render_template('new_blog.html', form = form)