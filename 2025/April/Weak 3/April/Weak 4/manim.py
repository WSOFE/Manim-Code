from manim import*
config.pixel_height = 860
config.pixel_width = 1526
class T1(Scene):
  def construct(self):

    T3 = Text("কিছু গুরুত্বপূর্ণ ধারা", font="Li Oporajita Unicode", font_size=30)
    T3.move_to([0,3.7,0]);
    T3.set_color(ORANGE)
    self.add(T3)

    self.add(T3)
    m1 =MathTex(r"e^{x} = 1 + \frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!} ... \; ...\;..");
    m1.move_to([-2.5,3,0]);
    m1.scale(0.8)
    m1.set_color(YELLOW)
    self.add(m1)
    m2 =MathTex(r"e^{-x} = 1 - \frac{x}{1!}+\frac{x^{2}}{2!}-\frac{x^{3}}{3!}+\frac{x^{4}}{4!} ... \; ...\;..");
    
    m2.next_to(m1,DOWN)
    
    m2.scale(0.8)
    m2.set_color(YELLOW)
    self.add(m2)

    m3 =MathTex(r"sinx = x -\frac{x^{3}}{3}+\frac{x^{5}}{5}-\frac{x^{7}}{7} ... \; ...\;...");
    
    m3.next_to(m2,DOWN)
    m3.scale(0.8)
    m3.set_color(YELLOW)
    self.add(m3)

    m4 =MathTex(r"tanx = x + \frac{x^{3}}{3}+\frac{2x^{5}}{15}... \; ...\;...");
    
    m4.next_to(m3,DOWN)
    m4.scale(0.8)
    m4.set_color(YELLOW)
    self.add(m4)
    m5 = MathTex(r"ln(1+x) = x - \frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\frac{x^{5}}{5} -... \; ...\;...")
    m5.next_to(m4,DOWN)
    
    m5.scale(0.8)
    m5.set_color(YELLOW)
    self.add(m5)
    m6 = MathTex(r"ln(1-x) = -x - \frac{x^{2}}{2}-\frac{x^{3}}{3}-\frac{x^{4}}{4}-\frac{x^{5}}{5} -... \; ...\;...")
    m6.next_to(m5,DOWN)
    
    m6.scale(0.8)
    m6.set_color(YELLOW)
    self.add(m6)
    

class T2(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to 0} \frac{sinx}{x} = ?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T3(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to 0} \frac{tanx}{x} = ?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T4(Scene):
  def construct(self):
    T3 = Text("কিছু অনুসিদ্ধান্ত", font="Li Oporajita Unicode", font_size=30)
    T3.move_to([0,3.7,0]);
    T3.set_color(ORANGE)
    self.add(T3)
        

    M = MathTex(r"\lim_{x \to 0} \frac{\sin^{-1}x}{x} = 1")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])
    M2 = MathTex(r"\lim_{x \to 0} \frac{\tan^{-1}x}{x} = 1")
    M2.set_color(YELLOW)
    M2.next_to(M,DOWN)



    self.add(M,M2)
class T5(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to 0} \frac{ln(1+x)}{x} = ?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T6(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to 0} \frac{e^{x}-1}{x} = ?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T7(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to 0} (1+x)^{\frac{1}{x}} =?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T8(Scene):
  def construct(self):
    

    M = MathTex(r"\lim_{x \to \infty } (1+\frac{1}{x})^{x} =?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T9(Scene):

  def construct(self):
    

    M = MathTex(r"\lim_{x \to a }\frac{x^{n}-a^{n}}{x-a} =?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)
class T10(Scene):
  
  def construct(self):
    

    M = MathTex(r"\lim_{x \to a }\frac{x^{n}-a^{m}}{x^{n}-a^{n}} =?")
    M.set_color(YELLOW)
    

    M.move_to([-4.2,3,0])


    self.add(M)


