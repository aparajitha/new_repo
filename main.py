from math_operations import Maths
class main:
    m = Maths(16, 4)
    print("Sum of 16 & 4 = " +str(m.add_nums()))
    print("Difference of 16 & 4 = " +str(m.substract_nums()))
    print("Multiplication of 16 & 4 = " +str(m.multiply_nums()))
    print("Division of 16 & 4 = " +str(m.divide_nums()))
    f = open("SampleText.txt", "r")
    print(f.read())
    
