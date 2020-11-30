from django.views.generic import TemplateView
from django.shortcuts import render

class Testpage(TemplateView):
    template_name = 'test.html'


class Thankspage(TemplateView):
    template_name = 'thanks.html'


class Homepage(TemplateView):
    template_name = 'index.html'


def AboutUs(request):
    return render(request,'aboutus.html')


def Contact(request):
    return render(request,'contact.html')