#!/usr/bin/env python3
from typing import Sequence, Any, Union, NewType

def safe_first_element(lst: Sequence[Any]) -> Union[Any[Any], type(None)]:
    if lst:
        return lst[0]
    else:
        return None