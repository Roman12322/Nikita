from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Registr),
    path('GeneralForm', views.General),
    path('MakeCalculations', views.GetPrimeNumbers),
    path('regUser', views.SignUp),
    path('results', views.Results),
    path('showResults', views.ShowRes)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)