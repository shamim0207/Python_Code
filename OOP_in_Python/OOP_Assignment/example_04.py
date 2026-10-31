class shape():
    def area():
        pass
    
    
class circle(shape):
    def calc_area(self,radious):
        pie=3.1416
        area_of_circle=pie*radious*radious
        print(f"The area of circle is: {area_of_circle}")
        

class rectangle(shape):
    def calc_area(self,length,width):
        area_of_rectangle=length*width
        print(f"The area of circle is: {area_of_rectangle}")



class triangle(shape):
    def calc_area(self,base,height):
        calc_triangle=0.5*base*height
        print(f"The area of circle is: {calc_triangle}")
        





#=================================================
circle=circle()
circle.calc_area(5)


rectangle=rectangle()
rectangle.calc_area(20,10)


triangle=triangle()
triangle.calc_area(20,10)