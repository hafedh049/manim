from manim import *

class Kruskal(Scene):
    def construct(self):
        nodes= ['H', 'B', 'K', 'N', 'L',"AA"]
        edges= [('H', 'K'), ('B', 'N'), ('K', 'L'), ('N', 'B'), ('L', 'N')]
        edge_config = {
            "stroke_width": 2,
        }
        graph: Graph = Graph(vertices=nodes,edges=edges,labels=True,edge_config=edge_config,layout="kamada_kawai")
        self.play(Create(graph))