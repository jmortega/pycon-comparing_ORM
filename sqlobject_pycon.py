#!/usr/python
# -*- coding: utf-8 -*-

from sqlobject import *
from sets import Set
from sqlobject.sqlbuilder import *

import os
import datetime
from time import time

class Base(SQLObject):
	name = StringCol(length=255)
		
class Speaker(Base):
	events = RelatedJoin('Event',
			intermediateTable="speaker_event",
			joinColumn="speakerID",
			otherColumn="eventID")

class Track(Base):	
	events = MultipleJoin('Event', joinColumn='event_id')

class Event(SQLObject):
	type = StringCol(length=255) #workshop /talk
	description = StringCol(length=255)
	date = DateCol(default=None)
	track = ForeignKey('Track')
	speakers = RelatedJoin('Speaker',
			intermediateTable="speaker_event",
			joinColumn="eventID",
			otherColumn="speakerID")
	
def sqlite_connect():
	filename = "sqlobject_pycon.sqlite"
	abs_path = os.path.abspath(filename)
	connection_uri = 'sqlite:///' + abs_path
	connection = connectionForURI(connection_uri)
	sqlhub.processConnection = connection
	try:
		create_schema()
	except Exception,e:
		print e

def create_schema():
	Track.createTable(ifNotExists=True)
	Speaker.createTable(ifNotExists=True)
	Event.createTable(ifNotExists=True)

def insert_speakers_tracks_events():
	#Speaker._connection.debug = True
	#Event._connection.debug = True
	track1 = Track(name="Track PSF (basico)")
	track2 = Track(name="Track Avanzado")
	track3 = Track(name="Track BigML (cientifico)")
	track4 = Track(name="WorkShop")
	track4.name = "WorkShop/Taller" #update
	
	speaker1 = Speaker(name="Francesc Alted")
	speaker2 = Speaker(name="Joaquin del Cerro")
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
	
	date1 = datetime.date(2015,11,20).strftime("%Y-%m-%d")
	date2 = datetime.date(2015,11,21).strftime("%Y-%m-%d")
	date3 = datetime.date(2015,11,22).strftime("%Y-%m-%d")


	event1 = Event(type="workshop",description="Usando contenedores para Big Data",date=date1,track = track4);
	event1.addSpeaker(speaker1);
	
	event2 = Event(type="workshop",description="Python en gvSIG, el Sistema de Informacion Geografica Libre",date=date1,track = track4);
	event2.addSpeaker(speaker2);
	
	event3 = Event(type="workshop",description="Single-Page Applications con Django y Backbone",date=date1,track = track4);
	event3.addSpeaker(speaker3);
	
	event4 = Event(type="workshop",description="Introduccion a visualizaciones interactivas con Bokeh",date=date1,track = track4);
	event4.addSpeaker(speaker4);
	
	event5 = Event(type="workshop",description="Simplifica tu vida con sistemas complejos y algoritmos geneticos",date=date1,track = track4);
	event5.addSpeaker(speaker5);
	event5.addSpeaker(speaker6);
	
	event6 = Event(type="workshop",description="Better async code with Python 3",date=date1,track = track4);
	event6.addSpeaker(speaker7);
	
	event7 = Event(type="talk",description="Python en entornos reales: rendimiento, monitorizacion y entornos cloud",date=date2,track = track1);
	event7.addSpeaker(speaker8);
	
	event8 = Event(type="talk",description="DSLs: Cant parse that",date=date2,track = track2);
	event8.addSpeaker(speaker9);
	
	event9 = Event(type="talk",description="Navigating the Data Science Python Ecosystem",date=date2,track = track3);
	event9.addSpeaker(speaker10);
	
	event10 = Event(type="talk",description="Click: Como hacer interfaces de comandos con Python",date=date2,track = track1);
	event10.addSpeaker(speaker11);
	
	event11 = Event(type="talk",description="Escalando una web con python",date=date2,track = track2);
	event11.addSpeaker(speaker12);
	
	event12 = Event(type="talk",description="Autosubmit: investigando el clima con Python",date=date2,track = track3);
	event12.addSpeaker(speaker13);
	
	event13 = Event(type="talk",description="Django + micro-servicios: Como enfocar nuestros proyectos",date=date2,track = track1);
	event13.addSpeaker(speaker8);
	
	event14 = Event(type="talk",description="Syntactic Macros in Python",date=date2,track = track2);
	event14.addSpeaker(speaker14);
	
	event15 = Event(type="talk",description="SocialLearning: encontrando materiales formativos de manera colaborativa",date=date2,track = track3);
	event15.addSpeaker(speaker15);
	
	event16 = Event(type="talk",description="La maquinaria de import, ese magico desconocido",date=date2,track = track1);
	event16.addSpeaker(speaker16);
	
	event17 = Event(type="talk",description="Embedding de Python en otras aplicaciones",date=date2,track = track2);
	event17.addSpeaker(speaker17);
	
	event18 = Event(type="talk",description="Introduccion a visualizaciones interactivas con Bokeh",date=date2,track = track3);
	event18.addSpeaker(speaker18);
	
	event19 = Event(type="talk",description="Python Funcional",date=date2,track = track1);
	event19.addSpeaker(speaker19);
	
	event20 = Event(type="talk",description="Acelera y escala tus tests con nodepool",date=date2,track = track2);
	event20.addSpeaker(speaker20);
	
	event21 = Event(type="talk",description="Python en la industria: el problema de optimizacion (matematica)",date=date2,track = track3);
	event21.addSpeaker(speaker21);
	event21.addSpeaker(speaker22);
	
	event22 = Event(type="talk",description="Objetos mutable e inmutables y errores tipicos",date=date2,track = track1);
	event22.addSpeaker(speaker23);
	
	event23 = Event(type="talk",description="SQJobs: Sencillo sistema de tareas en segundo plano",date=date2,track = track2);
	event23.addSpeaker(speaker24);
	
	event24= Event(type="talk",description="Know your models - Statsmodels!",date=date2,track = track3);
	event24.addSpeaker(speaker25);
	event24.addSpeaker(speaker26);
	
	event25 = Event(type="talk",description="Revision de codigo en Python",date=date2,track = track1);
	event25.addSpeaker(speaker27);
	
	event26 = Event(type="talk",description="Learning by Trolling",date=date2,track = track2);
	event26.addSpeaker(speaker28);
	
	event27 = Event(type="talk",description="Data structures beyond dicts and lists",date=date2,track = track3);
	event27.addSpeaker(speaker29);
	
	event28 = Event(type="talk",description="Python descriptors al detalle",date=date2,track = track1);
	event28.addSpeaker(speaker23);
	
	event29 = Event(type="talk",description="Django request-response: Un viaje de ida y vuelta",date=date2,track = track2);
	event29.addSpeaker(speaker30);
	
	event30 = Event(type="talk",description="Seguridad y criptografia en Python",date=date2,track = track3);
	event30.addSpeaker(speaker31);
	
	event31 = Event(type="talk",description="Extending Python",date=date2,track = track1);
	event31.addSpeaker(speaker32);
	
	event32 = Event(type="talk",description="Integrando Apache Storm como servidor de aplicaciones Python",date=date1,track = track2);
	event32.addSpeaker(speaker33);
	
	#update date in event object
	event32.date = date2
	
	event33 = Event(type="talk",description="Implantacion de ElasticSearch: problemas y soluciones",date=date3,track = track1);
	event33.addSpeaker(speaker34);
	
	event34 = Event(type="talk",description="Sirviendo 1M de tickets en 50 idiomas y 35 divisas",date=date3,track = track2);
	event34.addSpeaker(speaker35);
	
	event35 = Event(type="talk",description="Es posible hacer una tesis doctoral en turbulencia con Python",date=date3,track = track3);
	event35.addSpeaker(speaker36);
	
	event36 = Event(type="talk",description="Como crear un bot para Telegram",date=date3,track = track1);
	event36.addSpeaker(speaker37);
	
	event37 = Event(type="talk",description="asyncIO: pongase a la cola por favor",date=date3,track = track2);
	event37.addSpeaker(speaker9);
	
	event38 = Event(type="talk",description="Deteccion de fraude en medios de pago con python",date=date3,track = track3);
	event38.addSpeaker(speaker38);
	event38.addSpeaker(speaker39);
	
	event39 = Event(type="talk",description="Plone 5: el CMS del futuro, en el presente.",date=date3,track = track1);
	event39.addSpeaker(speaker40);
	
	event40 = Event(type="talk",description="Un python nuevo para ti: decorators",date=date3,track = track2);
	event40.addSpeaker(speaker41);
	
	event41 = Event(type="talk",description="Machine Learning in the Cloud with Python",date=date3,track = track3);
	event41.addSpeaker(speaker42);
	
	event42 = Event(type="talk",description="Funcional para trollear",date=date3,track = track1);
	event42.addSpeaker(speaker43);
	
	event43 = Event(type="talk",description="El modulo tracemalloc",date=date3,track = track2);
	event43.addSpeaker(speaker17);
	
	event44 = Event(type="talk",description="Trolling Detection with Scikit-learn and NLTK",date=date3,track = track3);
	event44.addSpeaker(speaker44);
	
	event45 = Event(type="talk",description="Having it All: Distributed services with Django, Boto, and SQS queues",date=date3,track = track1);
	event45.addSpeaker(speaker45);
	
	event46 = Event(type="talk",description="Comparing Python ORM",date=date3,track = track2);
	event46.addSpeaker(speaker31);
	
	event47 = Event(type="talk",description="Tratando datos mas alla de los limites de la memoria",date=date3,track = track3);
	event47.addSpeaker(speaker1);
	
	event48 = Event(type="talk",description="Introduccion a los DSL (Domain Specific Languages) en Python",date=date3,track = track1);
	event48.addSpeaker(speaker46);
	
	event49 = Event(type="talk",description="Metaprogramacion en Python",date=date3,track = track2);
	event49.addSpeaker(speaker16);
	
	event50 = Event(type="talk",description="Dive into Scrapy",date=date3,track = track3);
	event50.addSpeaker(speaker47);
	
	event51 = Event(type="talk",description="Life of a Python program",date=date3,track = track1);
	event51.addSpeaker(speaker32);
	
	event52 = Event(type="talk",description="Python in the Sky",date=date3,track = track1);
	event52.addSpeaker(speaker48);
	
	event53 = Event(type="talk",description="Amqp from Python, advanced design patterns",date=date3,track = track2);
	event53.addSpeaker(speaker49);
	event53.addSpeaker(speaker50);
	
	event54 = Event(type="talk",description="Agujeros negros y optimizacion de codigo en python",date=date3,track = track3);
	event54.addSpeaker(speaker51);
	
	
	
	
def select_tracks():
	#The select() class method it returns all instances in the table.
	tracks = list(Track.select())
	print tracks

def select_events_track(idTrack):
	#The select() class method it returns all instances in the table.
	print '\nEvents track' + str(idTrack)
	print '--------------'
	countEvents = Event.select(LIKE(Event.q.trackID, idTrack)).count()
	print '\nNumber events ' + str(countEvents)
	events = Event.select(LIKE(Event.q.trackID, idTrack))
	for event in Set(events):
		print event.track.name + " " + event.type + " " +event.description
		for speaker in Set(event.speakers):
			print speaker.name
			print '***********'

	
def select_speakers():
	#The select() class method it returns all instances in the table.
	print '\nSpeakers'
	print '--------------'
	countSpeakers = Speaker.select().count()
	print '\nNumber speakers ' + str(countSpeakers)
	speakers = list(Speaker.select())
	speakers = Set(Speaker.selectBy())
	for speaker in Set(speakers):
		print speaker.name

def select_Events_byDescription(description):
	print '\select_Events_byDescription'
	#events = Event.select(Event.q.description == description)
	events = Event.select("""event.description LIKE '%"""+description+"""%'""",clauseTables=['event'])
	#events = Event.selectBy(description = description)
	print Set(events)
	for event in Set(events):
		print event.speakers
	
def selectEventBuilder():
	print '\Select all events'
	conn = Event._connection
	conn.debug = True    # So we can see the query execute
	fields = [Event.q.type, Event.q.description]
	select = conn.sqlrepr(Select(fields))
	#select = "select * from event"
	results = conn.queryAll(select)
	print set(results)
	
def updateEventBuilder(idEvent,descripcion):
	start_time = time()
	print '\Update event Builder'
	conn = Event._connection
	conn.debug = True    # So we can see the query execute
	#update = "update event SET description='"+descripcion +"'" +" where id="+str(idEvent)
	update = conn.sqlrepr(Update(Event.q,{Event.q.description.fieldName:descripcion},where=(Event.q.id == idEvent)))
	results = conn.queryAll(update)
	elapsed_time = time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)
	
		
def updateEvent(idEvent,description):
	start_time = time()
	print '\Update event'
	events = Event.select(LIKE(Event.q.id, idEvent))
	for event in Set(events):
		event.description = description
	elapsed_time = time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)
			

def select_WorkShops_Talks():
	print '\nWorkShops'
	print '--------------'
	events = Event.select(LIKE(Event.q.type, "workshop"))
	for event in Set(events):
		print event.description

	print '\nTalks'
	print '--------------'

	events = Event.select(LIKE(Event.q.type, "talk"))
	for event in Set(events):
		print event.description

if __name__ == "__main__":
		
	sqlite_connect()

	insert_speakers_tracks_events()

	select_tracks()
	select_speakers()

	select_events_track(1)
	select_events_track(2)
	select_events_track(3)
	select_events_track(4)

	select_WorkShops_Talks()

	selectEventBuilder()
	
	select_Events_byDescription("macros")