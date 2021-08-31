from django.shortcuts import render

# Create your views here.
# Create your views here.
def organizations(request):
    return render(request, 'organizations/organizations.html')
