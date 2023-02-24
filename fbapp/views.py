from flask import Flask, render_template, request

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
app.app_context().push() # Ne pas oublier pour le terminal SQLAlchemy


@app.route('/')
#@app.route('/index/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()