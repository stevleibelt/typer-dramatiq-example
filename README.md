# typer-dramatiq-example

Example installation using docker, typer and dramatiq.

I could not find any example project out there with more than one actor defined, so I had written this one.

This example project has multiple branches. Each branch shows an implementation with possible issues.

* [one_workers_file_per_context](https://github.com/stevleibelt/typer-dramatiq-example/tree/one_workers_file_per_context)
  * Upside: Each actor can be called to enqueue a message
  * Downside: Only the messages from the actors defined in the first workers file where processed
* [all_actors_in_one_workers_file](https://github.com/stevleibelt/typer-dramatiq-example/tree/all_actors_in_one_workers_file)
  * Upside: Each actor can be called to enqueue a message
  * Downside: Only the messages from the last imported actors where processed
* [all_actors_in_one_workers_file_working](https://github.com/stevleibelt/typer-dramatiq-example/tree/all_actors_in_one_workers_file_working)
  * This is my current best approach
  * Upside:
    * Each actor can be called to enqueue a message
    * All messages where processed
    * You can call the actor directly in the code
  * Downside: One worker file combines all actors (take care of good and uniq naming)
* [one_broker](https://github.com/stevleibelt/typer-dramatiq-example/tree/one_broker)
  * Upside:
    * Each actor can be called to enqueue a message
    * All messages where processed
  * Downside: Only one actor is defined

## Setup Steps

* Checkout source code
* cd into project path
* `docker compose up`

## Development Notes

```bash
uv init .
uv venv --python 3.11
uv pip sync requirements.txt
```
