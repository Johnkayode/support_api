from django.db import models
from django.utils.translation import gettext_lazy as _

from decimal import Decimal



class Item(models.Model):
    name = models.CharField(
        _("name"),
        max_length=150,
        null=False,
        blank=False
    )
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        decimal_places=2, 
        max_digits=12, 
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)