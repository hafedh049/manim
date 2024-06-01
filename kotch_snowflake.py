from manim import *

class KotchSnowFlake(MovingCameraScene):
    def construct(self):
        triangle = RegularPolygram(3,color = WHITE).scale(3)
        edges = [edge for edge in triangle.get_pieces(3)]
        iter = 0
        angle = np.pi/2
        while iter < 5:
            tempo_edges = []
            
            for edge in edges:
                start,end = edge.get_start(),edge.get_end()
                piece = (end - start) / 3
                first_tier = Line(start,start + piece)
                middle_tier = Line( start + 2*piece,start + piece)
                last_tier = Line(start + 2*piece,end)
                tempo_edges.extend([first_tier,last_tier])
                triangle = Polygon(middle_tier.get_start(),middle_tier.get_end(),middle_tier.copy().rotate(angle).get_start(),color=WHITE)
                sides = list(filter(lambda x:x.get_start().tolist()!= middle_tier.get_start().tolist() or x.get_end().tolist() != middle_tier.get_end().tolist() ,triangle.get_pieces(3)))
                tempo_edges.extend([edge for edge in sides])

            self.play(*[Create(edge) for edge in edges],run_time=.3)
        
            edges.clear()
            edges.extend(tempo_edges)
            iter += 1
        
        print(len(edges),'hhhhhhhhhhhhh')

        self.camera.frame.save_state()
        for i in range(5):
            self.play(ApplyMethod(self.camera.frame.move_to,edges[-1]),ApplyMethod(self.camera.frame.scale,.5 ))
            self.wait()
            self.play(Restore(self.camera.frame))

        self.wait(2)