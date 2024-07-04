import re

class PasswordValidationError(Exception):
    pass

def validar_password(password):
    try:
        if not (8 <= len(password) <= 16):
            raise PasswordValidationError("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
        if not re.search('[a-z]', password):
            raise PasswordValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search('[A-Z]', password):
            raise PasswordValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search('[0-9]', password):
            raise PasswordValidationError("La contraseña debe contener al menos un dígito.")
        if not re.search('[$@#]', password):
            raise PasswordValidationError("La contraseña debe contener al menos uno de los siguientes caracteres: $@#.")
        return True
    except Exception as e:
        print(f"Error al validar la contraseña: {e}")
        return False
try:
    # Solicitamos al usuario que ingrese la contraseña
    clave = input('Escriba la contraseña: ')
    if not clave:
        # Si la entrada está vacía, lanzamos una excepción ValueError
        raise ValueError("La contraseña no puede estar vacía")
    
    # Intentamos validar la contraseña ingresada
    print(validar_password(clave))
except ValueError as ve:
    # Capturamos específicamente excepciones de tipo ValueError y mostramos un mensaje de error.
    print(f"Entrada inválida: {ve}")
except Exception as e:
    # Capturamos cualquier otra excepción y mostramos un mensaje de error.
    print(f"Error inesperado: {e}")