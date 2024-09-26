__all__ = ["b_a"]

from shared.utility import get_current_datetime

def b_a(data: dict = None) -> None:
    print(f"[{get_current_datetime()}]: This is b_a speaking")
