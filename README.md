# typer-dramatiq-example

Example installation using docker, typer and dramatiq

This is an example where [one actor broker](app/shared/actor_broker.py) is used to dynamically load and call a function from a bounded context.
This is currently the only way I found where each enqueued message is processed.

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## What is working and what not

* In a separate window
* cd into the project path
* `docker compose exec cli-dev bash`
* `python /app/cli.py send-a-a`
  * This results in a log message like `worker-dev  | [2024-09-26 22:08:32: The message in a_a is: The message is love`
* `python /app/cli.py send-a-b`
  * This results in a log message like `worker-dev  | [2024-09-26 22:08:38: a_b sleeping has been finished`
* `python /app/cli.py send-b-a`
  * This results in a log message like `worker-dev  | [2024-09-26 22:08:39]: This is b_a speaking`
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
