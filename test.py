from waveshare_epd import epd7in5_V2
from PIL import Image
from waveshare_epd import epd7in5_V2 as epd

image = Image.open('static/converted.jpg')

epaper = epd.EPD()

epaper.init()
epaper.Clear()

epaper.display(epaper.getbuffer(image))

epaper.sleep()
