#导入
import sys
import pygame
import random
from pygame.locals import *


#全局变量加载
import huaxue_global_var_set
import huaxue_global_var_cofig as glv
#功能、角色加载
import huaxue_function as fc
import huaxue_character as char







def main():
    '''
    初始化
    '''
    pygame.init()
    
    
    #obstacle=char.ObstacleClass()
    #迷惑行为？？？一大堆Obstacle
    
    # 声音
    pygame.mixer.init()
    pygame.mixer.music.load("./music/bg_music.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    # 屏幕
    screen = pygame.display.set_mode([640, 640])
    pygame.display.set_caption('滑雪游戏')

# ====================================================
    # 主频创建时钟对象（可以控制游戏循环频率）
    clock = pygame.time.Clock()

    # 滑雪者
    skier = char.SkierClass()
    # # 记录滑雪的距离
    distance = 0
    # # 速度
    speed = [0,6]
    # 分数设置
    font = pygame.font.Font(None, 50)
    score = int(glv.get_var('initial_score'))
    score_text = font.render("Score: "+str(score), True, (0, 0, 0))

# ===========================================================
    fc.Show_Start_Interface(screen, 640, 640)

    # 创建障碍物
# ==========================================================================
    # 第一屏的障碍物10个
    obstacle1 = fc.create_obstacles(0, 9)

    # 第二屏障碍物10个
    obstacle2 = fc.create_obstacles(10, 19)

    # 20个精灵
    obstacles = fc.AddObstacles(obstacle1, obstacle2)


    # 更新屏幕
    def update():
        screen.fill([255, 255, 255])
        pygame.display.update(obstacles.draw(screen))
        # 绘制位图（加载图片，和图片的矩形大小）
        screen.blit(skier.person, skier.rect)
        screen.blit(score_text, [10, 10])	

        pygame.display.flip()

    while True:
        # 左右键控制人物方向
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    speed = skier.turn(1)

        skier.move()
        # 滚屏的距离
        distance += speed[1]
        # ===============================================================

        if distance >= 640:
            distance =0
            for obstacle in obstacle2:
                obstacle.location[1] -= 640
            obstacle1 = obstacle2
            obstacle2 = fc.create_obstacles(10, 19)
            obstacles = fc.AddObstacles(obstacle1, obstacle2)


        #滚屏机制,从精灵组里拿出类
        for obstacle in obstacles:
            # 调用函数缩小距离，y坐标再减少
            obstacle.move(distance)

        is_hit = pygame.sprite.spritecollide(skier, obstacles, True)
        if is_hit:
            if is_hit[0].attribute == "tree" :
                score -= int(glv.get_var("deduct_score"))#碰到树扣分处
                skier.person = pygame.image.load("./images/skier_fall.png")
                update()
                # 摔倒后暂停一会再站起来
                pygame.time.delay(1000)
                skier.person = pygame.image.load("./images/skier_forward.png")
                update()
                skier.direction = 0
                speed = [0, 6]
            elif is_hit[0].attribute == "flag" :
                score += int(glv.get_var("add_score"))
        score_text = font.render("Score: "+str(score), True, (0, 0, 0))
        if score <  int(glv.get_var('over_score')):
            fc.over(screen,640,640)

        update()
    # 	# 每秒循环４０次
        clock.tick(40)




main()


