from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
    "Dev":95,
    "Mohit":88,
    "Kavan":85,
    "Raj":92,
    "Gandu":10,
    }
    return render_template("index.html" , marks=marks)

app.run(debug=True)