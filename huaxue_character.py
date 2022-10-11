#角色目录

#备用
import pygame

#全局变量加载
import huaxue_global_var_set
import huaxue_global_var_cofig as glv

#滑雪者精灵类
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 滑雪者的朝向(-2到2)
        self.direction = 0
        self.imgs = ["./images/skier_forward.png", "./images/skier_right1.png", "./images/skier_right2.png", "./images/skier_left2.png", "./images/skier_left1.png"]
        self.person = pygame.image.load(self.imgs[self.direction])
        # 即获取矩形的方法就是函数get_rect()
        self.rect = self.person.get_rect()
        self.rect.center = [320, 100]
        # # [0,6]
        self.speed = [self.direction, 6-abs(self.direction)*2]
    # 改变滑雪者的朝向
    # 负数为向左，正数为向右，0为向前
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        # [320, 100]起始小人位置,每一次加载位图的时候小人就会跑到左上角，所以要先拿到换造型之前的位置
        center = self.rect.center
        # 加载位图
        self.person = pygame.image.load(self.imgs[self.direction])
        # 得到位图的矩形
        self.rect = self.person.get_rect()
        # 再得到小人的中心点位置
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed
    # 移动滑雪者
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

# 障碍物精灵类
# Input:
# 	-img_path: 障碍物图片路径
# 	-location: 障碍物位置
# 	-attribute: 障碍物类别属性
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        # 拿到图片路径加载图片
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        # 先拿到原来图片的位置，再给新的图片位置赋值
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        # 是树就拿树图片，是啥拿啥
        self.attribute = attribute
        self.passed = False
    # 移动
    def move(self, num):
        # y坐标-num，num=speed[1],左右转向控制，
        self.rect.centery = self.location[1] - num
