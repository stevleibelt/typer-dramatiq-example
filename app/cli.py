import os
import subprocess
import typer

from shared.utility import project_app_source_base_path

app = typer.Typer()


@app.command(name="send-a-a")
def app_send_a_a(
    message: str = "The message is love"
) -> None:
    from context.a.workers import a_a

    a_a.send(message=message)


@app.command(name="send-a-b")
def app_send_a_b(
    sleep_in_seconds: int = 2
) -> None:
    from context.a.workers import a_b

    a_b.send(sleep_in_seconds=sleep_in_seconds)


@app.command(name="send-b-a")
def app_send_b_a() -> None:
    from context.b.workers import b_a

    b_a.send()


@app.command(name="start-workers")
def app_start_workers() -> None:
    command_list: list = [
        "env",
        f"PYTHONPATH={project_app_source_base_path}",
        "dramatiq-gevent",
        "context.a.workers",
        "context.b.workers",
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
