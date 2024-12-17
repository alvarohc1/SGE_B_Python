class Cotxe: 

    def __init__(self, precio, marca, any_creacio, generacion, nom):
        #atrbutos
        self.marca = marca 
        self.nom = nom
        self.precio = precio 
        self.any_creacio = any_creacio
        self.generacion = generacion
        
    def getMarca(self):
        return self.marca
    
    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.name = new_nom
    
    def getPreu(self):
        return self.precio
    def setPreu(self, new_precio):
        self.precio = new_precio
    
    def getAnyC(self):
        return self.any_creacio
    
    def getGeneretion(self):
        return self.generacion
    def setGeneretion(self, new_generacion):
        self.generacion = new_generacion
     
 
     
