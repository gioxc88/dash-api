import sys
import dash_cytoscape as module

from .._wrapper import base_wrapper

this_module = sys.modules[__name__]


def __getattr__(name):
    # print(name)
    return base_wrapper(name, module)


__all__ = module.__all__
