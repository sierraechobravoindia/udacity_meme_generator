from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import random

class MemeEngine():
    """Create Memes.
    
    """
    def __init__(self, path):
        self.path = path
    
    def make_meme(self, img_path, text, author, width=500) -> str:
        """Makes the meme from image and quote
        
        """
        
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('/usr/share/fonts/truetype/tlwg/Laksaman-Bold.ttf', size=20)
        message = f"'{text}' - {author}"
        wrapped = wrap(message, 25)
        w, h = random.randint(5,200), random.randint(5,300)
        text_y = h
        for line in wrapped:
            width, height = font.getsize(line)
            draw.text((w, text_y), line, fill='white', font=font)
            text_y += height
        meme_path = f"meme_{random.randint(0,1000000)}.jpg"
        img.save(meme_path)
        return meme_path

