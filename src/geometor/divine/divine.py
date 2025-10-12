"""
divine
"""
from geometor.model import Model
from .events import point_added_listener

def analyze_model(model: Model):
    """
    Initializes the divine analysis by registering event listeners.
    """

    model.add_event_listener("point_added", lambda pt: point_added_listener(model, pt))

