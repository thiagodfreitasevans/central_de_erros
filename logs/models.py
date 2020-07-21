from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class OwnedModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    class Meta:
        abstract = True

class Log(OwnedModel):
    ENV_CHOICES = (
        ('production', 'produção'),
        ('homologation', 'homologação'),
        ('dev', 'dev'),
    )
    LEVEL_CHOICES = (
        ('warning', 'warning'),
        ('information','information'),
        ('error','error'),
        ('debug','debug'),
    )
    title = models.CharField(max_length=254)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    events = models.IntegerField()
    env = models.CharField(choices=ENV_CHOICES, max_length=254)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=254)
    origin = models.GenericIPAddressField()
    archived = models.BooleanField(default=False)


    def __str__(self):
        return self.title