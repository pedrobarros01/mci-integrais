from abc import ABC, abstractmethod

class Integral(ABC):
    def __init__(self, 
                 limite_inf: int = None, 
                 limite_sup:int = None, 
                 h: float = None, 
                 quant_pontos:int = None, 
                 x: list[float] = None,
                 func_integral = None,
                 func_derivada_integral = None
                 ) -> None:
        self.y = []
        self.func_integral = func_integral
        self.func_derivada_integral = func_derivada_integral
        if h is None:
            self.x = x
            self.limite_inf = x[0]
            self.limite_sup =  x[-1]
            self.quant_pontos = quant_pontos
            self.h = (self.limite_sup - self.limite_inf) / quant_pontos
        else:
            self.h = h
            self.limite_inf = limite_inf
            self.limite_sup = limite_sup
            self.x = []
            self.criar_vetor_x()
            self.quant_pontos = int((self.limite_sup - self.limite_inf) / self.h)

    def saber_maior(self, x, y):
        if abs(x) > abs(y):
            return x
        else:
            return y
    
    def criar_vetor_x(self):
        i = self.limite_inf
        while round(i, 2 ) <= round(self.limite_sup, 2):
            self.x.append(round(i, 2))
            i += self.h
        
    @abstractmethod
    def erro_simples(self):
        pass

    @abstractmethod
    def erro_generalizado(self):
        pass

    @abstractmethod
    def integral(self):
        pass
