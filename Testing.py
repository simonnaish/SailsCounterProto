#from here testing without main. 4/02/2020 21:40
"""from Sail import Sail

bl=['BL40201']#,'BL37200','BL53203' ]
blp=['BLP33201']#, 'BLP47202', 'BLP53202']
s1=['S136101']#,'S148202']
gt=['GT55200']
s1p=['S1P40202']#, 'S1P44200']
gtp=['GTP60204']
nc=['NC65206']
ncp=['NCP75100']
m2=['M282200']
fr=['FR40200','FR48202']
ovd=['OVD78201']
tb=['TB72113']
sails=set()
for x in bl: sails.add(Sail(x))
for x in blp: sails.add(Sail(x))
for x in s1: sails.add(Sail(x))
for x in s1p: sails.add(Sail(x))
for x in gt: sails.add(Sail(x))
for x in gtp: sails.add(Sail(x))
for x in nc: sails.add(Sail(x))
for x in ncp: sails.add(Sail(x))
for x in m2: sails.add(Sail(x))
for x in fr: sails.add(Sail(x))
for x in ovd: sails.add(Sail(x))
for x in tb: sails.add(Sail(x))id, category, model, size, year, firstDate

for x in sails: x.printDetails(), print('\n')
"""
import databaseHandler
from Sail import Sail
databaseHandler.addSail('BL53205')
"""Sail('GT57211').addSailtoSQLite()
Sail.addSailtoSQLite('OVD78902')
Sail.addSailtoSQLite('FR44200')
"""
databaseHandler.getSail('BL42901')
databaseHandler.addSail('GT57911')
databaseHandler.addSail('OVD78902')
databaseHandler.addSail('FR44900')
databaseHandler.getSail('BL45204')
databaseHandler.getSail('FR44200')
databaseHandler.deleteSail('BL45201')
databaseHandler.getSail('BL45201')
databaseHandler.addSail('BL45201')
#Sail.addSailtoSQLite('BL45201')
databaseHandler.getSail('BL45201')
