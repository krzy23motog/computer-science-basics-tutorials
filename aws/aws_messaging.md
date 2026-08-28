# Table of Contents
- [Event-driven architecture in AWS](#EventDrivenAws)
  - [SQS](#SQS)
  - [SNS](#SNS)

# Event-driven architecture on aws <a id="EventDrivenAws"></a>

__design__: event storming -> ( command (play video), query, event (video uploaded) ) -> services -> add communication patterns (queue, pub-sub (kafka, event-bridge), streaming) -> workflows (step functions)

__pros__: decoupled, scalaility, extensibility,  

__issues__ with data in event: need more data (enrich), sensitive data (encrypt), large messages, 

__event schema__

__cross-domain events__ (boundaries)

__standards__: timestamp, corelationId, domain name, 

__discoverability__: schema registry, 

## SQS  <a id="SQS"></a>

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.

Benefits:
- __Security__ – You control who can send messages to and receive messages from an Amazon SQS queue. 
You can encrypt Amazon SQS messages with managed server-side encryption (SSE), or by using custom SSE keys managed in AWS Key Management Service (AWS KMS).
- __Durability__ – For the safety of your messages, Amazon SQS stores them on multiple servers. Standard queues support at-least-once message delivery, and FIFO queues support exactly-once message processing and high-throughput mode.
- __Availability__ – Amazon SQS uses redundant infrastructure to provide highly-concurrent access to messages and high availability for producing and consuming messages.
- __Scalability__ – Amazon SQS can process each buffered request independently, scaling transparently to handle any load increases or spikes without any provisioning instructions.
- __Reliability__ – Amazon SQS locks your messages during processing, so that multiple producers can send and multiple consumers can receive messages at the same time.

Queue Types:
- standard
  - Unlimited throughput: very high, nearly unlimited number of API calls per second
  - At-least-once delivery
  - Best-effort ordering
  - Durability and redundancy – Standard queues ensure high durability by storing multiple copies of each message across multiple AWS Availability Zones. 
  - Visibility timeout – Amazon SQS allows you to configure a visibility timeout to control how long a message stays hidden after being received, ensuring that other consumers do not process the message until it has been fully handled or the timeout expires.
  - If a message is not deleted by the consumer, it stays in the queue until this period expires. You can configure from 60 seconds (1 minute) to 14 days (336 hours)
- FIFO
  - High throughput – When you use batching, FIFO queues process up to 3,000 messages per second per API method ( 300 API calls/s * batch of 10 message)
  - Exactly-once processing – FIFO queues deliver each message once and keep it available until you process and delete it.
  - First-in-first-out delivery – FIFO queues ensure that you receive messages in the order
  - Key terms:
    - Message deduplication ID: A token used in Amazon SQS FIFO queues to uniquely identify messages and prevent duplication. If multiple messages with the same deduplication ID are sent within a 5 minute deduplication interval, they are treated as duplicates, and only one copy is delivered. If you don't specify a deduplication ID and content-based deduplication is enabled, Amazon SQS generates a deduplication ID by hashing the message body.
    - Message group ID: The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are always processed one by one, in a strict order relative to the message group
      - By using Message Group IDs, SQS can maintain strict ordering for each group, while still allowing high throughput across multiple groups.
    - Sequence number: The large, non-consecutive number that Amazon SQS assigns to each message
    - Sending messages: messages are ordered based on message group ID. If multiple hosts (or different threads on the same host) send messages with the same message group ID to a FIFO queue, Amazon SQS stores the messages in the order in which they arrive for processing.
    - Receiving a message: You can't request to receive messages with a specific message group ID. When receiving messages from a FIFO queue with multiple message group ID
    - FIFO queues allow the producer or consumer to attempt multiple retries: SendMessage or ReceiveMessage

Dead Letter queues: 
- Amazon SQS supports dead-letter queues (DLQs), which source queues can target for messages that are not processed successfully. 
- For optimal performance, it is a best practice to keep the source queue and DLQ within the same AWS account and Region
- You can Move messages out of the dead-letter queue using dead-letter queue redrive.
  - __Redrive__ is the process of moving messages from a DLQ back to the source queue or another queue after fixing the underlying problem.
- Amazon SQS does not create the dead-letter queue automatically. You must first create the queue before using it as a dead-letter queue. 
- The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.
- Use a redrive policy to specify the maxReceiveCount. The maxReceiveCount is the number of times a consumer can receive a message from a source queue before it is moved to a dead-letter queue. For example, if the maxReceiveCount is set to a low value such as 1, one failure to receive a message would cause the message to move to the dead-letter queue.
- When a message is moved to a dead-letter queue, the enqueue timestamp is unchanged

SQS short and long polling:
- Short polling (default) – The ReceiveMessage request queries a subset of servers (based on a weighted random distribution) to find available messages and sends an immediate response, even if no messages are found.
- Long polling – ReceiveMessage queries all servers for messages, sending a response once at least one message is available, up to the specified maximum. An empty response is sent only if the polling wait time expires. This option can reduce the number of empty responses and potentially lower costs.
  Long polling helps reduce the cost of using Amazon SQS by eliminating the number of empty responses (when there are no messages available for a ReceiveMessage request) and false empty responses (when messages are available but aren't included in a response).

Short polling occurs when the WaitTimeSeconds parameter of a ReceiveMessage request is set to 0 in one of two ways:
- The ReceiveMessage call sets WaitTimeSeconds to 0.
- The ReceiveMessage call doesn’t set WaitTimeSeconds, but the queue attribute ReceiveMessageWaitTimeSeconds is set to 0.

SQS visibility timeout:
- When a consumer receives a message from an Amazon SQS queue, the message remains in the queue but becomes temporarily invisible to other consumers. This temporary invisibility is controlled by the visibility timeout, a mechanism that prevents other consumers from processing the same message while it is being worked on. Amazon SQS does not automatically delete the message; instead, the consumer must explicitly delete the message using the DeleteMessage action after it has been successfully processed
- If the consumer fails to delete the message before the visibility timeout expires, the message becomes visible again in the queue and can be retrieved by another consumer.
- SQS queue has a default visibility timeout of 30 seconds,

In flight messages:
- in-flight messages are those that have been received from a queue by a consumer but have not yet been deleted.
- To manage in-flight messages effectively:
  - Prompt deletion – Ensure that messages are deleted as soon as they are successfully processed
  - Monitor with CloudWatch – Use Amazon CloudWatch to monitor the number of in-flight messages
  - Distribute load – Consider increasing the number of queues if you are processing a high volume of messages

## SNS <a id="SNS"></a>

https://docs.aws.amazon.com/sns/latest/dg/welcome.html

Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers). Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel. Clients can subscribe to the SNS topic and receive published messages using a supported endpoint type, such as Amazon Data Firehose, Amazon SQS, AWS Lambda, HTTP, email, etc.

Use cases:
- __Application-to-application__ messaging (Amazon Data Firehose delivery streams, Lambda functions, Amazon SQS queues, HTTP/S endpoint)
- __Application-to-person__ notifications (mobile applications, mobile phone numbers, and email addresses)

__Standard and FIFO topics__: FIFO topics ensure strict message ordering, message grouping, and deduplication, allowing FIFO and standard queues to subscribe for message processing. Standard topics are used when message ordering and possible duplication are not critical, supporting all delivery protocols for broader use cases.

__Message durability__: Amazon SNS uses a number of strategies that work together to provide message durability:
- Published messages are stored across multiple, geographically separated servers and data centers.
- If a subscribed endpoint isn't available, Amazon SNS runs a delivery retry policy.
- To preserve any messages that aren't delivered before the delivery retry policy ends, you can create a dead-letter queue.

__Message archiving, replay, and analytics__: subscribing Firehose delivery streams to SNS topics, and later send notifications to Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift tables, and more.

__Message attributes__ let you provide any arbitrary metadata about the message.

__Message filtering__: By default, each subscriber receives every message published to the topic. To receive a subset of the messages, a subscriber must assign a filter policy to the topic subscription. A subscriber can also define the filter policy scope to enable __payload-based__ or __attribute-based__ filtering.

__Message security__: Server-side encryption protects the contents of messages that are stored in Amazon SNS topics, using __encryption keys provided by AWS KMS__

__Typical SNS scenario__ = __Fanout scenario__ is when a message published to an SNS topic is replicated and pushed to multiple endpoints, such as Firehose delivery streams, Amazon SQS queues, HTTP(S) endpoints, and Lambda functions. This allows for parallel asynchronous processing
```
Publisher -> SNS topic -> SQS_1 -> EC2_1
                       -> SES_2 -> EC2_2
```

### SNS event sources

- __Amazon Athena__: Receive notifications when control limits are exceeded like: If the aggregate amount of data scanned exceeds the threshold, you can push a notification to an Amazon SNS topic
- __AWS Data Pipeline__: Receive notifications about the status of pipeline components and send SNS Alarms
- __Amazon Redshift__: Receive notifications of Amazon Redshift events like: The Amazon Redshift cluster did not succeed while acquiring capacity from our capacity pool.
- __Amazon EventBridge__: Receive notifications of EventBridge events. 
- __AWS Step Functions__: Receive notification of Step Functions events
- __AWS Billing and Cost Management__: Receive budget notifications, price change notifications, and anomaly alerts.
- __Amazon EC2 Auto Scaling__ : Receive notifications when Auto Scaling launches or terminates Amazon EC2 instances in your Auto Scaling group
- __AWS Lambda__: Receive function output data by setting an SNS topic as a Lambda dead-letter queue or a Lambda destination.

### SNS event destinations
- __Amazon Data Firehose__: Deliver events to delivery streams for archiving and analysis purposes. Through delivery streams, you can deliver events to AWS destinations like Amazon Simple Storage Service (Amazon S3), Amazon Redshift, and Amazon OpenSearch Service
- __AWS Lambda__: Deliver events to functions for triggering the execution of custom business logic.
- __Amazon SQS:__ Deliver events to queues for application integration purposes.
- __HTTPS__: Deliver events to external webhooks
- SMS
- EMAIL
etc.

### Concepts

- __SNS topic__ is a logical access point that acts as a communication channel. A topic lets you group multiple endpoints (such as AWS Lambda, Amazon SQS, HTTP/S, or an email address).
- __subscriptions__: To receive messages published to a topic, you must subscribe an endpoint to the topic. When you subscribe an endpoint to a topic, the endpoint begins to receive messages published to the associated topic.
  - create subscription
  - select Topic ARN
  - select protocol
  - enter endpoint

### FIFO topics

You can use Amazon SNS FIFO (first in, first out) topics with Amazon SQS FIFO queues to provide strict __message ordering__ and message __deduplication__.

Amazon SNS FIFO topics define ordering in the context of a __message group__

The FIFO capabilities of each of these services work together to act as a fully managed service to integrate distributed applications that require __data consistency in near-real time.__

An Amazon SNS FIFO topic always delivers messages to subscribed Amazon SQS queues in the exact order in which the messages are published to the topic, and only once. 
With an Amazon SQS FIFO queue subscribed, the consumer of the queue receives the messages in the exact order in which the messages are delivered to the queue, and no duplicates.

You can have multiple applications (or multiple threads within the same application) publishing messages to an SNS FIFO topic in parallel. 
When you do this, you effectively delegate message sequencing to the Amazon SNS service.

The __sequence number__ is a large, non-consecutive number that Amazon SNS assigns to each message. 
The length of the sequence number is 128-bits, and continues to __increase for each Message Group__. 
The __sequence number is passed to the subscribed Amazon SQS queues as part of the message body__. 
However, if you enable raw message delivery, the message that's delivered to the Amazon SQS queue doesn't include the sequence number or any other Amazon SNS message metadata.

#### Message grouping

Messages that belong to the same group are processed one by one, in a strict order relative to the group.

When you publish messages to an Amazon SNS FIFO topic, you set the message group ID. 
The __group ID is a mandatory token__ that specifies that a message belongs to a specific message group. 
The __SNS FIFO topic passes the group ID to the subscribed Amazon SQS FIFO queues__. 
There is no limit to the number of group IDs in SNS FIFO topics or SQS FIFO queues. __Message group ID is not passed to Amazon SQS standard queues__.

There's no affinity between a message group and a subscription. Therefore, messages that are published to any message group are delivered to all subscribed queues, subject to any filter policies 

Amazon SNS FIFO topics deliver messages from __different message groups in parallel__, while message order is strictly maintained within each message group. 
Each individual message group can deliver a maximum of 300 messages per second. 

#### Filtering

When you subscribe an Amazon SQS FIFO or standard queue to an SNS FIFO topic, you can use message filtering to specify that the subscriber receives a subset of messages, rather than all of them. 
__Each subscriber can set its own filter policy__ as subscription attributes. 
Based on the filter policy scope, __filter policy is matched against incoming message-attributes or message-body__.

The filter policy {"business":["wholesale"]} matches every message which contains a key named business and with wholesale in the set of values

#### Message deduplication

__Amazon SNS FIFO topics and Amazon SQS FIFO queues support message deduplication__, which provides exactly-once message delivery and processing as long as the following __conditions__ are met:
- The subscribed Amazon SQS FIFO queue exists and has permissions that allow the Amazon SNS service principal to deliver messages to the queue.
- The Amazon SQS FIFO queue consumer processes the message and __deletes it from the queue before the visibility timeout expires__.
- The Amazon SNS subscription topic has __no message filtering.__
- There are __no network disruptions__ that prevent acknowledgment of the message delivery.

When you publish a message to an Amazon SNS FIFO topic, the message must include a __deduplication ID__. 
This ID is included in the message that the Amazon SNS FIFO topic delivers to the subscribed Amazon SQS FIFO queues.

If a message with a particular deduplication ID is successfully published to an Amazon SNS FIFO topic, any message published with the same deduplication ID, 
within the five-minute deduplication interval, is accepted but not delivered

If the __message body__ is guaranteed to be unique for each published message, you can enable __content-based deduplication__ for an Amazon SNS FIFO topic and the subscribed Amazon SQS FIFO queues. 
Amazon SNS uses the message body to generate a unique hash value to use as the deduplication ID for each message, so you don't need to set a deduplication ID when you send each message.

#### Message security

You can choose to have Amazon SNS and Amazon SQS __encrypt__ messages sent to FIFO topics and queues, using AWS Key Management Service (AWS KMS)

Amazon SNS and Amazon SQS __encrypt only the body of the message__. They don't encrypt the message attributes, resource metadata, or resource metrics.

In addition, SNS FIFO topics and SQS FIFO queues support message privacy with interface VPC endpoints powered by AWS PrivateLink. 
Using __interface endpoints__, you can send messages from Amazon Virtual Private Cloud (Amazon VPC) subnets to FIFO topics and queues without traversing the public internet.

#### Message durability

Amazon SNS FIFO topics and Amazon SQS queues are __durable__. 
Both resource types store messages redundantly across __multiple Availability Zones__, and __provide dead-letter queues__ to handle exceptional cases.

In Amazon SNS, message delivery fails when the Amazon SNS topic can't access a subscribed Amazon SQS queue due to a client-side or server-side error:
- Client-side errors occur when the Amazon SNS FIFO topic has stale __subscription metadata__
  - Deletes the queue or changes queue policy
  - Changes the queue policy in a way that prevents the Amazon SNS service principal from delivering messages to it.
  - __Amazon SNS doesn't retry delivering messages that failed due to client-side errors__.
- Server-side errors can occur in these situations:
  - The Amazon SQS service is unavailable
  - Amazon SQS fails to process a valid request from the Amazon SNS service
  - When server-side errors occur, Amazon SNS FIFO topics retry the failed deliveries up to 100,015 times over 23 days. 

Dead letter queue:
- For any type of error, Amazon SNS can sideline messages to Amazon SQS dead-letter queues so data isn't lost.
- The dead-letter queue associated with an Amazon SNS subscription must be an Amazon SQS queue of the same type as the subscribing queue

#### Message replay

Message archiving provides the ability to archive a single copy of all messages published to your topic. 
You can __store published messages within your topic by enabling the message archive__ policy on the topic, which enables message archiving for all subscriptions linked to that topic. 
Messages can be archived for a minimum of one day to a maximum of 365 days.

Amazon SNS replay lets topic subscribers retrieve archived messages from the topic data store and redeliver (or replay) them to a subscribed endpoint. 
Messages can be replayed as soon as the subscription is created. 
A replayed message has the same content, MessageId, and Timestamp as the original copy, and also contains the attribute Replayed, to help you identify that it's a replayed message. 

### SNS message publishing

To publish a SNS message:
- message details:
  - Subject - optional
  - Message group ID - required for FIFO topic
  - Message deduplication ID - for FIFO topic. Optional else Content-based message deduplication 
  - Time to Live (TTL) - optional for mobile push
- message body:
  - Choose Identical payload for all delivery protocols, and then enter a message.
  - Custom payload for each delivery protocol, and then enter a JSON object to define the message to send for each delivery protocol.
- Message attributes: add any attributes that you want Amazon SNS to match with the subscription attribute FilterPolicy
  - For Type, choose an attribute type, such as String.Array.
  - Name, such as customer_interests.
  - Value, such as ["soccer", "rugby", "hockey"].

Message size: current maximum of 256 KB

__Batching__:An alternative to publishing messages to either Standard or FIFO topics in individual Publish API requests, is using the Amazon SNS PublishBatch API to publish up to 10 messages in a single API request. 
Sending messages in batches can help you reduce the cost. API request needs to be assigned a unique batch ID

For SQS subscriptions, a maximum of 10 message attributes can be sent when Raw Message Delivery is enabled. To send more than 10 message attributes, Raw Message Delivery must be disabled.

### Message data protection 

Scans data in motion for personally identifiable information (PII) and protected health information (PHI) using data identifiers.

Message data protection supports the following actions to help protect sensitive customer information:
- Audit – Audit up to 99% of the data that's published to an Amazon SNS topic. You can then choose to send the findings to Amazon CloudWatch, Amazon S3, or Amazon Data Firehose.
- De-identify – Mask or redact sensitive data without interrupting message publishing or delivering.
- Deny – Block the transmission of data between applications and AWS resources if sensitive data is present within the payload.

### Message delivery

#### RAW message delivery

- When you enable raw message delivery for Amazon Data Firehose or Amazon SQS endpoints, any Amazon __SNS metadata is stripped from the published message__ and the message is sent as is.
- When you enable raw message delivery for HTTP/S endpoints, the HTTP header x-amz-sns-rawdelivery with its value set to true is added to the message, indicating that the message has been published without JSON formatting.

#### Cross account delivery

To let the queue owner subscribe to the topic owner's topic, the topic owner must give the queue owner's account permission to call the Subscribe action on the topic

#### Cross region delivery

Amazon SNS supports the cross-region delivery of notifications to Amazon SQS queues and to AWS Lambda functions

#### Message Delivery status

Amazon SNS provides support to log the delivery status of notification messages sent to topic

After you configure the message delivery status attributes, log entries are sent to CloudWatch Logs for messages sent to topic subscribers. 
Logging message delivery status helps provide better operational insight, such as the following:
- Knowing whether a message was delivered to the Amazon SNS endpoint.
- Identifying the response sent from the Amazon SNS endpoint to Amazon SNS.

#### Message Delivery retries

Amazon SNS defines a delivery policy for each delivery protocol. 
The delivery policy defines how Amazon SNS retries the delivery of messages when server-side errors occur (when the system that hosts the subscribed endpoint becomes unavailable). 
When the delivery policy is exhausted, Amazon SNS stops retrying the delivery and discards the message—unless a dead-letter queue is attached to the subscription

Phases:
- Immediate re-try (3 times)
- pre-backoff phase (2 times, 1 s apart)
- backoff phase: 10 times, with exponential backoff, from 1 second to 20 seconds
- Post-backoff phase: 100,000 times, 20 seconds apart






