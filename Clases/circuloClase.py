from math import pi

class Circulo:
    
    def __init__ (self,radio):
        try:
            if(radio) <= 0:
                raise ValueError
            else:
                self.radio = radio
        except ValueError:
            print("Error, intenta con un radio mayor que cero")

    def __str__(self):
        return f"Circulo con radio: {self.radio}"
           
    def area(self):
        resultado = pi * self.radio ** 2
        return  resultado
    
    def perimetro(self):
        resultado = 2 * pi * self.radio
        return  resultado

    def setear_radio(self, nuevoRadio):
        try:
            if(nuevoRadio) <= 0:
                raise ValueError
            else:
                self.radio = nuevoRadio
        except ValueError:
            print("Error, intenta con un radio mayor que cero")
    
    def __mul__(self,num):
        try:
            if num <= 0:
                raise ValueError
            else:
                return Circulo(self.radio * num)
        except ValueError:
            print("Error, intenta con un radio mayor que cero")
        


c = Circulo(8)

print("Area:", c.area())
print("Perimetro:", c.perimetro())
print(c)
c.setear_radio(10)
print("Area:", c.area())
print("Perimetro:", c.perimetro())
print(c)

c2 = c * (2)
print(c2)