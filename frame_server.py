from flask import Flask, request, render_template
from PIL import Image
from lib.photo_processing import process_photo
from waveshare_epd import epd7in5_V2 as epd
from concurrent.futures import ThreadPoolExecutor


app = Flask(__name__)
executor = ThreadPoolExecutor(2)

@app.route('/')
def index():
  return render_template('show_photo.html', image_type='converted')

@app.route('/original')
def original():
  return render_template('show_photo.html', image_type='original')

@app.route('/photo', methods=['POST'])
def set_photo():
  photo = Image.open(request.files['image'])
  photo = photo.convert("RGB")
  photo.save('static/original.jpg')
  photo = process_photo(photo)
  photo.save('static/converted.jpg')
  executor.submit(update_frame, photo)
  return render_template('show_photo.html', image_type='converted')

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

def update_frame(photo):
  epaper = epd.EPD()
  epaper.init()
  #epaper.Clear()
  epaper.display(epaper.getbuffer(photo))
  epaper.sleep()
