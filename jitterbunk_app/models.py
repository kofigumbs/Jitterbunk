from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=15)
    photo = models.URLField()

    def __unicode__(self):
        return self.name


class Bunk(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='from_user')
    to_user = models.ForeignKey(UserProfile, related_name='to_user')
    time = models.DateTimeField('time occurred')  # from 'date published'

    def __unicode__(self):
        return str(self.time)
