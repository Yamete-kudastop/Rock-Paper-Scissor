from PIL import Image, ImageDraw

size = (100, 100)

img = Image.new("RGBA", size, (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse([20, 20, 80, 80], fill=(128, 128, 128))
img.save("rock.png")

img = Image.new("RGBA", size, (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rectangle([20, 20, 80, 80], fill=(200, 200, 200))
img.save("paper.png")

img = Image.new("RGBA", size, (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.line([20, 20, 80, 80], fill=(150, 0, 0), width=5)
draw.line([80, 20, 20, 80], fill=(150, 0, 0), width=5)
img.save("scissors.png")
