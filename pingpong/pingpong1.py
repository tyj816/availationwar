import turtle as t
#创建背景
game = t.Screen()
game.title('乒乓对战')
game.bgcolor('black')
game.setup(1000,800)
game.tracer(False)
#创建球2
p1=t.Turtle()
p1.ht()
p1.up()
p1.speed(0)
p1.color('yellow')
p1.shape('square')
p1.shapesize(5,1)
p1.goto(-400,0)
p1.st()

p2=t.Turtle()
p2.ht()
p2.up()
p2.speed(0)
p2.color('red')
p2.shape('square')
p2.shapesize(5,1)
p2.goto(400,0)
p2.st()

player_speed = 10
p1_score = 0
p2_score = 0

def write_score():
    pen.clear()
    score_txt='p1:{}  p2:{}'.format(p1_score,p2_score)
    pen.write(score_txt,align='center',font=('Arial',20,'bold'))

pen=t.Turtle()
pen.ht()
pen.up()
pen.goto(-20,350)
pen.color('white')
write_score()
#移动球拍
def p1_up():
    y=p1.ycor()
    y=y+player_speed
    p1.sety(y)

    #p1.right(20)

def p1_down():
    y=p1.ycor()
    y=y-player_speed
    p1.sety(y)

def p2_up():
    y=p2.ycor()
    y=y+10
    p2.sety(y)

def p2_down():
    y=p2.ycor()
    y=y-10
    p2.sety(y)



game.listen()
game.onkeypress(p1_up,'w')
game.onkeypress(p1_down,'s')
game.onkeypress(p2_up,'Up')
game.onkeypress(p2_down,'Down')
#创建乒乓球
pp=t.Turtle()
pp.up()
pp.color('white')
pp.shape('circle')
pp.dx= 0.2
pp.dy= 0.2

running=True
def stop_loop():
    global running
    running = False

root = game.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW',stop_loop)

#print(f"{p2.width()} ,{p2.height()}")
#让乒乓球移动起来

while running:
    game.update()
    pp.setx(pp.xcor() + pp.dx)
    pp.sety(pp.ycor() + pp.dy)

    if (pp.ycor()>=400) or (pp.ycor()<=-400):
        pp.dy*=-1
    #让球拍接球
    y_up=p2.ycor()+50
    y_down=p2.ycor()-50
    if (pp.ycor()>y_down and pp.ycor()<y_up and pp.xcor()>385) :
        pp.dx*=-1
        pp.setx(384)

    if (pp.ycor()>p1.ycor() - 50 and pp.ycor()<p1.ycor() + 50 and pp.xcor()<-385) :
        pp.dx*=-1
        pp.setx(-384)

    if (pp.xcor()>390):
        pp.goto(0,0)
        p1_score+=1
        write_score()

    if (pp.xcor()<-390):
        pp.goto(0,0)
        p2_score+=1
        write_score()
#game.mainloop()
