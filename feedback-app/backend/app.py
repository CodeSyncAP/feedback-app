from flask import Flask, render_template, request

app = Flask(__name__)
feedbacks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        comment = request.form["comment"]
        feedbacks.append({"name": name, "comment": comment})
    return render_template("index.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
