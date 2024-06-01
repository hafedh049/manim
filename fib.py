from manim import *
def fibo(n):
    if n == 0:
        return 0
    elif n in [1,2]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

class Fib(Scene):
    def construct(self):
        seq = MathTex(r", ".join(
            ["0", "1", "1", "2", "3", "5", "8", "..."]), font_size=85)
        self.play(Write(seq), run_time=6)
        self.wait()
        fib = Text(r"Fibonacci Sequence", font_size=100, t2c={
                   "Fibonacci": BLUE, "Sequence": PURPLE})
        self.play(ReplacementTransform(seq, fib))
        self.wait(2)
        fib_form = MathTex(
            r"\begin{cases}F_0 = 1,\:\:\: F_1 = 1\\F_n = F_{n - 1} + F_{n - 2} \:\:\:, n > 1\end{cases}")
        self.play(ReplacementTransform(fib, fib_form))
        self.wait()
        fibs = [fibo(n) for n in range(8)]
        polar_plane = Axes(x_length=config.frame_width // 2)
        graph = polar_plane.plot_polar_graph(lambda theta:1-np.sin(theta),color = RED)
        self.play(ReplacementTransform(fib_form, polar_plane))
        n = MathTex(fr"n = {1}",tex_to_color_map={str(1):RED}).next_to(polar_plane,LEFT)
        fn = MathTex(fr"F_{1} = {fibs[1]}",tex_to_color_map={str(1):RED,str(fibs[1]):RED}).next_to(n, DOWN, 1)
        self.play(Create(n),Create(fn),Create(graph))
        for i in range(2,8):
            new_n = MathTex(str(i).join([r"n = {",r"}"]),tex_to_color_map={str(i):RED}).next_to(polar_plane,LEFT)
            new_fn = MathTex(str(i).join([r"F_{",r"} = "+str(fibs[i])]),tex_to_color_map={str(i):RED,str(fibs[i]):RED}).next_to(n, DOWN, 1)
            new_graph = polar_plane.plot_polar_graph(lambda theta:1-np.sin(fibs[i] * theta),color = RED)
            self.play(ReplacementTransform(n,new_n),ReplacementTransform(fn,new_fn),ReplacementTransform(graph,new_graph),run_time = 1.5)
            n,fn,graph = new_n,new_fn,new_graph
        
        self.wait(2)
        self.clear()
        frac = MathTex(r"\lim_{n \to \infty} \frac{F_{n + 1}}{F_n}",font_size = 80,color = GOLD)
        self.play(Write(frac))
        self.wait(2)
        self.play(ApplyMethod(frac.move_to,2*LEFT),run_time = .5)
        phi_dec = MathTex(r" =  1.61...",font_size = 80,color = GOLD).next_to(frac)
        self.play(Write(phi_dec),run_time = .5)
        self.wait()
        self.play(Uncreate(phi_dec),Uncreate(frac))
        self.wait()
        golden_ratio = MathTex(r"\text{GOLDEN RATIO}",font_size = 80,color = GOLD).shift(2*UP)
        phi_exp = MathTex(r"\phi = \frac{1 + \sqrt{5}}{2} = 1.61...",font_size = 80,color = GOLD).next_to(golden_ratio,DOWN,1)
        self.play(Write(golden_ratio))
        self.play(Write(phi_exp))
        self.wait()
        self.clear()
        self.wait()
        rule1 = MathTex(r"\phi = 1 + \phi^{-1}",font_size = 80,color = BLUE).shift(2.5*UP)
        rule2 = MathTex(r"\phi^2 = \phi + 1",font_size = 80,color = GREEN).next_to(rule1,DOWN,.55)
        rule3 = MathTex(r"\phi^n = \phi^{n - 1} + \phi^{n - 2},\:\:\:n > 2",font_size = 80,color = RED).next_to(rule2,DOWN,.55)
        rule4 = MathTex(r"\phi = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + ...}}}",font_size = 80,color = RED).next_to(rule3,DOWN,.55)
        self.play(Write(rule1))
        self.play(Write(rule2))
        self.play(Write(rule3))
        self.play(Write(rule4),run_time = 2)
        self.wait()
        self.clear()
        bonus = MathTex(r"\frac{1}{89} = 0.",font_size = 80,color = ORANGE)
        mapper = {"0":MathTex(fr"{fibo(0)}",font_size = 80,color = ORANGE).next_to(bonus)}
        for i in range(1,6):
            mapper[str(i)] = MathTex(fr"{fibo(i)}",font_size = 80,color = ORANGE).next_to(mapper[str(i - 1)],buff=.1)
        complete_b = VGroup(bonus,*mapper.values()).move_to(ORIGIN)
        self.play(Write(complete_b))
        arrows = [Line(start=UP,end=UP * .3).next_to(item,UP) for item in mapper.values()]
        headers = [MathTex(fr"F_{i}",font_size = 35,color = BLUE,tex_to_color_map={str(i):GOLD}).next_to(arrows[i],UP) for i in range(6)]
        for i in range(6):
            self.play(Write(arrows[i]),Write(headers[i]),run_time = .15)

        self.wait(3)
        self.clear()
        self.play(Write(Text("END.",font_size=120,color=BLUE)),run_time = 2)
        self.wait(2.5)