from flask import Flask, render_template
# from waitress import serve

app = Flask(__name__)

# @app.route('/')
# @app.route('/index') 
# def home():
# 	return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
	return render_template("login.html")

@app.route('/<user>')
def user(user):
	return f'<h1>{user}</h1>'

app.debug = True
app.run(host='0.0.0.0', port=8000)