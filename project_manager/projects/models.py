from django.core.urlresolvers import reverse

from core.models import SlugModel


class Project(SlugModel):
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('projects:edit', kwargs={'slug': self.slug})
