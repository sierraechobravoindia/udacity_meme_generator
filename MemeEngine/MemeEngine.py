from PIL import Image, ImageDraw, ImageFont
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
        #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        message = f"'{text}' - {author}"
        draw.text((10, 30), message, fill='white')
        meme_path = f"meme_{random.randint(0,1000000)}.jpg"
        img.save(meme_path)
        return meme_path

