# typer-dramatiq-example

Example installation using docker, typer and dramatiq

This is an example where the [first loaded](app/context/a/workers.py) file containing dramatiq actors is able to process the enqueued messages.
All other actors are ignored within the worker process.

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## What is working and what not

* In a separate window
* cd into the project path
* `docker compose exec cli-dev bash`
* `python /app/cli.py send-a-a`
  * This results in a log message like `worker-dev  | [2024-09-26 15:45:27: The message in a_a is: The message is love`
* `python /app/cli.py send-a-b`
  * This results in a log message like `worker-dev  | [2024-09-26 15:47:32: a_b sleeping has been finished`
* `python /app/cli.py send-b-a`
  * This is not working, no message was produced
* `docker compose exec valkey-dev sh`
* `valkey-cli`
* `SELECT 2`
* `KEYS *`
```bash
127.0.0.1:6379[2]> KEYS *
1) "dramatiq:b_a"
2) "dramatiq:__heartbeats__"
3) "dramatiq:b_a.msgs"
127.0.0.1:6379[2]> LRANGE dramatiq:b_a 0 -1
1) "4847ecfe-7dfd-4781-bdbd-aadc963dfc16"
```
  * A message was enqueued but it is not processed by dramatiq
