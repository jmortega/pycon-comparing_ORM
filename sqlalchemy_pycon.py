#!/usr/python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, ForeignKey, Integer, String , Date, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from sets import Set

import datetime
import os
import sys

Base = declarative_base()
	
class Speaker(Base):
	__tablename__ = 'Speaker'
	# Here we define columns for the table speaker
	# Notice that each column is also a normal Python instance attribute.
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	events = relationship('Event',secondary='Event_Speaker')#Event_Speaker is the table for many-to-many relationship
	
	def __repr__(self):
		return "<Speakers(events='%s')>" % self.events

class Track(Base):
	__tablename__ = 'Track'
	# Here we define columns for the table track
	# Notice that each column is also a normal Python instance attribute.
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	
class Event(Base):
	__tablename__ = 'Event'
	# Here we define columns for the table event.
	# Notice that each column is also a normal Python instance attribute.
	id = Column(Integer, primary_key=True)
	type = Column(String(255))#workshop /talk
	description = Column(String(255))
	date = Column(Date)
	track_id = Column(Integer, ForeignKey('Track.id'))
	track = relationship(Track,backref=backref('events',uselist=True,cascade='delete,all'))
	speakers = relationship(Speaker,secondary='Event_Speaker')#Event_Speaker is the table for many-to-many relationship

#many-to-many relationship
class EventSpeaker(Base):
	__tablename__ = 'Event_Speaker'
	eventId = Column('event_id',Integer, ForeignKey('Event.id'), primary_key=True)
	speakerId = Column('speaker_id',Integer, ForeignKey('Speaker.id'), primary_key=True)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
#with echo=True you can log queries at runtime
engine = create_engine('sqlite:///sqlalchemy_pycon.sqlite', echo=True)
 
#The MetaData class describes a connection
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

#Manipulating data requires a session. Sessions come from Session classes, which are in
#turn created by the sessionmaker() function. The session must be bound to a database engine

DBSession = sessionmaker(bind=engine,autoflush=True)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert data
def insert_speakers_tracks_events():

	track1 = Track(name="Track PSF (basico)")
	session.add(track1)
	track2 = Track(name="Track Avanzado")
	session.add(track2)
	track3 = Track(name="Track BigML (cientifico)")
	session.add(track3)
	track4 = Track(name="WorkShop")
	session.add(track4)
	track4.name = "WorkShop/Taller" #update
	
	speaker1 = Speaker(name="Francesc Alted")
	session.add(speaker1)
	speaker2 = Speaker(name="Joaquin del Cerro")
	session.add(speaker2)
	speaker3 = Speaker(name="Miguel Sanchez Rodriguez")
	session.add(speaker3)
	speaker4 = Speaker(name="Alejandro Vidal")
	session.add(speaker4)
	speaker5 = Speaker(name="Carlos Dorado")
	session.add(speaker5)
	speaker6 = Speaker(name="Siro Moreno")
	session.add(speaker6)
	speaker7 = Speaker(name="Anton Caceres")
	session.add(speaker7)
	speaker8 = Speaker(name="Daniel Garcia (cr0hn)")
	session.add(speaker8)
	speaker9 = Speaker(name="Miguel Araujo Perez")
	session.add(speaker9)
	speaker10 = Speaker(name="Christine Doig")
	session.add(speaker10)
	speaker11 = Speaker(name="Roberto Majadas Lopez")
	session.add(speaker11)
	speaker12 = Speaker(name="Jose Ignacio Galarza")
	session.add(speaker12)
	speaker13 = Speaker(name="Javier Vegas Regidor")
	session.add(speaker13)
	speaker14 = Speaker(name="Salvador de la Puente Gonzalez")
	session.add(speaker14)
	speaker15 = Speaker(name="Alberto Labarga")
	session.add(speaker15)
	speaker16 = Speaker(name="Raul Cumplido")
	session.add(speaker16)
	speaker17 = Speaker(name="Jesus Cea")
	session.add(speaker17)
	speaker18 = Speaker(name="Alejandro Vidal")
	session.add(speaker18)
	speaker19 = Speaker(name="Guillermo Vaya Perez")
	session.add(speaker19)
	speaker20 = Speaker(name="Yolanda Robla")
	session.add(speaker20)
	speaker21 = Speaker(name="Daniel Domene")
	session.add(speaker21)
	speaker22 = Speaker(name="Carlos Planelles")
	session.add(speaker22)
	speaker23 = Speaker(name="Pablo Enfedaque")
	session.add(speaker23)
	speaker24 = Speaker(name="Federico Mon")
	session.add(speaker24)
	speaker25 = Speaker(name="Israel Saeta Perez")
	session.add(speaker25)
	speaker26 = Speaker(name="Miquel Camprodon")
	session.add(speaker26)
	speaker27 = Speaker(name="Cesar Cardenas Desales")
	session.add(speaker27)
	speaker28 = Speaker(name="Jesus Espino")
	session.add(speaker28)
	speaker29 = Speaker(name="Sergi Sorribas")
	session.add(speaker29)
	speaker30 = Speaker(name="Imanol Cea")
	session.add(speaker30)
	speaker31 = Speaker(name="Jose Manuel Ortega")
	session.add(speaker31)
	speaker32 = Speaker(name="Francisco Fernandez Castanyo")
	session.add(speaker32)
	speaker33 = Speaker(name="Carlos Perello Marin")
	session.add(speaker33)
	speaker34 = Speaker(name="Miguel Sanchez Rodriguez")
	session.add(speaker34)
	speaker35 = Speaker(name="Jose Gargallo")
	session.add(speaker35)
	speaker36 = Speaker(name="Guillem Borrell Nogueras")
	session.add(speaker36)
	speaker37 = Speaker(name="Urtzi Odriozola Lizaso")
	session.add(speaker37)
	speaker38 = Speaker(name="David Gomez-Ullate")
	session.add(speaker38)
	speaker39 = Speaker(name="Pablo Suarez Garcia")
	session.add(speaker39)
	speaker40 = Speaker(name="Mikel Larreategi")
	session.add(speaker40)
	speaker41 = Speaker(name="Braulio Valdivielso")
	session.add(speaker41)
	speaker42 = Speaker(name="Merce Martin")
	session.add(speaker42)
	speaker43 = Speaker(name="Alejandro Brito Monedero")
	session.add(speaker43)
	speaker44 = Speaker(name="Rafa Haro")
	session.add(speaker44)
	speaker45 = Speaker(name="Julio Vicente Trigo Guijarro")
	session.add(speaker45)
	speaker46 = Speaker(name="Juan Ignacio Rodriguez de Leon")
	session.add(speaker46)
	speaker47 = Speaker(name="Juan Riaza")
	session.add(speaker47)
	speaker48 = Speaker(name="David Arcos")
	session.add(speaker48)
	speaker49 = Speaker(name="Pau Freixes")
	session.add(speaker49)
	speaker50 = Speaker(name="Arnau Orriols")
	session.add(speaker50)
	speaker51 = Speaker(name="Pablo Galindo Salgado")
	session.add(speaker51)
	
	date1 = datetime.date(2015,11,20)
	date2 = datetime.date(2015,11,21)
	date3 = datetime.date(2015,11,22)
	
	# Insert an Event in the event table
	event1 = Event(type="workshop",description="Usando contenedores para Big Data",date=date1,track = track4);
	event1.speakers.append(speaker1);
	
	event2 = Event(type="workshop",description="Python en gvSIG, el Sistema de Informacion Geografica Libre",date=date1,track = track4);
	event2.speakers.append(speaker2);
	
	event3 = Event(type="workshop",description="Single-Page Applications con Django y Backbone",date=date1,track = track4);
	event3.speakers.append(speaker3);
	
	event4 = Event(type="workshop",description="Introduccion a visualizaciones interactivas con Bokeh",date=date1,track = track4);
	event4.speakers.append(speaker4);
	
	event5 = Event(type="workshop",description="Simplifica tu vida con sistemas complejos y algoritmos geneticos",date=date1,track = track4);
	event5.speakers.append(speaker5);
	event5.speakers.append(speaker6);
	
	event6 = Event(type="workshop",description="Better async code with Python 3",date=date1,track = track4);
	event6.speakers.append(speaker7);
	
	event7 = Event(type="talk",description="Python en entornos reales: rendimiento, monitorizacion y entornos cloud",date=date2,track = track1);
	event7.speakers.append(speaker8);
	
	event8 = Event(type="talk",description="DSLs: Cant parse that",date=date2,track = track2);
	event8.speakers.append(speaker9);
	
	event9 = Event(type="talk",description="Navigating the Data Science Python Ecosystem",date=date2,track = track3);
	event9.speakers.append(speaker10);
	
	event10 = Event(type="talk",description="Click: Como hacer interfaces de comandos con Python",date=date2,track = track1);
	event10.speakers.append(speaker11);
	
	event11 = Event(type="talk",description="Escalando una web con python",date=date2,track = track2);
	event11.speakers.append(speaker12);
	
	event12 = Event(type="talk",description="Autosubmit: investigando el clima con Python",date=date2,track = track3);
	event12.speakers.append(speaker13);
	
	event13 = Event(type="talk",description="Django + micro-servicios: Como enfocar nuestros proyectos",date=date2,track = track1);
	event13.speakers.append(speaker8);
	
	event14 = Event(type="talk",description="Syntactic Macros in Python",date=date2,track = track2);
	event14.speakers.append(speaker14);
	
	event15 = Event(type="talk",description="SocialLearning: encontrando materiales formativos de manera colaborativa",date=date2,track = track3);
	event15.speakers.append(speaker15);
	
	event16 = Event(type="talk",description="La maquinaria de import, ese magico desconocido",date=date2,track = track1);
	event16.speakers.append(speaker16);
	
	event17 = Event(type="talk",description="Embedding de Python en otras aplicaciones",date=date2,track = track2);
	event17.speakers.append(speaker17);
	
	event18 = Event(type="talk",description="Introduccion a visualizaciones interactivas con Bokeh",date=date2,track = track3);
	event18.speakers.append(speaker18);
	
	event19 = Event(type="talk",description="Python Funcional",date=date2,track = track1);
	event19.speakers.append(speaker19);
	
	event20 = Event(type="talk",description="Acelera y escala tus tests con nodepool",date=date2,track = track2);
	event20.speakers.append(speaker20);
	
	event21 = Event(type="talk",description="Python en la industria: el problema de optimizacion (matematica)",date=date2,track = track3);
	event21.speakers.append(speaker21);
	event21.speakers.append(speaker22);
	
	event22 = Event(type="talk",description="Objetos mutable e inmutables y errores tipicos",date=date2,track = track1);
	event22.speakers.append(speaker23);
	
	event23 = Event(type="talk",description="SQJobs: Sencillo sistema de tareas en segundo plano",date=date2,track = track2);
	event23.speakers.append(speaker24);
	
	event24= Event(type="talk",description="Know your models - Statsmodels!",date=date2,track = track3);
	event24.speakers.append(speaker25);
	event24.speakers.append(speaker26);
	
	event25 = Event(type="talk",description="Revision de codigo en Python",date=date2,track = track1);
	event25.speakers.append(speaker27);
	
	event26 = Event(type="talk",description="Learning by Trolling",date=date2,track = track2);
	event26.speakers.append(speaker28);
	
	event27 = Event(type="talk",description="Data structures beyond dicts and lists",date=date2,track = track3);
	event27.speakers.append(speaker29);
	
	event28 = Event(type="talk",description="Python descriptors al detalle",date=date2,track = track1);
	event28.speakers.append(speaker23);
	
	event29 = Event(type="talk",description="Django request-response: Un viaje de ida y vuelta",date=date2,track = track2);
	event29.speakers.append(speaker30);
	
	event30 = Event(type="talk",description="Seguridad y criptografia en Python",date=date2,track = track3);
	event30.speakers.append(speaker31);
	
	event31 = Event(type="talk",description="Extending Python",date=date2,track = track1);
	event31.speakers.append(speaker32);
	
	event32 = Event(type="talk",description="Integrando Apache Storm como servidor de aplicaciones Python",date=date2,track = track2);
	event32.speakers.append(speaker33);
	
	event33 = Event(type="talk",description="Implantacion de ElasticSearch: problemas y soluciones",date=date3,track = track1);
	event33.speakers.append(speaker34);
	
	event34 = Event(type="talk",description="Sirviendo 1M de tickets en 50 idiomas y 35 divisas",date=date3,track = track2);
	event34.speakers.append(speaker35);
	
	event35 = Event(type="talk",description="Es posible hacer una tesis doctoral en turbulencia con Python",date=date3,track = track3);
	event35.speakers.append(speaker36);
	
	event36 = Event(type="talk",description="Como crear un bot para Telegram",date=date3,track = track1);
	event36.speakers.append(speaker37);
	
	event37 = Event(type="talk",description="asyncIO: pongase a la cola por favor",date=date3,track = track2);
	event37.speakers.append(speaker9);
	
	event38 = Event(type="talk",description="Deteccion de fraude en medios de pago con python",date=date3,track = track3);
	event38.speakers.append(speaker38);
	event38.speakers.append(speaker39);
	
	event39 = Event(type="talk",description="Plone 5: el CMS del futuro, en el presente.",date=date3,track = track1);
	event39.speakers.append(speaker40);
	
	event40 = Event(type="talk",description="Un python nuevo para ti: decorators",date=date3,track = track2);
	event40.speakers.append(speaker41);
	
	event41 = Event(type="talk",description="Machine Learning in the Cloud with Python",date=date3,track = track3);
	event41.speakers.append(speaker42);
	
	event42 = Event(type="talk",description="Funcional para trollear",date=date3,track = track1);
	event42.speakers.append(speaker43);
	
	event43 = Event(type="talk",description="El modulo tracemalloc",date=date3,track = track2);
	event43.speakers.append(speaker17);
	
	event44 = Event(type="talk",description="Trolling Detection with Scikit-learn and NLTK",date=date3,track = track3);
	event44.speakers.append(speaker44);
	
	event45 = Event(type="talk",description="Having it All: Distributed services with Django, Boto, and SQS queues",date=date3,track = track1);
	event45.speakers.append(speaker45);
	
	event46 = Event(type="talk",description="Comparing Python ORM",date=date3,track = track2);
	event46.speakers.append(speaker31);
	
	event47 = Event(type="talk",description="Tratando datos mas alla de los limites de la memoria",date=date3,track = track3);
	event47.speakers.append(speaker1);
	
	event48 = Event(type="talk",description="Introduccion a los DSL (Domain Specific Languages) en Python",date=date3,track = track1);
	event48.speakers.append(speaker46);
	
	event49 = Event(type="talk",description="Metaprogramacion en Python",date=date3,track = track2);
	event49.speakers.append(speaker16);
	
	event50 = Event(type="talk",description="Dive into Scrapy",date=date3,track = track3);
	event50.speakers.append(speaker47);
	
	event51 = Event(type="talk",description="Life of a Python program",date=date3,track = track1);
	event51.speakers.append(speaker32);
	
	event52 = Event(type="talk",description="Python in the Sky",date=date3,track = track1);
	event52.speakers.append(speaker48);
	
	event53 = Event(type="talk",description="Amqp from Python, advanced design patterns",date=date3,track = track2);
	event53.speakers.append(speaker49);
	event53.speakers.append(speaker50);
	
	event54 = Event(type="talk",description=u"Agujeros negros y optimización de código en python",date=date3,track = track3);
	event54.speakers.append(speaker51);
	
	#add events to session
	for event in [event1,event2,event3,event4,event5,event6,event7,event8,event9,event10,event11,event12,event13,event14,event15,event16,event17,event18,
	event19,event20,event21,event22,event23,event24,event25,event26,event27,event28,event29,event30,event31,event32,event33,event34,event35,event36,
	event37,event38,event39,event40,event41,event42,event43,event44,event45,event46,event48,event49,event50,event51]:
		session.add(event)
	
	# Add several events
	session.add_all([event52,event53,event54])
	
	session.commit()
	
	# Now we write all this out to the database in one single step, and
	# SQLAlchemy automatically figures out the correct order for the SQL
	# statements. Notice also how we didn't need to save the Keyword
	# instances, because a dependency relationship was set up when we
	# associated them with their articles just now.
	session.flush()


#queries

#All queries begin with the query() method; this has been show previously, but not noted.
#Queries differ in the subsequent filtering commands. With no filtering, a query returns all the
#rows in a table:

def select_tracks():
	print '\nTracks'
	print '--------------'
	countTracks = session.query(Track).count()
	print '\nNumber tracks ' + str(countTracks)
	#The select() class method it returns all instances in the table.
	tracks = session.query(Track).order_by(Track.id).all()
	for track in tracks:
		print track.name
	tracks = session.query(Track).filter(or_(Track.id == 1, Track.id == 2))
	for track in tracks:
		print track.name

def select_speakers():
	print '\nSpeakers'
	print '--------------'
	countSpeakers = session.query(Speaker).count()
	print '\nNumber speakers ' + str(countSpeakers)
	# Return the first Speaker from all Speaker in the database
	speaker = session.query(Speaker).first()
	print speaker.name
	
	#Make a query to find all Speakers in the database
	result = session.query(Speaker).all()
	for row in result:
		print row.name


def updateEvent(idEvent,description):
	print '\Update event'
	events = session.query(Event).filter(Event.id == idEvent)
	for event in Set(events):
		event.description = description
		
def select_Speaker_byName(name):
	p = session.query(Speaker).filter(Speaker.name == name)
	print p
		
def select_Events_byDescription(description):
	print '\nEvents with description '+description
	print '-------------------------'
	events = session.query(Event).filter(Event.description.like('%'+description+'%')).all()
	print len(Set(events))
	for event in Set(events):
		print event.description.encode('utf-8')

def select_Event_byId(idEvent):
	print session.query(Event).filter_by(id=idEvent)
	event = session.query(Event).filter_by(id = idEvent)
	for event in Set(event):
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')
		
def select_Events_byDate(mydate):
	print '\nEvent by date '+str(mydate)
	
	event = session.query(Event).filter_by(date = mydate)
	for event in Set(event):
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')
		
def select_Events_bySpeaker(idSpeaker):
	p = session.query(Speaker).filter(Speaker.id == idSpeaker).one()
	print 'Speaker '+str(p.name)
	for event in Set(p.events):
		print event.type.encode('utf-8') + " " + event.description.encode('utf-8')
		
# Find all Events whose track field is pointing to the track object
def select_events_track(idTrack):
	#The select() class method it returns all instances in the table.
	print '\nEvents track' + str(idTrack)
	print '--------------'
	#The count() method is used to determine how many rows the SQL statement would return.
	countEvents = session.query(Event).filter(Event.track_id == idTrack).count()
	print '\nNumber events ' + str(countEvents)
	track = session.query(Track).filter(Track.id == idTrack).one()
	for event in Set(track.events):
		print event.track.name.encode('utf-8') + " " + event.type.encode('utf-8') + " " +event.description.encode('utf-8')

def select_WorkShops_Talks():
	print '\nWorkShops'
	print '--------------'
	for u, a in session.query(Event, Track).filter(Track.id==Event.track_id).filter(Event.type=='workshop').all():
		print u.description.encode('utf-8')

	print '\nTalks'
	print '--------------'

	for u, a in session.query(Event, Track).filter(Track.id==Event.track_id).filter(Event.type=='talk').all():
		print u.description.encode('utf-8')
		
insert_speakers_tracks_events()

select_tracks()
select_speakers()

select_events_track(1)
select_events_track(2)
select_events_track(3)
select_events_track(4)

select_Events_bySpeaker(1)
select_Events_bySpeaker(2)
select_Events_bySpeaker(3)
select_Events_bySpeaker(4)

select_WorkShops_Talks()

date = datetime.date(2015,11,20)

select_Events_byDate(date)

date = datetime.date(2015,11,21)

select_Events_byDate(date)

date = datetime.date(2015,11,22)

select_Events_byDate(date)

select_Events_byDescription("python")

#cerrar sesion
session.close()
