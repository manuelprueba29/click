
import csv
import os
# El constructor __init__ se llama automáticamente cuando se crea una nueva instancia de la clase service = ClientService("clients.csv")
from clients.models import Client

class ClientService:

    def __init__(self, table_name):   #table_name: Es el nombre del archivo CSV donde se almacenarán los datos de los clientes
        self.table_name=table_name    #Se asigna a self.table_name, que se usará en todos los métodos de la clase para operar sobre ese archivo.
    """
    En el momento que desde el archivo commands se instancia clients_services=ClientService(ctx.obj['clients_table'])
    table_name tendra el nombre del archivo que en este caso seria clients_table por lo tanto esto se almacenara en 
    self.table_name=table_name permitiendo que el csv este diponible para todo los submetodos
    
    
    """
    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())#Esto agregará una fila con los datos de la instancia client.

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader= csv.DictReader( f, fieldnames=Client.schema())

            return list(reader)
        
    def update_client(self, updated_client):
        clients=self.list_clients()
      
        update_clients=[]
        for client in clients:
            if client['uid'] == updated_client.uid:
                update_clients.append(updated_client.to_dict())
            else:
                update_clients.append(client)
        self._save_to_disk(update_clients)

    def _save_to_disk(self, clients):
        tmp_table_name=self.table_name + '.tmp'
        with open(tmp_table_name, mode='w', newline='') as f:    # Agregar newline='' para evitar líneas en blanco entre filas en Windows
            writer=csv.DictWriter(f, fieldnames=Client.schema())
            #writer.writeheader() # Es opcional pero útil para incluir los nombres de las columnas en el CSV
            for client in clients:
                writer.writerow(client)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
#--------------------------------------------------------------------------------------------------------------
    
    def delete(self, delete_client):
        #validacion del párámetro delete_client
        if not isinstance(delete_client, dict) or 'uid' not in delete_client:
            raise ValueError("delete_client debe ser un diccionario con clave 'uid'.")

        clients=self.list_clients()
        declients=[client for client in clients if client['uid']!=delete_client['uid']]
        self._save_to_disk(declients)

    def _save_to_disk(self, clients):
        tmp_table_name=self.table_name + '.tmp'
        try:

            with open(tmp_table_name, mode='w', newline='') as f:    # Agregar newline='' para evitar líneas en blanco entre filas en Windows
                writer=csv.DictWriter(f, fieldnames=Client.schema())
                writer.writeheader() # Es opcional pero útil para incluir los nombres de las columnas en el CSV
                for client in clients:
                    writer.writerow(client)

            os.remove(self.table_name)
            os.rename(tmp_table_name, self.table_name)
        except Exception as e:
            print(f"Error al guardar los cambios: {e}")
            if os.path.exists(tmp_table_name):
                os.remove(tmp_table_name)  # Eliminar el archivo temporal si hay error
            raise

