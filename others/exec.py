#! /usr/bin/env python3
"""exec can be used to execute Python code during runtime
variables can be handed over as a dict
"""
exec("print('Hello ' + s)", {'s': 'World'})
