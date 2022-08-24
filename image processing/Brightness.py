from PIL import Image, ImageEnhance

image = Image.open('image/2.png')

image = ImageEnhance.Brightness(image)

factor = 1.5
image = image.enhance(factor)
image.save('image/original1.png')