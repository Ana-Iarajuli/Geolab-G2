from ext import app

if __name__ == "__main__":
    from routes import home, register, login, edit_movie, view_movie, delete_movie, add_movie
    app.run(debug=True)

