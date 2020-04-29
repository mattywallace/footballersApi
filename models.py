from peewee import *

import datetime



DATABASE = SqliteDatabase('footballers.sqlite')

class Footballer(Model):
	first_name = CharField()
	last_name = CharField()
	nationality = CharField()
	position = CharField()
	age = IntegerField(default=18)
	club_team = CharField()
	number = SmallIntegerField()
	created_at: DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE


def initialize(): 
	DATABASE.connect()
	DATABASE.create_tables([Footballer], safe=True)
	print('connected to the db and created tabels if they werent already there')
	DATABASE.close()