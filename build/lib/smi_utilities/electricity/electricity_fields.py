from django.db import models

from .electricity_tariff_type import RegElectTariffType, UnregElectTariffType
from .electricity_utility_company import ElectricityUtilityCompany


class ElectricityUtilityField(models.CharField):
    description = "Field to store electric utility company values"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        kwargs.setdefault('choices', [(m.value, m.value)
                          for m in ElectricityUtilityCompany])
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
