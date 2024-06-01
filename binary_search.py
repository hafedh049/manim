from manim import *

class BinarySearch(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=PURPLE,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        title = Text("BINARY SEARCH",font_size=120,t2c={"BINARY":BLUE,"SEARCH":"ORANGE"})

        self.play(Create(title))

        
        self.wait(2)
        
        self.play(Uncreate(title))

        numbers = sorted([-1,0,-9,4,7,5,2,17,20,11])
        array = [Square(side_length=1).add(MathTex(rf'{numbers[0]}'))]
        
        for i in range(1,10):
            array.append(Square(side_length=1).add(MathTex(rf'{numbers[i]}')).next_to(array[i - 1],buff=0))
                
        list = VGroup(*array).move_to(ORIGIN)
        self.play(Create(stream_lines))
        self.wait(5)
        self.remove(stream_lines)
        self.play(Create(list),run_time=2)
        self.wait()
        
        indexes_list = []
        for i in range(10):
            indexes_list.append(MathTex(rf"{i}",color = GREEN,font_size = 30).next_to(array[i],UP,buff=1))
        
        indexes = VGroup(*indexes_list)
        self.play(Create(indexes))

        target = MathTex(r"\text{let }x = " + str(numbers[-2]),font_size = 35).to_corner(LEFT + UP)
        self.play(Create(target))

        start, end,middle = 0, len(array) - 1,len(array)//2
        start_arrow = Arrow(start = indexes_list[start].get_bottom(),end = array[start].get_top(),color = RED)
        end_arrow = Arrow(start = indexes_list[end].get_bottom(),end = array[end].get_top(),color = RED)

        self.play(GrowArrow(start_arrow),GrowArrow(end_arrow),*[ApplyMethod(item.set_color,RED) for item in array[start:end + 1]],*[ApplyMethod(item.set_color,WHITE) for item in array[0:start] + array[end:len(array)-1]])
        
        first_step = MathTex(r"middle = \frac{start + end}{2} =",font_size = 35).next_to(array[0].get_corner(DOWN+LEFT),DOWN,aligned_edge=LEFT,buff=.3)
        first_step_exp = MathTex(r"\frac{"f"{start} + {end}"r"}""{2}",font_size = 35).next_to(first_step,buff=.09)
        middle_value = MathTex(fr"{(start+end)//2}",font_size = 35).next_to(first_step,buff=.09)
        self.play(Create(first_step),run_time=3)
        self.play(Create(first_step_exp),run_time=3)
        self.play(ReplacementTransform(first_step_exp,middle_value),run_time=3)
        middle_arrow = Arrow(start = indexes_list[(start + end) // 2].get_bottom(),end = array[(start + end) // 2].get_top(),color = GOLD)
        self.play(GrowArrow(middle_arrow),run_time=3)

        equality = MathTex(r"T[middle] = x : \text{Element exist}",font_size = 35).next_to(first_step.get_corner(DOWN+LEFT),DOWN,aligned_edge=LEFT,buff=.3)
        less = MathTex(r"T[middle] > x : \text{Element lies in the left side},\;end = middle - 1",font_size = 35,tex_to_color_map={"end = middle - 1":BLUE}).next_to(equality.get_corner(DOWN+LEFT),DOWN,aligned_edge=LEFT,buff=.3)
        greater = MathTex(r"T[middle] < x : \text{Element lies in the right side},\;start = middle + 1",font_size = 35,tex_to_color_map={"start = middle + 1":BLUE}).next_to(less.get_corner(DOWN+LEFT),DOWN,aligned_edge=LEFT,buff=.3)
        second_step = VGroup(equality,less,greater)

        self.play(Create(second_step))

        element = numbers[-2]
        self.wait(2)
        while start <= end:
            middle = (start + end) // 2
             
            self.play(ApplyMethod(middle_arrow.move_to,Line(indexes_list[middle].get_bottom(),list[middle].get_top())),run_time=.3)
            if numbers[middle] == element:
                for index in range(len(second_step.submobjects)):
                    if index == 0:
                        self.play(FadeToColor(second_step.submobjects[0],GREEN))
                        self.play(Circumscribe(second_step.submobjects[0]),Circumscribe(list[-2]),run_time = 2)
                        self.wait()
                        break
                break
            elif element < numbers[middle]:
                for index in range(len(second_step.submobjects)):
                    self.play(FadeToColor(second_step.submobjects[index],GREEN if index == 1 else RED),run_time = 1.25)
                    if index == 1:    
                        break
                end = middle - 1
            else:
                for index in range(len(second_step.submobjects)):
                    self.play(FadeToColor(second_step.submobjects[index],GREEN if index == 2 else RED),run_time = 1.25)
                    if index == 2:    
                        break
                start = middle + 1 
            self.play(*[ApplyMethod(item.set_color,RED) for item in array[start:end + 1]],*[ApplyMethod(item.set_color,WHITE) for item in array[0:start] + array[end:len(array)-1]],ApplyMethod(start_arrow.move_to,Line(indexes_list[start].get_bottom(),list[start].get_top())),ApplyMethod(end_arrow.move_to,Line(indexes_list[end].get_bottom(),list[end].get_top())))
            self.play(*[FadeToColor(second_step.submobjects[index],WHITE) for index in range(len(second_step.submobjects))])

            first_step_exp = MathTex(r"\frac{"f"{start} + {end}"r"}""{2}",font_size = 35).next_to(first_step,buff=.09)
            self.play(ReplacementTransform(middle_value,first_step_exp))
            middle_value = MathTex(fr"{(start+end)//2}",font_size = 35).next_to(first_step,buff=.09)
            self.wait(.75)
            self.play(ReplacementTransform(first_step_exp,middle_value))
            self.wait(1.5)