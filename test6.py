#test
import turtle as t
import time
def Drawline(draw):
    drawGrap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGrap()
    t.right(90)
def drawGrap():
    t.penup()
    t.fd(5)
def drawDight(dight):
    Drawline(True) if dight in [2,3,4,5,6,8,9] else Drawline(False)
    Drawline(True) if dight in [0,1,3,4,5,6,8,9] else Drawline(False)
    Drawline(True) if dight in [0,2,3,5,6,8,9] else Drawline(False)
    Drawline(True) if dight in [0,2,6,8] else Drawline(False)
    t.left(90)
    Drawline(True) if dight in [0,4,5,6,8,9] else Drawline(False)
    Drawline(True) if dight in [0,2,3,5,6,7,8,9] else Drawline(False)
    Drawline(True) if dight in [0,1,2,3,4,7,8,9] else Drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawdate(date):
    t.pencolor("red")
    for i in date:
        if i == "-":
            t.write("年",font = ("Arial",18,"normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == "=":
            t.write("月",font = ("Arial",18,"normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == "+":
             t.write("日",font = ("Arial",18,"normal"))
        else:
                drawDight(eval(i))
def main():
    t.setup(800,350)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawdate(time.strftime("%Y-%m=%d+",time.gmtime()))
    t.hideturtle()
    t.done()
main()
