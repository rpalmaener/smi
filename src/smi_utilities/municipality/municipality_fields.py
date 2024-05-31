from django.db import models

from .municipality import Municipality


class MunicipalityField(models.CharField):
    description = "Field to store municipality values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in Municipality])
        super().__init__(*args, **kwargs)
