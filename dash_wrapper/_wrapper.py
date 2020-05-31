import sys
from collections.abc import MutableSequence

this_module = sys.modules[__name__]


def base_wrapper(name, module):
    if name == '__path__':
        return
    Component = getattr(module, name)

    class ModComponent(Component):

        def __init__(self, *args, **kwargs):
            self._indent = 1
            self._count = 0
            self._last = self
            self._level = -1
            self._levels = {}

            super().__init__(*args, **kwargs)

        def __mul__(self, other):
            self._add_children(parent=self._last, children=other)
            self._level += 1
            self._levels.setdefault(self._level, self._last)
            self._last = other
            self._count += 1
            # print(other, self._count)

            return self

        def __matmul__(self, other):
            parent = self._levels.get(self._level)
            self._add_children(parent=parent, children=other)
            self._last = other
            self._count += 1
            # print(other, self._count)

            return self

        def __truediv__(self, other):
            if isinstance(other, int):
                self._indent = other
                return self

            parent = self._levels.get(self._level - self._indent)
            self._add_children(parent=parent, children=other)
            self._last = other

            for level in range(self._level, self._level - self._indent, -1):
                self._levels.pop(level)

            self._level -= self._indent
            self._count += 1
            self._indent = 1
            # print(other, self._count)

            return self

        def __mod__(self, other):
            if isinstance(other, int):
                self._indent = other
                return self

            parent = self._levels.get(self._indent - 1)
            self._add_children(parent=parent, children=other)
            self._last = other

            for level in range(self._indent, self._level + 1):
                self._levels.pop(level)

            self._level = self._indent - 1
            self._count += 1
            self._indent = 1
            # print(other, self._count)

            return self

        @staticmethod
        def _add_children(parent, children):
            if parent.children is None:
                parent.children = children
            elif isinstance(parent.children, (tuple, MutableSequence)):
                if isinstance(children, (tuple, MutableSequence)):
                    parent.children = [*parent.children, *children]
                else:
                    parent.children = [*parent.children, children]
            else:
                if isinstance(children, (tuple, MutableSequence)):
                    parent.children = [parent.children, *children]
                else:
                    parent.children = [parent.children, children]

    return ModComponent
