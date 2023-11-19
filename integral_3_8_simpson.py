from integral import Integral
import math


class IntegralTresOitavosSimpson(Integral):
    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x, func_integral, func_derivada_integral)

    def erro_generalizado(self):
        derivada_4_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_4_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_4_grau_limite_inf, derivada_4_grau_limite_sup)
        parcela_1 = (self.h**4 / 80) * (self.limite_sup - self.limite_inf)
        return abs(maior * parcela_1)



    def erro_simples(self):
        derivada_4_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_4_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_4_grau_limite_inf, derivada_4_grau_limite_sup)
        parcela_1 = (3*math.pow(self.h, 5)) / 80
        return abs(maior * parcela_1)
    
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
            func_integral=lambda x: x * math.sqrt(x**2 + 1),
            func_derivada_integral=lambda x: ((2 * math.pow(x, 3) + 3 * x)) / ((math.pow(x, 2) + 1) * (math.sqrt(x**2 + 1)))

            )
    print(f'Erro Geral = {int_3_8_simpson.erro_generalizado()}')
    print(round(int_3_8_simpson.integral(), 10))
        