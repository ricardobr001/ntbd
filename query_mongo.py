# -*- coding: utf-8 -*-
#first of all you must have an active mongo server.
from pymongo import MongoClient
import redis
import time
import re

#Precondition: desired values ein array must exist.
array_cpfs = [
    '419.729.539-15',
    '660.797.259-40',
    '410.408.113-29',
    '659.309.992-95',
    '020.005.327-21',
    '959.412.793-70',
    '516.646.796-50',
    '422.284.682-15',
    '458.757.102-41',
    '847.774.492-03'
]
################ MONGO OPERATIONS
client = MongoClient('localhost', 27017) #default Mongo address
db = client.ntbd #ntdb is the desired <database>
coll = db.benchmark #benchmark is the desired <collection>


start = time.time() # Inicializa o contador de tempo

# Querys cassandra
for cpf in array_cpfs:
    result = coll.find_one({"cpf":"\"" + cpf + "\""})

mongo_fulltime = str(time.time() - start)
print '\n#####\nTempo mongo: ' + mongo_fulltime + 's'


############## REDIS OPERATIONS


r = redis.StrictRedis(host='localhost', port=6379, db=0) # Conecta com o redis
start = time.time() # Inicializa o contador de tempo

for cpf in array_cpfs:
    res = r.get(''.join(re.split('\.|-', cpf)))

redis_fulltime = str(time.time() - start)
print '\n#####\nTempo redis: ' + redis_fulltime + 's'
