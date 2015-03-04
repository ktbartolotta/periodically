from flask import Flask, render_template, jsonify
import periodic


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_page():

    return render_template('index.html')


@app.route("/periodic/<word>")
def get_word(word):

    return jsonify({'periodics': periodic.get_periodics(word)})


if __name__ == "__main__":
    app.run(debug=True)
