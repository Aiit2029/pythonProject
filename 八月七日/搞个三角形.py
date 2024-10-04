class triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_triangle(a,b,c):
        if a+b>c and a+c>b and b+c>a:
            return True

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        half = self.perimeter() / 2
        return (half*((half -self.a)*(half -self.b)*(half-self.c)))**0.5

def main():
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    if triangle.is_triangle(a,b,c):
        t = triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print('这三条边不能组成一个三角形，请自重')



if __name__ == '__main__':
    main()