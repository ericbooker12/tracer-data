from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
	data = pd.read_csv("./static/data/tracer_data.csv")

	media = ["groundwater", "carbon"]
	dyes = ["fluorescein", "RWT"]

	# get list of wells


	return render_template('index.html')

@app.route('/about')
def about():
	return 'This is the About page'