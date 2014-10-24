from flask import Flask, render_template, request
import periodic


app = Flask(__name__)


@app.route("/")
def index_page():

    return render_template("base.html")


@app.route("/add", methods=["POST"])
def periodic_page():

    word = request.form['word_entry']
    words = periodic.get_periodics(word)
    return render_template("periodic.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)
