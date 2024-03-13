import turtle as t
#创建窗口
game = t.Screen()
game.title('乒乓对战')
game.bgcolor('black')
game.setup(1000,800)
game.tracer(False)

#创建球拍clz
clz=t.Pen()
clz.ht()
clz.up()
clz.speed(0)
clz.color('blue')
clz.shape('square')
clz.shapesize(5,1)
clz.goto(-400,0)
clz.st()

xz=t.Pen()
xz.ht()
xz.up()
xz.speed(0)
xz.color('orange')
xz.shape('square')
xz.shapesize(5,1)
xz.goto(400,0)
xz.st()
#让clz动起来
player_move=10
def clz_up():
    y=clz.ycor()
    y=y+player_move
    clz.sety(y)
def clz_down():
    y=clz.ycor()
    y=y-player_move
    clz.sety(y)
#让xz动起来
def xz_up():
    y=xz.ycor()
    y=y+player_move
    xz.sety(y)
def xz_down():
    y=xz.ycor()
    y=y-player_move
    xz.sety(y)
game.listen()
game.onkeypress(clz_up,'w')
game.onkeypress(clz_down,'s')
game.onkeypress(xz_up,'Up')
game.onkeypress(xz_down,'Down')
#创建乒乓球
pp=t.Pen()
pp.ht()
pp.up()
pp.color('white')
pp.shape('circle')
pp.st()
pp.dx=0.15
pp.dy=0.15

#计分器
clz_score=0
xz_score=0
pen=t.Pen()
pen.ht()
pen.up()
pen.color('white')
pen.goto(-20,300)
def write_score():
    pen.clear()
    score_txt='车厘子：{} 新竹：{}'.format(clz_score,xz_score)
    pen.write(score_txt,align='center',font=('Arial',20,'bold'))
write_score()

running=True
def stop_loop():
    global running
    running=False
root=game.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW",stop_loop)

#让乒乓球动起来
while running:
    game.update()
    pp.setx(pp.xcor()+pp.dx)
    pp.sety(pp.ycor()+pp.dy)
    if pp.ycor()>400 or pp.ycor()<-400:
        pp.dy*=-1
    if pp.ycor()<xz.ycor()+50 and pp.ycor()>xz.ycor()-50 and pp.xcor()>380:
        pp.dx*=-1
    if pp.ycor() < clz.ycor() + 50 and pp.ycor() > clz.ycor() - 50 and pp.xcor() < -380:
        pp.dx *= -1
    if pp.xcor()>400:
        clz_score+=1
        write_score()
        pp.goto(0,0)
    if pp.xcor()<-400:
        xz_score+=1
        write_score()
        pp.goto(0,0)
#game.mainloop()