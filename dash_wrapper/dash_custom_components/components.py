from ..dash_html_components import Div

class Row(Div):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, className='row', **kwargs)


class Col(Div):
    def __init__(self, *args, **kwargs):
        '''
        :param width: int or float. width of columns according to Skeleton CSS.
                       For example 2 corresponds to className='two columns', 0.5 corresponds to className='six columns'.
        :param offset: int or float. width of columns to offset according to Skeleton CSS.
                       For example 2 corresponds to className='offset-by-two',
                       0.5 corresponds to className='offset-by-six'
        '''

        width = args[0] if len(args) == 1 else kwargs.pop('width', 1.0)
        offset = args[1] if len(args) == 2 else kwargs.pop('offset', None)

        className = self._to_class_name(width, offset)
        super().__init__(*args[2:], className=className, **kwargs)

    @staticmethod
    def _to_class_name(width, offset=None):
        if isinstance(width, float):
            width = round(12 * width)

        width_map = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                      6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                      11: 'eleven', 12: 'twelve'}
        class_name = f'{width_map.get(width)} column{"" if width == 1 else "s"}'
        if offset:
            if isinstance(width, float):
                offset = round(12 * offset)
            offset = f'offset-by-{width_map.get(offset)}'
            class_name = f'{class_name} {offset}'
        return class_name


__all__ = [
    'Row',
    'Col'
]