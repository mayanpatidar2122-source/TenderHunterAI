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

    if keyword:
    url = f"https://etenders.gov.in/eprocure/app?page=FrontEndAdvancedSearch&searchType=active&tenderTitle={keyword}"

    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=20
        )

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        rows = soup.find_all("tr")

        for row in rows[:10]:
            text = row.get_text(" ", strip=True)

            if keyword.lower() in text.lower():
                results.append({
                    "title": text[:100],
                    "department": "CPPP",
                    "winner": "Available on portal"
                })

        if not results:
            results.append({
                "title": "No matching tenders found",
                "department": "-",
                "winner": "-"
            })

    except Exception as e:
        results.append({
            "title": "Error",
            "department": "System",
            "winner": str(e)
        })

    return render_template(
        "index.html",
        keyword=keyword,
        results=results
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
