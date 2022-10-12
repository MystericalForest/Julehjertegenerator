import math
import svgwrite 
from svgwrite import cm, mm

class Arc:
    def __init__(self, x, y, start_angle, end_angle, radius, no_of_lines=10, color="black", Closed_Arc=False):
        self.x = x
        self.y = y
        self.no_of_lines=no_of_lines
        self.color=color
        self.start_angle = math.radians(start_angle)
        self.end_angle = math.radians(end_angle)
        self.radius = radius
        self.Closed_Arc=Closed_Arc

    def get_lines(self):
        points=[]
        rtn=[]
        delta=(self.end_angle-self.start_angle)/self.no_of_lines
        for i in range(self.no_of_lines):
            start_angle=self.start_angle+delta*i
            end_angle=self.start_angle+delta*(i+1)
            x1=self.x+self.radius*math.cos(start_angle)
            y1=self.y+self.radius*math.sin(start_angle)
            x2=self.x+self.radius*math.cos(end_angle)
            y2=self.y+self.radius*math.sin(end_angle)
            rtn.append(Line(x1, y1, x2, y2, color=self.color))
            if (i==0):
                start_x=x1
                start_y=y1

        if self.Closed_Arc:
            rtn.append(Line(x2, y2, start_x, start_y, color=self.color))

        return rtn

class Circle:
    def __init__(self, x1, y1, radius, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.color=color
        self.radius = radius

class Line:
    def __init__(self, x1, y1, x2, y2, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color=color

class Lines:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.lines=[]

    def append(self, x, y, color="black"):
        self.lines.append(Line(self.x, self.y, x, y, color))
        self.x = x
        self.y = y

    def close_polygon(self):
        self.lines.append(Line(self.x, self.y, self.start_x, self.start_y))
        self.x = self.start_x
        self.y = self.start_y

class Drawing:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.objects=[]

    def append(self, obj):
        self.objects.append(obj)

    def generate(self, filename):
        svg_document = svgwrite.Drawing(filename = filename,
                                size = (self.width*mm, self.height*mm))
        for item in self.objects:
            if isinstance(item, Circle):
                svg_document.add(svg_document.circle(center = (item.x1*mm, item.y1*mm),
                                       r = item.radius*mm,
                                       stroke_width = "1",
                                       stroke = item.color,
                                       fill = "none"))
            elif isinstance(item, Line):
                svg_document.add(svg_document.line(start = (item.x1*mm, item.y1*mm),
                                       end = (item.x2*mm, item.y2*mm),
                                       stroke_width = "1",
                                       stroke = item.color)) 
            elif isinstance(item, Lines):
                for line in item.lines:
                    svg_document.add(svg_document.line(start = (line.x1*mm, line.y1*mm),
                                       end = (line.x2*mm, line.y2*mm),
                                       stroke_width = "1",
                                       stroke = line.color))
            elif isinstance(item, Arc):
                for line in item.get_lines():
                    svg_document.add(svg_document.line(start = (line.x1*mm, line.y1*mm),
                                       end = (line.x2*mm, line.y2*mm),
                                       stroke_width = "1",
                                       stroke = line.color))
            else:
                print("Unsupported type: ", type(item))
        svg_document.save()
