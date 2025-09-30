
from modules.base.model_inheritance import ModelExtension
from django.db import models

class LeadExtension(ModelExtension):
    _inherit = 'crm.lead'

    CATEGORY_CHOICES = [
        ('سكني', 'سكني'),
        ('تجاري', 'تجاري'),
        ('تعليمي', 'تعليمي'),
        ('صحي', 'صحي'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    number_of_floors = models.IntegerField(blank=True, null=True,default=1)