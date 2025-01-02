import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycles"""
    #pass


@clients.command()
@click.option('-n', '--name',
               type=str,
               prompt=True,
               help='The client name')
@click.option('-c', '--company',
               type=str,
               prompt=True,
               help='The client company')
@click.option('-e', '--email',
               type=str,
               prompt=True,
               help='The client email')
@click.option('-p', '--position',
               type=str,
               prompt=True,
               help='The client position')

@click.pass_context
def create(ctx, name, company, email, position):
    """create a new client"""
    client=Client(name, company, email, position)
    clients_services=ClientService(ctx.obj['clients_table'])
    clients_services.create_client(client)
    


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    clients_services=ClientService(ctx.obj['clients_table'])
    clients_list=clients_services.list_clients()

    click.echo(' ID | NAME | COMPANY | EMAIL | POSITION')
    click.echo('*' * 100)

    for client in clients_list:
        click.echo('{uid} | {name} |{company} | {email} | {position}'.format(

            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


@clients.command()
@click.argument('clients_uid', type=str)
@click.pass_context
def update(ctx, clients_uid):
    """Update a clients"""
    clients_services=ClientService(ctx.obj['clients_table'])
    clients_list=clients_services.list_clients()
    client = [client for client in clients_list if client['uid']==clients_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        clients_services.update_client(client)

        click.echo('Client updated')

    else:
        click.echo('client not found')

  

def _update_client_flow(client):
    click.echo('leave empty if you dont want to modify the value')

    client.name = click.prompt('new name', type=str, default=client.name)
    client.company = click.prompt('new company', type=str, default=client.company)
    client.email = click.prompt('new email', type=str, default=client.email)
    client.position = click.prompt('new position', type=str, default=client.position)
    return client


@clients.command()
@click.argument('clients_uid', type=str)
@click.pass_context
def delete(ctx, clients_uid):
    """Delete a clients"""
    clients_services=ClientService(ctx.obj['clients_table'])
    clients_list=clients_services.list_clients()

    client_delete = next((client for client in clients_list if client['uid']==clients_uid), None)
    if client_delete:
          # Llamar a delete con el cliente encontrado
        clients_services.delete(client_delete)

        click.echo("Client deleted")
    else:
        click.echo("client not found")

all=clients