import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    # Get a list of all the video files in the directory
    videos = os.listdir("video")

    # Render the home page HTML template with the list of videos
    return render_template("home.html", videos=videos)

# Define the route for the video upload form
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Get the uploaded file
        file = request.files["file"]

        # Save the file to the video directory
        filename = file.filename
        file.save(os.path.join("video", filename))

        # Redirect to the home page
        return redirect(url_for("home"))

    # Render the video upload HTML template
    return render_template("upload.html")


# Define route to serve video files
@app.route('/video/<path:path>')
def serve_video(path):
    return send_from_directory('video', path)

if __name__ == "__main__":
    app.run(host="192.168.1.10")
