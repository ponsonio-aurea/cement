"""
This module provides any dynamically loadable code for the Genshi 
Framework Extension such as hook and handler registration.  Additional 
classes and functions exist in cement2.lib.ext_genshi.
    
"""

from cement2.core import handler
from cement2.lib.ext_genshi import GenshiOutputHandler

handler.register(GenshiOutputHandler)