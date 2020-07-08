from flask import Flask, request,render_template,send_file
from flask import Response
import os
from flask_cors import CORS, cross_origin
import os
import time
import requests
from selenium import webdriver
from img_scrape import search_and_download




os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def my_form():
    return render_template('images.html')





@app.route("/imageScrapper", methods=['POST'])
@cross_origin()
def imageScrapper():

	import os.path
	from os import path
	

	if path.exists('images.zip'):
		os.remove('images.zip')


	

	search_term = request.form['text']
	num = int(request.form['num'])

	if num>20:
		num=20

	
	links=search_and_download(search_term=search_term, number_images=num)
	
	return render_template('images.html', links=links)





@app.route('/download',methods=['POST'])
def downloadFile ():
	import os
	import zipfile
	dir_name='./images'
    #For windows you need to use drive name [ex: F:/Example.pdf]
	output_filename='images'
	import shutil
	shutil.make_archive(output_filename, 'zip', dir_name)
	path = "images.zip"
	return send_file(path, as_attachment=True)

	
	
if __name__ == '__main__':
	app.run(debug=True)
	
	