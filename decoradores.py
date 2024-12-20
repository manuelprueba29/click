#decoradores el decorador se utiliza para que se ejecute una funcion que valida algunos datos, si es correcto se ejecuta la función principal que en este caso seria needs_password
PASSWORD='12345'

def password_required(func):
    def wrapper():
        password=input('Cual es tu contraseña?')

        if password==PASSWORD:
            return func()
        else:
            print("la contraseña no es correcta")
    return wrapper

@password_required
def needs_password():
    print('La contasena es correcta')

def upper(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        return result.upper()
    return wrapper

@upper
def say_my_name(name):
    return('hola, {}'.format(name))

if __name__=='__main__':
    needs_password()
    print(say_my_name('David'))


def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #Acciones adicionales que decoran

        print("Vamos a realizar un cálculo:")

        funcion_parametro()

        #accion a adicianal que decoran

        print("Hemos terminado el cálculo")
    return funcion_interior

@funcion_decoradora
def suma():
    print(5+8)

