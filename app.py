from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv
import os

app = Flask(__name__)

LOG_FILE = "logs/access_log.csv"
RESUME_PATH = "/static/resume.pdf"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        company = request.form.get("company")
        ip = request.remote_addr
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] {ip} - {name} from {company}")

        return redirect(RESUME_PATH)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
