from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import PersonalInfo, Skill, Experience, Contact, SocialMedia

def home(request):
    try:
        social_media = SocialMedia.objects.all()
    except:
        social_media = []
    
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'social_media': social_media,
        'skills': Skill.objects.all().order_by('order'),  # Sıralamaya göre getir
        'experiences': Experience.objects.all().order_by('-start_date'),
    }
    return render(request, 'main/home.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            contact = Contact.objects.create(
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to send message. Please try again.'
            })
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})