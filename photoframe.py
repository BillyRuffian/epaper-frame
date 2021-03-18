from PIL import Image
import os, random

size = 800, 480

filename = random.choice(os.listdir("photos"))

print(filename)

photo = Image.open("photos/"+filename)
photo.thumbnail(size)
photo = photo.convert(mode='1',dither=Image.FLOYDSTEINBERG)


photo.show
photo.save("converted.jpg")