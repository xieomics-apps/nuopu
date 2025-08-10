from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from tinymce.models import HTMLField  
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank = True)
    content = HTMLField(blank = True) 
    image = models.ImageField(upload_to = 'pic4platform/', default = 'pic4platform/plant_logo.png')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(167.26, 87)],
                                      format='JPEG',
                                      options={'quality': 60})
    image_thumbnail_sqaure = ImageSpecField(source='image',
                                      processors=[ResizeToFill(167, 167)],
                                      format='JPEG',
                                      options={'quality': 60})
    #tags = TaggableManager()

    def __str__(self):
        return 'Platform: ' + self.name

# SiteSetting model for site-wide settings like title
class SiteSetting(models.Model):
    title = models.CharField(max_length=255, default='Agilis Genomics')
    h1 = models.CharField(max_length=255, blank=True, default='', verbose_name="主标题（H1）")
    h2 = models.CharField(max_length=255, blank=True, default='', verbose_name="副标题（H2）")
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "网站信息"
        verbose_name_plural = "网站信息"

#https://www.osehfrank.com/en/blog/2020/2/9/create-blog-application-django-part-2-create-django-models-7v0hx3k244m/
class Post(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                           unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = HTMLField(blank = True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')

    class Meta:
        ordering = ('-publish',)
        verbose_name = "新闻中心"
        verbose_name_plural = "新闻中心"

    def __str__(self):
        return self.title

class Category(models.Model):
    title =  models.CharField(max_length=250)    
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "服务类别"
        verbose_name_plural = "服务类别"


class Service(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                           unique_for_date='publish')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    body = HTMLField(blank = True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "服务项目"
        verbose_name_plural = "服务项目"

class Aboutus(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    body = HTMLField(blank = True)
    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    def save(self, *args, **kwargs):
        if not self.pk and Aboutus.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There can be only one Aboutus instance')
        return super(Aboutus, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "关于我们"
        verbose_name_plural = "关于我们"


# 联系信息模型，允许用户在后台编辑联系方式
class ContactInfo(models.Model):
    phone = models.CharField(max_length=32, blank=True, verbose_name="手机")
    wechat = models.CharField(max_length=64, blank=True, verbose_name="微信")
    email = models.EmailField(blank=True, verbose_name="邮箱")
    address = models.CharField(max_length=255, blank=True, verbose_name="地址")

    class Meta:
        verbose_name = "联系信息"
        verbose_name_plural = "联系信息"

    def __str__(self):
        return f"手机: {self.phone} / 微信: {self.wechat}"
    
# 技术中心类别
class TechCenterCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="技术中心类别")
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "技术中心类别"
        verbose_name_plural = "技术中心类别"

# 技术中心内容
class TechCenter(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name="标题")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(TechCenterCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name="类别")
    body = HTMLField(blank=True, verbose_name="内容")
    publish = models.DateTimeField(default=timezone.now, verbose_name="发布时间")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="状态")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "技术中心"
        verbose_name_plural = "技术中心"