import pygame
import random
import math
#游戏主界面
pygame.init()#初始化所有导入的pygame模块
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption('aviationwar')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgImg=pygame.image.load('bg.png')

#添加音效
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)#-1表示但单曲循环
bang_sound=pygame.mixer.Sound('exp.wav')#创建了一个音效
#显示分数
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
def show_score():
    text =f"Score:{score}"
    score_render = font.render(text,True,(0,255,0))#三原色调色
    screen.blit(score_render,(10,10))

#飞机
playImg= pygame.image.load('player.png')
playX=400
playY=500
playerstep = 0

def move_player():
    global playX
    playX += playerstep
    if playX > 736:
        playX = 736
    if playX < 0:
        playX = 0
#创建敌人
number_of_enemies = 6
class Enemy():
    def __init__(self):
        self.img=pygame.image.load('enemy2.png')
        self.x=random.randint(100,700)
        self.y=random.randint(0,200)
        self.step=random.randint(1,2)
    def reset(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(0, 100)

enemies=[]
for i in range(number_of_enemies):
    enemies.append(Enemy())


is_over=False
over_font=pygame.font.Font('freesansbold.ttf',64)
def check_is_over():
    if is_over:
        text="Game Over"
        render=over_font.render(text,True,(255,0,0))
        screen.blit(render,(220,200))
def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img,(e.x,e.y))
        e.x+=e.step
        if e.x>736 or e.x<0:
            e.step*=-1
            e.y+=40
            if e.y>450:
                is_over=True
                enemies.clear()
#创建子弹
class Bullet():
    def __init__(self):
        self.img=pygame.image.load('bullet.png')
        self.x=playX+16
        self.y=playY-10
        self.step=10
    def hit(self):
        global score
        for e in enemies:
            if distance(self.x,self.y,e.x,e.y)<30 :
                bang_sound.play()
                bullets.remove(self)
                e.reset()
                score+=1
bullets=[]
def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.hit()
        b.y-=b.step
        if b.y < 0:
            bullets.remove(b)
def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+b*b)

#运行游戏
running = True
while running :
    screen.blit(bgImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerstep = 3
            elif event.key == pygame.K_LEFT:
                playerstep = -3
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:
            playerstep=0
    screen.blit(playImg, (playX, playY))
    move_player()
    show_enemy()
    show_bullets()
    show_score()
    check_is_over()
    pygame.display.update()