from manim import *


class ListMethods(Scene):
    def construct(self):
        # INTRO
        list_methods: Text = Text("List Methods", font_size=100, t2c={
                                  "List": BLUE, "Methods": GREEN})
        self.play(Write(list_methods))
        print([f".{item}" for item in dir(list) if not "_" in item])
        self.wait()
        self.play(FadeOut(list_methods))
        # APPEND
        appends_list: list = [Square(1.7).add(
            Text("0", font_size=35, color=RED_A))]
        appends: list = ["'🐍'", [None], 2 - 1j, "2e5"]
        for item in appends:
            appends_list.append(Square(1.7).add(Text(f"{item}", font_size=35, t2c={
                                "[None]": ORANGE, "2e5": GREEN, "(2-1j)": BLUE, "'🐍'": GOLD})).next_to(appends_list[appends.index(item)], buff=0))
        append_g: VGroup = VGroup(*appends_list).move_to(ORIGIN)
        self.play(FadeIn(append_g), run_time=2)
        self.play(ApplyMethod(append_g.add, Square(1.7).add(Text(
            "True", font_size=35, color=PINK)).next_to(appends_list[-1], buff=0)), run_time=2)
        self.play(ApplyMethod(append_g.move_to, ORIGIN))
        self.play(ApplyMethod(append_g.shift, UP + [0, .5, 0]))
        append_code = Code(background="window", style="fruity", font_size=30, font="Roboto", language="python",
                           file_name="list_methods_script.py", tab_width=4, line_spacing=1, background_stroke_width=1.5).next_to(append_g, DOWN, .8)
        self.play(Create(append_code))
        self.wait()
        self.play(Uncreate(append_g), Uncreate(append_code))
        # CLEAR
        clears_list: list = [Square(1.7).add(
            Text("3.14", font_size=35, color=RED_A))]
        clears: list = [-1, 2.17, "Hello", 10]
        for item in clears:
            clears_list.append(Square(1.7).add(Text(f"{item}", font_size=35, t2c={
                               "-1": ORANGE, "2.17": GREEN, "Hello": BLUE, "10": GOLD})).next_to(clears_list[clears.index(item)], buff=0))
        clear_g: VGroup = VGroup(*clears_list).move_to(ORIGIN)
        self.play(FadeIn(clear_g), run_time=2)
        empty = Text("[  ]").move_to(clear_g.get_center())
        self.play(ReplacementTransform(clear_g, empty))
        self.play(ApplyMethod(empty.shift, UP + [0, .5, 0]))
        clear_code = Code(background="window", font_size=30, code="#CLEARS THE LIST\nl = [-1, 2.17, 'Hello', 10]\nl.clear()", style="fruity",
                          font="Roboto", language="python", tab_width=4, line_spacing=1, background_stroke_width=1.5).next_to(clear_g, DOWN, .1)
        self.play(Create(clear_code))
        self.wait()
        self.play(Uncreate(empty), Uncreate(clear_code))
        # EXTENDS
        extends1_list: list = [Square(1.7).add(
            Text("None", font_size=35, color=RED_A))]
        extends1_list.append(Square(1.7).add(
            Text("1_000", font_size=35, color=GREEN)).next_to(extends1_list[-1], buff=0))
        extends2_list: list = [Square(1.7).add(
            Text("func", font_size=35, color=BLUE))]
        extends2_list.append(Square(1.7).add(
            Text("False", font_size=35, color=RED_A)).next_to(extends2_list[-1], buff=0))
        extends_g1: VGroup = VGroup(*extends1_list).move_to(ORIGIN)
        extends_g2: VGroup = VGroup(
            *extends2_list).next_to(extends_g1, RIGHT, 1)
        self.play(FadeIn(extends_g1), run_time=2)
        self.play(ApplyMethod(extends_g1.shift, 3.5*LEFT))
        self.play(FadeIn(extends_g2), run_time=2)
        link_arrow = Arrow(start=extends2_list[0].get_edge_center(
            LEFT), end=extends1_list[-1].get_edge_center(RIGHT))
        self.play(Create(link_arrow))
        self.wait()
        self.play(Uncreate(link_arrow))
        self.play(ApplyMethod(extends_g1.move_to, link_arrow.get_center(
        ), RIGHT), ApplyMethod(extends_g2.move_to, link_arrow.get_center(), LEFT))
        self.play(ApplyMethod(extends_g1.shift, 2 * UP),
                  ApplyMethod(extends_g2.shift, 2*UP))
        extend_code = Code(background="window", style="fruity", font_size=30, font="Roboto", language="python",
                           code="#CLEARS THE LIST\nl1 = [-1, 2.17, 'Hello', 10]\nl2 = [1, 2, 3]\nl1.extend(l2)", tab_width=4, line_spacing=1, background_stroke_width=1.5).next_to(link_arrow.get_center(), DOWN, .1)
        self.play(Create(extend_code))
        self.wait()
        self.play(Uncreate(extends_g1), Uncreate(
            extends_g2), Uncreate(extend_code))
        self.wait()
        #REVERSE
        reverse_list: list = [Square(1.7).add(
            Text("False", font_size=35, color=RED_A))]
        reverse_list.append(Square(1.7).add(
            Text("e", font_size=35, color=GREEN_A)).next_to(reverse_list[-1], buff=0))
        reverse_list.append(Square(1.7).add(
            Text("{ }", font_size=35, color=BLUE_A)).next_to(reverse_list[-1], buff=0))
        reverse_list.append(Square(1.7).add(
            Text("Python", font_size=35, color=GOLD_A)).next_to(reverse_list[-1], buff=0))
        reverse_list.append(Square(1.7).add(
            Text("♥", font_size=35, color=PURPLE_A)).next_to(reverse_list[-1], buff=0))
        reverse_list.append(Square(1.7).add(
            Text("2250", font_size=35, color=ORANGE)).next_to(reverse_list[-1], buff=0))
        reverse_g = VGroup(*reverse_list).move_to(ORIGIN)
        self.play(Create(reverse_g))
        self.wait()
        reversed_list: list = [Square(1.7).add(
            Text("2250", font_size=35, color=ORANGE))]
        reversed_list.append(Square(1.7).add(
            Text("♥", font_size=35, color=PURPLE_A)).next_to(reversed_list[-1], buff=0))
        reversed_list.append(Square(1.7).add(
            Text("Python", font_size=35, color=GOLD_A))  .next_to(reversed_list[-1], buff=0))
        reversed_list.append(Square(1.7).add(
            Text("{ }", font_size=35, color=BLUE_A)).next_to(reversed_list[-1], buff=0))
        reversed_list.append(Square(1.7).add(
            Text("e", font_size=35, color=GREEN_A)).next_to(reversed_list[-1], buff=0))
        reversed_list.append(Square(1.7).add(
            Text("False", font_size=35, color=RED_A)).next_to(reversed_list[-1], buff=0))
        reversed_g = VGroup(*sorted_list).move_to(ORIGIN)
        self.play(ReplacementTransform(reverse_g, reversed_g))

        self.play(ApplyMethod(reversed_g.shift, 2 * UP))
        reverse_code = Code(background="window", style="fruity", font_size=30, font="Roboto", language="python",
                           code="#REVERSE THE LIST\nl = ['False', e, { }, 'Python', '♥', 2250]\nl.reverse()", tab_width=4, line_spacing=1, background_stroke_width=1.5).next_to(link_arrow.get_center(), DOWN, .1)
        self.play(Create(reverse_code))
        self.wait()
        self.play(Uncreate(reversed_g), Uncreate(reverse_code))
        self.wait()
        #SORT
        sort_list: list = [Square(1.7).add(
            Text("False", font_size=35, color=RED_A))]
        sort_list.append(Square(1.7).add(
            Text("e", font_size=35, color=GREEN_A)).next_to(sort_list[-1], buff=0))
        sort_list.append(Square(1.7).add(
            Text("{ }", font_size=35, color=BLUE_A)).next_to(sort_list[-1], buff=0))
        sort_list.append(Square(1.7).add(
            Text("Python", font_size=35, color=GOLD_A)).next_to(sort_list[-1], buff=0))
        sort_list.append(Square(1.7).add(
            Text("♥", font_size=35, color=PURPLE_A)).next_to(sort_list[-1], buff=0))
        sort_list.append(Square(1.7).add(
            Text("2250", font_size=35, color=ORANGE)).next_to(sort_list[-1], buff=0))
        sort_g = VGroup(*sort_list).move_to(ORIGIN)
        self.play(Create(sort_g))
        self.wait()
        sorted_list: list = [Square(1.7).add(
            Text("2250", font_size=35, color=ORANGE))]
        sorted_list.append(Square(1.7).add(
            Text("♥", font_size=35, color=PURPLE_A)).next_to(sorted_list[-1], buff=0))
        sorted_list.append(Square(1.7).add(
            Text("Python", font_size=35, color=GOLD_A))  .next_to(sorted_list[-1], buff=0))
        sorted_list.append(Square(1.7).add(
            Text("{ }", font_size=35, color=BLUE_A)).next_to(sorted_list[-1], buff=0))
        sorted_list.append(Square(1.7).add(
            Text("e", font_size=35, color=GREEN_A)).next_to(sorted_list[-1], buff=0))
        sorted_list.append(Square(1.7).add(
            Text("False", font_size=35, color=RED_A)).next_to(sorted_list[-1], buff=0))
        sorted_g = VGroup(*sorted_list).move_to(ORIGIN)
        self.play(ReplacementTransform(sort_g, sorted_g))
        self.wait()

