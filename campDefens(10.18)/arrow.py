from pico2d import*

class Arrow:
    def __init__(self):
        self.image = load_image('image\\etc\\arrow.png')
        self.locaction = 0
        self.launch = False
        self.x , self.y= 0, 0

    def update(self):
        if self.launch:
            self.x += 30;
            self.y += 15;
            if self.x > 1000:
                self.launch = False


    def draw(self):
        if self.launch:
            self.image.clip_draw(0,0,50,30,self.x,self.y);