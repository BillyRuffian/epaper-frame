from flask import Flask, request, render_template
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('show_photo.html', image_type='converted')

@app.route('/original')
def original():
  return render_template('show_photo.html', image_type='original')

@app.route('/photo', methods=['POST'])
def set_photo():
  file = request.files['image']
  photo = Image.open(file)
  photo.save('static/original.jpg')
  width, height = photo.size
  if height > width:
    photo = photo.rotate(90, expand=True)
  photo.thumbnail((800,480))
  photo = photo.convert(mode='1',dither=Image.FLOYDSTEINBERG)
  photo.save('static/converted.jpg')
  return ('', 204)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
