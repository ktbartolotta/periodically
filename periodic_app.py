from flask import Flask, render_template
import periodic


app = Flask(__name__)


@app.route('/')
@app.route('/<word>')
def hello_world(word=""):

    words = periodic.get_periodics(word)
    return render_template("periodic.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)
