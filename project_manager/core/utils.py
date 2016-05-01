# -*- coding: utf-8 -*-

from enum import Enum


class ExtendedEnum(Enum):
    # @classmethod
    # def name_to_value(cls, name):
    #     return getattr(cls, name).value

    @classmethod
    def choices(cls):
        return [(c.value[0], c.value[1]) for c in list(cls)]
