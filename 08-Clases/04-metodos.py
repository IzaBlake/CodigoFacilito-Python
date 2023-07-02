# Attrs de clase
# Attrs de instancia

class Usuario:

    def inicializar(self, username, password):
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar('User1', 'password1')
user2.inicializar('User2', '12345')
user3.inicializar('Cody', 'password3')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
