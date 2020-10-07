import numpy as np

g = 9.81 #kg*m/s^2
m=1.0
mm=m/1000

class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy

    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        return self.ρ * A * L * g


    def obtener_rigidez(self, ret):
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy,-cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        W = self.calcular_peso(ret)

        return np.array([0,0, -W, 0,0, -W])


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)
        
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy,-cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ.T @ ue)





    def chequear_diseño(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        revisar si esta barra cumple las disposiciones de diseño.
        """
        A=self.calcular_area()
        Fn=A*self.σy
        
        if ϕ*Fn < abs(Fu):
            return False
        else:
            return True
        


    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        calcular y devolver el factor de utilización
        """
        A=self.calcular_area()
        Fn=A*self.σy
        
        factor_de_utilizacion = abs(Fu) / (ϕ*Fn)
        return factor_de_utilizacion


    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        re-calcular el radio y el espesor de la barra de modo que
        se cumplan las disposiciones de diseño lo más cerca posible
        a FU = 1.0.
        """
        # hay 2 posibles casos:
        # 1) se |Fu| >= 1.0
        # 2) que el |Fu| << 1:
        # if Fu>0:
            
            # se obtiene esbeltez
        Largo=self.calcular_largo(ret)
        I=(np.pi/4)*(self.R**4 - (self.R - self.t)**4)

        Area=self.calcular_area()
        
        radio_giro= np.sqrt(I/Area)
        
        lamba = np.sqrt(Largo/radio_giro)
        # ecuaciones:
        # lambda <=300:
        # factor_fu<=1
        
        # abs(fuerza)/(ϕ*(np.pi*(self.R**2) - np.pi*((self.R-self.t)**2))*self.σy)
        
        
        """
        # Caso 1
        if Fu==0.:
            return None
        c=1
        while True:
            # print(f"R : {self.R}")
            
            factor_fu=self.obtener_factor_utilizacion(Fu,ϕ=0.9)
            # print(f" Fu : {Fu}")
            # print(f"factor_fu : {factor_fu}")
            # print(f"area : {self.calcular_area()}")
            if 0.8 < factor_fu < 1.0:
                return None
            
            if factor_fu >= 1.0 and self.t>0:
                self.t+=1*mm
                print("A")
            elif factor_fu < 0.8 and self.t>0:
                self.t-=1*mm
                # print("B")
                if self.t==1*mm:
                    # print("C")
                    return None
                    while factor_fu < 0.8:
                        # print("D")
                        if self.R>10*mm:
                            self.R-=5*mm
                            # print("E")
                        else:
                            # print("F")
                            return None
          
            # if Fu==0:
            #     return None

            else:
                
                print(c)
                c+=1
                return None
        
            # R y t ==> A
            
        
        
        
        
        
        # A=self.calcular_area()
        # Fn=A*self.σy
        # if abs(Fu) < 0.95 or abs(Fu) > 1:
        #     Fu()    
            
        # # cambiando solo el espesor
        # self.t=np.Solve()
        """  
        factor_fu=self.obtener_factor_utilizacion(Fu,ϕ=0.9)
        x=0.90
        radio_real=self.R
        t_real=self.t
        while factor_fu < 0.96:
            # print(factor_fu)
            
            self.R = x*radio_real   #cambiar y poner logica de diseño
            self.t = x*t_real   #cambiar y poner logica de diseño
            factor_fu=self.obtener_factor_utilizacion(Fu,ϕ=0.9)
            x-=0.02
        
            # self.r*0.98=self.r*0.98*0.96
        return None
        


