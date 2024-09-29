__all__ = ["setup_dramatiq"]

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.middleware import AgeLimit, Retries, ShutdownNotifications

_setup_needed = True

def setup_dramatiq() -> None:
    global _setup_needed

    if _setup_needed:
        dramatiq.set_broker(
            broker=RedisBroker(
                db=2,
                host="valkey-dev",
                middleware=[
                    AgeLimit(max_age=3600000),  # 60 minutes are 3600000 milliseconds
                    Retries(max_retries=3),
                    ShutdownNotifications(True),
                ],
                port=6379,
            )
        )
        _setup_needed = False
