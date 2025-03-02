from flask import Flask, redirect, request

app = Flask(__name__)

KNOT_URL = "https://www.theknot.com/us/alex-holt-and-emma-eddy-jun-2025"
AMAZON_URL = "https://www.amazon.com/wedding/share/alexandemmaholt"
TARGET_URL = "https://www.target.com/gift-registry/gift/alexandemmaholt"

# Registry Redirects
@app.route("/amazon")
def redirect_amazon():
    return redirect(AMAZON_URL, code=302)  # 302 for temporary redirect

@app.route("/target")
def redirect_target():
    return redirect(TARGET_URL, code=302)  # 302 for temporary redirect

# Main Redirect
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_to_target():
    return redirect(KNOT_URL, code=302)  # 302 is a temporary redirect

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
