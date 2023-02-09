from flask import Flask
app = Flask('Football Betting for You')
app.route("/")
def home():
    return