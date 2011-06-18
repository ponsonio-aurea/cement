"""Cement core backend module."""

import sys
import logging

def defaults(app_name=None):
    """
    Get a standard, default config.
    
    Required Arguments:
    
        app_name
            The name of the application.
            
    """
    # default backend configuration
    dcf = {}
    dcf['base'] = {}
    dcf['base']['app_name'] = app_name
    dcf['base']['config_files'] = []
    dcf['base']['config_source'] = ['default']
    dcf['base']['debug'] = False
    dcf['base']['extensions'] = ['configparser', 'logging', 'argparse']
    dcf['base']['plugins'] = []
    dcf['base']['plugin_config_dir'] = None
    dcf['base']['plugin_dir'] = None
    
    # default handlers
    dcf['base']['config_handler'] = 'configparser'
    dcf['base']['log_handler'] = 'logging'
    dcf['base']['arg_handler'] = 'argparse'
    dcf['base']['plugin_handler'] = 'cement'
    dcf['base']['extension_handler'] = 'cement'
    dcf['base']['output_handler'] = 'cement'
    

    # default application configuration
    dcf['log'] = {}
    dcf['log']['file'] = None
    dcf['log']['level'] = 'INFO'
    dcf['log']['to_console'] = True
    dcf['log']['rotate'] = False
    dcf['log']['max_bytes'] = 512000
    dcf['log']['max_files'] = 4
    dcf['log']['file_formatter'] = None
    dcf['log']['console_formatter'] = None
    dcf['log']['clear_loggers'] = True
    return dcf

def minimal_logger(name, debug=False):
    """
    Setup just enough for cement to be able to do debug logging.
    """
                
    log = logging.getLogger(name)
    formatter = logging.Formatter(
                "%(asctime)s (%(levelname)s) %(name)s : %(message)s")
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)   
    log.setLevel(logging.INFO)
        
    # FIX ME: really don't want to hard check sys.argv like this but can't
    # figure any better way get logging started (only for debug) before the
    # app logging is setup.
    if '--debug' in sys.argv or debug:
        console.setLevel(logging.DEBUG)   
        log.setLevel(logging.DEBUG)
        
    log.addHandler(console)
    return log
    
# global handlers dict
handlers = {}

# global hooks dict
hooks = {}

# Save original stdout/stderr for supressing output.
# FIX ME: Removing this for now, need a sane way to do it... or not at all
#
STDOUT = sys.stdout
STDERR = sys.stderr

#
#class StdOutBuffer(object):
#    buffer = ''
#    def write(self, text):
#        self.buffer += text
#        
#class StdErrBuffer(object):
#    buffer = ''
#    def write(self, text):
#        self.buffer += text
#
#buf_stdout = StdOutBuffer()
#buf_stderr = StdErrBuffer()