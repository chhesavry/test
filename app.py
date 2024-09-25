import os
import requests
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# GitHub raw file URLs
GITHUB_BASE_URL = 'https://raw.githubusercontent.com/username/repo/branch/'  # Replace with your details
FILES = {
    'index.html': GITHUB_BASE_URL + 'index.html',
    'style.css': GITHUB_BASE_URL + 'style.css',
    'script.js': GITHUB_BASE_URL + 'script.js',
}

# Function to fetch files from GitHub
def fetch_files():
    for filename, url in FILES.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(filename, 'w') as f:
                f.write(response.text)
            print(f"Fetched {filename} successfully.")
        except Exception as e:
            print(f"Error fetching {filename}: {str(e)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    fetch_files()  # Fetch files at startup
    app.run(debug=True)
