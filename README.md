# typer-dramatiq-example

Example installation using docker, typer and dramatiq

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## What is working and what not

* In a separate window
* cd into the project path
* `docker compose exec cli-dev bash`
* `python /app/cli.py send-a-a`
  * This is not working, no message was produced
* `python /app/cli.py send-a-b`
  * This is not working, no message was produced
* `python /app/cli.py send-b-a`
  * This results in a log message like `worker-dev  | [2024-09-26 21:29:36]: This is b_a speaking`
  * This is not working, no message was produced
* `docker compose exec valkey-dev sh`
* `valkey-cli`
* `SELECT 2`
* `KEYS *`
```bash
127.0.0.1:6379[2]> KEYS *
1) "dramatiq:__heartbeats__"
2) "dramatiq:a_b_queue"
3) "dramatiq:a_a_queue.msgs"
4) "dramatiq:a_a_queue"
5) "dramatiq:a_b_queue.msgs"
127.0.0.1:6379[2]> LRANGE dramatiq:a_a_queue 0 -1
1) "88240463-404a-41b8-810c-68558f443aca"
127.0.0.1:6379[2]> LRANGE dramatiq:a_b_queue 0 -1
1) "e4a284bf-a6ab-4539-a080-f67f1725ee91"
```
  * This messages where enqueued but it is not processed by dramatiq

## Development Notes

```bash
uv init .
uv venv --python 3.11
uv pip sync requirements.txt
```
