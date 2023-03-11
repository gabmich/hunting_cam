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
    date            = models.DateTimeField()
    temperature     = models.IntegerField(null=True, blank=True)
    videofile       = models.FileField(null=True, blank=True)

    camera          = models.ForeignKey(Camera, null=True, blank=True, on_delete=models.SET_NULL)
    place           = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)

    animals         = models.ManyToManyField(Animal,
                                             through='AnimalToCrossing')

    class Meta:
        verbose_name        = 'Vidéo'

    def __str__(self):
        return f"{self.date.strftime('%d.%m.%Y')} - {self.place.name}"


class AnimalToCrossing(models.Model):
    animal          = models.ForeignKey(Animal, on_delete=models.CASCADE)
    video           = models.ForeignKey(Video, on_delete=models.CASCADE)
    behaviour       = models.ForeignKey(Behaviour, on_delete=models.CASCADE)
    speed           = models.ForeignKey(Speed, on_delete=models.CASCADE)

    class Meta:
        verbose_name        = "Passage d'animal"
        verbose_name_plural = "Passage d'animaux"
