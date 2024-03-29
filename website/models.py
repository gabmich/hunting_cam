from django.db import models


class Place(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)
    latitude        = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    class Meta:
        verbose_name        = 'Lieux'
        verbose_name_plural = 'Lieux'

    def __str__(self):
        return self.name if self.name else ''


class Animal(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name        = 'Animal'
        verbose_name_plural = 'Animaux'

    def __str__(self):
        return self.name if self.name else ''


class Behaviour(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name        = 'Comportement'

    def __str__(self):
        return self.name if self.name else ''


class Speed(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name        = 'Vitesse'

    def __str__(self):
        return self.name if self.name else ''


class Camera(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name        = 'Caméra'

    def __str__(self):
        return self.name if self.name else ''


class Video(models.Model):
    name            = models.CharField(max_length=255, null=True, blank=True)
    date            = models.DateTimeField(null=True, blank=True)
    temperature     = models.IntegerField(null=True, blank=True)
    videofile       = models.FileField(null=True, blank=True, upload_to='videos/')

    camera          = models.ForeignKey(Camera, null=True, blank=True, on_delete=models.SET_NULL)
    place           = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL, related_name='videos')

    animals         = models.ManyToManyField(Animal,
                                             through='AnimalToCrossing')

    class Meta:
        verbose_name        = 'Vidéo'

    def __str__(self):
        return f"{self.date.strftime('%d.%m.%Y')}"

    @property
    def animal_crossings(self):
        return [crossing for crossing in self.animals.all()]
    


class AnimalToCrossing(models.Model):
    animal          = models.ForeignKey(Animal, on_delete=models.CASCADE)
    video           = models.ForeignKey(Video, on_delete=models.CASCADE)
    behaviour       = models.ForeignKey(Behaviour, on_delete=models.CASCADE)

    class Meta:
        verbose_name        = "Passage d'animal"
        verbose_name_plural = "Passage d'animaux"
