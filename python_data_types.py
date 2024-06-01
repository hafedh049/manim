from manim import *


class DataTypes(Scene):
    def construct(self):
        datatypes = [{"chapter": "Text Type",
                      "types": [{'type': 'Strings', "examples": [
                          Text("x = 'Welcome To Flamingo'"),
                          Text('y = str("Python Expert 🐍")'),
                      ], },],

                      },

                     {"chapter": "Numeric Types",
                      "types": [{'type': 'Integers', "examples": [
                          Text("x = -10"),
                          Text('y = int(2)'),
                          Text('z = 0'),
                      ], },
                          {'type': 'Floats', "examples": [
                              Text("x = -.75  (OR -0.75)"),
                              MathTex(
                                  r'y = 2e5\:\:(2 * 10^5)\:\:\text{Scientific Notation}'),
                              MathTex(r"z = float('\pm inf')\:\:( \pm\infty )"),
                          ], },
                          {'type': 'Complexes', "examples": [
                              Text("x = 1j"),
                              Text('y = complex(2, -1j)'),
                              MathTex(r'z = \frac{1}{2}j'),
                          ], },],

                      },


                     {"chapter": "Sequence Types",
                      "types": [{'type': 'Lists', "examples": [
                          Text("x = list([1, 2])"),
                          Text('y = [[0], None, "Hello"]'),
                      ], },
                          {'type': 'Tuples', "examples": [
                              Text("x = (1, 2)"),
                              Text('y = (( ), ( ))'),
                              Text("z = ('x',)"),

                          ], },
                          {'type': 'Ranges', "examples": [
                              Text("x = range(10)"),
                              Text('y = range(1,10,2)'),
                              Text('z = range(-5,2,-2)'),

                          ], },
                      ],

                      },


                     {"chapter": "Mapping Type",
                      "types": [{'type': 'Dictionaries', "examples": [
                          Text("x = {1 : 1,'a' : 10}"),
                          Text("y = {(0,0):10, 'hey':None, True:[ [ ] ]}"),
                      ], },],

                      },


                     {"chapter": "Set Types",
                      "types": [{'type': 'Sets', "examples": [
                          Text("x = {.1,True,False,None}"),
                          Text('y = {1,1,1,0,0,0}'),
                      ], },
                          {'type': 'Frozen Sets', "examples": [
                              Text("x = frozenset({1, True, False, None})"),
                          ], },],

                      },


                     {"chapter": "Boolean Type",
                      "types": [{'type': 'Booleans', "examples": [
                          Text("x = True"),
                          Text('y = bool("False")'),
                      ], },],

                      },

                     {"chapter": "Binary Types",
                      "types": [{'type': 'Bytes', "examples": [
                          Text("x = b'Hello'"),
                      ], },
                          {'type': 'Bytearrays', "examples": [
                              Text("x = bytearray(1225)"),
                          ], },
                          {'type': 'Memomryviews', "examples": [
                              Text("x = memoryview(bytes(5))"),
                          ], },],

                      },

                     {"chapter": "None Type",
                      "types": [{'type': 'None', "examples": [
                          MathTex("x = None"),
                      ], },],

                      },

                     ]

        for map_item in datatypes:
            chapter = Text(map_item["chapter"], color=BLUE)
            self.play(Write(chapter))
            self.wait(.75)
            self.play(Unwrite(chapter))

            for type_ in map_item["types"]:
                title = Text(type_["type"], color=GREEN).shift(2*UP)
                self.play(Write(title),run_time = .5)
                self.wait(.25)
                for index in range(len(type_["examples"])):
                    self.wait(.25)
                    if index == 0:
                        self.play(Write(type_["examples"][index].next_to(
                            title, DOWN, 1, aligned_edge=ORIGIN)), run_time=.5)
                    else:
                        self.play(Write(type_["examples"][index].next_to(
                            type_["examples"][index - 1], DOWN, 1, aligned_edge=ORIGIN)), run_time=.5)
                self.wait(.25)
                self.clear()
