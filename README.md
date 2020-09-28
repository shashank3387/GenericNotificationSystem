# Generic Notification System

Problem Statement 
Most applications have the need to implement notifications for a variety of use cases and scenarios. Create a centralized generic service for notification that can be used by a variety consuming application for their notification needs e.g. an incident workflow system may use this system when each incident ticket moves from one state to another, similarly a order management system may use this service to notify the customer of the status of the order whenever it changes 
 
The system should allow for the following capabilities: 
 
1.	Accept messages including from, to and subject 
2.	Ability to notify on multiple channels (e.g email, slack, you can stub out/mock if required) 
3.	Deliver messages in correct order for each consumer of this  
 
Deliverables 
1.	The code for the service in github with instructions on how to set it up and run it 
****************************

Solution
Using Apache Kafka and Python-kafka to design Notification system.

Installation
 Apache Kafka -
 $useradd kafka -m
 $passwd kafka
 $usermod -aG wheel kafka
 $su -l kafka
 $mkdir ~/Downloads
 $tar -xvzf ~/Downloads/kafka-2.6.0-src.tgz --strip 1
 $vi ~/kafka/config/server.properties
  -> Add - delete.topic.enable = true
 
 Add service to start stop
 $sudo vi /etc/systemd/system/zookeeper.service
  ->
  [Unit]
  Requires=network.target remote-fs.target
  After=network.target remote-fs.target

  [Service]
  Type=simple
  User=kafka
  ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties
  ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
  Restart=on-abnormal

  [Install]
  WantedBy=multi-user.target
  
 $sudo vi /etc/systemd/system/kafka.service
  ->
  [Unit]
  Requires=zookeeper.service
  After=zookeeper.service

  [Service]
  Type=simple
  User=kafka
  ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties > /home/kafka/kafka/kafka.log 2>&1'
  ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
  Restart=on-abnormal

  [Install]
  WantedBy=multi-user.target
  
 Start
 $sudo systemctl start kafka
 To ensure that the server has started successfully, check the journal logs for the kafka unit:
 $journalctl -u kafka 

 You now have a Kafka server listening on port 9092
 To enable kafka on server boot, run:
 $sudo systemctl enable kafka
 
 First, create a topic named Target by typing:
 $~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Target
  -> Created topic Target.
 
 You can create a producer from the command line using the kafka-console-producer.sh script. It expects the Kafka server’s hostname, port, and a topic name as arguments.
 Publish the string "Hello, World" to the Target topic by typing:
 $echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic Target > /dev/null
 
 Next, you can create a Kafka consumer using the kafka-console-consumer.sh script. It expects the ZooKeeper server’s hostname and port, along with a topic name as arguments.
 The following command consumes messages from TutorialTopic. Note the use of the --from-beginning flag, which allows the consumption of messages that were published before
 the consumer was started:
 $~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Target --from-beginning
 
 Describe Topic
 $~/kafka1/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group=TargetG --describe
 

 Install kafka-python -
 $pip install kafka-python



