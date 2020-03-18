from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template
import json
import sys
import os

app = Flask(__name__)

@app.route('/')
def signup():
        return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
