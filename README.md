# typer-dramatiq-example

Example installation using docker, typer and dramatiq

This is an example where the [first loaded](app/context/a/workers.py) file containing dramatiq actors is able to process the enqueued messages.
----
This branch differs to the [one_workers_file_per_context](https://github.com/stevleibelt/typer-dramatiq-example/tree/one_workers_file_per_context) branch in the way how and when the dramatiq broker is set up. In this example, once the broker is set up, no second set up is made.

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## What is working and what not

* In a separate window
* cd into the project path
* `docker compose exec cli-dev bash`
* `python /app/cli.py send-a-a`
  * This results in a log message like `worker-dev  | [2024-09-29 22:12:38: The message in a_a is: The message is love`
* `python /app/cli.py send-a-b`
  * This results in a log message like `worker-dev  | [2024-09-29 22:12:42: a_b sleeping has been finished`
* `python /app/cli.py send-b-a`
  * This results in a log message like `worker-dev  | [2024-09-29 22:12:36]: This is b_a speaking`
* `docker compose exec valkey-dev sh`
* `valkey-cli`
* `SELECT 2`
* `KEYS *`
```bash
127.0.0.1:6379[2]> KEYS *
2) "dramatiq:__heartbeats__"
```
