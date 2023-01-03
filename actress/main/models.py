from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")
    
    def __str__(self):
        return str(self.name)
    
    # def get_absolute_url(self):
    #     return reverse('urls.category', kwargs={'cat_id': self.pk})
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        ordering = ['id']
        

class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Famous women"
        verbose_name_plural = "Famous women"
        ordering = ['-time_update', 'title']
        
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse("main:post", kwargs={'post_slug':self.slug})
    
    # def get_absolute_url(self):
    #     return reverse('urls.post',kwargs={'post_id':self.pk})
    