from . import views
from django.urls import path, re_path
#from . import views 
from basicapp.views import PlatformListView, ServiceListView, ServiceDetailView, ContactInfoView

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('blog/', views.BlogView.as_view(), name="blog-comesoon"),
    path('aboutus/<int:pk>', views.AboutusDetailView.as_view(), name="about-us"),
    path('platform/', PlatformListView.as_view(), name='platform-list'),
    path('contactus/', views.contactus_form, name='contact-us'),
    path('contactus2/', ContactInfoView.as_view(), name='contact-us2'),
]
