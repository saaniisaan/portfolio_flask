from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/fotografie")
def fotografie():
    return render_template("fotografie.html")


@app.route("/musik")
def musik():
    return render_template("musik.html")


if __name__ == "__main__":
    print("Flask Server wird gestartet...")
    app.run(debug=True)
