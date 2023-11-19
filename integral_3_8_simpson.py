from integral import Integral
import math


class IntegralTresOitavosSimpson(Integral):
    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x, func_integral, func_derivada_integral)

    def erro_generalizado(self):
        return super().erro_generalizado()
    
    def erro_simples(self):
        return super().erro_simples()
    
    def integral(self):
        quant_x = len(self.x)
        if quant_x % 2 == 0:
            for x in self.x:
                self.y.append(self.func_integral(x))
            primeiro = self.y.pop(0)
            ultimo = self.y.pop()
            cte = (3*self.h) / 8
            soma3x = 0
            soma2x = 0
            cont = 0
            for i in range(0, len(self.y)):
                if cont >= 2:
                    soma2x += (2 * self.y[i])
                    cont = 0
                else:
                    soma3x += (3 * self.y[i])
                    cont += 1
            return cte * (primeiro + soma3x + soma2x + ultimo)
        else:
            b = self.x.pop()
            penultimo = self.x[-1]
            for x in self.x:
                self.y.append(self.func_integral(x))
            primeiro = self.y.pop(0)
            ultimo = self.y.pop()
            cte = (3*self.h) / 8
            soma3x = 0
            soma2x = 0
            cont = 0
            for i in range(0, len(self.y)):
                if cont >= 2:
                    soma2x += (2 * self.y[i])
                    cont = 0
                else:
                    soma3x += (3 * self.y[i])
                    cont += 1
           
            y_aux = self.func_integral(penultimo)
            y_b = self.func_integral(b)
            int_1 = (self.h / 2) * (y_aux + y_b)
            return (cte * (primeiro + soma2x + soma3x + ultimo)) + int_1
    

if __name__ == '__main__':
    int_3_8_simpson = IntegralTresOitavosSimpson(
            limite_inf=0, 
            limite_sup=1, 
            h=0.1,
            func_integral=lambda x: x * math.sqrt(x**2 + 1)
            )
    print(round(int_3_8_simpson.integral(), 10))
        