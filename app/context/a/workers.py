__all__ = ["a_a", "a_b"]

from dramatiq import actor
from time import sleep
from shared.dramatiq import setup_dramatiq
from shared.utility import get_current_datetime

setup_dramatiq()

@actor(queue_name="a_a_queue")
def a_a(message: str) -> None:
    print(f"[{get_current_datetime()}: The message in a_a is: {message}")


@actor(queue_name="a_b_queue")
def a_b(sleep_in_seconds: int) -> None:
    print(f"[{get_current_datetime()}: a_b is sleeping for: {sleep_in_seconds} seconds")
    sleep(sleep_in_seconds)
    print(f"[{get_current_datetime()}: a_b sleeping has been finished")
