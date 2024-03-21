from django.db import models
from smi_utilities.municipality import MunicipalityField


class MunicipalityExampleModel(models.Model):
    """
    Example model demonstrating the use of the MunicipalityField.
    """

    name = MunicipalityField(
        verbose_name="Name",
    )
