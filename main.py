from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Tender Hunter AI</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding:40px;">
        <h1>🚀 Tender Hunter AI</h1>
        <p>Deployment Successful</p>
        <hr>
        <h3>Features (Coming Soon)</h3>
        <ul style="display:inline-block;text-align:left;">
            <li>🔍 Search CPPP Tenders</li>
            <li>🏆 Tender Winners</li>
            <li>📈 Listed Company Alerts</li>
            <li>🤖 AI Tender Analysis</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
