# -*- coding:utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os.path
import time
from conf import font_config

class VerifyCode:

    _lower = "abcddefghijklmnopqrstuvwxyz"
    _upper = _lower.upper()
    _number = "0123456789"
    chars = "".join((_lower, _upper, _number))
    font_type = font_config.font

    def __init__(self,\
                img_path,
                size=(120, 30),\
                img_type="gif",\
                mode="RGB",\
                bg_color=(255,255,255),\
                fg_color=(0,0,255),\
                length=4,\
                font_size=18,\
                font_type=font_type,\
                draw_point=True,\
                point_chance=2
                ):
        try:
            img = Image.new(mode, size, bg_color)
            draw = ImageDraw.Draw(img)
            if draw_point:
                self.create_point(draw, point_chance, size)
            chars = "".join((self._lower, self._upper, self._number))
            self.strs = self.create_str(draw, chars, length, size, \
                            font_size, font_type, fg_color)
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.name = "%s.gif" %time.time()
            img.save(os.path.join(img_path, self.name))
        except Exception as e:
            print e
            self.strs = "mlgb"
            self.name = "default.jpg"

    def create_str(self, draw, chars, length, size, \
                    font_size, font_type, fg_color):
        char = random.sample(chars, length)
        strs = " %s " % " ".join(char)
        font = ImageFont.truetype(font_type, font_size)
        font_w, font_h = font.getsize(strs)
        width, height = size
        draw.text(((width-font_w)/3, (height-font_h)/3), \
                    strs, font=font, fill=fg_color)
        return "".join(char)

    def create_point(self, draw, point_chance, size):
        width, height = size
        chance = min(100, max(0, int(point_chance)))
        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > (100-chance):
                    draw.point((w, h), fill=(0,0,0))
