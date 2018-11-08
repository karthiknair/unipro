import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
img=Image.open('/home/pi/Desktop/hfresh/apple.jpg')
font_type=ImageFont.truetype("/home/pi/Downloads/arial.ttf",72)
draw=ImageDraw.Draw(img)
draw.text(xy=(500,750),text='HELLO',fill=(0,0,0), font=font_type)
img.save('output2.jpg')
img.show()
