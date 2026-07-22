from django.http import HttpResponse

def ola_django(request):
    return HttpResponse("<h1>Olá, Django!</h1><p>Meu primeiro projeto estruturado está rodando.</p>")