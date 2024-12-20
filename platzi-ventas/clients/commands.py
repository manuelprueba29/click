import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycles"""
    pass


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
    pass


@clients.command()
@click.pass_context
def update(ctx, clients_uid):
    """Update a clients"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a clients"""
    pass

all=clients