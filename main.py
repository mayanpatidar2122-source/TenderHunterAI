from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    keyword = ""

    if request.method == "POST":
        keyword = request.form.get("keyword", "")

    return render_template("index.html", keyword=keyword)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
