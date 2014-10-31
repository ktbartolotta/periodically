from flask import Flask, render_template, request
import periodic


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_page():

    if request.method == "GET":
        return render_template("base.html")
    else:
        word = request.form['word_entry']
        words = periodic.get_periodics(word)
        return render_template("periodic.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)
