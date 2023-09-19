import turtle as trtl
paint = trtl.Turtle()

paint.pensize(9999)
paint.pencolor("DeepSkyBlue2")
paint.forward(1)


# -----Head/Neck-----#
paint.pencolor("black")
paint.pensize(5)
paint.circle(65)
paint.right(90)
paint.forward(35)

#-----arms-----#
paint.left(120)
paint.forward(125)
paint.left(180)
paint.forward(125)
paint.right(120)
paint.left(62.5)
paint.forward(125)
paint.left(180)
paint.forward(125)

#-----torso-----#
paint.right(62.5)
paint.forward(200)

#-----legs-----#
paint.right(45)
paint.forward(100)
paint.right(180)
paint.forward(100)
paint.right(90)
paint.forward(100)

#-----grass-----#
paint.pencolor("green")
paint.left(45)
paint.forward(300)
paint.left(180)
paint.forward(700)

#-----sun-----#
paint.pensize(25)
paint.penup()
paint.right(90)
paint.forward(600)
paint.pendown()
paint.pencolor("Gold")
paint.circle(90)

#-----grassFinalizer-----#
paint.right(180)
paint.penup()
paint.forward(610)
paint.left(90)
paint.pendown()
paint.pencolor("green")
paint.forward(800)
paint.right(180)
paint.forward(900)

#-----end-----#
wn = trtl.Screen()
wn.mainloop()
