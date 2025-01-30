from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="News name")
    content = models.TextField(blank=True, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of update")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Picture", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Published")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Cat.")

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NEWS"
        verbose_name_plural = "NOVYNA"
        ordering = ["-created_at", "title"]# порядок сортировки, влияет на views, соответственно можно указать .all() во views

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="News Category")

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Category"
        ordering = ["title"]



