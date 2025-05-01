from manim import *
config.pixel_width = 1526
config.pixel_height = 910-50
config.background_color = "#000000"
class T7(Scene):
  def construct(self):


    t4 = Text("লিমিট কী?", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t4.set_color("#FAA111");
    t4.move_to([0,3.5,0])

    t2 = Rectangle(width=4,height=1, stroke_width=1)
    t2.move_to([0,3.45,0]);
    
    self.add(t2)


    
    self.add(t4)
    
    ax = Axes().move_to([0,-0.5,0])
    ax.set_color(TEAL)
    self.add(ax)
class T2(Scene):
  def construct(self):


    t4 = Text("লিমিট", font="Li Oporajita Unicode", font_size=25).scale(5)
    t4.set_color("#FAA111");
    t4.move_to([0,1,0])
    self.add(t4)

class T3(Scene):
  def construct(self):
    t4 = Text("লিমিট", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t4.set_color("#FAA111");
    t4.move_to([0,3.5,0])
    self.add(t4)
    t = Text("১.অনির্ণেয়", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t.set_color(WHITE)
    t.move_to([0,1,0])
    self.add(t);

    t = Text("২.অসংজ্ঞায়িত", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t.set_color(WHITE)
    t.move_to([0,-0.8,0])
    self.add(t);
class T4(Scene):
  def construct(self):
    t4 = Text("অসংজ্ঞায়িত", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t4.set_color("#FAA111");
    t4.move_to([0,3.5,0])
    self.add(t4)
    m1 = MathTex(r"\frac{1}{0} = ?").scale(2)
    m1.move_to([-5,1.5,0])
    self.add(m1)
    ax = NumberLine(x_range=[-3, 3, 1], unit_size=2,include_numbers=True, font_size=24);
    ax.move_to([0,-2,0])
    ax.set_color(TEAL)
    self.add(ax)
class T5(Scene):
  def construct(self):
    t4 = Text("অনির্ণেয়", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t4.set_color("#FAA111");
    t4.move_to([0,3.5,0])
    self.add(t4)
    m1 = MathTex(r"\frac{0}{0} = ?").scale(2)

    m1.move_to([-5,1.5,0])
    self.add(m1)
  
class T6(Scene):
  def construct(self):
    t4 = Text("অনির্ণেয়", font="Li Oporajita Unicode", font_size=25).scale(2.5)
    t4.set_color("#FAA111");
    t4.move_to([0,3.5,0])
    self.add(t4)
    m1 = MathTex(r"\frac{0}{0} \;\;\frac{\infty}{\infty } \;\;\ \infty - \infty \;\; 0^{0} \; \; 1^{\infty } \; \; \infty ^{0} \; \; 0 \ast \infty ").scale(1.5)
    m1.move_to([0,0,0])
    self.add(m1)
    
    



    