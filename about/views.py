from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def about(request):
    """ A view to return the about me page """

    return render(request, 'about/about.html')
