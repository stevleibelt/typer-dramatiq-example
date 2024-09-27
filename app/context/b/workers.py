__all__ = ["b_a"]

from dramatiq import actor

from shared.utility import get_current_datetime

@actor(queue_name="b_a")
def b_a() -> None:
    print(f"[{get_current_datetime()}]: This is b_a speaking")
