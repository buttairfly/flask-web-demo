import os
import signal
import threading
import webbrowser

from connexion import FlaskApp
from flask import render_template
from measurements import read_all

app = FlaskApp(__name__)
app.add_api("swagger.yml")


@app.route("/")
def index():
    return render_template("index.html.j2")


@app.route("/measurements")
def measurements():
    return render_template("index.html.j2", measurements=read_all())


def exit():
    os.kill(os.getpid(), signal.SIGINT)
    return "Shutdown"


def ui():
    pass


def openapi():
    pass


def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:3000")


def main():
    # delay browser opening
    t = threading.Timer(1, open_browser)
    t.start()
    # start webapp
    app.run(port=3000)
    # cancel browser starting when aborted...
    t.cancel()


if __name__ == "__main__":
    main()
