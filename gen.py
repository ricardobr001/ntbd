# -*- coding: utf-8 -*-
from pycpfcnpj import gen
import random
import names
import json
import sys
import re

def insert_string(pos):
    return FILENAME[:pos] + '-mongo' + FILENAME[pos:], FILENAME[:pos] + '-redis' + FILENAME[pos:], FILENAME[:pos] + '-cassandra.csv'

def cassandra_table():
    string = ''

    for i in range(1,3):        
        string += 'produto_' + str(i) + '|quantidade_' + str(i) + '|produto_' + str(i) + '|'

    string += 'nome|cpf'
    return string

def cassandra_register(obj):
    string = ''

    for i in obj['carrinho']:
        string += i['produto'] + '|' + str(i['quantidade']) + '|' + str(i['preco']) + '|'
    
    string += obj['nome'] + '|'
    string += obj['cpf']
    return string

if len(sys.argv) != 3:
    print 'usage:'
    print 'python redis-gen.py <file.txt> <number of registers>'
    sys.exit()

FILENAME = sys.argv[1]
VALUES = int(sys.argv[2])

produtos = [ 'geladeira', 'fogao', 'radio', 'laptop', 'celular',
'televisao', 'ventilador', 'ar condicionado', 'maquina de lavar'
]

file_mongo, file_redis, file_cassandra = insert_string(FILENAME.find('.txt'))

f_redis = open(file_redis, 'w')
f_mongo = open(file_mongo, 'w')
f_cassandra = open(file_cassandra, 'w')

print >> f_mongo, '['
print >> f_cassandra, cassandra_table()

for i in range(0,VALUES):
    obj = {}
    obj['nome'] = names.get_full_name().encode('utf-8')
    obj['cpf'] = gen.cpf_with_punctuation()
    cpf_key = ''.join(re.split('\.|-', obj['cpf']))
    obj['carrinho'] = []
    carrinho = {}

    for j in range(1,3):
        carrinho['produto'] = produtos[random.randint(0,8)]
        carrinho['quantidade'] = random.randint(1,3)
        carrinho['preco'] = round(random.uniform(200, 1000),2)

        obj['carrinho'].append(carrinho)
    
    print >> f_redis, 'SET ' + cpf_key + ' \'' + json.dumps(obj) + '\''
    print >> f_mongo, '\t' + json.dumps(obj)
    print >> f_cassandra, cassandra_register(obj)

print >> f_mongo, ']'
