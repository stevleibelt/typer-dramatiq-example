from dramatiq import actor
from enum import StrEnum
from importlib import import_module

from .dramatiq import setup_dramatiq

setup_dramatiq()

class ContextModuleStrEnum(StrEnum):
    a: str = "a"
    b: str = "b"

@actor(queue_name="example_queue")
def actor_broker(context_module: ContextModuleStrEnum, actor_function_name: str, data: dict) -> None:
    try:
        module = import_module(f"context.{context_module}.workers")

        actor_function = getattr(module, actor_function_name)

        actor_function(data=data)

    except ImportError as error:
        print(f"Could not import module {context_module}: {error}")
    except AttributeError as error:
        print(f"Could not import function {actor_function_name} from module {context_module}: {error}")
    except Exception as exception:
        print(f"An error occurred: {exception}")
