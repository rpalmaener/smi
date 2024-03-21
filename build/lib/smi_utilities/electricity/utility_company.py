from django.db.models import TextChoices


class UtilityCompany(TextChoices):
    """
    Enumeration for electric utility distribution companies.
    """

    CGE = "CGE"
    ENEL = "Enel"
