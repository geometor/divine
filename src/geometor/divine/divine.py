"""
divine
"""
from geometor.model import Model
from .events import point_added_listener

def register_divine_hook(model: Model, logger=None):
    """
    Initializes the divine analysis by registering the listener with the model's hook.
    """
    model.set_analysis_hook(lambda model, pt: point_added_listener(model, pt, logger))

