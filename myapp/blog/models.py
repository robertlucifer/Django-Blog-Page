from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=6 )

    def save(self, *args,**kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            print(f"DEBUG: Slug {slug} already exists. Trying next...")
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug= f"{base_slug}-{counter}"
                counter +=1

            self.slug = slug
        super().save(*args,**kwargs)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()
    class Meta:
        verbose_name_plural = "About Us"
        verbose_name = "About Us"