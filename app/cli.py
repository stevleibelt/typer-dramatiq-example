import os
import subprocess
import typer

from shared.actor_broker import ContextModuleStrEnum, actor_broker
from shared.utility import project_app_source_base_path

app = typer.Typer()


@app.command(name="send-a-a")
def app_send_a_a(
    message: str = "The message is love"
) -> None:
    actor_broker.send(context_module=ContextModuleStrEnum.a, actor_function_name='a_a', data={'message': message})


@app.command(name="send-a-b")
def app_send_a_b(
    sleep_in_seconds: int = 2
) -> None:
    actor_broker.send(context_module=ContextModuleStrEnum.a, actor_function_name='a_b', data={'sleep_in_seconds': sleep_in_seconds})


@app.command(name="send-b-a")
def app_send_b_a() -> None:
    actor_broker.send(context_module=ContextModuleStrEnum.b, actor_function_name='b_a', data=None)


@app.command(name="send-b-b", help="This will create an AttributeError")
def app_send_b_b() -> None:
    actor_broker.send(context_module=ContextModuleStrEnum.b, actor_function_name='b_b', data=None)


@app.command(name="start-workers")
def app_start_workers() -> None:
    command_list: list = [
        "env",
        f"PYTHONPATH={project_app_source_base_path}",
        "dramatiq-gevent",
        "shared.actor_broker",
        "-p 4",
        "-t 8",
        "--watch",
        f"{project_app_source_base_path}",
        "--watch-use-polling",
        "--verbose",
    ]

    typer.echo(f"Starting command: {' '.join(command_list)}")
    result = subprocess.run(command_list, check=True, env=os.environ)

    typer.echo(f"Result: {result}")

if __name__ == "__main__":
    app(prog_name="Typer Dramatiq Example")
