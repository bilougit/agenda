# -*-coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Evenement(models.Model):
  """
  This class has all data information.
   - a name to find it easily
   - a description to save all other information
   - participants who are users
   - date of event
   - place of the event

  # création d'un événement.
  >>> from datetime import datetime, timedelta
  >>> from personal_calendar.models import *
  >>> event = Evenement(nom="rendez-vous chez le dentiste", description="pas très agréable :(", date=datetime.now()+timedelta(days=5), lieu="chez le dentiste")
  >>> event.save()
  >>> rendezvous = Evenement.objects.get(lieu="chez le dentiste")
  >>> rendezvous
  <Evenement: rendez-vous chez le dentiste>
  >>> rendezvous.nom
  u'rendez-vous chez le dentiste'
  """
  nom = models.CharField(max_length=250, unique=True)
  description = models.TextField()
  participants = models.ManyToManyField(
      User,
      through="Evenement_Participant",
      null=True, blank=True
    )
  date = models.DateTimeField()
  lieu = models.TextField()

  def __unicode__(self):
    return self.nom

  def delete_url(self):
    return reverse("delete", kwargs={'pk': self.pk})

  def get_absolute_url(self):
    return reverse("details", kwargs={'pk': self.pk})


class Evenement_Participant(models.Model):
  """
  This class made to manage many_to_many relation
   - evenement is the event
   - participant is the user
   - status

  >>> from datetime import datetime, timedelta
  >>> from django.contrib.auth.models import User
  >>> from personal_calendar.models import *
  >>> user = User(username='new', email='new@new.fr', password='pass')
  >>> user.save()
  >>> event = Evenement(nom="rendez-vous", description="très agréable :)", date=datetime.now()+timedelta(days=5), lieu="chez le dentiste")
  >>> event.save()
  >>> event_par = Evenement_Participant(evenement=event, participant=user, status=1)
  >>> event_par.save()
  >>> event_par
  <Evenement_Participant: Evenement_Participant object>
  >>> status = event_par.status
  >>> new_p = event_par.participant
  >>> new_p
  <User: new>
  >>> status
  1
  """
  evenement = models.ForeignKey(Evenement)
  participant = models.ForeignKey(User)
  status_choices = (
      (0, "hôte"),
      (1, "invité"),
      (2, "désisté"),
      (3, "confirmé"),
      )
  status = models.IntegerField(choices=status_choices)
  class Meta:
    unique_together = ('evenement', 'participant')

  def delete_url(self):
    return "/agenda/{0}/participant/{1}/delete/".format(self.evenement.id,
                                                        self.participant.id)
