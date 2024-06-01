from manim import *
from random import choice

class DragonCurve(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        init = [["L","L","R"],["LLR","RLL","LRR"],["LLRLLRR","RRLLRLL","LLRRLRR"],["LLRLLRRLLLRRLRR","RRLRRLLLRRLLRLL","LLRLLRRRLLRRLRR"]]
        first = Text(init[0][0],font_size = 27).to_corner(LEFT+UP)
        aces = [first]
        self.play(Create(first))
        first_arrow = MathTex(r"=>",color = GREEN,font_size = 33).next_to(first)
        self.play(Create(first_arrow))
        reverse_text = Text(init[0][1],color=RED,font_size = 27).next_to(first_arrow,buff=.1)
        self.play(Create(reverse_text))
        second_arrow = MathTex(r"=>",color = GREEN,font_size = 33).next_to(reverse_text)
        self.play(Create(second_arrow))
        interchange_text = Text(init[0][2],color=GOLD,font_size = 27).next_to(second_arrow,buff=.1)
        self.play(Create(interchange_text))
        
        for i in range(1,len(init)):
            first = Text(init[i][0],font_size = 27).next_to(aces[i - 1],direction = DOWN,aligned_edge=LEFT)
            aces.append(first)
            self.play(Create(first))
            first_arrow = MathTex(r"=>",color = GREEN,font_size = 33).next_to(first)
            self.play(Create(first_arrow))
            reverse_text = Text(init[i][1],color=RED,font_size = 27).next_to(first_arrow,buff=.1)
            self.play(Create(reverse_text))
            second_arrow = MathTex(r"=>",color = GREEN,font_size = 33).next_to(reverse_text)
            self.play(Create(second_arrow))
            interchange_text = Text(init[i][2],color=GOLD,font_size = 27).next_to(second_arrow,buff=.1)
            self.play(Create(interchange_text))

        
        self.clear()
        self.play(Restore(self.camera.frame))
        lets = Text("UNLEACH THE DRAGON",color = PINK)
        self.play(Create(lets))
        self.wait()
        self.play(Uncreate(lets))
            
        
        dragon_holder :list= [Line(start=DOWN,end=ORIGIN)]
        dragon_string:str = "L"
        counter:int = 0
        while counter < 10:
            dragon_string= self.dragon_builder(dragon_string)
            counter += 1
       
        self.play(Create(dragon_holder[0]),run_time=.05)
        k = 1
        counter = 1
        vbox = VGroup()
        colors = color_gradient([BLUE,GREEN,PINK,RED,ORANGE,WHITE],len(dragon_string))
        print(len(colors))
        for dragon in dragon_string[1:]:
            k += 1 if dragon == "L" else -1
            line = Line(start=dragon_holder[-1].get_end(),end =self.end_point(dragon_holder[-1].get_end(),k*np.pi/2),color = colors[counter%len(colors)])
            vbox.add(line)
            dragon_holder.append(line)
            self.play(Create(dragon_holder[-1]),run_time=.05)
            self.play(self.camera.frame.animate.move_to(dragon_holder[-1]),run_time=.05)
            counter += 1
        
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(vbox.get_center()))
        self.play(self.camera.frame.animate.scale(4.2))

        self.wait(2)

        self.clear()
        self.play(Restore(self.camera.frame))
        conc = Text("Dragon Curve",t2c={"Dragon":BLUE,"Curve":RED})
        expr = MathTex(r"\begin{cases} n = 2^{ i + 1} - 1 \\i = \log_2(n + 1) - 1\end{cases}").next_to(conc,DOWN,.3)
        
        group = VGroup(conc,expr).move_to(ORIGIN).scale(1.7)

        self.play(Create(group))
        self.wait()
        self.play(Circumscribe(expr))
        self.wait()
        self.play(Uncreate(group))
        self.wait()

    def dragon_builder(self,old_dragon:str)->str: 
        new_dragon = ""
        for dragon in old_dragon[::-1]:
            new_dragon += "L" if dragon == "R" else "R"

        return "L".join([old_dragon,new_dragon])
    
    def end_point(self,start,angle):
        return start + np.array([np.cos(angle),np.sin(angle),0])