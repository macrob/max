from typing import Callable
from pywebio.session import run_js
from pywebio import start_server as start_server_pw

def reload_page(timeout_ms: int):
    timeout = str(timeout_ms)
    reload_js = 'setTimeout(function() { location.reload(); }, ' + timeout +');'
    run_js(reload_js)
    
def start_server(handler: Callable, port: int, current_file: str):
    if current_file == '__main__':
        start_server_pw(handler, port=port)