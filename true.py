from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hack.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
