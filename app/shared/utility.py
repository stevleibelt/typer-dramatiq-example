from datetime import datetime
from os import path

project_app_source_base_path = path.split(path.abspath(path.dirname(__file__)))[0]

def get_current_datetime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
