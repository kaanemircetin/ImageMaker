from PIL import Image, ImageDraw

image = Image.new("RGB", (500, 500), (0,0,255))

draw_image = ImageDraw.Draw(image)

draw_image.ellipse([(50, 50), (150, 150)], fill=(255, 0, 0))
#you can draw circles how many you wish
#draw.ellipse([(70, 70), (200, 200)], fill=(255, 0, 0))

draw_image.rectangle((200,200,300,300), fill =(122,122,122))
#and also you can draw whatever you wish forever
#draw.rectangle((200,200,300,300), fill =(255,0,0))

image.show()

image.save("image.png")
# And that'll show the image

