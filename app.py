from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
	status = 0
	url_list = []
	if request.method == "POST":
		if request.form.get('youtube') == "Generate Thumbnail":
			video_url = request.form.get("video-url")
			video_url = video_url.split("=")
			status = 1
			video_id = video_url[1]
			#120x90
			url_list.append("https://img.youtube.com/vi/"+video_id+"/default.jpg")
			#640x480
			url_list.append("https://img.youtube.com/vi/"+video_id+"/sddefault.jpg")
			#320x180
			url_list.append("https://img.youtube.com/vi/"+video_id+"/mqdefault.jpg")
			#480x360
			url_list.append("https://img.youtube.com/vi/"+video_id+"/hqdefault.jpg")
			#1280x720
			url_list.append("https://img.youtube.com/vi/"+video_id+"/maxresdefault.jpg")
			print(url_list)

			for indx, img_url in  enumerate(url_list):
				img = requests.get(img_url)
				img_file = open("static/"+str(indx+1)+".jpg", "wb")
				img_file.write(img.content)
				img_file.close()

		return render_template("index.html", status=status)
	return render_template("index.html", status=status)


if "__name__" == "__main__":
	app.run(debug=True)