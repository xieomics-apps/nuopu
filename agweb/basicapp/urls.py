
from . import views
from django.urls import path, re_path
from basicapp.views import PlatformListView, ServiceListView, ServiceDetailView, ContactInfoView, TechCenterListView, TechCenterDetailView

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('blog/', views.BlogView.as_view(), name="blog-comesoon"),
    path('aboutus/<int:pk>', views.AboutusDetailView.as_view(), name="about-us"),
    path('platform/', PlatformListView.as_view(), name='platform-list'),
    path('contactus/', views.contactus_form, name='contact-us'),
    path('contactus2/', ContactInfoView.as_view(), name='contact-us2'),

    # 技术中心
    path('techcenter/', TechCenterListView.as_view(), name='techcenter-list'),
    path('techcenter/category/<int:category_id>/', TechCenterListView.as_view(), name='techcenter-list'),
    path('techcenter/<int:pk>/', TechCenterDetailView.as_view(), name='techcenter-detail'),
]
