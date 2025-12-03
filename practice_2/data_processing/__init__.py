# data_processing/__init__.py
from .core import process_data
from . import preprocessing, postprocessing

__all__ = ["process_data", "preprocessing", "postprocessing"]


