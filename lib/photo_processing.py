from PIL import Image, ImageEnhance

def process_photo(photo):
  photo = orient(photo)
  photo = brighten(photo)
  photo = contrast(photo)
  photo.thumbnail((800,800))
  photo = crop(photo)
  return photo.convert(mode='1',dither=Image.FLOYDSTEINBERG)

def orient(photo):
  width, height = photo.size
  if height > width:
    photo = photo.rotate(90, expand=True)
  return photo

def brighten(photo):
    enhancer = ImageEnhance.Brightness(photo)
    return enhancer.enhance(1.5)

def contrast(photo):
    enhancer = ImageEnhance.Contrast(photo)
    return enhancer.enhance(1.5)

def crop(photo):
  width, height = photo.size
  left = (width - 800)/2
  top = (height - 480)/2
  right = (width + 800)/2
  bottom = (height + 480)/2
  return photo.crop((left, top, right, bottom))
