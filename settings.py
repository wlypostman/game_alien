""" 一个设置类"""


class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = '外星人入侵'
        self.bg_color = (230,200,10)

        #ship
        self.ship_speed = 1.5


        #bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.2
        