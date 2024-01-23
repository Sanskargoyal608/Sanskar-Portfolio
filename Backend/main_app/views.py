from django.shortcuts import render,get_object_or_404

# Create your views here.
# portfolio/views.py
from django.shortcuts import render,redirect
from .models import Upload_Form
from .forms import UploadFormDoc, ContactUs

# from .models import Project
from django.views.decorators.http import require_http_methods


# @require_http_methods(["GET"])
def portfolio_view(request):
    return render(request, 'portfolio/desktop-1.html')


# @require_http_methods(["GET"])
def admin_upload_view(request):
    if request.method == 'POST':
        form = UploadFormDoc(request.POST, request.FILES)

        print(form.is_valid(), form.errors)
        if form.is_valid():
            form.save()
        return redirect('UploadNow') 
    else:
        form = UploadFormDoc()

    return render(request, 'portfolio/uploading-project-skills.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactUs(request.POST, request.FILES)

        print(form.is_valid(), form.errors)
        if form.is_valid():
            form.save()
        return redirect('ContactUs') 
    else:
        form = ContactUs()
    


    return render(request, 'portfolio/contact-us.html', {'form': form})

def skills_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='Skills')

    return render(request, 'portfolio/skills.html', {'upload_data': upload_data})

def certificates_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='Certificate')

    return render(request, 'portfolio/certificates.html', {'upload_data': upload_data})

def project_view(request,blog_id):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = get_object_or_404(Upload_Form, pk = blog_id)

    return render(request, 'portfolio/project-page.html', {'upload_data': upload_data})


def uiux_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='UI/UX Project')

    return render(request, 'portfolio/ui-ux-designs.html', {'upload_data': upload_data})

def unity_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='UnityProject')

    return render(request, 'portfolio/unityprojects.html', {'upload_data': upload_data})


def app_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='AppProject')

    return render(request, 'portfolio/app-webev.html', {'upload_data': upload_data})

def projects_view(request):

    # Fetch data from the Upload_Form model where topic is 'Skills'
    upload_data = Upload_Form.objects.filter(topic='Project')

    return render(request, 'portfolio/projects.html', {'upload_data': upload_data})
