from manim import *
class T(Scene):
  def construct(self):
    ax = NumberPlane();
    ax.set_color(GRAY)
    self.add(ax);
    graph=ax.plot(lambda x:np.sin(x))
    graph2 = ax.plot(lambda x:np.tan(x));
    self.add(graph2,graph);
class T2(Scene):
  def construct(self):
    ax =PolarPlane();
    ax.set_color(GRAY)
    self.add(ax);
class T3(Scene):
  def construct(self):
    ax =RegularPolygon(10);
    ax.scale(3)
    ax.set_color(GRAY)
    ax2 =RegularPolygon(13);
    ax2.scale(2)
    ax2.set_color(TEAL)
    self.add(ax2,ax);
    # graph=ax.plot(lambda x:np.sin(x))
    # graph2 = ax.plot(lambda x:np.tan(x));
    # self.add(graph2,graph);