from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(verbose_name='decription')
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField()
    tags = models.ManyToManyField(Tag)


class Review(models.Model):
    review_book = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="review_book", null=True
    )
    stars = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.created_at}"

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"