from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


    def save(self, *args,**kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists:
                slug= f"{base_slug}-{counter}"
                counter +=1

            self.slug = slug
        super().save(*args,**kwargs)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
#Category Table
class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name