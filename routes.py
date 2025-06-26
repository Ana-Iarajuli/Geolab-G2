from ext import app, db, login_manager
from flask import render_template, redirect, flash
from forms import RegisterForm, MovieForm, LoginForm
from os import path
from models import Movie, User
from flask_login import login_user, logout_user, login_required



@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        # print(user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("წარმატებით გაიარე ავტორიზაცია")
            return redirect("/")
        else:
            flash("სახელი ან პაროლი არასწორია. სცადეთ თავიდან")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    # flash("logout was successful")
    return redirect("/")


@app.route("/about")
def about():
    return "About Page"

@app.route("/register", methods=["get", "post"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()

        return redirect("/")

    return render_template("register.html", form=form)


@app.route("/movie/<int:movie_id>")
def view_movie(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template("movie.html", movie=movie)


@app.route("/add_movie", methods=["GET", "POST"])
@login_required
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(name=form.name.data, release_year=form.release_year.data)

        image = form.image.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)
        new_movie.image = image.filename

        new_movie.create()

        return redirect("/")

    return render_template("add_movie.html", form=form)


@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    print(movie.name)

    form = MovieForm(name=movie.name, release_year=movie.release_year, image=movie.image)
    if form.validate_on_submit():
        movie.name = form.name.data
        movie.release_year = form.release_year.data
        movie.image = form.image.data
        movie.save()

        return redirect("/")

    return render_template("edit_movie.html", form=form)



@app.route("/delete_movie/<int:movie_id>")
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    movie.delete()

    return redirect("/")