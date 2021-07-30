"""fastapi-chameleon - Adds integration of the Chameleon template language to FastAPI."""

__version__ = '0.1.10'
__author__ = 'Michael Kennedy <michael@talkpython.fm>'
__all__ = ['template', 'global_init', 'not_found', ]

from .engine import global_init
from .engine import template
from .engine import response
from .engine import not_found
