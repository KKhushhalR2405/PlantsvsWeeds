import os
import urllib.request
from flask import *
from werkzeug.utils import secure_filename
import filetype
import requests
import json
import cv2
import cloudinary
import cloudinary.uploader as up
import os
cloudinary.config.update = ({
    'cloud_name':'drlf6gntz',
    'api_key': '894749617857176',
    'api_secret': 'Qp-ckIp4k_xIresVZF7Gms0WrPY'
})

url = 'http://localhost:5000/'

upload_folder = r".\static\uploads"



app.secret_key = 'dsdsqqwqw'



app = Flask(__name__)




@app.route('/',methods=["GET","POST"])

def upload_image():
	try:
		file = request.files['files']
		filename = secure_filename(file.filename)
		path = os.path.join(upload_folder, filename)
		file.save(path)
		kind = filetype.guess(path)
		type,extension = str(kind.mime).split("/")


		img=up.upload(path,cloud_name='drlf6gntz',api_key='894749617857176',api_secret='Qp-ckIp4k_xIresVZF7Gms0WrPY')
		img_url=img["url"]
		j_data = json.dumps({"data":img_url,"type":"image"})
		headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
		r = requests.post(url, data=j_data, headers=headers)
		print(r.text)
		return render_template("index.html")
	except Exception as e:
		print(e)
		return render_template("index.html")

if __name__=="__main__":
    app.run(host='127.0.0.1',port=1025,debug=True)