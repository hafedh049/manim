from manim import *

class Powers(Scene):
    def construct(self):
        scale:list = []
        with open("csv.csv") as csv:
            scale.extend([item.split(",") for item in csv.readlines()[37:]])

        name:MathTex = Text(f'{scale[0][0].title()}',font_size = 100,color = BLUE)
        number:MathTex = MathTex(scale[0][1].join([r"10^{",r"}"]),font_size = 100,tex_to_color_map = {scale[0][1]:GOLD}).next_to(name,DOWN,buff=2)
        holder:VGroup = VGroup(name,number).move_to(ORIGIN)
        self.play(Write(holder),run_time = .1)

        for item in range(1,len(scale)):
            if item < 22:
                self.wait(.5)
            elif item == 33:
                self.wait(1.6)
            else: 
                self.wait(.8)
            next_name = Text(f'{scale[item][0].title()}',font_size = 100,color = BLUE)
            next_number = MathTex(scale[item][1].join([r"10^{",r"}"]) ,font_size = 100,tex_to_color_map = {scale[item][1]:GOLD}).next_to(name,DOWN,buff=2)
            next_holder = VGroup(next_name,next_number).move_to(ORIGIN)
            self.play(ReplacementTransform(holder,holder := next_holder),run_time = .4)

        
        self.wait(.4)
        self.clear()
        
        conc = Text("Large Numbers Scale",t2c={"Large":BLUE,"Numbers":RED,"Scale":GOLD},font_size=100)
        
        self.play(Write(conc))
        self.wait(.5)
        self.play(Circumscribe(conc))
        self.wait(.5)
        self.play(Unwrite(conc))
