#ko ap dung de tinh so phuc 
import math
a = float(input("nhap a:"))
b = float(input("nhap b:"))
c = float(input("nhap c:"))
delta = float(b**2) - float(4 * a* c )
if delta > 0:
    print("x1: ", (-b-math.sqrt(delta))/(2*a) )
    print("x2: ", (-b+math.sqrt(delta))/(2*a))
elif delta == 0:
    print("x: ", (-b/2*a))
elif delta < 0:
    print("pt vo nghiem") 
