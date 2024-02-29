from turtle import Turtle,Screen
myobject = Turtle()
myobject.color("red")
myobject.shape("turtle")
for i in range(4):
    
    myobject.circle(50)
    myobject.forward(20)
    myobject.circle(50)
    myobject.forward(20)
myobject.right(180)
for i in range(8):
    
    myobject.forward(15)
    myobject.circle(50)
    

mywindow = Screen()
mywindow.exitonclick()