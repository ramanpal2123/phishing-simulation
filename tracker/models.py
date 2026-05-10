from django.db import models

class PhishingCampaign(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PhishingClick(models.Model):
    campaign = models.ForeignKey(PhishingCampaign, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField(null=True)
    clicked_at = models.DateTimeField(auto_now_add=True)
    submitted_data = models.BooleanField(default=False)

class PhishingSubmission(models.Model):
    campaign = models.ForeignKey(PhishingCampaign, on_delete=models.CASCADE, related_name='submissions')
    email_entered = models.EmailField(blank=True)
    ip_address = models.GenericIPAddressField(null=True)
    clicked_at = models.DateTimeField(auto_now_add=True)