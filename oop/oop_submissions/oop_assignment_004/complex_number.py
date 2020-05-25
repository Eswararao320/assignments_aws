import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        if type(self.real_part)==str and type(self.imaginary_part)==str:
            raise ValueError("Invalid value for real and imaginary part")
        elif type(self.real_part)==str:
            raise ValueError("Invalid value for real part")
        elif type(self.imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
            
    def __str__(self):
        if self.imaginary_part>=0:
            return('{}+{}i'.format(str(self.real_part),str(self.imaginary_part)))
        else:
            return('{}{}i'.format(str(self.real_part),str(self.imaginary_part)))
    
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
    
    def __mul__(self,other):
        return ComplexNumber(self.real_part*other.real_part-self.imaginary_part*other.imaginary_part,self.imaginary_part*other.real_part+self.real_part*other.imaginary_part)
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
    def __eq__(self,other):
        return (self.real_part==other.real_part)and(self.imaginary_part==other.imaginary_part)
    def conjugate(self):
        x=-self.imaginary_part
        return ComplexNumber(self.real_part,x)
    def __truediv__(self,other):
        sr,si,otr,oti=self.real_part,self.imaginary_part,other.real_part,other.imaginary_part
        r=float(otr**2+oti**2)    
        return ComplexNumber((sr*otr+si*oti)/r,(si*otr-sr*oti)/r)