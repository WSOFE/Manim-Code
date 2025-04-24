from manim import *
# config.pixel_height = 1920
# config.pixel_width = 1080

class T(Scene):
  def construct(self):
    dot1 = [0,2,0]
    dot2 = [-1.5,-1.3229,0]
    dot3 = [1.5,-1.3229,0]
    self.play(Create(Dot(dot1).set_color(YELLOW)),run_time = 1)
    self.play(Create(Dot(dot2).set_color(YELLOW)),run_time = 1)
    self.play(Create(Dot(dot3).set_color(YELLOW)),run_time = 1)
    tri = Polygon(dot1,dot2,dot3)
    self.play(Create(tri),run_time = 2)
    cir = Circle(radius=2,color=TEAL)
   
    self.play(Create(cir),run_time= 1)
    dot4 = Dot([0,0,0]);
    self.play(Create(dot4.scale(1.5)),run_time=1)
    T1 = Text("পরিকেন্দ্র", font="Li Oporajita Unicode", font_size=15)
    T1.move_to([0,-0.5,0])
    self.play(Create(T1),run_time = 1)
    self.wait(2)
class T2(Scene):
  def construct(self):
    dot1 = [0,2,0]
    dot2 = [-2,-2,0]
    dot3 = [1.2,-1.7,0]
    dot4 = [-1,0,0]
    line1 = Line(dot3,dot4)
    dot5 = [-0.4,-1.85,0]
    line2 = Line(dot1,dot5)
    dot6 = [0.6,0.15,0]
    line3 = Line(dot2,dot6)
    self.play(Create(Dot(dot1).set_color(YELLOW)),run_time = 1/2)
    self.play(Create(Dot(dot2).set_color(YELLOW)),run_time = 1/2)
    self.play(Create(Dot(dot3).set_color(YELLOW)),run_time = 1/2)
    tri = Polygon(dot1,dot2,dot3)
    self.play(Create(tri),run_time = 2)
    self.play(Create(Dot(dot5).set_color(YELLOW)),run_time = 1/2)
    self.play(Create(Dot(dot4).set_color(YELLOW)),run_time = 1/2)
    self.play(Create(Dot(dot6).set_color(YELLOW)),run_time = 1/2)
    line1.set_color(TEAL_B)
    line2.set_color(RED_B)
    line3.set_color(YELLOW)
    self.play(Create(line1),run_time = 1/2)
    self.play(Create(line2),run_time = 1/2)
    self.play(Create(line3),run_time = 1/2)

    dot9 = Dot([-0.267,-0.567,0])
    dot9.set_color(TEAL)
    dot9.scale(1.5)
    self.play(Write(dot9),run_time= 1/2)
    T1 = Text("ভরকেন্দ্র", font="Li Oporajita Unicode", font_size=15)
    T1.scale(2.5)
    T1.set_color("#FF1111")
    T1.move_to([-0.267,-1,0])
    self.play(Write(T1),run_time = 1/2)
    self.wait(0.5)
    