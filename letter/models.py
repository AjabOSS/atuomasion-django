from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# from django.contrib.auth.models import User
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

    target          = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.PROTECT,
                        default = None
                        )

    publishing_date = models.DateTimeField(
                        default = timezone.now,
                        
                        )

    file            = models.FileField(_(" پیوست : "), upload_to="docs/", default="", blank = "True", validators=[validate_file_extension])   # TODO: blank
    objects         = EventManager()
    delete_status   = models.BooleanField(_(" بعد از یک سال پاک شود ؟ "), default=True)  #TODO : default true or false
    
    allow_for_l_1   = models.BooleanField(default=False)
    allow_for_l_2   = models.BooleanField(default=False)
    allow_for_l_3   = models.BooleanField(default=False)
    read            = models.BooleanField(default=False)
    replay          = models.ManyToManyField("Letter", related_name="letters", blank=True, null=True)
    
    reject          = models.BooleanField(default=False)
    accepted        = models.BooleanField(default=False)
    
    reject_description = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        ordering = ['-publishing_date']

    # class Allow(models.Model):
    #     perm        = models.CharField(_("دسترسی  "), max_length=50)