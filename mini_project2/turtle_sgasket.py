import turtle
import math

def draw_triangle(t,size,pos,color,opposite=True):
    # triangles are drawn from the top or bottom point
    t.setposition(pos)
    t.begin_fill()
    t.down()
    t.color(color)
    if opposite:
        #code for drawing opposite triangle
        t.left(60)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(-180)
    else:
        #code for drawing proper triangle
        t.left(-60)
        t.forward(size)
        t.left(-120)
        t.forward(size)
        t.left(180)
    t.up()
    t.end_fill()

def draw_gasket(t,size,pos,color,n,m):
    if n != 0:
        x = pos[0]
        opp = math.tan(math.pi / 3) * size / 2
        y = pos[1] - opp
        if n != m:
            #draw top center triangle
            #pos[1] will be poiniting to bottom of parent triangle
            #so added with the height (opp) to bring it to the top
            draw_triangle(t,size/2,(x,pos[1]+opp),color)
            #draw bottom left triangle
            draw_triangle(t,size/2,(x-size/2,pos[1]),color)
            #draw bottom right triangle
            draw_triangle(t,size/2,(x+size/2,pos[1]),color)
            draw_gasket(t,size/2,(x,pos[1]+opp),color,n-1,m)
            draw_gasket(t,size/2,(x-size/2,pos[1]),color,n-1,m)
            draw_gasket(t,size/2,(x+size/2,pos[1]),color,n-1,m)
        else:
            #code for drawing center traingle when recursion n is exactly 1
            draw_triangle(t,size/2,(x,y),color)
            draw_gasket(t,size/2,(x,y),color,n-1,m)

def sierpinski_gasket(main_color,gasket_color,size,pos,final_color,recursions):
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    t.up()
    draw_triangle(t,size,pos,main_color,False)
    draw_gasket(t,size,pos,gasket_color,recursions,recursions)
    #final turtle color
    t.color(final_color)

if __name__ == "__main__":
    w = turtle.Screen()
    w.bgcolor("red")
    sierpinski_gasket("blue","yellow",500,(0,250),"white",3)
    w.exitonclick()
