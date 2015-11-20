# models.py
from peewee import *

import datetime


db = SqliteDatabase("pewee_pycon.sqlite",  threadlocals=True)

class BaseModel(Model):
	"""A base model that will use our Sqlite database."""
	class Meta:
		database = db
		
########################################################################
#ORM model of the Speaker table
class Speaker(BaseModel):

    name = CharField()
 
########################################################################
#ORM model of the Track table
class Track(BaseModel):

	name = CharField()
 

########################################################################
#ORM model of the Event table
class Event(BaseModel):
    
	type = CharField()
	description = CharField()
	date = DateTimeField(default=datetime.datetime.now)
	track = ForeignKeyField(Track,related_name='events')

		
class SpeakerEvent(Model):

    speaker_id = ForeignKeyField(Speaker, related_name='speakers')
    event_id = ForeignKeyField(Event, related_name='events')

    # Specify a unique multi-column index on speaker/event.
    class Meta:
        database = db
        #indexes = (['speaker_id', 'event_id'], True)
        primary_key = CompositeKey('speaker_id', 'event_id')
	
def create_schema():

    db.connect()

    #db.create_tables([Speaker, Track, Event, SpeakerEvent],safe=True)
    
    try:
        Speaker.create_table()
    except OperationalError:
        print "Speaker table already exists!"
 
    try:
        Track.create_table()
    except OperationalError:
        print "Track table already exists!"
		
    try:
        Event.create_table()
    except OperationalError:
        print "Event table already exists!"
		
    try:
        SpeakerEvent.create_table()
    except OperationalError:
        print "SpeakerEvent table already exists!"
        

def insert_speakers_tracks_events():
    
	tracks = ["Track PSF (basico)", "Track Avanzado", "Track BigML (cientifico)", "WorkShop"]
        for track in tracks:
            new_track = Track.create(name=track)
            new_track.save()

        track1 = Track.get(Track.id == 1)
        track2 = Track.get(Track.id == 2)
        track3 = Track.get(Track.id == 3)
        track4 = Track.get(Track.id == 4)
	track4.name = "WorkShop/Taller" #update
	track4.save()
	
	speaker1 = Speaker(name="Francesc Alted")
	speaker1.save()
	speaker2 = Speaker(name="Joaquin del Cerro")
	speaker2.save()
	speaker3 = Speaker(name="Miguel Sanchez Rodriguez")
	speaker3.save()
	speaker4 = Speaker(name="Alejandro Vidal")
	speaker4.save()
	speaker5 = Speaker(name="Carlos Dorado")
	speaker5.save()
	speaker6 = Speaker(name="Siro Moreno")
	speaker6.save()
	speaker7 = Speaker(name="Anton Caceres")
	speaker7.save()
	speaker8 = Speaker(name="Daniel Garcia (cr0hn)")
	speaker8.save()
	speaker9 = Speaker(name="Miguel Araujo Perez")
	speaker9.save()
	speaker10 = Speaker(name="Christine Doig")
	speaker10.save()
	speaker11 = Speaker(name="Roberto Majadas Lopez")
	speaker11.save()
	speaker12 = Speaker(name="Jose Ignacio Galarza")
	speaker12.save()
	speaker13 = Speaker(name="Javier Vegas Regidor")
	speaker13.save()
	speaker14 = Speaker(name="Salvador de la Puente Gonzalez")
	speaker14.save()
	speaker15 = Speaker(name="Alberto Labarga")
	speaker15.save()
	speaker16 = Speaker(name="Raul Cumplido")
	speaker16.save()
	speaker17 = Speaker(name="Jesus Cea")
	speaker17.save()
	speaker18 = Speaker(name="Alejandro Vidal")
	speaker18.save()
	speaker19 = Speaker(name="Guillermo Vaya Perez")
	speaker19.save()
	speaker20 = Speaker(name="Yolanda Robla")
	speaker20.save()
	speaker21 = Speaker(name="Daniel Domene")
	speaker21.save()
	speaker22 = Speaker(name="Carlos Planelles")
	speaker22.save()
	speaker23 = Speaker(name="Pablo Enfedaque")
	speaker23.save()
	speaker24 = Speaker(name="Federico Mon")
	speaker24.save()
	speaker25 = Speaker(name="Israel Saeta Perez")
	speaker25.save()
	speaker26 = Speaker.create(name="Miquel Camprodon")
	speaker27 = Speaker.create(name="Cesar Cardenas Desales")
	speaker28 = Speaker.create(name="Jesus Espino")
	speaker29 = Speaker.create(name="Sergi Sorribas")
	speaker30 = Speaker.create(name="Imanol Cea")
	speaker31 = Speaker.create(name="Jose Manuel Ortega")
	speaker32 = Speaker.create(name="Francisco Fernandez Castanyo")
	speaker33 = Speaker.create(name="Carlos Perello Marin")
	speaker34 = Speaker.create(name="Miguel Sanchez Rodriguez")
	speaker35 = Speaker.create(name="Jose Gargallo")
	speaker36 = Speaker.create(name="Guillem Borrell Nogueras")
	speaker37 = Speaker.create(name="Urtzi Odriozola Lizaso")
	speaker38 = Speaker.create(name="David Gomez-Ullate")
	speaker39 = Speaker.create(name="Pablo Suarez Garcia")
	speaker40 = Speaker.create(name="Mikel Larreategi")
	speaker41 = Speaker.create(name="Braulio Valdivielso")
	speaker42 = Speaker.create(name="Merce Martin")
	speaker43 = Speaker.create(name="Alejandro Brito Monedero")
	speaker44 = Speaker.create(name="Rafa Haro")
	speaker45 = Speaker.create(name="Julio Vicente Trigo Guijarro")
	speaker46 = Speaker.create(name="Juan Ignacio Rodriguez de Leon")
	speaker47 = Speaker.create(name="Juan Riaza")
	speaker48 = Speaker.create(name="David Arcos")
	speaker49 = Speaker.create(name="Pau Freixes")
	speaker50 = Speaker.create(name="Arnau Orriols")
	speaker51 = Speaker.create(name="Pablo Galindo Salgado")
	
	date1 = datetime.date(2015,11,20)
	date2 = datetime.date(2015,11,21)
	date3 = datetime.date(2015,11,22)


	event1 = Event.create(type="workshop",description="Usando contenedores para Big Data",date=date1,track = track4);

	#speaker1 = Speaker.select().where(Speaker.id == 1).get()
	SpeakerEvent.create(speaker_id=speaker1,event_id= event1)

	event2 = Event.create(type="workshop",description="Python en gvSIG, el Sistema de Informacion Geografica Libre",date=date1,track = track4);
	SpeakerEvent.create(speaker_id=speaker2,event_id= event2)
	
	event3 = Event.create(type="workshop",description="Single-Page Applications con Django y Backbone",date=date1,track = track4);
	SpeakerEvent.create(speaker_id=speaker3,event_id= event3)
	
	event4 = Event.create(type="workshop",description="Introduccion a visualizaciones interactivas con Bokeh",date=date1,track = track4);
	SpeakerEvent.create(speaker_id=speaker4,event_id= event4)
	
	event5 = Event.create(type="workshop",description="Simplifica tu vida con sistemas complejos y algoritmos geneticos",date=date1,track = track4);
	SpeakerEvent.create(speaker_id=speaker5,event_id= event5)
	SpeakerEvent.create(speaker_id=speaker6,event_id= event5)


	event6 = Event.create(type="workshop",description="Better async code with Python 3",date=date1,track = track4);
	SpeakerEvent.create(speaker_id=speaker7,event_id= event6)
	
	event7 = Event.create(type="talk",description="Python en entornos reales: rendimiento, monitorizacion y entornos cloud",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker8,event_id= event7)

	event8 = Event.create(type="talk",description="DSLs: Cant parse that",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker9,event_id= event8)

	event9 = Event.create(type="talk",description="Navigating the Data Science Python Ecosystem",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker10,event_id= event9)
	
	event10 = Event.create(type="talk",description="Click: Como hacer interfaces de comandos con Python",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker11,event_id= event10)
	
	event11 = Event.create(type="talk",description="Escalando una web con python",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker12,event_id= event11)
	
	event12 = Event.create(type="talk",description="Autosubmit: investigando el clima con Python",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker13,event_id= event12)
	
	event13 = Event.create(type="talk",description="Django + micro-servicios: Como enfocar nuestros proyectos",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker8,event_id= event13)
	
	event14 = Event.create(type="talk",description="Syntactic Macros in Python",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker14,event_id= event14)
	
	event15 = Event.create(type="talk",description="SocialLearning: encontrando materiales formativos de manera colaborativa",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker15,event_id= event15)
	
	event16 = Event.create(type="talk",description="La maquinaria de import, ese magico desconocido",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker16,event_id= event16)
	
	event17 = Event.create(type="talk",description="Embedding de Python en otras aplicaciones",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker17,event_id= event17)
	
	event18 = Event.create(type="talk",description="Introduccion a visualizaciones interactivas con Bokeh",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker18,event_id= event18)
	
	event19 = Event.create(type="talk",description="Python Funcional",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker19,event_id= event19)
	
	event20 = Event.create(type="talk",description="Acelera y escala tus tests con nodepool",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker20,event_id= event20)
	
	event21 = Event.create(type="talk",description="Python en la industria: el problema de optimizacion (matematica)",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker21,event_id= event21)
	SpeakerEvent.create(speaker_id=speaker22,event_id= event21)
	
	event22 = Event.create(type="talk",description="Objetos mutable e inmutables y errores tipicos",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker23,event_id= event22)
	
	event23 = Event.create(type="talk",description="SQJobs: Sencillo sistema de tareas en segundo plano",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker24,event_id= event23)
	
	event24= Event.create(type="talk",description="Know your models - Statsmodels!",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker25,event_id= event24)
	SpeakerEvent.create(speaker_id=speaker26,event_id= event24)
	
	event25 = Event.create(type="talk",description="Revision de codigo en Python",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker27,event_id= event25)

	event26 = Event.create(type="talk",description="Learning by Trolling",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker28,event_id= event26)
	
	event27 = Event.create(type="talk",description="Data structures beyond dicts and lists",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker29,event_id= event27)
	
	event28 = Event.create(type="talk",description="Python descriptors al detalle",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker23,event_id= event28)
	
	event29 = Event.create(type="talk",description="Django request-response: Un viaje de ida y vuelta",date=date2,track = track2);
	SpeakerEvent.create(speaker_id=speaker30,event_id= event29)
	
	event30 = Event.create(type="talk",description="Seguridad y criptografia en Python",date=date2,track = track3);
	SpeakerEvent.create(speaker_id=speaker31,event_id= event30)
	
	event31 = Event.create(type="talk",description="Extending Python",date=date2,track = track1);
	SpeakerEvent.create(speaker_id=speaker32,event_id= event31)
	
	event32 = Event.create(type="talk",description="Integrando Apache Storm como servidor de aplicaciones Python",date=date1,track = track2);
	SpeakerEvent.create(speaker_id=speaker33,event_id= event32)
	
	#update date in event object
	event32.date = date2
	event32.save()
	
	event33 = Event.create(type="talk",description="Implantacion de ElasticSearch: problemas y soluciones",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker34,event_id= event33)
	
	event34 = Event.create(type="talk",description="Sirviendo 1M de tickets en 50 idiomas y 35 divisas",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker35,event_id= event34)
	
	event35 = Event.create(type="talk",description="Es posible hacer una tesis doctoral en turbulencia con Python",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker36,event_id= event35)

	event36 = Event.create(type="talk",description="Como crear un bot para Telegram",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker37,event_id= event36)
	
	event37 = Event.create(type="talk",description="asyncIO: pongase a la cola por favor",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker9,event_id= event37)
	
	event38 = Event.create(type="talk",description="Deteccion de fraude en medios de pago con python",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker38,event_id= event38)
	SpeakerEvent.create(speaker_id=speaker39,event_id= event38)
	
	event39 = Event.create(type="talk",description="Plone 5: el CMS del futuro, en el presente.",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker40,event_id= event39)
	
	event40 = Event.create(type="talk",description="Un python nuevo para ti: decorators",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker41,event_id= event40)
	
	event41 = Event.create(type="talk",description="Machine Learning in the Cloud with Python",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker42,event_id= event41)

	event42 = Event.create(type="talk",description="Funcional para trollear",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker43,event_id= event42)
	
	event43 = Event.create(type="talk",description="El modulo tracemalloc",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker17,event_id= event43)
	
	event44 = Event.create(type="talk",description="Trolling Detection with Scikit-learn and NLTK",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker44,event_id= event44)
	
	event45 = Event.create(type="talk",description="Having it All: Distributed services with Django, Boto, and SQS queues",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker45,event_id= event45)
	
	event46 = Event.create(type="talk",description="Comparing Python ORM",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker31,event_id= event46)
	
	event47 = Event.create(type="talk",description="Tratando datos mas alla de los limites de la memoria",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker1,event_id= event47)

	event48 = Event.create(type="talk",description="Introduccion a los DSL (Domain Specific Languages) en Python",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker46,event_id= event48)
	
	event49 = Event.create(type="talk",description="Metaprogramacion en Python",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker16,event_id= event49)
	
	event50 = Event.create(type="talk",description="Dive into Scrapy",date=date3,track = track3);
	SpeakerEvent.create(speaker_id=speaker47,event_id= event50)
	
	event51 = Event.create(type="talk",description="Life of a Python program",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker32,event_id= event51)
	
	event52 = Event.create(type="talk",description="Python in the Sky",date=date3,track = track1);
	SpeakerEvent.create(speaker_id=speaker48,event_id= event52)
	
	event53 = Event.create(type="talk",description="Amqp from Python, advanced design patterns",date=date3,track = track2);
	SpeakerEvent.create(speaker_id=speaker49,event_id= event53)
	SpeakerEvent.create(speaker_id=speaker50,event_id= event53)

	
	#event54 = Event.create(type="talk",description="Agujeros negros y optimizacion de codigo en python",date=date3,track = track3);
	#SpeakerEvent.create(speaker_id=speaker51.id,event_id= event54.id)

	data_source_event = [
    {'type': 'talk', 'description': 'Agujeros negros y optimizacion de codigo en python','date':date3,'track':track3},
	]
	
	data_source_speaker_event = [
    {'speaker_id': speaker51,'event_id':'54'},
	]

	for data_dict in data_source_event:
		Event.create(**data_dict)
		
	# Fastest.
	with db.atomic():
		SpeakerEvent.insert_many(data_source_speaker_event).execute()
		
def select_tracks():
    print '\nTracks'
    print '--------------'
    countTracks =  Track.select().count()
    print '\nNumber tracks ' + str(countTracks)
    for track in Track.select():
        print track.name.encode('utf-8')

def select_speakers():
    print '\nSpeakers'
    print '--------------'
    countSpeakers =  Speaker.select().count()
    print '\nNumber speakers ' + str(countSpeakers)
    for speaker in Speaker.select().order_by(Speaker.name.desc()):
        print speaker.name.encode('utf-8')

# Find all Events whose track field is pointing to the track object
def select_events_track(idTrack):
    print '\nEvents track' + str(idTrack)
    print '--------------'
    trackObject = Track.select().where(Track.id == idTrack).get()
    events = Event.select().where(Event.track == trackObject)
    print '\nNumber events ' + str(events.count())+"\n"
    for event in events:
        print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')

# Find all Events whose track field is pointing to the track object
def select_events_track2(idTrack):
	print '\nEvents track' + str(idTrack)
	print '--------------'
	trackObject = Track.select().where(Track.id == idTrack).get()
	print '\nNumber events ' + str(trackObject.events.count())+"\n"
	for event in trackObject.events:
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')


# Find all Events whose track field is pointing to the track object
def select_events_track_join(idTrack):
	print '\nEvents track join' + str(idTrack)
	trackObject = Track.select().where(Track.id == idTrack).get()
	events = Event.select(Event, Track).join(Track).where(Event.track == trackObject).order_by(Event.date.desc())
	for event in events:
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')
		
def select_Events_byDate(mydate):
    print '\nEvent by date '+str(mydate)
    print '--------------'
    events = Event.select().where(Event.date == mydate).order_by(Event.type)
    for event in events:
        print event.type.encode('utf-8') + " " + event.description.encode('utf-8')


def select_WorkShops_Talks():
    print '\nWorkShops'
    print '--------------'
    workshops = Event.select().where(Event.type=='workshop')
    print '\nNumber workshops ' + str(workshops.count())+"\n"
    for event in workshops:
        print str(event.track.name) + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')

    print '\nTalks'
    print '--------------'
    talks = Event.select().where(Event.type=='talk')
    print '\nNumber talks ' + str(talks.count())+"\n"
    for event in talks:
        print str(event.track.name) + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')


def select_Events_byDescription(description):
    print '\nEvent by description '+description
    print '--------------'
    events = Event.select().where(Event.description==description)
    for event in events:
        print event.type.encode('utf-8') + " " + event.description.encode('utf-8')
		
def select_Events_Optimized_byTrack(name):
	print '\nEvent optimized '+str(name)
	print '-----------------'
	for event in Event.select().join(Track).where(Track.name == name).order_by(Event.type):
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')

		
def select_Events_By_Speaker_Many_to_Many():
	query = (SpeakerEvent
         .select(SpeakerEvent, Speaker, Event)# Note that we are selecting all models.
         .join(Event,on=(SpeakerEvent.speaker_id == Speaker.id))# Use an INNER join because every SpeakerEvent has an event.
		 .join(Speaker,on=(SpeakerEvent.event_id == Event.id))# Use an INNER join because every SpeakerEvent has an speaker.
         .switch(SpeakerEvent)
		 .distinct()
         .order_by(Speaker.name))
		 
	#for each speaker_event shows speaker name and event description 
	last = None
	for speaker_event in query:
		speaker = speaker_event.speaker_id
		if speaker != last:
			last = speaker
			print 'Spaker: %s' % speaker.name
		print '    - %s' % speaker_event.event_id.description
		
if __name__ == "__main__":
    
	create_schema()

	insert_speakers_tracks_events()
	
	select_tracks()
	
	select_speakers()

	select_events_track2(1)
	select_events_track2(2)
	select_events_track2(3)
	select_events_track2(4)

	date = datetime.date(2015,11,20)
	
	select_Events_byDate(date)
	
	date = datetime.date(2015,11,21)
	select_Events_byDate(date)
	
	date = datetime.date(2015,11,22)
	select_Events_byDate(date)

	select_WorkShops_Talks()
	
	select_events_track_join(4)
	
	select_Events_Optimized_byTrack("Track Avanzado")
	
	select_Events_By_Speaker_Many_to_Many()