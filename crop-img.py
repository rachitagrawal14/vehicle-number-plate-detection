from PIL import Image
imageObject  = Image.open("./iceberg.jpg")
cropped     = imageObject.crop((xmin, ymin, xmax, ymax))
cropped.show()
