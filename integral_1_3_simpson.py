from integral import Integral
import math

class IntegralUmTercoSimpson(Integral):
    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x, func_integral, func_derivada_integral)
        

    def erro_generalizado(self):
        derivada_4_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_4_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_4_grau_limite_inf, derivada_4_grau_limite_sup)
        parcela_1 = (self.h**4 / 180) * (self.limite_sup - self.limite_inf)
        return abs(maior * parcela_1)
    
    def erro_simples(self):
        derivada_4_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_4_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_4_grau_limite_inf, derivada_4_grau_limite_sup)
        return abs(-1 * (self.h ** 5 / 90) * maior)
    
    def integral(self):
        for x in self.x:
            self.y.append(self.func_integral(x))
        
        primeiro = self.y.pop(0)
        ultimo = self.y.pop()
        cte = self.h / 3
        somaImpares = 0
        somaPares = 0
        for i in  range(0, len(self.y)):
            if i  % 2 == 0:
                somaImpares += (4 * self.y[i])
            if i % 2 == 1:
                somaPares += (2 * self.y[i])
        return cte * (primeiro + somaImpares + somaPares + ultimo)
    


if __name__ == '__main__':
    inte_1_3_simpson = IntegralUmTercoSimpson(
            limite_inf=0, 
            limite_sup=1, 
            h=0.1, 
            func_integral=lambda x: x * math.sqrt(x**2 + 1),
            func_derivada_integral=lambda x: ((2 * math.pow(x, 3) + 3 * x)) / ((math.pow(x, 2) + 1) * (math.sqrt(x**2 + 1)))
        )
    print(f'Erro Geral = {inte_1_3_simpson.erro_generalizado()}')
    print(round(inte_1_3_simpson.integral(), 5))