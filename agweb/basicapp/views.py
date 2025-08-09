# 新的联系信息页面视图
from django.views.generic import TemplateView

from django.shortcuts import render
from django.views.generic import (TemplateView)
from django.views.generic.list import ListView

from basicapp.models import Platform, Post, Service, Category, Aboutus
from .forms import ContactusForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic import DetailView 
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context  = super(IndexView, self).get_context_data(**kwargs)
        context['nav_status_home'] = "active"
        from basicapp.models import SiteSetting
        try:
            context['sitesetting'] = SiteSetting.objects.first()
        except SiteSetting.DoesNotExist:
            context['sitesetting'] = None
        return context

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-published']

class ServiceListView(ListView):
    template_name = 'service_list.html'
    model = Service
    context_object_name = 'services'
    #ordering = ['-published']

class ServiceDetailView(DetailView):
    template_name = 'service_detail.html'
    model = Service
    context_object_name = 'services'
    #ordering = ['-published']
    def get_context_data(self,**kwargs):
        context  = super(ServiceDetailView, self).get_context_data(**kwargs)
        #category_obj = Category.objects.all()
        context['nav_status_service'] = "active"
        #context['category_obj'] = category_obj
        category_obj = Category.objects.all()
        category_dict = {}
        for category in category_obj:
            service = Category.objects.get(pk=category.pk).service_set.filter(status='published').all()
            #for s in service:
            #    print(s.id)
            category_dict[category] = service
        context['category'] = category_dict
        return context

class BlogView(TemplateView):
    template_name = 'blog_comesoon.html'
    def get_context_data(self,**kwargs):
        context  = super(BlogView, self).get_context_data(**kwargs)
        context['injectme'] = "Basic Injection12!"
        return context

#class AboutusView(TemplateView):
#    template_name = 'aboutus.html'
#    def get_context_data(self,**kwargs):
#        context  = super(AboutusView, self).get_context_data(**kwargs)
#        context['nav_status_aboutus'] = "active"
#        return context

class AboutusDetailView(DetailView):
    template_name = 'aboutus_detail.html'
    model = Aboutus
    #context_object_name = 'aboutus'
    #ordering = ['-published']
    def get_context_data(self,**kwargs):
        context  = super(AboutusDetailView, self).get_context_data(**kwargs)
        #category_obj = Category.objects.all()
        context['nav_status_aboutus'] = "active"
        #context['category_obj'] = category_obj
        return context

class PlatformListView(ListView):
    model = Platform
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_status_platform'] = "active"
        return context


def contactus_form(request):
    form = ContactusForm()
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data["email"]
            subject = f'Message from {form.cleaned_data["subject"]}'
            message = form.cleaned_data["message"]
            recipients = ['agilisgenomics@gmail.com', settings.SERVER_EMAIL]
        
            print(sender)
            print(subject)
            print(message)
            try:
                send_mail(subject, "From " + sender + ":\n"+message,  sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            message = "Success...Your email has been sent"
            messages.success(request, message)
            #return HttpResponse('Success...Your email has been sent')
            return HttpResponseRedirect(request.path_info)
            #return render(request, 'basicapp/contactus.html', {'form': form, 
            #                                           'nav_status_contactus': 'active',
            #                                           'message': message})
    return render(request, 'basicapp/contactus.html', {'form': form, 'nav_status_contactus': 'active'})

class ContactInfoView(TemplateView):
    template_name = 'basicapp/contact_info.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = {
            '手机': '138-0000-0000',
            '微信': 'your_wechat_id',
            '邮箱': 'your@email.com',
            '地址': '中国某地',
            # 可根据需要添加更多信息
        }
        return context