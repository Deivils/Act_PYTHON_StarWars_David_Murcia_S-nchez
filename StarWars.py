import random
import math #Importo la librería math para realizar el factorial y el redondeo hacia abajo .floor

################################ FUNCIÓN DE INICIO #####################################

def Inicio():

    while True:
        print("=== STAR WARS CÓDIGOS SECRETOS ===")
        print("Hace mucho tiempo, en una galaxia muy, muy lejana… La Princesa")
        print("Leia, Luke Skywalker, Han Solo, Chewbacca, C3PO y R2D2 viajan")
        print("en una nave imperial robada en una misión secreta para infiltrarse")
        print("en otra estrella de la muerte que el imperio está construyendo para")
        print("destruirla.\n")

        iniciar = input("Pulse intro para continuar...")
        if iniciar == "":
            print("Nivel 1\n")
            nivel_1()
            break
        else:
            print("Entrada no válida\n")
            break

#################################### NIVEL 1 #############################################


def nivel_1():
    S1 = random.randint(1, 10)
    S2 = random.randint(20, 30)
    
    while True:
        print("Los problemas empiezan cuando deben realizar un salto")
        print(f"hiperespacial hasta al sistema {S1} en el sector {S2}, pero el sistema de")
        print("navegación está estropeado y el computador tiene problemas para")
        print("calcular parte de las coordenadas de salto. Chewbacca, piloto")
        print("experto, se da cuenta que falta el cuarto número de la serie.")
        print("Recuerda de sus tiempos en la academia de pilotos que para")
        print("calcularlo hay que calcular el sumatorio entre el nº del sistema y el")
        print("nº del sector (ambos inclusive).")
        try:
            respuesta_sumatorio = int(input("¿Qué debe introducir?..  "))
            sumatorio = sum(range(S1, S2 + 1))
            if respuesta_sumatorio == sumatorio:
                print("Nivel 2\n")
                nivel_2()
                break
            else: 
                print("Ese no era el código correcto... La misión ha sido un fracaso... :(:(:(")
                print("Todavía no eres un Maestro Jedi de las matemáticas.")

                while True:
                    
                    print("¿Quieres volver a jugar?\n")
                    perder = input("Pulse Y para ir a inicio o N para salir: ") 
                    
                    if perder == 'Y':
                        Inicio()
                        break

                    elif perder == 'N':
                        print("Gracias por jugar \u2665")
                        break
                    else:
                        print("Tiene que ser Yes o No ")
                        
                # Vuelvo a hacer este if para romper el while principal
                if perder == 'N': 
                    break

        except ValueError:
            print("Tiene que ser un número entero...Vuelva a intentarlo\n")
            
#################################### NIVEL 2 #############################################

def nivel_2():
    P1 = random.randint(1, 7)
    P2 = random.randint(8, 12)
    
    while True:
        print("Gracias a Chewbacca consiguen llegar al sistema correcto y ven a lo")
        print("lejos la estrella de la muerte. Como van en una nave imperial robada")
        print("se aproximan lentamente con la intención de pasar desapercibidos.")
        print("De repente suena el comunicador. “Aquí agente de espaciopuerto")
        print(f"{P1} contactando con nave imperial {P2}. No están destinados en este")
        print("sector. ¿Qué hacen aquí?”. Han Solo coge el comunicador e")
        print("improvisa. “Eh… tenemos un fallo en el… eh… condensador de")
        print("fluzo... Solicitamos permiso para atracar y reparar la nave”. El")
        print("agente, que no se anda con tonterías, responde “Proporcione código")
        print("de acceso o abriremos fuego”. Han Solo ojea rápidamente el manual")
        print("del piloto que estaba en la guantera y da con la página correcta. El")
        print("código es el productorio entre el nº del agente y el nº de la nave")
        print("(ambos inclusive).")
        
        try:
            respuesta_Nivel2 = int(input("¿Cuál es el código?.. "))
            productorio = math.prod(range(P1, P2 + 1))
            if respuesta_Nivel2 == productorio:
                print("Nivel 3\n")
                nivel_3()
                break
            else:
                print("Ese no era el código correcto... La misión ha sido un fracaso... :(:(:(")
                print("Todavía no eres un Maestro Jedi de las matemáticas.")
                
                while True:
                    print("¿Quieres volver a jugar?\n")
                    perder = input("Pulse Y para ir a inicio o N para salir: ") 
                    if perder == 'Y':
                        Inicio()
                        break
                    
                    elif perder == 'N':
                        print("Gracias por jugar \u2665")
                        break
                    else:
                        print("Tiene que ser Yes o No ")
                        
                if perder == 'N':
                    break        
        except ValueError:
            print("Tiene que ser un número entero...Vuelva a intentarlo\n")

#################################### NIVEL 3 #############################################

def nivel_3():
    N = random.randint(50, 100)
    
    while True:
        
        print("Han Solo proporciona el código correcto. Atracan en la estrella de la")
        print("muerte, se equipan con trajes de soldados imperiales que")
        print("encuentran en la nave para pasar desapercibidos y bajan. Ahora")
        print(f"deben averiguar en qué nivel de los {N} existentes se encuentra el")
        print("reactor principal. Se dirigen al primer panel computerizado que")
        print("encuentran y la Princesa Leia intenta acceder a los planos de la")
        print("nave pero necesita introducir una clave de acceso. Entonces")
        print("recuerda la información que le proporcionó Lando Calrissian “La")
        print("clave de acceso a los planos de la nave es el factorial de N/10")
        print("(redondeando N hacia abajo), donde N es el nº de niveles”.")
        
        try:
            respuesta_Nivel3 = int(input("¿Cuál es el código?.. "))
            # Creo la variable número con math.floor para redondear la division de N / 10 hacia abajo
            numero = math.floor(N // 10)
            if respuesta_Nivel3 == math.factorial(numero): # Factorizo la variable número
                print("Nivel 4\n")
                nivel_4()
                break
            else:
                print("Ese no era el código correcto... La misión ha sido un fracaso... :(:(:(")
                print("Todavía no eres un Maestro Jedi de las matemáticas.")
                        
                while True:
                    
                    print("¿Quieres volver a jugar?\n")
                    perder = input("Pulse Y para ir a inicio o N para salir: ")        
                    
                    if perder == 'Y':
                        Inicio()
                        break
                            
                    elif perder == 'N':
                        print("Gracias por jugar \u2665")
                        break 
                    else:
                        print("Tiene que ser Yes o No ")
                        
                if perder == 'N':
                    break        
        except ValueError:
            print("Tiene que ser un número entero...Vuelva a intentarlo\n")
        
#################################### NIVEL 4 #############################################        
    
def nivel_4():
    P = random.randint(10, 100)
    es_primo = True
    if P <= 1:
        es_primo = False
    else:
        for i in range(2, P):
            if P % i == 0:
                es_primo = False
                break
            else:
                es_primo = True
                break

    
    while True:
        print("Gracias a la inteligencia de Leia llegan al nivel correcto y encuentran")
        print("la puerta acorazada que da al reactor principal. R2D2 se conecta al")
        print("panel de acceso para intentar hackear el sistema y abrir la puerta.")
        print(f"Para desencriptar la clave, necesita verificar si el número {P} es primo")
        print("o no. Si es primo introduce un 1, si no lo es introduce un 0.")
        try:
            
            respuesta_Nivel4 = int(input("¿Cuál es el número?.. "))
            resultado = 1 if es_primo else 0
            
            if respuesta_Nivel4 == resultado: 
                print("Nivel 5\n")
                nivel_5()
                break
            else:
                print("Ese no era el código correcto... La misión ha sido un fracaso... :(:(:(")
                print("Todavía no eres un Maestro Jedi de las matemáticas.")
                                
                while True:
                            
                    print("¿Quieres volver a jugar?\n")
                    perder = input("Pulse Y para ir a inicio o N para salir: ")        
                            
                    if perder == 'Y':
                        Inicio()
                        break
                                    
                    elif perder == 'N':
                        print("Gracias por jugar \u2665")
                        break 
                    
                    else:
                        print("Tiene que ser Yes o No ")
                                
                if perder == 'N':
                    break 
                
        except ValueError:
                    print("Tiene que ser (1 o 0)....Vuelva a intentarlo\n")

#################################### NIVEL 5 #############################################

def nivel_5():
    M = random.randint(5, 10)
    S = random.randint(5, 10)


    while True:

        print("Consiguen entrar al reactor. Ya solo queda que Luke Skywalker")
        print("coloque la bomba, programe el temporizador y salir de allí corriendo.")
        print(f"Necesita programarlo para que explote en exactamente {M} minutos y")
        print(f"{S} segundos, el tiempo suficiente para escapar antes de que explote")
        print("pero sin que el sistema de seguridad anti-explosivos detecte y")
        print("desactive la bomba. Pero el temporizador utiliza un reloj Zordgiano")
        print("un tanto peculiar. Para convertir los minutos y segundos al sistema")
        print("Zordgiano hay que sumar el factorial de M y el factorial de S.")

        try:
            respuesta_Nivel5 = int(input("¿Cuanto tiempo hay que poner?.. "))
            resultado = math.factorial(M) + math.factorial(S)
            
            if respuesta_Nivel5 == resultado: 
                print("Nivel 6\n")
                nivel_6()
                break
            else:
                print("Ese no era el código correcto... La misión ha sido un fracaso... :(:(:(")
                print("Todavía no eres un Maestro Jedi de las matemáticas.")
                        
                while True:
                    
                    print("¿Quieres volver a jugar?\n")
                    perder = input("Pulse Y para ir a inicio o N para salir: ")        
                    
                    if perder == 'Y':
                        Inicio()
                        break
                            
                    elif perder == 'N':
                        print("Gracias por jugar \u2665")
                        break 
                    else:
                        print("Tiene que ser Yes o No ")
                        
                if perder == 'N':
                    break        
        except ValueError:
            print("Tiene que ser un número entero...Vuelva a intentarlo\n")


#################################### NIVEL 6 #############################################        

def nivel_6():

    print("Luke Skywalker introduce el tiempo correcto, activa el temporizador")
    print("y empiezan a sonar las alarmas. Salen de allí corriendo, no hay")
    print("tiempo que perder. La nave se convierte en un hervidero de")
    print("soldados de arriba a abajo y entre el caos que les rodea consiguen")
    print("llegar a la nave y salir de allí a toda prisa. A medida que se alejan")
    print("observan por la ventana la imagen de la colosal estrella de la muerte")
    print("explotando en el silencio del espacio, desapareciendo para siempre")
    print("junto a los restos del malvado imperio.")
    print("¡Has salvado la galaxia gracias a la Fuerza Jedi de las matemáticas!")
    print("Enhorabuena ;D\n")

    ganar = input("Pulsa intro para continuar...\n")
    print("Que la fuerza te acompañe...")
    print("Gracias por jugar; :D\n")
    print("\u2665" * 30 + "\n")
    




#######################   JUEGO   ##############################

Inicio()