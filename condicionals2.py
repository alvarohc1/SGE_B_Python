######2######

dia = "hoy"

if dia == "hoy":
   print("¿Quin dia és avui?")
   dia_setmana = input()
   print( "Avui es",dia_setmana )
   
######3######



print("Introudeix la nota del alumne")  
nota = float(input())
if nota < 5:
   print("L'alumne ha suspès")
elif nota > 8:
   print("L'alumne ho ha fet excel·lent ")
elif nota > 6.6 and nota > 8:
   print("L'alumne ha suspès")
else:
   print("L'alumne ha aprovat")   
   
   
   
######4######

print("Introudeix el salari") 
salari = float(input())

if salari > 0 and salari < 15000:
   salarIva = float (salari * (0/100))
   print("El IVA es",salarIva)

elif salari < 30000: 
   salarIva = float (salari * (10/100))
   print("El IVA es",salarIva)
   
else:
   salarIva = float (salari * (21/100))
   print("El IVA es",salarIva)


   
   

