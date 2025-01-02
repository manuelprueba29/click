import click
from clients import commands as clients_commands

CLIENTS_TABLE='.clients.csv'

@click.group()
@click.pass_context # permite que una función reciba el contexto (ctx) de la CLI. El contexto (ctx) es un objeto que contiene información compartida y útil para todos los subcomandos de la aplicación.
def cli(ctx):
    ctx.obj={}
    ctx.obj['clients_table']=CLIENTS_TABLE


cli.add_command(clients_commands.all)


if __name__ == "__main__":
        cli()
   
