import math
import svgwrite 
from svgwrite import cm, mm
from drawing import Arc, Circle, Line, Lines, Drawing

class BraidedChristmasHeart:
    def __init__(self, width, no_of_strains, gap_width=3):
        self.width=width
        self.no_of_strains=no_of_strains
        self.gap_width=gap_width

    def _get_cord(self, x1, y1, x2, y2, fraction):
        if (x1==x2):
            a=0
        else:
            a=(y2-y1)/(x2-x1)
        b=y1-a*x1

        rtn_x=(x2-x1)*fraction+x1
        rtn_y=a*rtn_x+b

        return (rtn_x, rtn_y)

    def generate(self, filename):
        self.drw=Drawing(self.width, self.width*1.5)
        # initial calculations
        arc_size=self.width*0.5
        strain_width=self.width/self.no_of_strains
        Bottom_of_heart=self.width*1.5
        Top_of_strain=self.width*0.5
        model_size=self.width/6
        model_calc=math.sqrt(2*model_size*model_size)/2
        model_x=self.width*0.5
        model_y=model_size*1.5
        model_x1=model_x-model_calc
        model_x2=model_x
        model_x3=model_x+model_calc
        model_y1=model_y-model_calc/2
        model_y2=model_y+model_calc/2
        model_y3=model_y+model_calc*1.5 #/2+model_size/2
        cut_color="black"
        draw_color="red"

        # frame of heart
        lines=Lines(0, Top_of_strain)
        lines.append(0, Bottom_of_heart, cut_color)
        # gap code start
        for i in range(1, self.no_of_strains):
            lines.append(i*strain_width-self.gap_width/2, Bottom_of_heart, cut_color)
            lines.append(i*strain_width-self.gap_width/2, Top_of_strain, cut_color)
            lines.append(i*strain_width+self.gap_width/2, Top_of_strain, cut_color)
            lines.append(i*strain_width+self.gap_width/2, Bottom_of_heart, cut_color)
        # gap code end
        lines.append(self.width,self.width*1.5, cut_color)
        lines.append(self.width,Top_of_strain, cut_color)
        self.drw.append(lines)
        self.drw.append(Arc(arc_size,
                            arc_size,
                            0,
                            -180,
                            arc_size,
                            no_of_lines=50, color=cut_color))

        # Draw model example
        self.drw.append(Arc(model_x+model_calc/2,
                            model_y,
                            45,
                            -135,
                            model_size/2,
                            no_of_lines=50, color=draw_color))
        self.drw.append(Arc(model_x-model_calc/2,
                            model_y,
                            -45,
                            -225,
                            model_size/2,
                            no_of_lines=50, color=draw_color))
        self.drw.append(Line(model_x1,
                            model_y2,
                            model_x2,
                            model_y3,
                            color=draw_color))
        self.drw.append(Line(model_x3,
                            model_y2,
                            model_x2,
                            model_y3,
                            color=draw_color))
        self.drw.append(Line(model_x1,
                            model_y2,
                            model_x2,
                            model_y1,
                            color=draw_color))
        self.drw.append(Line(model_x3,
                            model_y2,
                            model_x2,
                            model_y1,
                            color=draw_color))

        for i in range(1, self.no_of_strains):
            x1, y1 = self._get_cord(model_x1, model_y2, model_x2, model_y1, i/self.no_of_strains)
            x2, y2 = self._get_cord(model_x2, model_y3, model_x3, model_y2, i/self.no_of_strains)
            self.drw.append(Line(x1, y1, x2, y2, color=draw_color))
            x1, y1 = self._get_cord(model_x2, model_y1, model_x3, model_y2, i/self.no_of_strains)
            x2, y2 = self._get_cord(model_x1, model_y2, model_x2, model_y3, i/self.no_of_strains)
            self.drw.append(Line(x1, y1, x2, y2, color=draw_color))

        # Generate file
        self.drw.generate(filename)

if __name__ == "__main__":
    heart=BraidedChristmasHeart(150, 4)
    heart.generate("output\\heart.svg")
    print("Done")
