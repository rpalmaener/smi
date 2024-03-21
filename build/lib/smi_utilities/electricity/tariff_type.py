from django.db.models import TextChoices


class RegElectTariffType(TextChoices):
    """
    Enumeration for regulated electricity tariff types.
    """
    BT1 = "BT1"
    BT2 = "BT2"
    BT3 = "BT3"
    BT41 = "BT4.1"
    BT42 = "BT4.2"
    BT43 = "BT4.3"
    BT5 = "BT5"
    AT2 = "AT2"
    AT3 = "AT3"
    AT41 = "AT4.1"
    AT42 = "AT4.2"
    AT43 = "AT4.3"
    AT5 = "AT5"
    CBRE_Golf = "CBRE-Golf"


class UnregElectTariffType(TextChoices):
    """
    Enumeration for unregulated electricity tariff types.
    """
    BT = "BT"
    AT = "AT"
