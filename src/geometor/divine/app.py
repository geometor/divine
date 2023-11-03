"""
run the main app
"""
from .divine import Divine


def run() -> None:
    reply = Divine().run()
    print(reply)
