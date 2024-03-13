import turtle as t#导入海龟库

#创建一个屏幕
game = t.Screen()#绘制游戏框
game.bgcolor('black')#设置画布颜色
game.title("乒乓对战")#设置窗口颜色
game.setup(1000,800)#设置窗口大小
game.tracer(0)#停止屏幕自动刷新
player_speed=10#设置球拍的移动速度
#创建球拍1
zq=t.Pen()
zq.ht()#隐藏画笔的标识
zq.up()#将画笔抬起来以免留下绘画痕迹
zq.speed(5)#设置画笔速度
zq.color('yellow')#设置画笔颜色
zq.shape('square')#设置画的形状
zq.shapesize(5,1)#设置大小
zq.goto(-400,0)#设置坐标
zq.st()#将画出的东西显示出来
#创建球拍2
ll=t.Pen()
ll.ht()
ll.up()
ll.speed(5)
ll.color('red')
ll.shape('square')
ll.shapesize(5,1)
ll.goto(400,0)
ll.st()
#初始化得分
zq_score = 0
ll_score = 0
#计分器
pen=t.Pen()
pen.ht()
pen.up()
pen.color('white')
pen.goto(-20,350)
#设置函数显示得分情况
def write_score():
    pen.clear()#防止叠加
    score_txt='张强:{} 刘莉:{}'.format(zq_score,ll_score)#设置打印形式
    pen.write(score_txt,align='center',font=('Arial',20,'bold'))#写分数

write_score()#开始前先打印一次

#让球拍动起来
def zq_up():
    y=zq.ycor()#先得到球拍现在的位置
    y=y+player_speed#将他的位置加上移动的速度
    zq.sety(y)#让球拍到指定位置
def zq_down():
    y=zq.ycor()
    y=y-player_speed
    zq.sety(y)
def ll_up():
    y=ll.ycor()
    y=y+player_speed
    ll.sety(y)
def ll_down():
    y=ll.ycor()
    y=y-player_speed
    ll.sety(y)
#键盘事件
game.listen()#将注意力集中在键盘或点击上
game.onkeypress(zq_up,'w')#移动方向对应按键的设置
game.onkeypress(zq_down,'s')
game.onkeypress(ll_up,'Up')
game.onkeypress(ll_down,'Down')

#创造乒乓球
pp=t.Pen()
pp.ht()
pp.up()
pp.shape('circle')
pp.color('white')
pp.st()
pp.dx = 0.15#球的移动规则
pp.dy = 0.15

#判断是否退出
running = True
def stop_loop():
    global running
    running = False
#注册退出事件
root = game.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW',stop_loop)
while running:
    game.update()#手动更新
    #让球上下左右移动
    pp.setx(pp.xcor()+pp.dx)
    pp.sety(pp.ycor()+pp.dy)
    #防止球上下出界
    if (pp.ycor()>395 or pp.ycor()<-395):
        pp.dy*=-1
    #让球拍接球，如果球在球拍的范围内且接触到球拍，则击中反弹
    if pp.ycor()<ll.ycor()+50 and pp.ycor()>ll.ycor()-50 and pp.xcor()>380:
        pp.dx*=-1
        pp.setx(379)
    if (pp.ycor()<zq.ycor()+50 and pp.ycor()>zq.ycor()-50 and pp.xcor()<-380):
        pp.dx*=-1
    #判断得分，输后自动回到中心处重新开始
    if pp.xcor()>410:
        zq_score+=1
        pp.goto(0,0)
        write_score()
    if pp.xcor()<-410:
        ll_score+=1
        pp.goto(0,0)
        write_score()


#让乒乓球动起来
#game.mainloop()