from django.db import models

from .water_groups import WaterGroups
from .water_utility_company import WaterUtilityCompany


class WaterUtilityField(models.CharField):
    description = "Field to store water utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in WaterUtilityCompany])
        super().__init__(*args, **kwargs)


class WaterGroupsField(models.CharField):
    description = "Field to store electric utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in WaterGroups])
        super().__init__(*args, **kwargs)
