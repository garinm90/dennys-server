from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.utils.text import slugify
# Create your models here.


class Job(models.Model):
    job_number = models.IntegerField(
        verbose_name='Job Number', validators=[MinValueValidator(0)])
    customer = models.ForeignKey(
        'customers.Customer', related_name='jobs', on_delete=models.CASCADE)
    ride = models.ForeignKey(
        'rides.Ride', related_name='jobs', on_delete=models.CASCADE)
    job_created = models.DateTimeField(auto_now_add=True)
    job_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('job_created', )

    def __str__(self):
        return str(self.job_number)

    def get_absolute_url(self):
        return reverse('jobs:detail_job', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_number)
        super(Job, self).save(*args, **kwargs)
