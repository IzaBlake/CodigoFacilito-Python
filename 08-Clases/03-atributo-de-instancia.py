# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__


user1 = Usuario()
# 1.- Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attrs existe dentro de la clase -> Lectura
# 3.- Lanzar un error
print(user1.username)


Usuario.username = 'User1'
Usuario.email = 'info@codigofacilito.com'

print(Usuario.username)
print(Usuario.email)
