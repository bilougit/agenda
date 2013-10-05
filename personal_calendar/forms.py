from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User

from personal_calendar.models import Evenement, Evenement_Participant

class EventForm(ModelForm):
  class Meta:
    model = Evenement
    exclude = ('participants',)

class Evenement_ParticipantForm(ModelForm):
  class Meta:
    model = Evenement_Participant

  def __init__(self, *args, **kwargs):
    super(Evenement_ParticipantForm, self).__init__(*args, **kwargs)
    self.fields['evenement'].widget = HiddenInput()
    if 'evenement' in self.initial:
      participants = [user.pk for user in \
                      self.initial['evenement'].participants.all()]
      self.fields['participant'].queryset = User.objects.exclude(
          pk__in=participants)
