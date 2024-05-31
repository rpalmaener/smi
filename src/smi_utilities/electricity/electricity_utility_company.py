from django.db.models import TextChoices


class ElectricityUtilityCompany(TextChoices):
    """
    Enumeration for electric utility distribution companies.
    """

    CGE = "CGE"
    ENEL = "Enel"
    CHILQUINTA = "Chilquinta"
