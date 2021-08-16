from flask import Flask
#add flask content
app = Flask(__name__)

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"