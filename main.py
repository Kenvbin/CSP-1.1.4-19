#   a114_nested_loops_4.py 
import turtle as trtl
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
while (1 == 1):
  move_x = 100
  move_y = 100
  while (x < 100):
    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -100
      
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 100
  move_x = -100
  for i in range(2):
    while (y > -100):
      x = x + move_x
      y = y - move_y
      painter.goto(x,y)
    move_y = -100
        
    while (y < 0):
      x = x + move_x
      y = y - move_y
      painter.goto(x,y)
    move_y = 100

wn = trtl.Screen()
wn.mainloop()