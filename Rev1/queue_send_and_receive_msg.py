from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Service bus infomation setting
CONNECTION_STR = "Endpoint=sb://mwmservicebusns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=HcIv7f4bPPSvgQo9HDFWPbN9Ef/0Myu3sXt+CBtgREQ="
QUEUE_NAME = "servicebusqueue"

# Add a method to send a single message
def send_single_message(sender):
    # create a Service Bus message
    message = ServiceBusMessage("Single Message")
    # send the message to the queue
    sender.send_messages(message)
    print("Sent a single message")

# Add a method to send a list of messages
def send_a_list_of_messages(sender):
    # create a list of messages
    messages = [ServiceBusMessage("Message in list") for _ in range(5)]
    # send the list of messages to the queue
    sender.send_messages(messages)
    print("Sent a list of 5 messages")

def send_batch_message(sender):
    batch_message = sender.create_message_batch()
    # add message to bratch_message
    for _ in range(10):
        try:
            batch_message.add_message(ServiceBusMessage("Message inside a ServiceBusMessageBatch"))
        except ValueError:
            # ServiceBusMessageBatch object reaches max_size.
            # New ServiceBusMessageBatch object can be created here to send more data.
            break
    # send out
    sender.send_messages(batch_message)
    print("Sent a batch of 10 messages")

# Create service client
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

# Send message if servicebus_client exist
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        send_single_message(sender)
        send_a_list_of_messages(sender)
        send_batch_message(sender)

print("Done sending messages")
print("-----------------------")


# Receive message if service_bus exist
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg))
            receiver.complete_message(msg)