from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')

if __name__ == "__main__":
    app.run(debug=True)