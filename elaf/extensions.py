
from modules.base.model_inheritance import ModelExtension
from django.db import models
from modules.base.fields import AttachmentForeignKeyField


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
    quotation_document = AttachmentForeignKeyField(
        upload_to='crm/leads',
        allowed_types=['document','pdf'],
        blank=True,
        null=True
    )  





class PartnerExtension(ModelExtension):
    _inherit = 'base.partner'
    responsible_user = models.ForeignKey('base.user', on_delete=models.SET_NULL, null=True, blank=True, related_name='partners_responsible_user')