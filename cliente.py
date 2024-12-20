

import random
import sys


clients=[
     {
          'name':'Pablo',
          'company': 'Google',
          'email':'pablo@google.com',
          'position':'software enginner',
     },
     {
         'name':'Ricardo',
          'company': 'Facebook',
          'email':'ricardo@facebook.com',
          'position':'Data enginner', 
     }
]


def create_client(client_name):
    global clients

    if client_name not in clients:
         clients.append(client_name)
         
    else:
         print('Client already is in the client\'s list')

def list_clients():
    for idx, client in enumerate(clients):   
         print('{uid}|{name}|{company}|{email}|{position}'.format(
              uid=idx,
              name=client['name'],
              company=client['company'],
              email=client['email'],
              position=client['position']))
         
def update_client(client_name, updated_name):
     
     if client_name in clients:
          index=clients.index(client_name)
          clients[index]=updated_name
     else:
          print("No se encontro el cliente en la lista")

def delete_client(client_name):
 
     if client_name in clients:
          clients.remove(client_name)
     else:
          print('Cliente no existe en la lista')

def search_client(client_name):
     for client in clients:
          if client != client_name:
               continue
          else:
               return True

def _get_client_field(field_name):
     field=None

     while not field:
          field=input('what is the client {}?'.format(field_name))
     return field
          
def Welcome():
        print('Bienvenido a platzi')
        print('*'*50)
        print('Que haces hoy')
        print('[C]Crear varios clientes')
        print('[U]update')
        print('[D]Eliminar cliente ')
        print('[B]Buscar')


def _get_cliente_name():
     return input('nombre del cliente')


if __name__=='__main__':
    Welcome()
    comando = input()
    comando = comando.upper()

    if comando =='C':
         cliente= {
              'name': _get_client_field('name'),
              'company': _get_client_field('company'),
              'email': _get_client_field('email'),
              'position':_get_client_field('position'),
         }
         create_client(cliente)
         list_clients()
    elif comando=='D':
         
         client_namee=_get_cliente_name()
         delete_client(client_namee)
         list_clients()
        
    elif comando=='U':
         client_namee=_get_cliente_name()
         updateClienname=input('Ingresa el nuevo nombre')
         update_client(client_namee, updateClienname)
         list_clients()

    elif comando=='B':
         cliente=_get_cliente_name()
         found=search_client(cliente)
         if found:
              print('El cliente esta en la lista')
         else:
              print('cliente: {} NO se encontro '.format(cliente))

         pass
    
    else:
         print('Comando invalido')

a=1,2,3,4

print(type(a))

studen_uid=[1,2,3]

students=['Juan', 'Jose', 'Larsen']

students_with_uid={}

