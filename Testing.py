#from here testing without main. 4/02/2020 21:40
from Sail import Sail

bl=['BL40201']#,'BL37200','BL53203' ]
blp=['BLP33201']#, 'BLP47202', 'BLP53202']
s1=['S136101']#,'S148202']
s1p=['S1P40202']#, 'S1P44200']
gt=['GT55200']
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
for x in tb: sails.add(Sail(x))

for x in sails: x.printDetails(), print('\n')