from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")

    first_name = models.CharField(max_length=32, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=32, verbose_name=_("Фамилия"))

    def __str__(self) -> str:
        return f"{self.id}"
