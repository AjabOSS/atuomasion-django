from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import User
from .validators import validate_file_extension
from django.utils import timezone
from django.contrib.auth import get_user_model


class EventManager(models.Manager):
    def get_queryset(self):
        if (Letter.delete_status):
            return super().get_queryset().filter(
                publishing_date__gte=timezone.now()-timezone.timedelta(days=12) #TODO: should set a time for delete letters
            )

class Letter(models.Model):
    STATUS_OF_LETTER = (
        ("checking", "Checking"),
        ("rejected", "Rejected"),
        ("accepted", "Accepted"),
    )

    title           = models.CharField(_("موضوع  "), max_length=50)
    description     = models.TextField(_("توضیحات  "), max_length=255)
    author          = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.PROTECT,
                        related_name = 'Letter',
                        )

    publishing_date = models.DateTimeField(
                        default = timezone.now,
                        blank = True,
                        )

    file            = models.FileField(_(" پیوست : "), upload_to="docs/", default="", validators=[validate_file_extension])
    objects         = EventManager()
    delete_status   = models.BooleanField(_(" بعد از یک سال پاک شود ؟ "), default=True)  #TODO : default true or false
