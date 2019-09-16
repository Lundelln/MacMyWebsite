
from flask import Flask, render_template, flash, redirect, url_for

from . import content_management

TOPIC_DICT = content_management.Content()

#from content_management import Content
#TOPIC_DICT = Content()

app = Flask(__name__)

app.secret_key = 'erhehwth532r23r'


@app.route('/')
def homepage():
	try:
		return render_template("main.html")
	except Exception as e:
		return(str(e))

@app.route('/coding/')
def coding():
	try:
		return render_template("coding.html", TOPIC_DICT = TOPIC_DICT)
	except Exception as e:
		return(str(e))


@app.route('/dashboard/')
def dashboard():
	try:
		return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)
	except Exception as e:
		return str(e)

@app.errorhandler(404)
def page_not_found(e):
	try:
		return render_template("404.html", error=e)
	except Exception as e:
		return(str(e))


if __name__ == "__main__":
    app.run()
