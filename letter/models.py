from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import User
from .validators import validate_file_extension

class Letter(models.Model):
    title           = models.CharField(_("موضوع : "), max_length=50)
    description     = models.TextField(_("توضیحات : "), max_length=255)
    author          = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.PROTECT,
                        # related_name = 'blog_posts',
                        )
    file            = models.FileField(_(" پیوست : "), upload_to="docs/", default="", validators=[validate_file_extension])