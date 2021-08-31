from django.shortcuts import render, redirect
from .models import Project, ProjectLocation
from .forms import ProjectForm, ProjectLocationForm
from django.contrib import messages
from django.db.models import Q
from googletrans import Translator
from .filters import ProjectFilter

# Create your views here.
def index(request):
    page = "index"
    context = {
        'page': index
    }
    return render(request, 'pplaces/index.html', context)

def projects(request):
    projects = Project.objects.all().order_by('-created')
    myFilter = ProjectFilter(request.GET, queryset=projects)
    projects = myFilter.qs

#    locations = ProjectLocation.objects.all()  projects.projectLocation_set.all()
    records = projects.count()
    context = {
        'projects': projects,
        'records': records,
        'myFilter': myFilter,
#        'locations': locations,
     }
    return render(request, 'pplaces/projects.html', context)

def project_fr(request, pk):
    project = Project.objects.get(id = pk)
    context = { 
        'project': project,
         }
    return render(request, 'pplaces/single-project-fr.html', context)

def project(request, pk):
    project = Project.objects.get(pk = pk)
    context = { 
        'project': project,
         }
    return render(request, 'pplaces/single-project.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
# ---------  Translate section ---------------
            translator = Translator()
            Title_fr = translator.translate(project.ProjectTitleEnglish,dest='fr')
            PurposeDescripton_fr = translator.translate(project.ProjectPurposeDescriptonEnglish,dest='fr')
            LocationDescripton_fr = translator.translate(project.GeneralLocationDescriptonEnglish,dest='fr')
            project.ProjectTitleFrench = Title_fr.text
            project.ProjectPurposeDescriptonFrench = PurposeDescripton_fr.text
            project.GeneralLocationDescriptonFrench = LocationDescripton_fr.text
# ---------  End Translate section ---------------
            project.save()
            messages.success(request, 'Project was created')
            return redirect('projects')
#		   project = form.save(commit=False)
#		   project.owner = profile

    context = {'form': form, 'title': 'Create Project' }

#   profile = request.user.profile 
#   
#	   form = ProjectForm(request.POST, request.FILES)
#	   
    return render(request, "pplaces/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project has been updated')
            return redirect('projects')
    
    context = {'form': form, 'title': 'Update Project' }
    return render(request, 'pplaces/project_form.html', context)

def deleteProject(request, pk):
#	profile = request.user.profile
#	project = profile.objects_set.get(id=pk)
	project = Project.objects.get(id=pk)
	if request.method == 'POST':
		project.delete()
		return redirect('projects')
	context = {'object': project}
	return render(request, "delete_template.html", context)


def CreateProjectLocation(request, pk):
    projectObj = Project.objects.get(id=pk)
    title = 'Add Site'
    subtitle= projectObj.ProjectTitleEnglish
    form = ProjectLocationForm()

    if request.method == 'POST':
        form = ProjectLocationForm(request.POST)
        print(form)
        if form.is_valid():
            review = form.save(commit=False)
            review.Project_id = projectObj.id
            review.save()
            messages.success(request, 'Project location was added successfully!')
            return redirect('project', pk = projectObj.id)

    context = {
        'form': form, 
        'title': title, 
        'pk': pk,
        'subtitle': subtitle
        }
    return render(request, 'pplaces/plocation_form.html', context)

def removeProjectLocation(request, prj_id, pl_id):
    projectObj = Project.objects.get(id = prj_id)
    plocation = ProjectLocation.objects.get(id=pl_id)
    projectObj.ProjectLocation.remove(plocation)
    return redirect('project', pk = projectObj.id)
