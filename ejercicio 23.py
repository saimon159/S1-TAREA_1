#Dado un número entero N que representa una contraseña y asumiendo que una contraseña debe tener al menos 10 dígitos para ser segura, determine si la contraseña ingresada por el usuario es correcta, de no serlo debe pedirla nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta mostrar un mensaje de éxito al usuario, por salida estándar. 

def checkPassword(password): 
    has_upper = False
    has_lower = False
    has_num = False
    
    for ch in password: 
        if ch >= 'A' and ch <= 'Z': 
            has_upper = True
        elif ch >= 'a' and ch <= 'z': 
            has_lower = True
        elif ch >= '0' and ch <= '9':    
            has_num = True
    
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False

def main(): 
    p = input("Ingrese Contraseña: " )
    if checkPassword(p): 
        print("La contraseña es buena")
    else: 
        print("La contraseña es débil")

if __name__ == "__main__": 
    main()