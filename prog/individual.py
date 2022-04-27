#Даны основания и высота равнобедренной трапеции. Найти периметр трапеции.
import math

h = float(input("Enter the height of the trapezoid: "))
a = float(input("Enter a larger trapezoid base: "))
b = float(input ("Enter a smaller trapezoid base: "))
c = 2*math.sqrt(pow(h,2) + pow (((a-b)/2),2))+a+b
print("The perimeter of the trapezoid: ", c)