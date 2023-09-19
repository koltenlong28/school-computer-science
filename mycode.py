import turtle as trtl
paint = trtl.Turtle()

paint.speed(0)

#-----variables-----#
f = paint.forward
r = paint.right
l = paint.left

#-----sky-----#
paint.pensize(9999)
paint.pencolor("DeepSkyBlue2")
f(1)
# -----Head/Neck-----#
paint.pencolor("black")
paint.pensize(5)
paint.circle(65)
r(90)
f(35)
#-----arms-----#
l(120)
f(125)
l(180)
f(125)
r(120)
l(62.5)
f(125)
l(180)
f(125)
#-----torso-----#
r(62.5)
f(200)
#-----legs-----#
r(45)
f(100)
r(180)
f(100)
r(90)
f(100)
#-----grass-----#
paint.pencolor("green")
l(45)
f(300)
l(180)
f(700)
#-----sun-----#
paint.pensize(25)
paint.penup()
r(90)
f(600)
paint.pendown()
paint.pencolor("Gold")
paint.circle(90)
l(90)
f(90)
paint.pensize(200)
f(1)
r(180)
paint.penup()
f(91)
r(90)
f(700)
#-----wait(for debuging)-----#
import time
print("initial print")
time.sleep(0)
print("second print")


paint.pendown()
#-----grassFinalizer-----#
l(90)
paint.penup()
f(710)
l(180)
paint.pendown()
paint.pencolor("green")
f(800)
r(180)
f(900)
#-----end-----#
wn = trtl.Screen()
wn.mainloop()

