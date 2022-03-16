from utilities.choices import ChoiceSet


class AnimalStatusChoices(ChoiceSet):
    """Valid values for Animal "status"."""

    STATUS_FREE = "free"
    STATUS_BUSY = "busy"

    CHOICES = (
        (STATUS_FREE, "free"),
        (STATUS_BUSY, "busy"),
    )

    CSS_CLASSES = {
        STATUS_FREE: 'success',
        STATUS_BUSY: 'danger',
    }

