from azure.servicebus import ServiceBusClient, ServiceBusMessage
from random import randint, choice

# Service bus infomation setting
CONNECTION_STR = "Endpoint=sb://mwmservicebusns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=HcIv7f4bPPSvgQo9HDFWPbN9Ef/0Myu3sXt+CBtgREQ="
TOPIC_NAME = "servicebustopic"

# Create a Service Bus client and then a topic sender object to send messages
# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

# Send if servicebus_client have been created
with servicebus_client:
    # get a Topic Sender object to send messages to the topic
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:

        for i in range(8):
            # msg = ServiceBusMessage('Msg {0}'.format(i).encode('utf-8'), custom_properties={'StoreId':i})
            # msg = ServiceBusMessage('Msg {0}'.format(i).encode('utf-8'), custom_properties={'storeId':'Store%d' % (i)})
            # sender.send_messages(msg)
            price = randint(0,10000)
            location_list = ["Kaoshiung","Taipei","Taichung"]
            location = choice(location_list)
            props = {'StoreId':'Store%d' % i,
                    'location': location,
                    'price': price,
                    'quote_message': "Hello World"}
            msg = ServiceBusMessage(b'message %d with properties' % i, application_properties=props)
            sender.send_messages(msg)
            # print ("Send Msg %d of data 'StoreId':'Store%d'" % (i,i))
            # print (msg)


print("Done sending messages")
print("-----------------------")

# Recieve msg for subscription
# Receive msg if servicebus_client have been created
SUBSCRIPTION_NAME = "S1"
print("Showing details of Subscription - " + SUBSCRIPTION_NAME)
with servicebus_client:
    # get the Subscription Receiver object for the subscription
    receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME, max_wait_time=10)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg.application_properties))
            # complete the message so that the message is removed from the subscription
            receiver.complete_message(msg)

SUBSCRIPTION_NAME = "S2"
print("Showing details of Subscription - " + SUBSCRIPTION_NAME)
with servicebus_client:
    # get the Subscription Receiver object for the subscription
    receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME, max_wait_time=10)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg.application_properties))
            # complete the message so that the message is removed from the subscription
            receiver.complete_message(msg)

SUBSCRIPTION_NAME = "S3"
print("Showing details of Subscription - " + SUBSCRIPTION_NAME)
with servicebus_client:
    # get the Subscription Receiver object for the subscription
    receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME, max_wait_time=10)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg.application_properties))
            # complete the message so that the message is removed from the subscription
            receiver.complete_message(msg)
