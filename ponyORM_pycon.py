#!/usr/python
# -*- coding: utf-8 -*-

import datetime
from pony.orm import *
from pony.orm.serialization import to_dict

def generate_new_schema():
	db = Database("sqlite", "ponyORM_pycon.sqlite", create_db=True)
	return db
	
db = generate_new_schema()

#"Event" is specified as a string here because we didnt declare the entity Event by that moment yet.
class Speaker(db.Entity):
	"""
    Pony ORM model of the Speaker table
    """
	id = PrimaryKey(int, auto=True)
	name = Required(str)
	#events = Set("Event")#relationship with event
	events = Set(lambda: Event,reverse="speakers")
	
	def get_Data(self):
		return "%s (%s)" % (self.id, self.name)


class Track(db.Entity):
	"""
    Pony ORM model of the Track table
    """
	id = PrimaryKey(int, auto=True)
	name = Required(str ,column="track_name")
	events = Set("Event",reverse="track")#relationship with event
	
	def get_Data(self):
		return "%s (%s)" % (self.id, self.name)


class Event(db.Entity):
	"""
    Pony ORM model of the Event table
    """
	id = PrimaryKey(int, auto=True)
	type = Required(str, py_check=lambda val: val == 'talk' or val == 'workshop')
	description = Required(str)
	date = Required(datetime.date)
	track = Required(Track)
	speakers = Set(Speaker,reverse="events")#relationship with speaker
	
	def get_Data(self):
		return "%s (%s) (%s) (%s)" % (self.id, self.type,self.description,self.date,self.track.name)

# Insert data
@db_session
def insert_speakers_tracks_events():

	track1 = Track(name="Track PSF (basico)")
	track2 = Track(name="Track Avanzado")
	track3 = Track(name="Track BigML (cientifico)")
	track4 = Track(name="WorkShop")
	track4.name = "WorkShop/Taller" #update
	track4.set(name="WorkShop/Taller")#update
	
	speaker1 = Speaker(name="Francesc Alted")
	speaker2 = Speaker(name=u"Joaquín del Cerro")
	speaker3 = Speaker(name="Miguel Sanchez Rodriguez")
	speaker4 = Speaker(name="Alejandro Vidal")
	speaker5 = Speaker(name="Carlos Dorado")
	speaker6 = Speaker(name="Siro Moreno")
	speaker7 = Speaker(name="Anton Caceres")
	speaker8 = Speaker(name="Daniel Garcia (cr0hn)")
	speaker9 = Speaker(name="Miguel Araujo Perez")
	speaker10 = Speaker(name="Christine Doig")
	speaker11 = Speaker(name="Roberto Majadas Lopez")
	speaker12 = Speaker(name="Jose Ignacio Galarza")
	speaker13 = Speaker(name="Javier Vegas Regidor")
	speaker14 = Speaker(name="Salvador de la Puente Gonzalez")
	speaker15 = Speaker(name="Alberto Labarga")
	speaker16 = Speaker(name="Raul Cumplido")
	speaker17 = Speaker(name="Jesus Cea")
	speaker18 = Speaker(name="Alejandro Vidal")
	speaker19 = Speaker(name="Guillermo Vaya Perez")
	speaker20 = Speaker(name="Yolanda Robla")
	speaker21 = Speaker(name="Daniel Domene")
	speaker22 = Speaker(name="Carlos Planelles")
	speaker23 = Speaker(name="Pablo Enfedaque")
	speaker24 = Speaker(name="Federico Mon")
	speaker25 = Speaker(name="Israel Saeta Perez")
	speaker26 = Speaker(name="Miquel Camprodon")
	speaker27 = Speaker(name="Cesar Cardenas Desales")
	speaker28 = Speaker(name="Jesus Espino")
	speaker29 = Speaker(name="Sergi Sorribas")
	speaker30 = Speaker(name="Imanol Cea")
	speaker31 = Speaker(name="Jose Manuel Ortega")
	speaker32 = Speaker(name="Francisco Fernandez Castanyo")
	speaker33 = Speaker(name="Carlos Perello Marin")
	speaker34 = Speaker(name="Miguel Sanchez Rodriguez")
	speaker35 = Speaker(name="Jose Gargallo")
	speaker36 = Speaker(name="Guillem Borrell Nogueras")
	speaker37 = Speaker(name="Urtzi Odriozola Lizaso")
	speaker38 = Speaker(name="David Gomez-Ullate")
	speaker39 = Speaker(name="Pablo Suarez Garcia")
	speaker40 = Speaker(name="Mikel Larreategi")
	speaker41 = Speaker(name="Braulio Valdivielso")
	speaker42 = Speaker(name="Merce Martin")
	speaker43 = Speaker(name="Alejandro Brito Monedero")
	speaker44 = Speaker(name="Rafa Haro")
	speaker45 = Speaker(name="Julio Vicente Trigo Guijarro")
	speaker46 = Speaker(name="Juan Ignacio Rodriguez de Leon")
	speaker47 = Speaker(name="Juan Riaza")
	speaker48 = Speaker(name="David Arcos")
	speaker49 = Speaker(name="Pau Freixes")
	speaker50 = Speaker(name="Arnau Orriols")
	speaker51 = Speaker(name="Pablo Galindo Salgado")
	
	date1 = datetime.date(2015,11,20)
	date2 = datetime.date(2015,11,21)
	date3 = datetime.date(2015,11,22)
	
	# Insert an Event in the event table
	event1 = Event(type="workshop",description="Usando contenedores para Big Data",date=date1,track = track4);
	event1.speakers.add(speaker1);
	
	event2 = Event(type="workshop",description="Python en gvSIG, el Sistema de Informacion Geografica Libre",date=date1,track = track4);
	event2.speakers.add(speaker2);
	
	event3 = Event(type="workshop",description="Single-Page Applications con Django y Backbone",date=date1,track = track4);
	event3.speakers.add(speaker3);
	
	event4 = Event(type="workshop",description="Introduccion a visualizaciones interactivas con Bokeh",date=date1,track = track4);
	event4.speakers.add(speaker4);
	
	event5 = Event(type="workshop",description="Simplifica tu vida con sistemas complejos y algoritmos geneticos",date=date1,track = track4);
	event5.speakers.add(speaker5);
	event5.speakers.add(speaker6);
	
	event6 = Event(type="workshop",description="Better async code with Python 3",date=date1,track = track4);
	event6.speakers.add(speaker7);
	
	event7 = Event(type="talk",description="Python en entornos reales: rendimiento, monitorizacion y entornos cloud",date=date2,track = track1);
	event7.speakers.add(speaker8);
	
	event8 = Event(type="talk",description="DSLs: Cant parse that",date=date2,track = track2);
	event8.speakers.add(speaker9);
	
	event9 = Event(type="talk",description="Navigating the Data Science Python Ecosystem",date=date2,track = track3);
	event9.speakers.add(speaker10);
	
	event10 = Event(type="talk",description="Click: Como hacer interfaces de comandos con Python",date=date2,track = track1);
	event10.speakers.add(speaker11);
	
	event11 = Event(type="talk",description="Escalando una web con python",date=date2,track = track2);
	event11.speakers.add(speaker12);
	
	event12 = Event(type="talk",description="Autosubmit: investigando el clima con Python",date=date2,track = track3);
	event12.speakers.add(speaker13);
	
	event13 = Event(type="talk",description="Django + micro-servicios: Como enfocar nuestros proyectos",date=date2,track = track1);
	event13.speakers.add(speaker8);
	
	event14 = Event(type="talk",description="Syntactic Macros in Python",date=date2,track = track2);
	event14.speakers.add(speaker14);
	
	event15 = Event(type="talk",description="SocialLearning: encontrando materiales formativos de manera colaborativa",date=date2,track = track3);
	event15.speakers.add(speaker15);
	
	event16 = Event(type="talk",description="La maquinaria de import, ese magico desconocido",date=date2,track = track1);
	event16.speakers.add(speaker16);
	
	event17 = Event(type="talk",description="Embedding de Python en otras aplicaciones",date=date2,track = track2);
	event17.speakers.add(speaker17);
	
	event18 = Event(type="talk",description="Introduccion a visualizaciones interactivas con Bokeh",date=date2,track = track3);
	event18.speakers.add(speaker18);
	
	event19 = Event(type="talk",description="Python Funcional",date=date2,track = track1);
	event19.speakers.add(speaker19);
	
	event20 = Event(type="talk",description="Acelera y escala tus tests con nodepool",date=date2,track = track2);
	event20.speakers.add(speaker20);
	
	event21 = Event(type="talk",description="Python en la industria: el problema de optimizacion (matematica)",date=date2,track = track3);
	event21.speakers.add(speaker21);
	event21.speakers.add(speaker22);
	
	event22 = Event(type="talk",description="Objetos mutable e inmutables y errores tipicos",date=date2,track = track1);
	event22.speakers.add(speaker23);
	
	event23 = Event(type="talk",description="SQJobs: Sencillo sistema de tareas en segundo plano",date=date2,track = track2);
	event23.speakers.add(speaker24);
	
	event24= Event(type="talk",description="Know your models - Statsmodels!",date=date2,track = track3);
	event24.speakers.add(speaker25);
	event24.speakers.add(speaker26);
	
	event25 = Event(type="talk",description="Revision de codigo en Python",date=date2,track = track1);
	event25.speakers.add(speaker27);
	
	event26 = Event(type="talk",description="Learning by Trolling",date=date2,track = track2);
	event26.speakers.add(speaker28);
	
	event27 = Event(type="talk",description="Data structures beyond dicts and lists",date=date2,track = track3);
	event27.speakers.add(speaker29);
	
	event28 = Event(type="talk",description="Python descriptors al detalle",date=date2,track = track1);
	event28.speakers.add(speaker23);
	
	event29 = Event(type="talk",description="Django request-response: Un viaje de ida y vuelta",date=date2,track = track2);
	event29.speakers.add(speaker30);
	
	event30 = Event(type="talk",description="Seguridad y criptografia en Python",date=date2,track = track3);
	event30.speakers.add(speaker31);
	
	event31 = Event(type="talk",description="Extending Python",date=date2,track = track1);
	event31.speakers.add(speaker32);
	
	event32 = Event(type="talk",description="Integrando Apache Storm como servidor de aplicaciones Python",date=date2,track = track2);
	event32.speakers.add(speaker33);
	
	event33 = Event(type="talk",description="Implantacion de ElasticSearch: problemas y soluciones",date=date3,track = track1);
	event33.speakers.add(speaker34);
	
	event34 = Event(type="talk",description="Sirviendo 1M de tickets en 50 idiomas y 35 divisas",date=date3,track = track2);
	event34.speakers.add(speaker35);
	
	event35 = Event(type="talk",description="Es posible hacer una tesis doctoral en turbulencia con Python",date=date3,track = track3);
	event35.speakers.add(speaker36);
	
	event36 = Event(type="talk",description="Como crear un bot para Telegram",date=date3,track = track1);
	event36.speakers.add(speaker37);
	
	event37 = Event(type="talk",description="asyncIO: pongase a la cola por favor",date=date3,track = track2);
	event37.speakers.add(speaker9);
	
	event38 = Event(type="talk",description="Deteccion de fraude en medios de pago con python",date=date3,track = track3);
	event38.speakers.add(speaker38);
	event38.speakers.add(speaker39);
	
	event39 = Event(type="talk",description="Plone 5: el CMS del futuro, en el presente.",date=date3,track = track1);
	event39.speakers.add(speaker40);
	
	event40 = Event(type="talk",description="Un python nuevo para ti: decorators",date=date3,track = track2);
	event40.speakers.add(speaker41);
	
	event41 = Event(type="talk",description="Machine Learning in the Cloud with Python",date=date3,track = track3);
	event41.speakers.add(speaker42);
	
	event42 = Event(type="talk",description="Funcional para trollear",date=date3,track = track1);
	event42.speakers.add(speaker43);
	
	event43 = Event(type="talk",description="El modulo tracemalloc",date=date3,track = track2);
	event43.speakers.add(speaker17);
	
	event44 = Event(type="talk",description="Trolling Detection with Scikit-learn and NLTK",date=date3,track = track3);
	event44.speakers.add(speaker44);
	
	event45 = Event(type="talk",description="Having it All: Distributed services with Django, Boto, and SQS queues",date=date3,track = track1);
	event45.speakers.add(speaker45);
	
	event46 = Event(type="talk",description="Comparing Python ORM",date=date3,track = track2);
	event46.speakers.add(speaker31);
	
	event47 = Event(type="talk",description="Tratando datos mas alla de los limites de la memoria",date=date3,track = track3);
	event47.speakers.add(speaker1);
	
	event48 = Event(type="talk",description="Introduccion a los DSL (Domain Specific Languages) en Python",date=date3,track = track1);
	event48.speakers.add(speaker46);
	
	event49 = Event(type="talk",description="Metaprogramacion en Python",date=date3,track = track2);
	event49.speakers.add(speaker16);
	
	event50 = Event(type="talk",description="Dive into Scrapy",date=date3,track = track3);
	event50.speakers.add(speaker47);
	
	event51 = Event(type="talk",description="Life of a Python program",date=date3,track = track1);
	event51.speakers.add(speaker32);
	
	event52 = Event(type="talk",description="Python in the Sky",date=date3,track = track1);
	event52.speakers.add(speaker48);
	
	event53 = Event(type="talk",description="Amqp from Python, advanced design patterns",date=date3,track = track2);
	event53.speakers.add(speaker49);
	event53.speakers.add(speaker50);
	
	event54 = Event(type="talk",description="Agujeros negros y optimizacion de codigo en python",date=date3,track = track3);
	event54.speakers.add(speaker51);
	
	#db.commit() # not neccesary
	
@db_session
def select_tracks():
	print '\nTracks'
	print '--------------'
	countTracks =  Track.select().count()
	print '\nNumber tracks ' + str(countTracks)
	#The select() class method it returns all instances in the table.
	for track in Track.select():
		print track.name
		for event in track.events:
			print event.type.encode('utf-8')
			print event.description.encode('utf-8')

@db_session
def select_speakers():
	print '\nSpeakers'
	print '--------------'
	countSpeakers =  Speaker.select().count()
	print '\nNumber speakers ' + str(countSpeakers)
	#The select() class method it returns all instances in the table.
	for speaker in select(speaker for speaker in Speaker):
		print to_dict(speaker)
		print speaker.name.encode('utf-8')

@db_session
def select_speakers_db():
	for row in db.select("* from Speaker"):
		print row


# Find all Events whose track field is pointing to the track object
@db_session
def select_events_track(idTrack):
	print '\nEvents track' + str(idTrack)
	print '--------------'
	trackObject = Track.select(lambda track: track.id==idTrack).get()
	events = Event.select(lambda event: event.track==trackObject)
	print '\nNumber events ' + str(len(events))+"\n"
	for event in events:
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')
		

@db_session		
def select_speakers_sql():
	print '\nSpeakers sql'
	print '--------------'
	speakers = Speaker.select_by_sql("SELECT * FROM Speaker")
	for speaker in speakers:
		print speaker.name.encode('utf-8')

@db_session
def select_speakers_byId(speakerId):
	print '\nSpeakers'
	speakers = Speaker.select(lambda s: s.id==speakerId)
	speaker1 = Speaker[speakerId]
	print speaker1.name
	for speaker in speakers:
		print speaker.name.encode('utf-8')

@db_session
def select_Events_byDate(mydate):
	print '\nEvent by date '+str(mydate)
	print '--------------'
	events = Event.select(lambda event: event.date == mydate).order_by(Event.type)
	for event in events:
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')

@db_session
def select_Events_byDescription(description):
	print '\nEvent by description '+description
	print '--------------'
	events = select(e for e in Event if e.description == description)
	for event in events:
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')
		
		
@db_session
def select_Events_byDate2(mydate):
	print '\nEvent by date '+str(mydate)
	print '--------------'
	events = select(e for e in Event if e.date == mydate).order_by(Event.type)
	for event in events:
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')

		
@db_session
def select_WorkShops_Talks():
	print '\nWorkShops'
	print '--------------'
	workshops = Event.select(lambda event: event.type=='workshop')
	print '\nNumber workshops ' + str(len(workshops))+"\n"
	for event in workshops:
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')

	print '\nTalks'
	print '--------------'
	talks =Event.select(lambda event: event.type=='talk')
	print '\nNumber talks ' + str(len(talks))+"\n"
	for event in talks:
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')
	

	
	
# map the models to the database 
# and create the tables, if they don't exist
# create tables to store the objects data
db.generate_mapping(check_tables=True, create_tables=True)

#Using debug mode True/False
sql_debug(True)

if __name__ == "__main__":
 
    # use db_session as a context manager
    with db_session:

	insert_speakers_tracks_events()
	
	select_tracks()
	
	select_speakers()
	select_speakers_sql()
	
	select_events_track(1)
	select_events_track(2)
	select_events_track(3)
	select_events_track(4)
	
	select_WorkShops_Talks()
	
	date = datetime.date(2015,11,20)
	
	select_Events_byDate(date)
	
	date = datetime.date(2015,11,21)
	select_Events_byDate2(date)
	
	date = datetime.date(2015,11,22)
	select_Events_byDate2(date)
	select_speakers_byId(1)
	
	select_Events_byDescription("python")
	
	Event.select().show()
	
	Track.select().show()
	
	Speaker.select().show()
	
