class Persona:
    def __init__(self, name, age) :
        self.name=name
        self.age=age
    
    def say_hello(self):
        print('Hello, my name is {} and I am {} years old'.format(self.name, self.age))#Se utiliza el self para acceder a los valores de las variables o atributo

if __name__=='__main__':
    persona1=Persona('David', 34)#objeto, instancia de la clase

    print('Age {} '.format(persona1.age))
    persona1.say_hello()
