from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PhishingCampaign, PhishingClick, PhishingSubmission

def fake_login(request, campaign_id):
    try:
        campaign = PhishingCampaign.objects.get(id=campaign_id)
        ip = request.META.get('REMOTE_ADDR')
        PhishingClick.objects.create(campaign=campaign, ip_address=ip)
    except:
        pass

    if request.method == 'POST':
        email = request.POST.get('email', '')
        ip = request.META.get('REMOTE_ADDR')
        PhishingSubmission.objects.create(
            campaign=campaign,
            email_entered=email,
            ip_address=ip
        )
        return redirect('warning')

    return render(request, 'tracker/fake_login.html', {'campaign_id': campaign_id})

def warning(request):
    return render(request, 'tracker/warning.html')

def dashboard(request):
    campaigns = PhishingCampaign.objects.all()
    data = []
    for c in campaigns:
        data.append({
            'name': c.name,
            'clicks': c.clicks.count(),
            'submissions': c.submissions.count(),
            'created_at': c.created_at
        })
    return render(request, 'tracker/dashboard.html', {'data': data})