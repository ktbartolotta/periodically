from flask import Flask, render_template, jsonify
import periodic


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_page():

    return render_template('index.html')


@app.route("/periodic/<word>")
def get_word(word):

    periodics = periodic.get_periodics(word)
    if len(periodics) > 0:
        return jsonify({'periodics': periodics})
    else:
        return jsonify({
            'no_periodics': {
                'suggestions': ['jim', 'bob', 'amy']
            }
        })


if __name__ == "__main__":
    app.run(debug=True)
