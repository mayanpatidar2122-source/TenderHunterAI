from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    keyword = ""
    results = []

    if request.method == "POST":
        keyword = request.form.get("keyword", "")
results = []

url = f"https://etenders.gov.in/eprocure/app?page=FrontEndTenderSearch&searchType=all&keyword={keyword}"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    if response.status_code == 200:
        results.append({
            "title": "Connection successful",
            "department": "Government Portal",
            "winner": "Data fetch started"
        })
    else:
        results.append({
            "title": "Website responded with error",
            "department": str(response.status_code),
            "winner": "-"
        })

except Exception as e:
    results.append({
        "title": "Connection failed",
        "department": "Error",
        "winner": str(e)
    })



    return render_template(
        "index.html",
        keyword=keyword,
        results=results
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
