from transformer.registry import register
from transformer.transforms.base import BaseTransform
from transformer.util import try_parse_number, expand_special_chargroups

import random


class UtilConvert_s_liTransform(BaseTransform):

    category = 'util'
    name = 'convert_s_li'
    label = 'Convert string to line-item'
    help_text = 'Convert a comma delimited string to a line-item. `a,b,c,d` becomes [a,b,c,d]'

    noun = 'String'
    verb = 'Convert'

    def transform(self, str_input, **kwargs):
        
        if not str_input:
            return u''
        
        segments = str_input.split(',')
        return segments

register(UtilConvert_s_liTransform())
