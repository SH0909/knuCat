from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    
    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse('catdex:show_catdex',args=[self.slug])

class Subcategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='subcategories')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    class Meta:
        ordering=['category','name']
        verbose_name='subcategory'
        verbose_name_plural='subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catdex:show_catdex',args=[self.slug])

class Cat(models.Model):
    subcategory=models.ManyToManyField(Subcategory,blank=True,related_name='cat')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    image=models.ImageField(upload_to='cat/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']
        index_together=[['id','slug']]

    def __str__(self):
        return self.name
