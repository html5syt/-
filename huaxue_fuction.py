#功能目录

#备用
#import pygame
#import random

#全局变量加载
import huaxue_global_var_set
import huaxue_global_var_cofig as glv

#创建障碍物函数
# 创建障碍物，在障碍物函数里面实例化类，返回值是10个障碍物的类
def create_obstacles(s, e):
    # 创建精灵组
    obstacles = pygame.sprite.Group()
    # 为了让障碍物的位置不重复
    locations = []
    # 循环10次创建障碍物
    for i in range(10):
        # x坐标不变
        col = random.randint(0, 9)
         # y坐标变化
        row = random.randint(s, e)
        # 创建 x，y位置，添加到位置们里
        location  = [col*64+20, row*64+20]
        if location not in locations:
            locations.append(location)
            attribute = random.choice(["tree", "flag"])
            if attribute == "tree":
                img_path = './images/tree.png'
            else:
                img_path = './images/flag.png'
            # 实例化类，参数是图片路径，位置【x,y】，还有随机选择的字符串
            obstacle = ObstacleClass(img_path, location, attribute)
            # 把实例对象添加到精灵组里面了
            obstacles.add(obstacle)
    return obstacles
# 创建返回10障碍物的类（10个障碍物），调用时输入第几屏的位置，第二屏（10，19），第三屏（20，29）
# ======================================================================




# 二
# 合并障碍物函数
def AddObstacles(obstacle0, obstacle1):
    obstacles = pygame.sprite.Group()
    # 循环遍历两个创建障碍物的函数，然后把每一个类都添加到一个新的障碍物列表里
    # 将两屏的障碍物合成一个屏里
    for obstacle in obstacle0:
        obstacles.add(obstacle)
    for obstacle in obstacle1:
        obstacles.add(obstacle)
    return obstacles


#-----游戏角色创建模块代码结束---



# 显示游戏开始界面函数
def Show_Start_Interface(Demo, width, height):
    Demo.fill((255, 255, 255))
    tfont = pygame.font.Font(glv._get("font_set"), width//4)
    cfont = pygame.font.Font(glv._get("font_set"), width//20)
    title = tfont.render(u'滑雪游戏', True, (255, 0, 0))
    content = cfont.render(u'按任意键开始游戏', True, (0, 0, 255))
    trect = title.get_rect()
    trect.midtop = (width/2, height/10)
    crect = content.get_rect()
    crect.midtop = (width/2, height/2.2)
    Demo.blit(title, trect)
    Demo.blit(content, crect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return





# 显示结束页面函数
def over(Demo, width, height):
    Demo.fill((125,125,125))
    overt= pygame.font.Font(glv._get("font_set"), width//4)
    overx = overt.render('游戏结束', True, (255, 0, 0))
    overg = overx.get_rect()
    overg.midtop = (width/2, height/10)
    Demo.blit(overx, overg)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()		
    
    
    
#显示背景图片函数（备用）
def bg():
    theClock = pygame.time.Clock()

    # 载入图片
    background = pygame.image.load('background.jpg')

    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    w,h = background_size

    # 背景1 初始位置
    x, y = 0, 0
    # 背景2 初始位置
    x1, y1 = 0, -h

    running = True

    while running:
        screen.blit(background,background_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 不断更新位置、实现背景滚动
        y1 += 5
        y += 5
        screen.blit(background,(x,y))
        screen.blit(background,(x1,y1))
        if y > h:
            y = -h
        if y1 > h:
            y1 = -h
        
        pygame.display.flip()
        pygame.display.update()
        theClock.tick(10)