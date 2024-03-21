from django.db import models

from .tariff_type import RegElectTariffType, UnregElectTariffType
from .utility_company import UtilityCompany


class ElectricUtilityField(models.CharField):
    description = "Field to store electric utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in UtilityCompany])
        super().__init__(*args, **kwargs)


class RegElectTariffTypeField(models.CharField):
    description = "Field to store electric utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in RegElectTariffType])
        super().__init__(*args, **kwargs)


class UnregElectTariffTypeField(models.CharField):
    description = "Field to store electric utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in UnregElectTariffType])
        super().__init__(*args, **kwargs)
