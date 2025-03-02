from flask import Flask, redirect, request

app = Flask(__name__)

TARGET_URL = "https://www.theknot.com/us/alex-holt-and-emma-eddy-jun-2025"  # Change this to the desired destination

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_to_target(path):
    return redirect(TARGET_URL, code=302)  # 302 is a temporary redirect

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
