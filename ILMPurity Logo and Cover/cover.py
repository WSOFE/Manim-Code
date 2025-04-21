from manim import *
config.pixel_height =315*10
config.pixel_width = 851*10

class T(Scene):
  def construct(self):
    T1 = Text("আল্লাহ সর্ববিষয়ে সর্ব শক্তিমান", font="Li Oporajita Unicode", font_size=30)
    T2 = Text("আল-কুরআন(২ , ২৮৪)", font="Li Oporajita Unicode", font_size=30)
    T2.next_to(T1,2*DOWN)
    
    T1.scale(2)
    T1.set_color(ORANGE)
    self.add(T1,T2)