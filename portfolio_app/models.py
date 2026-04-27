from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    full_name = models.CharField(_('Full Name'), max_length=120)
    rating = models.PositiveSmallIntegerField(_('Rating'), choices=RATING_CHOICES, default=5)
    text = models.TextField(_('Review text'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(_('Approved'), default=True)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.rating}★"

    @property
    def stars_range(self):
        return range(self.rating)

    @property
    def empty_stars_range(self):
        return range(5 - self.rating)


class Project(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    description = models.TextField(_('Description'))
    tech_stack = models.CharField(_('Tech Stack'), max_length=300, blank=True,
                                  help_text='e.g. Django, PostgreSQL, Docker')
    link = models.URLField(_('Project Link'), blank=True)
    github = models.URLField(_('GitHub Link'), blank=True)
    image1 = models.ImageField(_('Image 1'), upload_to='projects/', blank=True, null=True)
    image2 = models.ImageField(_('Image 2'), upload_to='projects/', blank=True, null=True)
    image3 = models.ImageField(_('Image 3'), upload_to='projects/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)
    is_active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def images(self):
        return [img for img in [self.image1, self.image2, self.image3] if img]
