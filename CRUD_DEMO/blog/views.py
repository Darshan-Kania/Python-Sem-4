from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from .models import BlogModel
from .forms import BlogForms


def create_view(request):
    context = {}
    form = BlogForms(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context['dataset'] = BlogModel.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}
    try:
        context['data'] = BlogModel.objects.get(id=id)
    except:
        context['data'] = None
    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(BlogModel, id=id)
    form = BlogForms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/blog/"+id)
    context['form'] = form
    return render(request, "update_view.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(BlogModel, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request, "delete_view.html", context)
