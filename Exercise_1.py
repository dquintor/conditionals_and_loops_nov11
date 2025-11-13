Inicio_edad = False
Inicio_estudia = False

while not Inicio_edad:
    edad = input("Ingrese su edad:")
    if not edad:
        print("La edad no puede estar vacia. Por favor ingrese un valor")
        continue
    if not edad.isdigit():
        print("Valor incorrecto. Ingrese un valor numerico")
        continue
    edad = int(edad)
    if 0 > edad > 100:
        print("Valor incorrecto. Por favor ingres un numero valido")
        continue
    Inicio_edad = True

while not Inicio_estudia:
    if edad < 6: 
        infante= True
        continue
    estudia = int(input("\nSi estudias digita 1.\nSi trabajas digita 2.\n\nTu selección:"))
    if estudia not in (1,2):
        print("Valor incorrecto. Ingrese una opcion valida")
        continue
    
    Inicio_estudia= True


infante = False 

if infante:
    print("Eres un infante")
    
elif 5 < edad < 18 and estudia == 1:
    print("Estudiante escolar")

elif 17 < edad < 26 and estudia == 1: 
    print("Universitario")
    
elif 25 < edad < 61 and estudia == 2: 
    print("Adulto activo")

elif 59 < edad and estudia == 2:
    print("Adulto mayor jubilado")
    
else: 
    print("No determinado")

menu = False


    

        
        
    
        
