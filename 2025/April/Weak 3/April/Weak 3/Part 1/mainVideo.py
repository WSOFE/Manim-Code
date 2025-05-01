from manim import*
# config.pixel_height = 860
# config.pixel_width = 1526
class T1(Scene):
  def construct(self):
    

    M = MathTex(r"f(x) = \frac{\left| x \right|+5}{1-\left| sinx \right|}")
    M.set_color(YELLOW)
    

    M.move_to([-4,3,0])
    
    T2 = Text("হলে", font="Li Oporajita Unicode", font_size=30)
    T2.next_to(M,RIGHT)
    M3 = MathTex(r"x = 0")
    M3.next_to(T2,RIGHT)
    T3 = Text("বিন্দুতে লিমিটের অস্তিত্ব নির্ণয় কর।", font="Li Oporajita Unicode", font_size=30)
    T3.next_to(M3,RIGHT)

    self.add(M,T2,M3,T3)
class T2(Scene):
  def construct(self):
    

    M = MathTex(r"f(x) = \frac{\left| tanx \right|}{x}")
    M.set_color(ORANGE)
    

    M.move_to([-4,3,0])
    
    T2 = Text("হলে", font="Li Oporajita Unicode", font_size=30)
    T2.next_to(M,RIGHT)
    M3 = MathTex(r"x = 0")
    M3.next_to(T2,RIGHT)
    T3 = Text("বিন্দুতে লিমিটের অস্তিত্ব নির্ণয় কর।", font="Li Oporajita Unicode", font_size=30)
    T3.next_to(M3,RIGHT)

    self.add(M,T2,M3,T3)
class T30(Scene):
  def construct(self):
    M = MathTex(r"\lim_{x \to 0} \frac{e^{\left| tanx \right|}-1}{tanx}")
    M.move_to([-4,3,0])
    self.add(M)
class T3(Scene):
  def construct(self):
    M = MathTex(r"\lim_{x \to 0} \frac{e^{\left| sinx \right|}-1}{sinx} = ?")
    M.set_color(ORANGE)
    M.move_to([-4,3,0])
    self.add(M)
class T4(Scene):
  def construct(self):
    

    M = MathTex(r"f(x)= \left\{ \begin{array}{cl} a + bx + 10 & , \ x > -1 \\15 & , \ x = -1 \\b\left| x \right|+a-10 & , \ x < -1\end{array} \right.")
    M.set_color(YELLOW)
    

    M.move_to([-3,2.5,0])
    T1 = Text("এবং", font="Li Oporajita Unicode", font_size=30)
    T1.next_to(M,RIGHT)
    M2 = MathTex(r"\lim_{x \to -1} f(x) = f(-1)")
    M2.next_to(T1,RIGHT)
    T2 = Text("হলে", font="Li Oporajita Unicode", font_size=30)
    T2.next_to(M2,RIGHT)
    M3 = MathTex(r"a")
    M3.move_to([-6.5,1,0])
    T3 = Text("এবং", font="Li Oporajita Unicode", font_size=30)
    T3.next_to(M3,RIGHT)
    M4 = MathTex(r"b")
    #\left| x \right|
    M4.next_to(T3,RIGHT)
    T4 =  Text("এর মান নির্ণয় কর।", font="Li Oporajita Unicode", font_size=30)
    T4.next_to(M4,RIGHT)
    self.add(M,T1,M2,T2,M3,T3,M4,T4)
class T5(Scene):
  def construct(self):
    M =MathTex(r"\lim_{x \to 1} \frac{\sqrt{1-cos^{2}(x-1)}}{x-1} = ?");
    M.set_color(BLUE)
    M.move_to([-4,3,0])
    self.add(M)
class T6(Scene):
  def construct(self):
    M =MathTex(r"\lim_{x \to 0} \frac{lnx}{secx} = ?");
    M.scale(1.5)
    M.set_color(YELLOW)  
    M.move_to([-4,3,0])
    self.add(M)

class S(Scene):
  def construct(self):
    d1 = [-1,-1,0]
    d2 = [-1,3,0]
    d3 = [2,-1,0]
    self.play(Create(Dot(d1).set_color(BLUE)),Create(Dot(d2)),Create(Dot(d3).set_color(YELLOW)),run_time=1)
    l1 = Line(d1,d2).set_color(ORANGE)
    l2 = Line(d2,d3).set_color(YELLOW)
    l3 = Line(d3,d1).set_color(TEAL)
    self.play(Create(l1),Create(l2),Create(l3),run_time=2)
    arc = Arc(radius=0.5,start_angle=0,angle=3.1416/2,arc_center=np.array([-1,-1,0]),num_components=90)
    t = MathTex(r"90^{\circ }");
    t.set_color(BLUE)
    t.move_to([-0.1,-0.7,0])
    self.play(Write(arc),Create(t),run_time = 2)
    self.wait(1)
class S2(Scene):
  def construct(self):
    d1 = [-1,-1,0]
    d2 = [-1,3,0]
    d3 = [2,-1,0]
    self.add(Dot(d1).set_color(BLUE),Dot(d2),Dot(d3).set_color(YELLOW))
    l1 = Line(d1,d2).set_color(ORANGE)
    l2 = Line(d2,d3).set_color(YELLOW)
    l3 = Line(d3,d1).set_color(TEAL)
    self.add(l1,l2,l3)
    arc = Arc(radius=0.5,start_angle=0,angle=3.1416/2,arc_center=np.array([-1,-1,0]),num_components=90)
    t = MathTex(r"90^{\circ }");
    t.set_color(BLUE)
    t.move_to([-0.1,-0.7,0])
    self.add(arc,t)
    i1 = Line(d3,d2).set_color("#FF1111")
    self.play(Write(i1),run_time = 1.25);
    self.play(i1.animate.scale(1.1),run_time = 0.25);

    
    
    arrowv = Transform(i1,Arrow(start=np.array([0.5,1,0]),end = np.array([1,2,0])))
    
    self.play(arrowv,run_time=1)
    t = Text("অতিভূজ",font="Li Oporajita Unicode",font_size=30);
    t.move_to([1,2.5,0])
    self.play(Create(t),run_time = 1)

    i2 = Line(d1,d2).set_color("#FF1111")
    self.play(Write(i2),run_time = 1.25);
    self.play(i2.animate.scale(1.1),run_time = 0.25);

    
    
    arrowv2 = Transform(i2,Arrow(start=np.array([-1.5,0,0]),end = np.array([-1.5,-1,0])))
    
    self.play(arrowv2,run_time=1)
    t = Text("লম্ব",font="Li Oporajita Unicode",font_size=30);
    t.next_to(np.array([-1.5,-1,0]),DOWN)
    self.play(Create(t),run_time = 1)

    i3 = Line(d3,d1).set_color("#FF1111")
    self.play(Write(i3),run_time = 1.25);
    self.play(i3.animate.scale(1.1),run_time = 0.25);

    
    
    arrowv = Transform(i3,Arrow(start=np.array([0.5,-1,0]),end = np.array([0.5,-2.5,0])))
    
    self.play(arrowv,run_time=1)
    t = Text("ভূমি",font="Li Oporajita Unicode",font_size=30);
    t.next_to(np.array([0.25,-2.5,0]),RIGHT)
    self.play(Create(t),run_time = 1)
class S3(Scene):
  def construct(self):
    t = MathTex(r"r^{2}= x^{2} + y^{2}")
    t.scale(1.1)
    self.play(Write(t),run_time =3)
    self.wait(3)
    
    
    




