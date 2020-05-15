import click
import yaml
import requests
import configparser


@click.group()
@click.option('-i', '--report-id', default=None)
@click.option('-c', '--config', default="statuscake.conf")
@click.pass_context
def cli(ctx, report_id, config):
    conf = configparser.ConfigParser()
    conf.read(config)

    ctx.obj['api-key'] = conf['default']['api-key']
    ctx.obj['report-id'] = report_id or conf['default']['default-reporting']



@cli.command()
@click.pass_context
def getreps(ctx):
    print(requests.get(
                "https://app.statuscake.com/API/PublicReporting",
                headers={"API": ctx.obj['api-key'], "Username": "volodymyr"},
            ).text)

@cli.command()
@click.pass_context
def getrep(ctx):
    print(requests.get(
                "https://app.statuscake.com/API/PublicReporting",
                headers={"API": ctx.obj['api-key'], "Username": "volodymyr"},
                params={"id": ctx.obj['report-id']}
            ).text)

@cli.command()
@click.argument("announce")
@click.pass_context
def postrep(ctx, announce):
    r = requests.post(
                "https://app.statuscake.com/API/PublicReporting/Update",
                headers={"API": ctx.obj['api-key'], "Username": "volodymyr"},
                data={
                        "id": ctx.obj['report-id'],
                        "announcement": announce,
                    }
            )
    print(r, r.text)

def main():
    cli(obj={})

if __name__ == "__main__":
    main()
