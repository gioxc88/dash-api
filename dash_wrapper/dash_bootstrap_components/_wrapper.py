import sys
import dash_bootstrap_components as module

from .._wrapper import base_wrapper

this_module = sys.modules[__name__]


def __getattr__(name):
    # print(name)
    return base_wrapper(name, module)


__all__ = [name for name in dir(module) if ((not name.startswith('_')) and
                                              (name not in ['METADATA_PATH', 'os', 'sys', 'themes']))]
