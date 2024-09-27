# typer-dramatiq-example

Example installation using docker, typer and dramatiq

This is an example where all actors where loaded in [one workers](app/shared/workers.py).
This branch differs to the [all actors in one workers file branch](https://github.com/stevleibelt/typer-dramatiq-example/tree/all_actors_in_one_workers_file) in the way how and when the dramatiq broker is set up.
In this example, all messages where enqueued and processed

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## What is working and what not

* In a separate window
* cd into the project path
* `docker compose exec cli-dev bash`
* `python /app/cli.py send-a-a`
  * This results in a log message like `worker-dev  | [2024-09-27 09:43:53: The message in a_a is: The message is love`
* `python /app/cli.py send-a-b`
  * This results in a log message like `worker-dev  | [2024-09-27 09:43:58: a_b sleeping has been finished`
* `python /app/cli.py send-b-a`
  * This results in a log message like `worker-dev  | [2024-09-27 09:44:00]: This is b_a speaking`
* `docker compose exec valkey-dev sh`
* `valkey-cli`
* `SELECT 2`
* `KEYS *`
```bash
127.0.0.1:6379[2]> KEYS *
1) "dramatiq:__heartbeats__"
```

## Development Notes

```bash
uv init .
uv venv --python 3.11
uv pip sync requirements.txt
```
