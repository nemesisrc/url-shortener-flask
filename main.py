from flask import Flask, render_template, redirect, url_for, request
import random
import string
import os
import json
from dotenv import load_dotenv
load_dotenv()  # this is required to load environment variables from .env file


app = Flask(__name__)

# database for storing shortend URLs
shortened_urls = {}

def generate_short_url(length=6):
    short_url = ""
    all_chars = string.ascii_letters + string.digits
    for _ in range(length):
        curr_char = random.choice(all_chars)
        short_url += curr_char
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long-url']
        short_url = generate_short_url()
        short_url = f"{request.url_root}{short_url}"
        if short_url in shortened_urls:
            return render_template('result.html', shortened_url=short_url)
        else:
            shortened_urls[short_url] = long_url
            return render_template('result.html', shortened_url=short_url)
    else:
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8000)