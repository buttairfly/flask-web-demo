import webbrowser
from flask import Flask, render_template, request
from connexion import FlaskApp
import os, signal

app = FlaskApp(__name__)
app.add_api("swagger.yml")

@app.route("/")
def index():
    return render_template('index.html.j2')

def exit():
    os.kill(os.getpid(),signal.SIGINT)
    return ("Shutdown")

def ui():
    pass

def openapi():
    pass

if __name__ == "__main__":
    webbrowser.open_new_tab('http://127.0.0.1:3000/')
    app.run(port=3000)
