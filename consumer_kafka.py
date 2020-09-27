# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:48:15 2020

@author: ssoni

KAFKA script for consumer to send alerts
"""
import datetime
import json
from kafka import KafkaConsumer

##############################
#-START EMAIL ALERT FUNCTION-#
##############################
def send_email(mail_from,mail_to,mail_sub):
    import smtplib
    from smtplib import SMTPException

    sender = mail_from
    receivers = mail_to
    message = mail_sub
    
    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Email - '",sender, ", ", receivers, ", ",message,"'" )

    #-UNCOMMENT BELOW AFTER ADDING CORRECT SMTP SERVER-#
    '''
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print ("Successfully sent email")
    except SMTPException:
            print ("Error: unable to send email")
            '''
############################
#-END EMAIL ALERT FUNCTION-#
############################

##############################
#-START SLACK ALERT FUNCTION-#
##############################
def send_slack(mail_from,mail_to,mail_sub):

    sender = mail_from
    receivers = mail_to
    message = mail_sub
    
    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Slack - '",sender, ", ", receivers, ", ",message,"'" )

############################
#-END SLACK ALERT FUNCTION-#
############################

################################
#-START UNKNOWN ALERT FUNCTION-#
################################
def send_unknown():
    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Unknown - ''" )

##############################
#-END UNKNOWN ALERT FUNCTION-#
##############################

#################################################
#-START CONSUMER COMMAND WITH DIFFERENT OPTIONS-#
#################################################

#-Working without offset-#
#consumer = KafkaConsumer('Target', bootstrap_servers='10.131.48.48:9092',auto_offset_reset='earliest',consumer_timeout_ms=5000)

#-Working with offset, but showing error for [Warning: Consumer group 'TargetG' is rebalancing.]-#
#consumer = KafkaConsumer('Target', bootstrap_servers='10.131.48.48:9092',auto_offset_reset='earliest',group_id='TargetG', enable_auto_commit=True,consumer_timeout_ms=30000)

#-Testing for JSON parsing-#
consumer = KafkaConsumer('Target', bootstrap_servers='10.131.48.48:9092',auto_offset_reset='latest',consumer_timeout_ms=5000, value_deserializer=lambda m: json.loads(m.decode('utf-8')))
###############################################
#-END CONSUMER COMMAND WITH DIFFERENT OPTIONS-#
###############################################

############################################
#-START LOOP TO READ MSG FROM KAFKA TOPICS-#
############################################
for msg in consumer:
    #print (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    data = msg.value
    if len(data) == 4:
        if data['index'] == "email":
            send_email(data['from'],data['to'],data['sub'])
        elif data['index'] == "slack":
            send_slack(data['from'],data['to'],data['sub'])
        else:
            send_unknown()
            
    else:
        send_unknown()
    #print (msg)
##########################################
#-END LOOP TO READ MSG FROM KAFKA TOPICS-#
##########################################

