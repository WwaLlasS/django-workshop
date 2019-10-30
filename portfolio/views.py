from django.shortcuts import render, redirect
from portfolio.models import Project
from portfolio.forms import ProjectForm


# Create your views here.
def home(request):
    template = 'home.html'
    context = {}
    method = request.method
    if method == 'GET':
        projects = Project.objects.all()
        project_form = ProjectForm()
        context['project_form'] = project_form
        context['projects'] = projects
        return render(request, template, context)
    if method == 'POST':
        post = request.POST
        files = request.FILES
        project_form = ProjectForm(post, files)
        if project_form.is_valid():
            project_form.save()
            return redirect('home')
        else:
            projects = Project.objects.all()
            context['project_form'] = project_form
            context['projects'] = projects
            return render(request, template, context)
