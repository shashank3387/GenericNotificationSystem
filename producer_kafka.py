# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:26:32 2020

@author: ssoni

KAFKA script for producer
"""
import json
from kafka import KafkaProducer
#from kafka.common import KafkaError

#################################################
#-START PRODUCER COMMAND WITH DIFFERENT OPTIONS-#
#################################################
#-Working-#
#producer = KafkaProducer(bootstrap_servers=['10.131.48.48:9092'])

#-Testing-#
producer = KafkaProducer(bootstrap_servers=['10.131.48.48:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
###############################################
#-END PRODUCER COMMAND WITH DIFFERENT OPTIONS-#
###############################################

##########################################
#-START LOOP TO SEND MSG TO KAFKA TOPICS-#
##########################################
for i in range(10):
    data = { "from ": "shashank3387@yahoo.com", "to" : "test@email.com", "index" : "email", "sub": "Target order " }
    
    #-Working-#
    #producer.send('Target', json.dumps(data).encode('utf-8'))
    
    #-Testing-#
    producer.send('Target', data)
########################################
#-END LOOP TO SEND MSG TO KAFKA TOPICS-#
########################################

# Asynchronous by default
#future = producer.send('Target', b'from:ssoni@yodlee.com;to:ssoni@yodlee.com;subject:testing;message:Testing')
producer.close()
print("DONE.")