from shared.dramatiq import setup_dramatiq

# You have to set up dramatiq before importing all actors
setup_dramatiq()

from context.a.workers import *
from context.b.workers import *
