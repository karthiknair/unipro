import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
img=Image.open('/home/pi/Desktop/hfresh/apple.jpg')
font_type=ImageFont.truetype("/home/pi/Downloads/arial.ttf",72)
draw=ImageDraw.Draw(img)
x, y= (25,1500)
text='APPLE Actual price= ▲5$, Discount Price= ▼2$'

w, h= font_type.getsize(text)

draw.rectangle((x,y, x+w, y+h), fill='black')
draw.text((x,y),text='APPLE  Price= ▼2$',fill=(209,239,8),font=font_type)


img.save('output2.jpg')
img.show()
