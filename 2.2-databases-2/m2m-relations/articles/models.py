from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/')
    published_at = models.DateTimeField()

    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_main', 'tag__name']

    def __str__(self):
        return f"{self.tag.name} ({'Main' if self.is_main else 'Secondary'})"