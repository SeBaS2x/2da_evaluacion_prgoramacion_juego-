# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año.
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”.
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche

destino = input("Escoja su destino: (Bariloche, Mar del plata, cataratas,) ")
estacion = input("Escoja su estación del año: (invierno, verano, otoño, primavera) ")
mensaje = "no se puede viajar"

match (destino, estacion):
    case "Bariloche", "invierno":
        mensaje = "Se puede viajar"
    case "Mar del plata" | "cataratas", "verano":
        mensaje = "Se puede viajar"
    case "Bariloche" | "Mar del plata" | "cataratas", "otoño":
        mensaje = "Se puede viajar"
    case "Mar de plata" | "cataratas", "primavera":
        mensaje = "Se puede viajar"

print(mensaje)
