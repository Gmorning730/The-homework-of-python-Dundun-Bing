import turtle
import pygame   #导入可以加载音乐的库
import os       #导入设置路径的库
# 定义画笔和当前的文件路径
os.chdir(r"E:\Pycharm\turtle库作业-冰墩墩\source")
pen=turtle.Turtle()
pygame.mixer.init()                           # 初始化
track = pygame.mixer.music.load('爱喝柠檬茶的喵 - 让我再睡5分钟.mp3')   # 加载音乐文件
pygame.mixer.music.play()                     # 开始播放音乐流
pygame.mixer.music.fadeout(70000)             # 设置音乐多久慢慢淡出结束

# 设置画笔速度
pen.speed(10)
turtle.speed(10)

def windows():
    """绘制窗口"""
    turtle.setup(800,600,450,100)
def outline():
    """绘制墩墩外轮廓线条函数"""
    turtle.penup()
    turtle.setpos(-120,200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.left(81)
    turtle.circle(-50,65,)
    turtle.circle(-40,85,)
    turtle.left(70)
    turtle.circle(-600,3)
    turtle.circle(-700,3)
    turtle.circle(-600,3)
    turtle.left(70)
    turtle.circle(-50,65,)
    turtle.circle(-40,100,)
    turtle.left(50)
    turtle.circle(-180,25)
    turtle.left(170)
    turtle.circle(-40,180)
    turtle.left(-20)
    turtle.circle(-600,8)
    turtle.circle(-80,30)
    turtle.left(60)
    turtle.circle(-300,26)
    turtle.circle(-800,5)
    turtle.left(30)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(15)
    turtle.circle(40,200)
    turtle.right(110)
    turtle.forward(90)
    turtle.right(90)
    turtle.circle(600,4)
    turtle.circle(500,7)
    turtle.circle(700,10)
    turtle.left(160)
    turtle.circle(-20,80)
    turtle.circle(-50,100)
    turtle.right(8)
    turtle.circle(-200,20)
    turtle.left(10)
    turtle.circle(-90,59)
    turtle.left(68)
    turtle.circle(-280,17)
    turtle.setpos(-120,200)
def colors_line():
    """绘制墩墩糖果线条圈函数"""
    pen.pensize(3)
    pen.penup()
    pen.setpos(-72,140)
    pen.pendown()
    pen.left(40)
    pen.circle(-140)
    # 定义颜色列表
    colors = ['blue','yellow','red','green','skyblue','blue','skyblue','black']
    setx = -71
    sety = 139
    r = -138
    i = 1
    # 利用循环画圆圈
    for color in colors:
        pen.penup()
        i = i + 3
        pen.setpos(setx + i,sety - i)
        pen.color(color)
        pen.pendown()
        pen.circle(r + i + 1 )
def oval(a):
    """椭圆函数"""
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
            a = a + 0.07
            pen.rt(3)  # 向左转3度
            pen.fd(a)  # 向前走a的步长
        else:
            a = a - 0.07
            pen.rt(3)
            pen.fd(a)
def eyes():
    """绘制墩墩左右双眼"""
    pen.penup()
    pen.setpos(70, 90)
    pen.pendown()
    pen.right(7)
    pen.begin_fill()
    pen.fillcolor('black')
    oval(1)
    pen.end_fill()
    pen.penup()
    pen.setpos(-70, 20)
    pen.pendown()
    pen.left(110)
    pen.fillcolor('black')
    pen.begin_fill()
    pen.fillcolor('black')
    oval(1)
    pen.end_fill()
def pupil_black(x, y):
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('black')
    pen.circle(6)
    pen.end_fill()
def pupil():
    """绘制瞳孔函数"""
    pen.penup()
    pen.setpos(-20, 75)
    pen.pendown()
    pen.pensize(2)
    pen.begin_fill()
    pen.fillcolor('white')
    pen.circle(18)
    pen.end_fill()
    pen.penup()
    pen.setpos(93, 75)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('white')
    pen.circle(18)
    pen.end_fill()
    pen.begin_fill()
    pen.penup()
    pen.setpos(-24, 70)
    pen.pendown()
    pen.fillcolor('brown')
    pen.circle(12)
    pen.end_fill()
    pen.penup()
    pen.setpos(90, 70)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('brown')
    pen.circle(12)
    pen.end_fill()
    pen.penup()
    pupil_black(-27, 65)
    pupil_black(86, 65)
def eye_light(x, y):
    """瞳孔上的小白点"""
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.color('white')
    pen.begin_fill()
    pen.fillcolor('white')
    pen.circle(2)
    pen.end_fill()
def fonts(x, y, word, font_size = 21, font_family = '楷体', font_type = 'normal'):
    """墩墩肚子上的汉字"""
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.color('black')
    pen.write(word, move=False, align="left", font=(font_family, font_size, font_type))
def left_ear(x, y):
    """绘制墩墩地左耳阴影颜色"""
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
def reset_pen():
    pen.penup()
    pen.home()
    pen.pendown()
def lover(x, y):
    '''绘制墩墩的的小桃心'''
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.left(100)
    pen.right(33)
    pen.color('red')
    pen.begin_fill()
    pen.fillcolor('red')
    pen.circle(-5,180)
    pen.left(180)
    pen.circle(-5, 180)
    for i in range(40):
        pen.circle(-i,1.5)
        i = i + 2
    pen.right(80)
    for i in range(40):
        pen.circle(-40+i,1.5)
        i = i + 2
    pen.circle(-5,170)
    pen.end_fill()
def nose(x, y):
    '''绘制墩墩鼻子'''
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.color('black')
    pen.begin_fill()
    pen.fillcolor('black')
    pen.left(44)
    i = 20
    for i in range(40):
        if i>30:
            pen.circle(-i, 1)
            i = i - 2
        else:
            pen.circle(-i, 2)
            i = i + 2
    pen.right(65)
    pen.circle(-13,80)
    pen.right(40)
    pen.circle(-7,16)
    pen.left(24)
    pen.circle(-13, 80)
    pen.end_fill()
    reset_pen()
def lears_black(x = 0, y = 0):

    ''''绘制墩墩的黑耳朵'''
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.fillcolor('black')
    pen.begin_fill()
    pen.left(90)
    for i in range(57):
        if i<30:
            pen.circle(i + 0.4, 3)
        else:
            pen.circle(i - 0.4, 3)
    pen.left(118)
    pen.circle(200,19)
    pen.end_fill()
def rears_black(x = 0, y = 0):
    ''''绘制墩墩的黑耳朵'''
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.right(45)
    pen.fillcolor('black')
    pen.begin_fill()
    pen.left(90)
    for i in range(55):
        if i<30:
            pen.circle(-i + 0.4, 3)
        else:
            pen.circle(-i - 0.4, 3)
    pen.right(135)
    pen.circle(170,20)
    pen.end_fill()
def left_arm(x=0, y=0):
    '''绘制墩墩左胳膊'''
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('black')
    pen.right(15)
    pen.left(230)
    pen.circle(130,60)
    pen.left(10)
    pen.circle(27,160)
    pen.left(10)
    pen.circle(-180,15)
    pen.left(30)
    pen.circle(-100,40)
    pen.end_fill()
def right_arm(x=0, y=0):
    '''绘制墩墩右胳膊'''
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('black')
    pen.left(50)
    pen.circle(24,200)
    pen.right(14)
    pen.forward(25)
    pen.left(70)
    pen.circle(-80,50)
    pen.left(145)
    pen.circle(150,30)
    pen.end_fill()
def mouth(x, y):
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.color('black')

    pen.forward(60)
    pen.right(90)
    pen.forward(8)
    pen.circle(-30,180)
    pen.forward(8)
    pen.right(180)
    pen.forward(8)
    pen.left(90)
    pen.begin_fill()
    pen.fillcolor('pink')
    pen.forward(40)
    pen.right(45)
    pen.forward(4)
    pen.left(90)
    pen.forward(4)
    pen.right(45)
    pen.forward(13)
    pen.right(90)
    pen.circle(-29, 180)
    pen.end_fill()
def left_leg(x, y):
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.right(70)
    pen.begin_fill()
    pen.fillcolor('black')
    pen.circle(-200,20)
    pen.circle(3,90)
    pen.forward(58)
    pen.circle(3,90)
    pen.forward(50)
    pen.left(50)
    pen.circle(120,40)
    pen.end_fill()
def right_leg(x, y):
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.right(105)
    pen.begin_fill()
    pen.fillcolor('black')
    pen.circle(200,20)
    pen.circle(3,-90)
    pen.forward(58)
    pen.circle(3,-90)
    pen.forward(50)
    pen.right(55)
    pen.circle(-120,35)
    pen.end_fill()
def Olympic_circle(x, y):
    reset_pen()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    colors = ['blue', 'black', 'red', 'yellow', 'green']
    num = 0
    m = 3
    for color in colors:
        pen.pensize(2)
        if num <= 2:
            pen.color(color)
            pen.circle(5)
            pen.penup()
            pen.forward(7)
            pen.down()
        elif 5>num>2:
            pen.penup()
            pen.setpos(x+m,y-7)
            pen.pendown()
            pen.color(color)
            pen.circle(5)
            m+=7
        num += 1
#绘制墩墩主体
outline()
colors_line()
eyes()
pupil()
eye_light(83, 70)
eye_light(-27, 70)
fonts(15, -145,"冬")
fonts(2, -160,"Beijing 2022",8,'微软雅黑','italic')
reset_pen()
nose(18, 30)
lears_black(-53, 217)
rears_black(81,213)
right_arm(238,100)
left_arm(-140,95)
lover(211, 114)
mouth(0,0)
left_leg(-85,-170)
right_leg(148, -170)
Olympic_circle(20,-182)
pen.hideturtle()
turtle.hideturtle()
turtle.exitonclick()
