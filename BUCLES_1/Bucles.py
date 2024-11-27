
######1#######

numeros = [1,2,3,4,5,6,7,8,9,10] 
print(f"Amb for")
for numero in numeros:
  print(numero)
  
  
print(f"Amb while") 
  
conInt = 1 
while conInt < 11: 
    
    print(conInt)
    conInt += 1
    
    

    
#####2#####
print(f"Amb for i range")

iFor = 1
for iFor in range (1,11):
  iFor += iFor
  print (iFor)



#####3####
print() ##salt

fruitas = ["poma", "platan", "pera", "raim"]
for fruta in (fruitas):
  print(fruta)


#####4####
print() ##salt

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print(f"Parells ", end=" ") 
for parellNum in (num):
  if parellNum%2 == 0:
      
     print(parellNum, end=" ")


nombres = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print(f"Senars ", end=" ") 
for senarNum in (nombres):
  if senarNum%2 == 1:
      
     print(senarNum, end=" ")
     
print() ##salt
print() ##salt
#####5####

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print(f"Suma de Parells")
for parellNum in (num):
  if parellNum%2 == 0:
     parellNum += parellNum
     print(parellNum)
     
print("Suma de Senars")   
for senarNum in (num):
  if senarNum%2 == 1:
     senarNum += senarNum
     print(senarNum)
     
#####6#####

print(f"Big suma")
numBi = 0
nuMe = 0
while nuMe < 100:
   numBi += 1
   nuMe = numBi
   nuMe = nuMe + numBi
   print(nuMe)
     

#####7#####



print()
print(f"El numero se encuentra entre 100 i 400")
nuMA = 0
numIco = 150
es_igual= False

while not es_igual:
   nuMA = nuMA + 2 * 2
   print(nuMA)
   if nuMA >= numIco:	
     print(f"El numero es, {numIco}.")
     es_igual = True








