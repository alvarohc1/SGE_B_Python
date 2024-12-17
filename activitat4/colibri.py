class Colibri: 

    def __init__(self, nom_conegut, especie, vida_media, color, procedencia, estado_dconservacion):
        
        self.nom_conegut = nom_conegut
        self.especie = especie
        self.vida_media = vida_media
        self.color = color
        self.procedencia = procedencia
        self.estado_dconservacion = estado_dconservacion
        
    def getNomC(self):
        return self.nom_conegut
    
    def getEspecie(self):
        return self.especie
    
    def getVidaM(self):
        return self.vida_media
    def setVidaM(self, new_vida_media):
        self.vida_media = new_vida_media
    
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
    
    def getProcedencia(self):
        return self.procedencia
   