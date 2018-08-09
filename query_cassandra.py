# -*- coding: utf-8 -*-
from cassandra.cluster import Cluster
import redis
import time
import json
import re

cpfs = [
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

cluster = Cluster(['127.0.0.1']) # Conecta no cluster do cassandra
session = cluster.connect('ntbd') # Seleciona o keyspace

start = time.time() # Inicializa o contador de tempo

# Querys cassandra
for i in cpfs:
    query = 'SELECT * FROM compras WHERE cpf = \'' + i + '\';'
    res = session.execute(query)

    # for j in res:
    #     print j[0], j[1], round(j[2], 2), round(j[3], 2), j[4], j[5], j[6], j[7]

print '\n#####\nTempo cassandra: ' + str(time.time() - start) + 's'

r = redis.StrictRedis(host='localhost', port=6379, db=0) # Conecta com o redis
start = time.time() # Inicializa o contador de tempo

# Query redis
for i in cpfs:
    res = r.get(''.join(re.split('\.|-', i)))
    # print json.dumps(json.loads(res), indent=4)

print '\n#####\nTempo redis: ' + str(time.time() - start) + 's'