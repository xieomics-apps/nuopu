from basicapp.models import Platform, Post, Service, Category, Aboutus, SiteSetting
from django.core.exceptions import ValidationError

def base_obj(request):
    category_obj = Category.objects.all()
    category_dict = {}
    for category in category_obj:
        service = Category.objects.get(pk=category.pk).service_set.filter(status='published').all() 
        for s in service:
            print(s.id)
        category_dict[category] = service
    aboutus = Aboutus.objects.filter(status='published').all()
    count = aboutus.count()
    print(aboutus)
    print(count)
    if count == 0:
        return {'category_obj': category_dict} 
    elif (count == 1):
        return {'category_obj': category_dict, 'aboutus_obj': aboutus}
    else:
        raise ValidationError('The count of Aboutus queryset should be either 1 or 0. ')

def site_title(request):
    try:
        title = SiteSetting.objects.first().title
    except AttributeError:
        title = 'Agilis Genomics'
    return {'site_title': title}
        #print(service)  
        #print("Serice:") 
        #print(service)
    #print(category_obj)
    aboutus = Aboutus.objects.filter(status='published').all()
    count = aboutus.count()
    print(aboutus)
    print(count)
    if count == 0:
        return {'category_obj': category_dict} 
    elif (count == 1):
        return {'category_obj': category_dict, 'aboutus_obj': aboutus}
    else:
        raise ValidationError('The count of Aboutus queryset should be either 1 or 0. ') 
    
