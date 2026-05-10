from django.contrib import admin
from .models import PhishingCampaign, PhishingClick, PhishingSubmission

admin.site.register(PhishingCampaign)
admin.site.register(PhishingClick)
admin.site.register(PhishingSubmission)