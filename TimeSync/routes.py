from flask import render_template, url_for, flash, redirect, request
from timesync import app, db, bcrypt
from timesync.forms import RegistrationForm, LoginForm
from timesync.models import User, Todo
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/home")
def home():
    todo_list = Todo.query.filter(Todo.user_id == current_user.id).all()
    print("current user", current_user.id)
    return render_template('home.html', todo_list=todo_list)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('landing'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')



### TASK ADDING STUFF ###
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    description = request.form.get("description")
    start_time = request.form.get("start_time")
    end_time = request.form.get("end_time")
    user_id = current_user.id

    new_todo = Todo(title=title, description=description, start_time=start_time, end_time=end_time, complete=False, user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))