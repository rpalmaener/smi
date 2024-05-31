from django.db.models import TextChoices


class WaterGroups(TextChoices):
    """
    Enumeration for regulated electricity tariff types.
    """
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    AT2 = "AT2"
    AT3 = "AT3"
    AT41 = "AT4.1"
    AT42 = "AT4.2"
    AT43 = "AT4.3"
    AT5 = "AT5"
    CBRE_Golf = "CBRE-Golf"
