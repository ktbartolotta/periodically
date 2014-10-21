from flask import Flask, render_template
import periodic


app = Flask(__name__)


@app.route('/')
@app.route('/<word>')
def hello_world(word=""):

    words2 = [
        [
            {
                "name": "apple",
                "atomic_no": 1,
                "symbol": "Ap",
                "atomic_wt": 2.132
            },
            {
                "name": "banana",
                "atomic_no": 2,
                "symbol": "Bn",
                "atomic_wt": 4.324
            }
        ],
        [
            {
                "name": "Cactus",
                "atomic_no": 3,
                "symbol": "Ct",
                "atomic_wt": 6.567
            },
            {
                "name": "Dong",
                "atomic_no": 4,
                "symbol": "Dg",
                "atomic_wt": 8.236
            }
        ]
    ]

    words = periodic.get_periodics(word)
    return render_template("periodic.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)
