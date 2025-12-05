def p1_etapa_vital():
    print("\n--- P1. Etapa vital y formativa ---")
    
    while True:
        try:
            edad_input = input("Ingresa la edad de la persona: ")
            if not edad_input.isdigit():
                print("Error: La edad debe ser un número entero.")
                continue

            edad = int(edad_input)
            if edad < 0 or edad > 120:
                print("Error: La edad ingresada no es coherente (0-120). Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Error de entrada. Intenta de nuevo.")

    while True:
        estudia_trabaja = input("¿Estudia (S/N)? ").strip().upper()
        if estudia_trabaja in ('S', 'N'):
            break
        print("Respuesta inválida. Debe ser 'S' para Sí o 'N' para No.")

    trabaja = False
    if edad >= 18:
        while True:
            trabaja_input = input("¿Trabaja (S/N)? ").strip().upper()
            if trabaja_input in ('S', 'N'):
                trabaja = (trabaja_input == 'S')
                break
            print("Respuesta inválida. Debe ser 'S' o 'N'.")

    estudia = (estudia_trabaja == 'S')
    etapa = "No determinado"

    if edad < 6:
        etapa = "Infante"
    elif 6 <= edad <= 17 and estudia:
        etapa = "Estudiante escolar"
    elif 18 <= edad <= 25 and estudia:
        etapa = "Universitario"
    elif edad > 25 and trabaja:
        etapa = "Adulto activo"
    elif edad > 60 and not trabaja:
        etapa = "Adulto mayor jubilado"

    print(f"\nResultado: La persona se clasifica como: **{etapa}**")
    print("-" * 30)


def p2_participante_elegible():
    print("\n--- P2. Participante elegible ---")

    while True:
        try:
            edad = int(input("Ingresa la edad del participante: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingresa un número para la edad.")

    while True:
        licencia = input("¿Tiene licencia vigente (S/N)? ").strip().upper()
        if licencia in ('S', 'N'):
            licencia_vigente = (licencia == 'S')
            break
        print("Respuesta inválida. Debe ser 'S' o 'N'.")

    while True:
        propio = input("¿Tiene vehículo propio (S/N)? ").strip().upper()
        if propio in ('S', 'N'):
            tiene_propio = (propio == 'S')
            break
        print("Respuesta inválida. Debe ser 'S' o 'N'.")

    while True:
        if not tiene_propio:
            prestamo = input("¿Tiene préstamo autorizado (S/N)? ").strip().upper()
            if prestamo in ('S', 'N'):
                prestamo_autorizado = (prestamo == 'S')
                break
            print("Respuesta inválida. Debe ser 'S' o 'N'.")
        else:
            prestamo_autorizado = False
            break

    elegible = (edad >= 18) and licencia_vigente and (tiene_propio or prestamo_autorizado)
    
    if elegible:
        resultado = "Apto"
    else:
        resultado = "No apto"

    print(f"\nResultado: La persona es **{resultado}** para la competencia.")
    print("-" * 30)


def p3_control_acceso():
    print("\n--- P3. Control de acceso ---")
    
    USUARIOS_RESTRINGIDOS = ["ADMIN", "SISTEMA", "TEST"]
    
    while True:
        usuario = input("Ingresa el nombre de usuario: ").strip().upper()
        if usuario:
            break
        print("El nombre de usuario no puede estar vacío.")

    while True:
        try:
            codigo_input = input("Ingresa el código numérico: ").strip()
            if not codigo_input.isdigit():
                print("El código debe ser un número entero.")
                continue
            codigo = int(codigo_input)
            break
        except ValueError:
            print("Error de entrada.")

    usuario_permitido = usuario not in USUARIOS_RESTRINGIDOS
    codigo_valido = (codigo % 2 == 0) or (codigo % 10 == 7)
    
    if usuario_permitido and codigo_valido:
        print(f"\n**ACCESO PERMITIDO** para el usuario: {usuario}")
    else:
        print("\n**ACCESO DENEGADO**.")
        if not usuario_permitido:
            print(f"Motivo: El usuario '{usuario}' está en la lista restringida.")
        elif not codigo_valido:
            print("Motivo: El código numérico no cumple las condiciones de seguridad.")

    print("-" * 30)


def p4_registro_asistentes():
    print("\n--- P4. Registro de asistentes ---")
    
    nombres_ingresados = []
    
    print("Comienza el registro. Escribe **'FIN'** para terminar.")
    
    while True:
        nombre = input("Ingresa un nombre (o FIN para salir): ").strip()
        
        if nombre.upper() == "FIN":
            break
            
        if not nombre:
            print("Entrada ignorada: No se permiten entradas vacías.")
            continue

        nombres_ingresados.append(nombre)
    
    total_nombres = len(nombres_ingresados)
    conteo_nombres = {}
    nombres_repetidos = False
    
    for nombre in nombres_ingresados:
        nombre_normalizado = nombre.upper()
        
        if nombre_normalizado in conteo_nombres:
            conteo_nombres[nombre_normalizado] += 1
            nombres_repetidos = True
        else:
            conteo_nombres[nombre_normalizado] = 1

    print("\n--- Resultados del Registro ---")
    print(f"Total de nombres ingresados: **{total_nombres}**")
    
    if nombres_repetidos:
        print("Presencia de nombres repetidos: **SÍ**")
        repetidos_list = [name for name, count in conteo_nombres.items() if count > 1]
        if repetidos_list:
            print(f"Nombres que se repiten: {', '.join(repetidos_list)}")
    else:
        print("Presencia de nombres repetidos: **NO**")
        
    print("-" * 30)


def p5_intentos_limitados():
    print("\n--- P5. Intentos limitados ---")
    
    USUARIO_CORRECTO = "admin"
    CONTRASENA_CORRECTA = "12345"
    MAX_INTENTOS = 3
    
    intentos = 0
    acceso_exitoso = False

    while intentos < MAX_INTENTOS and not acceso_exitoso:
        print(f"\nIntento {intentos + 1} de {MAX_INTENTOS}")
        
        usuario_input = input("Usuario: ").strip()
        contrasena_input = input("Contraseña: ").strip()
        
        if not usuario_input and not contrasena_input:
            print("Intento no válido: Ambos campos están vacíos. Intento no contado.")
            continue
        
        intentos += 1

        if usuario_input == USUARIO_CORRECTO and contrasena_input == CONTRASENA_CORRECTA:
            acceso_exitoso = True
            print("\n¡Acceso exitoso!")
        else:
            fallo_usuario = usuario_input != USUARIO_CORRECTO
            fallo_contrasena = contrasena_input != CONTRASENA_CORRECTA
            
            print("Credenciales incorrectas.")
            if fallo_usuario and fallo_contrasena:
                print("Motivo: Usuario y contraseña incorrectos.")
            elif fallo_usuario:
                print("Motivo: Usuario incorrecto.")
            elif fallo_contrasena:
                print("Motivo: Contraseña incorrecta.")

    if not acceso_exitoso:
        print(f"\nLímite de {MAX_INTENTOS} intentos alcanzado. Sesión bloqueada.")

    print("-" * 30)


def p6_analisis_numerico():
    print("\n--- P6. Análisis numérico ---")
    
    numeros = []
    i = 1

    while len(numeros) < 3:
        try:
            num = int(input(f"Ingresa el número entero {i} de 3: "))

            numeros.append(num)
            i += 1
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

    n1, n2, n3 = numeros

    print("\n--- Resultados del Análisis ---")
    
    tres_positivos = (n1 > 0) and (n2 > 0) and (n3 > 0)
    print(f"1. ¿Los tres son positivos? **{'Sí' if tres_positivos else 'No'}**")
    
    al_menos_uno_negativo = (n1 < 0) or (n2 < 0) or (n3 < 0)
    print(f"2. ¿Al menos uno es negativo? **{'Sí' if al_menos_uno_negativo else 'No'}**")
    
    exactamente_uno_cero = \
        ((n1 == 0) and (n2 != 0) and (n3 != 0)) or \
        ((n1 != 0) and (n2 == 0) and (n3 != 0)) or \
        ((n1 != 0) and (n2 != 0) and (n3 == 0))
        
    print(f"3. ¿Exactamente uno es cero? **{'Sí' if exactamente_uno_cero else 'No'}**")
    
    print("-" * 30)


def p7_clasificacion_cliente():
    print("\n--- P7. Clasificación de cliente ---")
    
    while True:
        try:
            monto_input = input("Ingresa el valor total de la compra: ").strip()
            if not monto_input.replace('.', '', 1).isdigit():
                print("Error: El monto ingresado es inválido (debe ser un número).")
                continue
            monto = float(monto_input)
            if monto < 0:
                print("Error: El monto no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: El monto ingresado es inválido.")
    
    print("\nTipos de membresía: [A]ctiva, [T]emporal, [I]nactiva")
    while True:
        membresia = input("Ingresa el tipo de membresía (A/T/I): ").strip().upper()
        if membresia in ('A', 'T', 'I'):
            break
        print("Respuesta inválida. Debe ser 'A', 'T' o 'I'.")

    MONTO_ALTO = 500
    MONTO_MEDIO = 100
    
    cliente = "Regular"
    
    if monto >= MONTO_ALTO and membresia == 'A':
        cliente = "Premium"
    elif monto >= MONTO_MEDIO or membresia == 'T':
        cliente = "Frecuente"
    
    print(f"\nResultado: El cliente se clasifica como: **{cliente}**")
    print("-" * 30)


def p8_encuesta_preferencias():
    print("\n--- P8. Encuesta de preferencias ---")
    
    respuestas_si = 0
    respuestas_no = 0
    
    print("Inicia la encuesta. Ingresa una edad mayor a cero para comenzar. Ingresa 0 (cero) para finalizar.")
    
    while True:
        try:
            edad_input = input("\nIngresa la edad (0 para salir): ").strip()
            if not edad_input.isdigit():
                print("Error: La edad debe ser un número entero.")
                continue
            
            edad = int(edad_input)
            
            if edad <= 0:
                break
        except ValueError:
            print("Error de entrada. Intenta de nuevo.")
            continue
            
        while True:
            respuesta = input("¿Te gusta programar (Sí/No)? ").strip().upper()
            
            if not respuesta:
                print("No se permiten respuestas vacías. Intenta de nuevo.")
                continue

            if respuesta in ('SÍ', 'SI'):
                respuestas_si += 1
                break
            elif respuesta in ('NO'):
                respuestas_no += 1
                break
            else:
                print("Respuesta incorrecta. Por favor, responde 'Sí' o 'No'.")

    print("\n--- Resultados de la Encuesta ---")
    print(f"Total de respuestas afirmativas ('Sí'): **{respuestas_si}**")
    print(f"Total de respuestas negativas ('No'): **{respuestas_no}**")
    print("-" * 30)
