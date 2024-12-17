from cotxe import Cotxe
from colibri import Colibri
    
def main ():
    
    #PRIMER COTXE
    cotxe1 = Cotxe("Chevrolet", "Camaro", 500.000, 1966, 5 )
    
    print(f'Mi cotxe es un: {cotxe1.getMarca()}')
    print(f'Y su nombre es: {cotxe1.getNom()}')
    print(f'Me costo: {cotxe1.getPreu()} €')
    print("Me hubiese gustado pagar por el")
    cotxe1.setPreu(50)
    print(cotxe1.getPreu())
    
    print(f'El primero de su clase se creo en: {cotxe1.getAnyC()}')
    print(f'La generacion definitiva fue: {cotxe1.getGeneretion()}')
    print("Otra generación muy buena fue la:")
    cotxe1.setGeneretion(4)
    print(cotxe1.getGeneretion())
    
    #SEGON COTXE
    cotxe2 = Cotxe("Ford", "Mustang", 1.000000, 1964, 6)
    
    print(f'Mi cotxe es un: {cotxe2.getMarca()}')
    print(f'Y su nombre es: {cotxe2.getNom()}')
    print(f'Me costo: {cotxe2.getPreu()} €')
    print("Me hubiese gustado pagar por el")
    cotxe2.setPreu(50)
    print(cotxe2.getPreu())
    
    print(f'El primero de su clase se creo en: {cotxe2.getAnyC()}')
    print(f'La generacion definitiva fue: {cotxe2.getGeneretion()}')
    print("Otra generación muy buena fue la:")
    cotxe2.setGeneretion(2)
    print(cotxe2.getGeneretion())
    
    
    #TERCER COTXE
    cotxe3 = Cotxe("Lamborghini", "Huracan", 2.000000, 2014, 6)
    
    print(f'Mi cotxe es un: {cotxe3.getMarca()}')
    print(f'Y su nombre es: {cotxe3.getNom()}')
    print(f'Me costo: {cotxe3.getPreu()} €')
    print("Me hubiese gustado pagar por el")
    cotxe3.setPreu(50)
    print(cotxe3.getPreu())
    
    print(f'El primero de su clase se creo en: {cotxe3.getAnyC()}')
    print(f'La generacion definitiva fue: {cotxe3.getGeneretion()}')
    print("Otra generación muy buena fue la:")
    cotxe3.setGeneretion(3)
    print(cotxe3.getGeneretion())
    

##COLIBRIEEEEEEEEEEEEES    
    primercolibri = Colibri("Jacobino nuquiblanco", "Florisuga Mellivora", 4 , "Azul", "Mexico", "Preocupación menor" )
    
    print(f'Lo conozco como: {primercolibri.nom_conegut} !')
    print(f'Es de la especie:{primercolibri.especie} ')
    print(f'Pero tan solo vive:{primercolibri.vida_media}')
    print("Me gustaria que viviese como...")
    primercolibri.setVidaM(100)
    print(primercolibri.getVidaM())
    print(f'Años más!')
    
    print(f'Aún asi siempre tendra ese color {primercolibri.color} tan bonito')
    print("No te mentire que un color como...")
    primercolibri.setColor("Purpura")
    print(f"Así {primercolibri.getColor()} Le quedaria monisimo")
    
    segoncolibri = Colibri("Colibrí Rubí", "Archilochus colubris", 5, "Verde metálico con garganta roja", "América del Norte", "Preocupación menor")
    
    print(f'Lo conozco como: {segoncolibri.nom_conegut} !')
    print(f'Es de la especie:{segoncolibri.especie} ')
    print(f'Pero tan solo vive:{segoncolibri.vida_media}')
    print("Me gustaria que viviese como...")
    segoncolibri.setVidaM(200)
    print(segoncolibri.getVidaM())
    print(f'Años más!')
    
    print(f'Aún asi siempre tendra ese color {segoncolibri.color} tan bonito')
    print("No te mentire que un color como...")
    segoncolibri.setColor("Rojo Vermellon")
    print(f"Así {segoncolibri.getColor()} Le quedaria monisimo")
    
    tercercolibri = Colibri("Colibrí Abeja", "Mellisuga helenae", 7, "Verde brillante y gris", "Cuba", "Casi amenazado")
    
    print(f'Lo conozco como: {tercercolibri.nom_conegut} !')
    print(f'Es de la especie:{tercercolibri.especie} ')
    print(f'Pero tan solo vive:{tercercolibri.vida_media}')
    print("Me gustaria que viviese como...")
    tercercolibri.setVidaM(500)
    print(tercercolibri.getVidaM())
    print(f'Años más!')
    
    print(f'Aún asi siempre tendra ese color {tercercolibri.color} tan bonito')
    print("No te mentire que un color como...")
    tercercolibri.setColor("Blanco Lomo Plateado")
    print(f"Así {tercercolibri.getColor()} Le quedaria monisimo")

if __name__ == "__main__":
    main()