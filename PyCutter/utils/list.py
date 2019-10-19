""" 列表工具类
Author: Yin
Date: 2019/10/19
License: MIT
"""

from typing import Any


class KeyCompareList(object):
    """Key Compare List

    根据指定的键值而声明的列表，该列表只支持同一类型的数据，且声明的时候必须指定比较的键。
    大部分操作与List数据类似，且可以依据键值直接使用xx in List或者 List[xx] 的方式进行访问。
    """

    def __init__(self, dtype: Any, attr: str):
        self.dtype = dtype
        self.attr = attr

        self.data = []

    def __getitem__(self, item_attr: Any):

        for item in self.data:
            if getattr(item, self.attr) == item_attr:
                return item

        raise KeyError

    def __len__(self):
        return len(self.data)

    def __contains__(self, item_attr: Any):
        for item in self.data:
            if getattr(item, self.attr) == item_attr:
                return True

        return False

    def append(self, item):
        if not isinstance(item, self.dtype):
            raise TypeError(f"object type is {type(item)}, and it isn't equal"
                            f"to dtype {self.dtype}")

        self.data.append(item)

    def remove(self, item):
        if not isinstance(item, self.dtype):
            raise TypeError(f"object type is {type(item)}, and it isn't equal"
                            f"to dtype {self.dtype}")

        pass
