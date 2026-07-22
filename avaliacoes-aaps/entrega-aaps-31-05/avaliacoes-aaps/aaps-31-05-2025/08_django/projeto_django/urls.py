from django.contrib import admin
from django.urls import path
from meu_app.views import ola_django  # Importando a função que você acabou de criar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ola/', ola_django),  # Quando o navegador acessar /ola, ele roda a sua função
]