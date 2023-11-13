from django.shortcuts import render


def main_view(request):
    context = {}
    template_name = 'generator/index.html'
    return render(request, template_name, context)