# models.py
from django.db import models

class BaseModel(models.Model):

    class Meta:
        app_label = 'demo'
		
########################################################################
#ORM model of the Speaker table
class Speaker(BaseModel):

    name = models.CharField(max_length=100)
    events = models.ManyToManyField('Event',related_name="speakers")


########################################################################
#ORM model of the Event table
class Event(BaseModel):
    
	type = models.TextField()
	description = models.CharField(max_length=100)
	date = models.DateField()
	track = models.ForeignKey(Track)
	speakers = models.ManyToManyField(Speaker,through='SpeakerEvent',related_name="events")
	

########################################################################
#ORM model of the Speaker-Event table for Many-to-Many relationship
class SpeakerEvent(BaseModel):

    speaker_id = models.ForeignKeyField(Speaker)
    event_id = models.ForeignKeyField(Event)

