__all__ = ["a_a", "a_b"]

from time import sleep
from shared.utility import get_current_datetime

def a_a(data: dict = None) -> None:
    if 'message' not in data:
        raise KeyError("Missing key: 'message'")

    if not isinstance(data['message'], str):
        raise TypeError("Expected 'message' to be of type str.")

    print(f"[{get_current_datetime()}: The message in a_a is: {data['message']}")


def a_b(data: dict = None) -> None:
    if 'sleep_in_seconds' not in data:
        raise KeyError("Missing key: 'sleep_in_seconds'")

    if not isinstance(data['sleep_in_seconds'], int):
        raise TypeError("Expected 'sleep_in_seconds' to be of type int.")

    print(f"[{get_current_datetime()}: a_b is sleeping for: {data['sleep_in_seconds']} seconds")
    sleep(data['sleep_in_seconds'])
    print(f"[{get_current_datetime()}: a_b sleeping has been finished")
