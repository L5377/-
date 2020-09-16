import turtle as t
t.bgcolor("black")
sides=6
colors=["red","yellow","green","blue","orange","purple"]
for i in range(270):
    t.pencolor(colors[i%sides])
    t.forward(i*1.2/sides+i)
    t.left(360/sides+1)
    t.width(i*sides/180)       
