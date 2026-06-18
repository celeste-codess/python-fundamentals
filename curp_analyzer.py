from stdnum.mx import curp as validador_curp

curp_usuario = input("Ingresa tu CURP: ").upper()

def analiza_curp(c):
    # Genero
    if c[10] == "M":
        genero = "Es mujer"
    else:
        genero = "Es hombre"

    # Fecha
    anio = c[4:6]
    mes = c[6:8]
    dia = c[8:10]
    fecha = dia + "/" + mes + "/" + anio

    # Diccionario de Estados
    estados = {
        "AS":"Aguascalientes","BC":"Baja California","BS":"Baja California Sur",
        "CC":"Campeche","CL":"Coahuila","CM":"Colima","CS":"Chiapas",
        "CH":"Chihuahua","DF":"Ciudad de México","DG":"Durango",
        "GT":"Guanajuato","GR":"Guerrero","HG":"Hidalgo",
        "JC":"Jalisco","MC":"Estado de México","MN":"Michoacán",
        "MS":"Morelos","NT":"Nayarit","NL":"Nuevo León",
        "OC":"Oaxaca","PL":"Puebla","QT":"Querétaro",
        "QR":"Quintana Roo","SP":"San Luis Potosí","SL":"Sinaloa",
        "SR":"Sonora","TC":"Tabasco","TS":"Tamaulipas",
        "TL":"Tlaxcala","VZ":"Veracruz","YN":"Yucatán","ZS":"Zacatecas"
    }

    # Validación y Estado
    if validador_curp.is_valid(c):
        codigo_estado = c[11:13]
        estado_final = estados.get(codigo_estado, "Estado desconocido")
    else:
        estado_final = "Escríbela bien"

    # Concatenación
    resumen = "GÉNERO: " + genero + "\nFECHA: " + fecha + "\nESTADO: " + estado_final
    print("\n--- RESULTADO ---")
    print(resumen)

# --- ESTO ES LO QUE TE FALTABA: LA LLAMADA ---
# Llamamos a la función y le pasamos lo que el usuario escribió
analiza_curp(curp_usuario)