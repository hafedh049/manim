from manim import *

class ElevenMult(Scene):
    def construct(self):

        digit =  MathTex(r'7',font_size=80,color = RED)
        mult = MathTex(r"*",font_size=80).next_to(digit,RIGHT,.8)
        eleven = MathTex(r"11",font_size=80).next_to(mult,RIGHT,.8)
        eq = MathTex(r"=",font_size=80).next_to(eleven,RIGHT,.8)

        holder = VGroup(digit,mult,eleven,eq)

        self.play(Write(holder.move_to(ORIGIN)))
        self.play(ApplyMethod(holder.move_to,LEFT))
        self.wait()
        self.play(ApplyMethod((cpy := digit.copy()).next_to,eq,RIGHT,.8))
        self.play(ApplyMethod(cpy.copy().next_to,cpy,RIGHT,.04))

        self.wait(4.5)
        self.clear()

        decimal =  MathTex(r'4',font_size=80,color = RED)
        unit =  MathTex(r'3',font_size=80,color = BLUE).next_to(decimal,RIGHT,.04)
        mult = MathTex(r"*",font_size=80).next_to(unit,RIGHT,.8)
        eleven = MathTex(r"11",font_size=80).next_to(mult,RIGHT,.8)
        eq = MathTex(r"=",font_size=80).next_to(eleven,RIGHT,.8)
 
        holder = VGroup(decimal,unit,mult,eleven,eq)

        self.play(Write(holder.move_to(ORIGIN)))
        self.play(ApplyMethod(holder.move_to,2*LEFT))
        self.wait()
        
        self.play(ApplyMethod((deccpy := decimal.copy()).next_to,eq,RIGHT,.8))
        self.play(ApplyMethod((unicpy := unit.copy()).next_to,deccpy,RIGHT,3))
        
        
        left_par = MathTex(r"(",font_size=80).next_to(deccpy,RIGHT)
        right_par = MathTex(r")",font_size=80).next_to(unicpy,LEFT)

        self.play(Create(left_par),Create(right_par))

        plus = MathTex(r"+",font_size=80).move_to((left_par.get_center() + right_par.get_center()) / 2)
        self.play(Create(plus))

        self.play(ApplyMethod((deccpy_ := decimal.copy()).next_to,plus,LEFT))
        self.play(ApplyMethod((unicpy_ := unit.copy()).next_to,plus,RIGHT))

        self.play(ReplacementTransform(VGroup(left_par,deccpy_,plus,unicpy_,right_par),res := MathTex(r"7",color = GOLD,font_size=80).move_to((deccpy.get_center() + unicpy.get_center()) / 2)))
        self.play(ApplyMethod(res.next_to,deccpy,RIGHT,.08))
        self.play(ApplyMethod(unicpy.next_to,res,RIGHT,.08))

        self.wait(3)
        self.clear()

        decimal =  MathTex(r'9',font_size=80,color = RED)
        unit =  MathTex(r'9',font_size=80,color = BLUE).next_to(decimal,RIGHT,.04)
        mult = MathTex(r"*",font_size=80).next_to(unit,RIGHT,.8)
        eleven = MathTex(r"11",font_size=80).next_to(mult,RIGHT,.8)
        eq = MathTex(r"=",font_size=80).next_to(eleven,RIGHT,.8)
 
        holder = VGroup(decimal,unit,mult,eleven,eq)

        self.play(Write(holder.move_to(ORIGIN)))
        self.play(ApplyMethod(holder.move_to,2*LEFT))
        self.wait()
        
        self.play(ApplyMethod((deccpy := decimal.copy()).next_to,eq,RIGHT,.8))
        self.play(ApplyMethod((unicpy := unit.copy()).next_to,deccpy,RIGHT,3))
        
        
        left_par = MathTex(r"(",font_size=80).next_to(deccpy,RIGHT)
        right_par = MathTex(r")",font_size=80).next_to(unicpy,LEFT)

        self.play(Create(left_par),Create(right_par))

        plus = MathTex(r"+",font_size=80).move_to((left_par.get_center() + right_par.get_center()) / 2)
        self.play(Create(plus))

        self.play(ApplyMethod((deccpy_ := decimal.copy()).next_to,plus,LEFT))
        self.play(ApplyMethod((unicpy_ := unit.copy()).next_to,plus,RIGHT))


        res_dec = MathTex(r"1", color = GREEN,font_size=80)
        res_uni = MathTex(r"8", color = PINK,font_size=80).next_to(res_dec)
        self.play(ReplacementTransform(VGroup(left_par,deccpy_,plus,unicpy_,right_par),res := VGroup(res_dec,res_uni).move_to((deccpy.get_center() + unicpy.get_center()) / 2)))
        self.play(ApplyMethod(res.next_to,deccpy))
        self.play(ApplyMethod(unicpy.next_to,res))
        self.play(ApplyMethod(unicpy.next_to,res))
        self.play(ApplyMethod(res_dec.scale,.5))
        upd_res_dec = res_dec.add(MathTex(r"+", color = GREEN,font_size=80).scale(.4).next_to(res_dec,LEFT,buff = .01))
        self.play(ApplyMethod(upd_res_dec.move_to,deccpy.get_top() + [0,.5,0]))
        self.play(Uncreate(upd_res_dec),ApplyMethod(deccpy.become,r := MathTex(r'10',font_size=80,color = GOLD).next_to(eq,RIGHT,.8)))
        self.play(ApplyMethod(res_uni.next_to,r,RIGHT,.08),run_time=.8)
        self.play(ApplyMethod(unicpy.next_to,res_uni,RIGHT,.08),run_time=.8)
        self.wait()
        self.clear()
        self.wait()

        conc = Text("Multiplication By 11",t2c={"Multiplication":BLUE,"By":RED,"11":GOLD})
        expr = MathTex(r"ab * 11 =\begin{cases}a(a+b)b & \text{if } a + b < 10 \\(a + 1)((a + b) - 10)b & \text{otherwise}\end{cases}",font_size = 60).next_to(conc,DOWN,.3)
        
        group = VGroup(conc,expr).move_to(ORIGIN)

        self.play(Create(group))
        self.wait()
        self.play(Circumscribe(expr))
        self.wait()
        self.play(Uncreate(group))
        self.wait()