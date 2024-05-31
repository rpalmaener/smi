from django.db import models

from .locality import Locality


class LocalityField(models.CharField):
    description = "Field to store locality values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in Locality])
        super().__init__(*args, **kwargs)
