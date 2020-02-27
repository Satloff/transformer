from transformer.registry import register
from transformer.transforms.base import BaseTransform
import re

class StringPatternExtractTransform(BaseTransform):

    category = 'string'
    name = 're_extract'
    label = 'Extract Pattern'
    help_text = 'Find the first match for a regular expression in a text field. Returns all matched groups with start and end position.'

    noun = 'Text'
    verb = 'find a pattern from'

    def transform(self, str_input, pattern, **kwargs):
        result = {
            '_matched': False,
        }

        if not str_input:
            return result
        
        match = re.search(re.compile(pattern), str_input)

        if not match:
            return result
            
        result.update({
            '_matched': True,
            '_start': match.start(),
            '_end': match.end(),
        })
        
        groups = match.groups()
        for idx, val in enumerate(groups):
            result[idx] = val

        if len(groups) < 1:
            result[0] = str_input[match.start():match.end()]

        
        result.update(match.groupdict())

        return result

    def fields(self, *args, **kwargs):
        return [
            {
                'type': 'unicode',
                'required': True,
                'key': 'pattern',
                'label': 'Pattern',
                'help_text': 'Enter a [Python Regular Expression](https://developers.google.com/edu/python/regular-expressions) to find the first match for, e.g. `f[o]+ (bar)`.'
            },
        ]


register(StringPatternExtractTransform())
