from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    keyword = ""
    results = []

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()

        # Demo data (baad me real CPPP data se replace karenge)
        if keyword:
            results = [
                {
                    "title": f"Tender for {keyword}",
                    "department": "CPPP",
                    "winner": "Demo Company Ltd"
                },
                {
                    "title": f"Supply of {keyword}",
                    "department": "Railways",
                    "winner": "ABC Industries"
                }
            ]

    return render_template(
        "index.html",
        keyword=keyword,
        results=results
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
