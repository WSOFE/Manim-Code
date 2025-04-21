from manim import *
import numpy as np
# config.pixel_height = 1500
# config.pixel_width = 1500
# # config.pixel_height =2160*2
# # config.pixel_width = 3840*2
def Rcolor():
    r1 = np.random.randint(0,15)
    s1 = str(hex(r1))[2]

    r2 = np.random.randint(0,15)
    s2 = str(hex(r2))[2]
    r3 = np.random.randint(0,15)
    s3 = str(hex(r3))[2]
    r4 = np.random.randint(0,15)
    s4 = str(hex(r4))[2]
    r5 = np.random.randint(0,15)
    s5 = str(hex(r5))[2]
    r6 = np.random.randint(0,15)
    s6 = str(hex(r6))[2]
    c = "#"+s1+s2+s3+s4+s5+s6
    return c
def func(t):

    return np.array((4*np.cos(t),4*np.sin(t),0))
class T(Scene):
    def construct(self):
        col = "#282828";
        # rec = Rectangle(height=8,width=8,color="#006A4E")
        # rec.set_fill("#006A4E")
        # rec.set_opacity(1)
        
        
        # self.add(rec)
        cir = Circle(radius= 4,color=col)
        cir.set_fill(col)
        cir.set_opacity(1)
        self.add(cir)
        # F42A41
        c = TEAL
        cir = Circle(radius= 2,color=c)
        cir.set_fill(c)
        cir.set_opacity(1)

        self.add(cir)
        x=-1.8
        d=0.1
        p1 = [x,(4-x**2)**0.5,0]
        p2 = [x+d,(4-(x+d)**2)**0.5,0]
        
        p3 = [x,-(16-x**2)**0.5,0]
        p6 = [x-1,2,0]
        p7 = [x-1,-2,0]
        gg = Polygon(p6,p7,p3,p1)
        
        gg.set_stroke(col)
        gg.set_fill(col)
        gg.set_opacity(1)
        self.add(gg)

        p4 = [x+d,-(16-(x+d)**2)**0.5,0]
        g = Polygon(p1,p2,p4,p3)
        g.set_stroke(YELLOW)
        g.set_fill(YELLOW)
        g.set_opacity(1)
        self.add(g)

        l = [-1.59,1.10,0]
        l2 = [-0.59,1.10,0]
        l3 = [-1.59,-1.10,0]
        l4 = [-0.59,-1.10,0]
        l5 = [-1.09,1.10,0]
        l6=[-1.09,-1.10,0]
        n = 8
        self.add(Line(l,l2).set_stroke(width=n),Line(l3,l4).set_stroke(width=n),Line(l5,l6).set_stroke(width=n))

        i = [-0.46,1.10,0]
        i2 =[-0.46,-1.10,0] 
        i3 = [0.54,-1.10,0] 
        self.add(Line(i,i2).set_stroke(width=n),Line(i2,i3).set_stroke(width=n))

        m = [0.67,1.10,0]
        m1 = [0.67,-1.10,0]

        m2 = [1.67,1.10,0]
        m3= [1.67,-1.10,0]
        m6 = [1.17,-0.25,0]


        self.add(Line(m,m1).set_stroke(width=n),Line(m2,m3).set_stroke(width=n),Line(m6,m).set_stroke(width=n),Line(m6,m2).set_stroke(width=n))
        