from manim import *

class CollatzConjucture(MovingCameraScene):
    def construct(self):
        circ_digits = [Circle(radius=.8,color=WHITE).add(Text("1"))]
        self.camera.frame.save_state()
        vgroup = VGroup()
        for index in range(2,10):
            item = Circle(radius=.9,color=WHITE).add(Text(f"{index}")).next_to(circ_digits[-1],RIGHT,.5)
            circ_digits.append(item)
            vgroup.add(item)

        
        self.play(Create(vgroup))
        self.play(self.camera.frame.animate.move_to(item))

        self.play(self.camera.frame.animate.move_to(circ_digits[-1]))

        self.play(circ_digits[-1].animate.set_style(stroke_color= GREEN))
        
        self.wait()

        item = circ_digits.pop()
        number = 9

        self.play(*[Uncreate(itm) for itm in circ_digits])

        circ_digits.clear()
        circ_digits.append(item)

        while number != 1:
            old_number = number
            number = 3*number+1 if number % 2 != 0 else number // 2
            next_item = Circle(radius=.9,color=WHITE).add(Text(f"{number}")).next_to(circ_digits[-1],RIGHT,4)
            self.play(Create(next_item),run_time=.25)
            self.play(Create(Text("ODD" if number %2 !=0 else "EVEN",font_size=30).next_to(next_item,DOWN,.5)),run_time=.25)
            self.play(next_item.animate.set_style(stroke_color= GREEN))
            self.play(self.camera.frame.animate.move_to(next_item),run_time=.5)
            circ_digits.append(next_item)
            self.play(circ_digits[-2].animate.set_style(stroke_color=WHITE),run_time=.1)
            arrow = Arrow(circ_digits[-2],circ_digits[-1])
            self.play(Create(arrow),run_time=.25)
            self.play(Create(Text(f"3*({old_number}) + 1" if old_number %2 !=0 else f"{old_number} // 2",font_size=30,t2c={str(number):GREEN}).next_to(arrow,DOWN+ORIGIN,.3)),run_time=.25)

        self.play(Create(ArcBetweenPoints(circ_digits[-1].get_top(),circ_digits[-3].get_top())),self.camera.frame.animate.move_to(circ_digits[-3]),run_time=.7)
        
        counter = 1
        cpy = circ_digits[-3:]
        self.play(cpy[-1].animate.set_style(stroke_color= WHITE))
        while counter <= 6:
            self.play(self.camera.frame.animate.move_to(cpy[counter%3]),run_time=.8)
            self.play(cpy[counter%3].animate.set_style(stroke_color= GREEN))
            counter +=1    
            self.play(cpy[counter%3].animate.set_style(stroke_color= WHITE))
        
        self.wait(2)
        self.clear()
        self.play(Restore(self.camera.frame),run_time=.5)
        
        conc = Text("Collatz Conjecture",t2c={"Collatz":BLUE,"Conjecture":RED})
        expr = MathTex(r"f(x) =\begin{cases}3x + 1 & \text{if } x \text{ is ODD}\\x / 2 & \text{otherwise}\end{cases}").next_to(conc,DOWN,.3)
        
        group = VGroup(conc,expr).move_to(ORIGIN)

        self.play(Create(group))
        self.wait()
        self.play(Circumscribe(expr))
        self.wait()
        self.play(Uncreate(group))
        self.wait()