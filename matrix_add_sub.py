from manim import *

class MatrixAddSub(Scene):
    def construct(self):
        matrix_addition = Text("Matrix Addition",font_size=120,t2c={"Matrix":ORANGE,"Addition":BLUE})
        self.play(Create(matrix_addition))
        self.wait(8)
        a_eq = MathTex(r"A = ",color = BLUE)
        A = Matrix([[4,8],[3,7]],element_to_mobject_config={"tex_to_color_map":{"4":BLUE,"3":BLUE,"8":BLUE,"7":BLUE}}).next_to(a_eq)
        b_eq = MathTex(r"B = ",color = RED).next_to(A,RIGHT,1)
        B = Matrix([[1,0],[5,2]],element_to_mobject_config={"tex_to_color_map":{"1":RED,"0":RED,"5":RED,"2":RED}}).next_to(b_eq)
        A_B_holder = VGroup(a_eq,A,b_eq,B).move_to(ORIGIN)
        self.play(ReplacementTransform(matrix_addition,A_B_holder),run_time = 4)
        self.wait()
        left_hand = MathTex(r"A + B = ",tex_to_color_map={"A":BLUE,"+":GOLD,"B":RED})
        sum_matrix1 = Matrix([["4 + 1","8 + 0"],["3 + 5","7 + 2"]],h_buff=2,element_to_mobject_config={"tex_to_color_map":{"4":BLUE,"3":BLUE,"8":BLUE,"7":BLUE,"+":GOLD,"1":RED,"0":RED,"5":RED,"2":RED}}).next_to(left_hand) 
        init_holder = VGroup(left_hand,sum_matrix1).move_to(ORIGIN+2*DOWN)
        shifted_ab = A_B_holder.copy()
        self.play(ApplyMethod(shifted_ab.shift,2*UP),run_time = 2)
        self.play(ReplacementTransform(A_B_holder,init_holder),run_time = 2)
        a_rows = shifted_ab[1].get_rows().submobjects
        b_rows = shifted_ab[3].get_rows().submobjects
        res = [j for i in sum_matrix1.get_rows() for j in i]
        k = 0
        for row in zip(a_rows,b_rows):
            for item in zip(row[0].submobjects,row[1].submobjects):
                self.play(Circumscribe(item[0]),Circumscribe(item[1]),Circumscribe(res[k]))
                k += 1
        self.wait()
        final_matrix = Matrix([["5","8"],["8","9"]],element_to_mobject_config={"color":ORANGE}).next_to(left_hand) 
        final_holder = VGroup(left_hand.copy(),final_matrix).move_to(ORIGIN)
        self.play(Uncreate(shifted_ab),ReplacementTransform(init_holder,final_holder))
        self.wait()

        matrix_sub = Text("Matrix Substraction",font_size=100,t2c={"Matrix":ORANGE,"Addition":BLUE})
        self.play(ReplacementTransform(final_holder,matrix_sub))
        self.wait()
        a_eq = MathTex(r"F = ",color = BLUE)
        A = Matrix([[4,8,1],[0,3,7],[10,4,-9]],element_to_mobject_config={"tex_to_color_map":{str(num):BLUE for num in range(-9,9)}}).next_to(a_eq)
        b_eq = MathTex(r"G = ",color = RED).next_to(A,RIGHT,1)
        B = Matrix([[5,2,-6],[-1,-5,-3],[6,2,-7]],element_to_mobject_config={"tex_to_color_map":{str(num):RED for num in range(-7,7)}}).next_to(b_eq)
        A_B_holder = VGroup(a_eq,A,b_eq,B).move_to(ORIGIN)
        self.play(ReplacementTransform(matrix_sub,A_B_holder),run_time = 2)
        self.wait()
        left_hand = MathTex(r"F + G = ",tex_to_color_map={"F":BLUE,"-":GOLD,"G":RED})
        sum_matrix1 = Matrix([["4 - 5","8 - 2","1 - (-6)"],["0 - (-1)","3 - (-5)","7 - (-3)"],["10 - 6","4 - 2","(-9) - (-7)"]],element_alignment_corner=ORIGIN,h_buff=3.5,element_to_mobject_config={"tex_to_color_map":{**{str(i):BLUE for i in [4,8,1,0,3,7,10,-9]},**{str(i):RED for i in [5,-6,-1,-5,-3,6,2,-7]}}}).next_to(left_hand) 
        init_holder = VGroup(left_hand,sum_matrix1).move_to(ORIGIN+2*DOWN)
        shifted_ab = A_B_holder.copy()
        self.play(ApplyMethod(shifted_ab.shift,2*UP))
        self.play(ReplacementTransform(A_B_holder,init_holder))
        a_rows = shifted_ab[1].get_rows().submobjects
        b_rows = shifted_ab[3].get_rows().submobjects
        res = [j for i in sum_matrix1.get_rows() for j in i]
        k = 0
        for row in zip(a_rows,b_rows):
            for item in zip(row[0].submobjects,row[1].submobjects):
                self.play(Circumscribe(item[0]),Circumscribe(item[1]),Circumscribe(res[k]))
                k += 1
        
        self.wait()
        final_matrix = Matrix([["-1","6","7"],["1","8","10"],["4","2","-2"]],h_buff=2,element_to_mobject_config={"color":ORANGE}).next_to(left_hand) 
        final_holder = VGroup(left_hand.copy(),final_matrix).move_to(ORIGIN)
        self.play(Uncreate(shifted_ab),ReplacementTransform(init_holder,final_holder))
        self.wait()



        matrix_smult = Text("Matrix Scalar\nMultiplication",font_size=100,t2c={"Matrix":ORANGE,"Multiplication":BLUE,"Scalar":GREEN})
        self.play(ReplacementTransform(final_holder,matrix_smult))
        self.wait()
        a_eq = MathTex(r"A = ",color = BLUE)
        A = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],element_to_mobject_config={"tex_to_color_map":{"1":BLUE}}).next_to(a_eq)
        scalar = MathTex(r"\;\;*\;\;\frac{1}{2}",color=YELLOW,tex_to_color_map={"*":WHITE}).next_to(A)
        A_holder = VGroup(a_eq,A,scalar).move_to(ORIGIN)
        self.play(ReplacementTransform(matrix_smult,A_holder),run_time = 2)
        self.wait()
        entries = A.get_entries().submobjects
        arrows = []
        for entry in entries:
            arrow = Arrow(scalar.get_center(),entry.get_center(),color=RED)
            arrows.append(arrow)
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait()
        new_A = Matrix([[r"1 * \frac{1}{2}",r"0 * \frac{1}{2}",r"0 * \frac{1}{2}",r"0 * \frac{1}{2}"],[r"0 * \frac{1}{2}",r"1 * \frac{1}{2}",r"0 * \frac{1}{2}",r"0 * \frac{1}{2}"],[r"0 * \frac{1}{2}",r"0 * \frac{1}{2}",r"1 * \frac{1}{2}",r"0 * \frac{1}{2}"],[r"0 * \frac{1}{2}",r"0 * \frac{1}{2}",r"0 * \frac{1}{2}",r"1 * \frac{1}{2}"]],v_buff=1.5,h_buff=1.5,element_to_mobject_config={"color":BLUE,"tex_to_color_map":{r"\frac{1}{2}":RED}}).next_to(a_eq)
        self.play(Uncreate(scalar),*[Uncreate(arrow) for arrow in arrows])
        self.play(ReplacementTransform(A,new_A))
        self.play(ReplacementTransform(new_A,Matrix([[r"\frac{1}{2}",r"0",r"0",r"0"],[r"0",r"\frac{1}{2}",r"0",r"0"],[r"0",r"0",r"\frac{1}{2}",r"0"],[r"0",r"0",r"0",r"\frac{1}{2}"]],v_buff=1.5,h_buff=1.5,element_to_mobject_config={"color":BLUE,"tex_to_color_map":{r"\frac{1}{2}":RED}}).next_to(a_eq)))
        self.wait(1)