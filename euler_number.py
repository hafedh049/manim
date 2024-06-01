from manim import *

class EulerNumber(ThreeDScene):
    def construct(self):
        phi,theta = self.camera.get_phi(),self.camera.get_theta()
        
        self.set_camera_orientation(phi=75*DEGREES)

        cube = Cube().set_color(BLUE)
        octahedron = Octahedron(graph_config =  {
                "vertex_type": Dot,
                "vertex_config":{"radius":0},
                "edge_config": {"stroke_opacity": 0}}).scale(2).next_to(cube,buff=2).set_color(RED)
        cone = Cone(height=2.5).next_to(octahedron,buff=2).set_color(GREEN)
        convex = VGroup(cube,octahedron,cone).move_to(ORIGIN)
        self.play(Create(convex))

        for item in convex:
            item.add_updater(lambda x:x.rotate(np.pi/180 ,axis=Z_AXIS))

        polyhedron_def = Text("Polyhedrons are 3D solids made up by joining polygons together",font_size=40).move_to(15*UP).rotate(np.pi/2,axis=X_AXIS)
        self.play(Write(polyhedron_def),run_time = 3)
        self.wait()
        self.clear()
        self.play(Create(cube.add(Line(cube[0].get_center(),cube[len(cube)//2].get_center(),color=RED)).move_to(ORIGIN)))
        self.wait()
        self.clear()
        euler_caracterstic = Text("Euler Characteristic",font_size=100,t2c={"Euler":BLUE,"Charecteristic":PURPLE})
        euler_number = Text("Euler Number",font_size=100,t2c={"Euler":BLUE,"Number":PURPLE})
        euler_poincaré = Text("Euler-Poincaré",font_size=100,t2c={"Euler":BLUE,"Poincaré":PURPLE})
        self.set_camera_orientation(phi = phi,theta = theta)
        self.play(Write(euler_caracterstic),run_time = 2)
        self.play(ReplacementTransform(euler_caracterstic,euler_number),run_time = 2)
        self.play(ReplacementTransform(euler_number,euler_poincaré),run_time = 2)
        self.wait()



        self.wait()
        