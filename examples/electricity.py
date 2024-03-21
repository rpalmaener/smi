from django.db import models

from smi_utilities.electricity import (
    ElectricUtilityField,
    RegElectTariffTypeField,
    UnregElectTariffTypeField,
)


class ElectricUtilityExampleModel(models.Model):
    """
    Example model demonstrating the use of the ElectricUtilityField.
    """

    name = ElectricUtilityField(
        verbose_name="Name",
    )


class RegElectTariffTypeExampleModel(models.Model):
    """
    Example model demonstrating the use of the RegElectTariffTypeField.
    """

    name = RegElectTariffTypeField(
        verbose_name="Name",
    )


class UnregElectTariffTypeFieldExampleModel(models.Model):
    """
    Example model demonstrating the use of the UnregElectTariffTypeField.
    """
    name = UnregElectTariffTypeField(
        verbose_name="Name",
    )
