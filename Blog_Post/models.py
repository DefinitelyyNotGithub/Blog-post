from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

from Account.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title[:30]


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=60)
    body = models.TextField()
    image = models.ImageField(upload_to='images/article_img')
    spread_date = models.DateTimeField(auto_now=True)
    visibility = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tags = TaggableManager()
    like = models.ManyToManyField(User, related_name="likes", blank=True)
    BookMarks = models.ManyToManyField(User, related_name="bookmarked", blank=True, verbose_name="bookmarked by ")


    @property
    def like_count(self):
        return self.like.count()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            return super().save(*args, **kwargs)

    def get_absolute_data(self):
        return reverse('post:post_details', args=[self.slug])

    def __str__(self):
        return self.title[:30]


class UserComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="reply")

    body = models.TextField(max_length=800)



    def __str__(self):
        return f'{self.post.title} --- {self.body[:25]}'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_date']
