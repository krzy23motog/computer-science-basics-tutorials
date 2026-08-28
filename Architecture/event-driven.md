# Table of Contents
- [What is an Event-Driven Architecture?](#Whatis)
  - [Benefits of an event-driven architecture](#Benefits)
  - [Quotes](#Quotes)
- [Considerations](#Considerations)
- [Design](#Design)
- [Patterns of Event driven architecture](#Patterns)
  - [Event Generation](#EventGeneraton)
  - [Event Communication](#EventCommunication)
  - [Event Consumption](#EventConsumption)
  - [Consumer Scalability](#ConsumerScalability)
  - [Deployment Architecture Patterns](#EventDeployment)
  - [Error Handling Patterns](#EventError)
  - [Governance Patterns](#EventGovernance)
  - [Migration Patterns](#EventMigration)
- [EDA - specifications](#EDASpecification)
  - [AsyncAPI spec](#AsyncAPI)
  - [CloudEvents](#CloudEvents)
  - [Serverless Workflow specification](#ServerlessWorkflow)
  - [Event Catalog](#EventCatalog)
  <a id="Considerations"></a>
- [Examples / Use Cases](#EDAExamples)
- [References](#References)


# What is an Event-Driven Architecture? <a id="Whatis"></a>

https://aws.amazon.com/event-driven-architecture/

An event-driven architecture uses events to trigger and communicate between decoupled services and is common in modern applications built with microservices. 
An event is a change in state, or an update, like an item being placed in a shopping cart on an e-commerce website.

Events can either carry the state (the item purchased, its price, and a delivery address) or events can be identifiers (a notification that an order was shipped).

Event-driven architectures have three key components: event producers, event routers or brokers, and event consumers. 
A producer publishes an event to the router, which filters and pushes the events to consumers. 
Producer services and consumer services are decoupled, which allows them to be scaled, updated, and deployed independently.

Event-driven architecture is a way of building enterprise IT systems that lets information flow between applications, microservices, and connected devices in a real-time manner as events occur throughout the business.

Event-driven architecture ensures that when an event occurs, information about that event is sent to all of the systems and people that need it

## Benefits of an event-driven architecture  <a id="Benefits"></a>

- __Scale__ and fail independently
- Develop with __agility__:  the event router will automatically filter and push events to consumers. The router also removes the need for heavy coordination between producer and consumer services
- __Cut costs__: Event-driven architectures are push-based, so everything happens on-demand as the event presents itself in the router. This way, you’re not paying for continuous polling to check for an event. This means less network bandwidth consumption, less CPU utilization, less idle fleet capacity, and less SSL/TLS handshakes.
- improved __responsiveness__, scalability, and agility. Being able to react to real-time information and being able to add new services and analytics quickly and easily, considerably enhances business processes and customer experience.
- __easy to evolve__

When to use it:
- Cross-account, cross-region data replication
- Fanout and __parallel processing__
- Resource state monitoring and alerting: Rather than continuously checking on your resources, you can use an event-driven architecture to monitor and receive alerts on any anomalies, changes, and updates. 
- __Integration__ of heterogeneous systems: If you have systems running on different stacks, you can use an event-driven architecture to share information between them without coupling
- Integrating applications
- Sharing and democratizing data across applications
- Event-enabling microservices

To set yourself up for success, consider the following:
- The durability of your event source. Your event source should be reliable and guarantee delivery if you need to process every single event. 
- Your performance control requirements. Your application should be able to handle the asynchronous nature of event routers. 
- Your event flow tracking. The indirection introduced by an event-driven architecture allows for dynamic tracking via monitoring services, but not static tracking via code analysis. 
- The data in your event source. If you need to rebuild state, your event source should be deduplicated and ordered.

## Nice quotes  <a id="Quotes"></a>

Event driven systems are __easy to evolve__

Event driven systems are __composable__

Workflows enable us to build applications from loosely coupled components (aws step functions or aws event bridge)

Use serverless components to stich together to get overall system you want.

# Considerations <a id="Considerations"></a>

- Eventual consistency: 
- Variable latency: Workloads that require consistent low-latency performance are not good candidates for event-driven architectures
- synchronous is fast 
- synchronous is fail fast

# Design <a id="Design"></a>

- Identifying events with event storming
- Event naming conventions
- Bounded context mappings: Patterns to help when consuming events
- Services can be consumers and producers of events

| Service                       | Event
|-------------------------------|-------------------
| ShoppingCart  --creates-->    | OrderRequested
| PaymentService <--receives--  | OrderRequested
| PaymentService --creates-->   | PaymentProcessed
| OrdersService <--receives--   | PaymentProcessed
| OrdersService --creates-->    | OrderConfirmed
| ShippingService <--receives-- | OrderConfirmed
| ShippingService --creates-->  | ShipmentPrepared
| ShippingService <--receives-- | ShipmentPrepared
| ShippingService --creates-->  | ShipmentDispatched
| ShippingService <--receives-- | ShipmentDispatched
| ShippingService --creates-->  | ShipmentDelivered
| OrdersService <--receives--   | ShipmentDelivered
| OrdersService --creates-->    | OrderCompleted

- easy extendable: we can add invoice service or emailnotification service

| Service                                | Event
|----------------------------------------|-------------------
| EmailNotificationService <--receives-- | ShipmentDispatched
| InvoiceService <--receives--           | ShipmentDispatched

# Patterns of Event driven architecture <a id="Patterns"></a>

https://solace.com/event-driven-architecture-patterns/

## Event generation patterns  <a id="EventGeneraton"></a>

### Event Carried State Transfer

Utilizes events as a mechanism for state propagation, rather than relying on synchronous request/response protocols

Each service can subscribe to the events that it is interested in and update its own local state accordingly. 
It also provides a mechanism for maintaining a consistent view of the system’s state. 
By propagating events to all interested parties, services can ensure that they have the most up-to-date view of the system’s state.

### Command Query Response Segregation (CQRS)

It separates the processing of commands from the processing of queries. 
In this pattern, commands are used to modify the state of an application while queries are used to retrieve the state of the application. 
The separation allows for the creation of dedicated components optimized for each operation.

### Change Data Capture (CDC)

capture and process changes made to a database. 
The CDC pattern is used to track changes to a source database and transform them into a format that can be easily consumed by downstream systems such as data warehouses, data lakes, and streaming applications.

### Event Sourcing

It  involves capturing all changes to an application’s state as a sequence of events, rather than just the current state. 
This sequence of events is used to build and rebuild the state of the application, making it an essential pattern for systems that require auditability and replayability.

## Communication patterns <a id="EventCommunication"></a>

Enabling communication and data exchange between different components and services within a distributed system

### Point-to-Point

If you need to deliver a message to a specific recipient, the publish-subscribe mode isn’t necessary. 
In such cases, the point-to-point message exchange pattern is used to deliver the message to a single recipient in what’s called a “one-to-one” exchange. 
It is also possible that several senders send messages to the same recipient, a “many-to-one” exchange. In these situations, the endpoint typically takes the form of a named queue.

### Publish-Subscribe

Publish-subscribe is a communication pattern that decouples applications by having them publish messages to an intermediary broker rather than communicating directly with consumers (as in point-to-point). 
This approach introduces an asynchronous mode of communication between publishers and subscribers, offering increased scalability, improved reliability, and the ability to defer processing with the use of a queue on the broker.

The publishers and consumers do not have any knowledge of each other; they simply produce or receive the events. 
The event broker, which may take the form of middleware software, an appliance, or a SaaS deployed in any environment, facilitates and distributes events as they occur, pushing them to consumers that may be located in a variety of environments (such as on-premises or public/private clouds).

### Request-Reply

A request-reply pattern is necessary when your goal is specifically to get a response from the recipient. 
This pattern ensures that the consumer sends a response to each consumed message, with the implementation varying from the use of a return address to sending a response to a separate endpoint.

### Event Streaming

Allows for the continuous delivery of events to interested parties. 
It is often used in event-driven architecture to decouple applications and services and to enable real-time processing of events. 
In this pattern, data is continuously ingested from various sources and streamed in real-time, enabling the ability to build instant insights and take immediate actions.

### Choreography 

Choreography achieves communication without tight control.

Communication __between bounded contexts__ is often where choreography can be most effective.
With choreography, producers don’t have expectations of how and when the event will be processed. 
They are only responsible for sending events to an event ingestion service and adhering to the schema. 
This reduces dependencies between the two bounded contexts.

Event buses, such as EventBridge, can be used for choreography.

### Orchestration

In orchestration, communication is more tightly controlled. A central service coordinates the interaction and order in which services are invoked.

__Often within a bounded context__, you need to __control the sequence of service integration__, maintain state, and handle errors and retries. 
These use cases are well suited for orchestration.

Workflow orchestration services like AWS Step Functions or Amazon Managed Workflows for Apache Airflow (Amazon MWAA) can help build for orchestration.

Together, choreography and orchestration give you the flexibility to address different needs in your domain-driven designs

## Event consumption patterns <a id="EventConsumption"></a>

strategies and techniques for consuming and processing events generated within the system

### Hierarchical Topics

A topic is a fundamental concept in event-driven architecture that allows events to be categorized and routed to interested consumers. 
However, the way topics are implemented varies between different event brokers.

Some brokers offer a flat topic structure, while others provide a hierarchical structure. 
Additionally, some brokers use partitioning to improve scalability and ensure related events are routed to the same partition. 
A hierarchical topic structure with wildcard subscriptions allows for more granular control over topic subscription and filtering, enabling consumers to receive only the events they are interested in.

### Event Filtering

Event filtering is a pattern that allows consumers to specify a set of rules to determine which events they will receive based on the event metadata or payload. 
This pattern is closely related to stream querying, but it applies specifically when a consumer uses an expression to decide which events to receive.

### Guaranteed Delivery

It focuses on ensuring the reliable and consistent delivery of events. 
In event-driven architecture, events represent significant occurrences or state changes within a system and are asynchronously communicated to components or services interested in them.

In distributed systems, it is vital to guarantee that events reach their intended recipients reliably, even in the presence of failures, network issues, or disruptions. 
The Guaranteed Delivery pattern addresses this requirement by introducing mechanisms that prevent event loss or omission during transmission.

By __persisting__ events, the system ensures they are durable and can be recovered in case of failures or disruptions. 
__Acknowledgments__ provide feedback to the sender, confirming successful event delivery. Delivery retry mechanisms allow for the retransmission of events in case of failures, with an approach that can optionally increase the time between attempts. 
__Idempotency__ ensures that processing the same event multiple times yields the same outcome as processing it once.

### Backpressure and Push

Backpressure and push is an event-driven architecture pattern that deals with managing the flow of data between systems or components with different processing speeds. 
It is designed to prevent data loss or degradation due to overload.

To avoid this problem, the backpressure and push pattern uses a mechanism where the receiver sends a signal back to the sender indicating its readiness to receive more data. 
This signal is called backpressure. When the sender receives this signal, it slows down the rate at which it generates and sends events, allowing the receiver to catch up. 
Once the receiver is ready to process more events, it sends another Backpressure signal to the sender, and the process continues. 

### Exclusive Consumer

The exclusive consumer pattern plays a crucial role in event-driven architectures, particularly in scenarios where the sequence and integrity of message processing are critical. 
This pattern ensures that while multiple consumers are set up for redundancy, only one consumer actively processes messages at any given time. 
This setup prevents message __duplication__ and guarantees that each message is processed in its correct __order__.

## Consumer scalability <a id="ConsumerScalability"></a>

### Competing Consumers

It involves distributing the workload of processing events among multiple consumers to improve throughput and reduce processing time. 
In this pattern, multiple consumers or worker processes are used to process events from a shared event stream or queue in parallel. 

### Consumer Groups

The consumer groups pattern is similar to the competing consumers pattern but with an added layer of abstraction. 
In this pattern, a group of consumers is created to receive messages from a single event stream or message queue. 
Each consumer in the group processes a subset of the events, and the events are load-balanced across the consumers in the group. 
The messaging system ensures that each event is processed by only one consumer in the group.

### Shock Absorber

mitigate the effects of bursty events that can lead to service degradation or failures. 
The pattern involves __introducing a buffer or a queue__ between the event source and the downstream services that consume the events.

By introducing this buffer, the pattern can smooth out the flow of events, ensuring that no service is overwhelmed by a sudden burst of events. 

### Partitioning

It helps to improve scalability, performance, and reliability by distributing events across multiple queue partitions. 
The main idea behind this pattern is to partition a single queue into multiple smaller queues, allowing for higher throughput and reduced latency by processing messages in parallel. 
Each partition can be processed independently, which can increase concurrency and parallelism, thereby increasing the overall processing speed of the event system.

## Deployment Architecture Patterns <a id="EventDeployment"></a>

different strategies and configurations for deploying and organizing the brokers involved in an event-driven system

### Event Bridge

 It involves the use of two interconnected brokers that enable applications and services to send events across the bridge connection. 
 This is achieved through subscriptions set on the bridge, which determine whether an event is allowed to flow across.

By adopting this pattern, each application or service can have its dedicated event broker. 
These brokers can be interconnected in a peer-to-peer manner, forming an ad-hoc network of brokers. 
Additionally, a broker can be part of multiple event bridges.

### Event Mesh

involves creating a network of interconnected event brokers that allow events to be published and consumed across different systems and environments. 
This pattern aims to address the challenges of event-driven architecture at scale, including event routing, discovery, and delivery, by creating a mesh-like network of brokers that can handle these tasks efficiently and reliably.

The event mesh pattern is designed to enable event-driven communication across complex distributed systems, which typically consist of multiple applications, services, and data stores. 
By creating a mesh of interconnected event brokers, this pattern allows events to be published and consumed by any component in the system, regardless of its location or technology stack.

### Event Gateway

It serves as a vital component in connecting and coordinating events between brokers within an event mesh or event bridge, extending its capabilities to edge brokers located outside the mesh. 
Acting as a gateway or entry point for events, it facilitates event routing, transformation, and delivery to the intended recipients on the edge, leveraging subscription settings configured on the gateway.

## Error Handling Patterns  <a id="EventError"></a>

Set of strategies and techniques for managing errors and exceptions that occur within an event-driven system. 
These patterns are designed to handle and recover from errors, ensuring the reliability and resilience of the system

### Dead Letter Queue

It  is used to handle messages that cannot be successfully processed by the system. 
When a message fails to be processed, it is typically routed to a dead letter queue, where it is stored and can be inspected and possibly reprocessed at a later time.

### Discard, Pause and Retry

Used to handle message processing failures. In this pattern, when a message processing error occurs, the message can be handled in one of three ways:
- Discard: The message is simply discarded, and no further action is taken. This option is typically used for non-critical messages that can be safely ignored.
- Pause: The message is temporarily paused and held in a retry buffer until the issue causing the failure is resolved. The message can then be retried and processed again.
- Retry: The message is retried immediately or after a specified delay. If the message processing still fails after a set number of retries, the message is either discarded or paused.

### Saga

To ensure consistent outcomes for an application or process. 
It is often used as an error-handling pattern because it can compensate for errors that occur in an event-driven or streaming application. 
A saga is a sequence of transactions or operations that must occur in the correct order to ensure a specific outcome.

The implementation of the saga pattern can be thought of as building your own transaction coordinator. 
You create a component that observes the transactions executing and, if it detects that something has gone wrong, it can start to execute compensation logic. 
The saga pattern ensures that any errors or failed transactions are handled gracefully, allowing the application to recover without any negative impact on the end-user experience.

By using the saga pattern in event-driven architecture, you can maintain data consistency and ensure that any transactions that occur are executed in the correct order.
This helps to avoid race conditions, data inconsistencies, and other issues that can arise when working with distributed systems.

A saga is a long-running process that is implemented as a series of small, independent transactions. Each transaction updates the state of the system and, if successful, triggers the next transaction in the saga. If any transaction fails, the saga is rolled back to a previous state. This pattern is useful for building applications that need to maintain consistency across multiple systems.

Example: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html

## Governance Patterns  <a id="EventGovernance"></a>

Essential for establishing control over access, management, security and oversight of the event-driven system. 
These patterns focus on establishing guidelines, policies, and frameworks for governing various aspects of the event-driven architecture ecosystem. 
Governance Patterns include topics such as event naming conventions, versioning and compatibility, security and access control, monitoring and auditing, and documentation standards. 
By implementing Governance Patterns, organizations can promote consistency, standardization, and best practices across the event-driven system. 

### Event Catalog

provides a centralized location for documenting business events, making them easier to consume. 
The pattern includes an event developer portal that offers self-service access to information and documentation for published events, similar to how an API Developer Portal works for RESTful APIs.

### Event APIs

It treats events as first-class APIs. Instead of using traditional request-response APIs, the event APIs pattern uses events to communicate between services. 
In this pattern, services publish events that describe the state changes in the system. Other services can then subscribe to these events to stay informed about the changes.

The key benefit of this pattern is that it provides loosely coupled, asynchronous communication between services. 

## Migration Patterns <a id="EventMigration"></a>

transitioning from an existing implementation – a monolith or an event-driven system to another event-driven system or upgrading the existing system while minimizing disruptions and ensuring a smooth migration process

### Strangler

Used to incrementally transition from a monolithic application to a microservices-based architecture in a controlled and gradual manner. 
This pattern involves identifying cohesive areas of functionality within the monolith, extracting them into independent services, and replacing the monolithic functionality with calls to the new services. 
Over time, the monolith is “strangled” as more and more functionality is migrated to the new services until the monolith is fully decommissioned.

### Data Synchronization

ensure the consistent transfer and synchronization of data between different systems or components during the migration process. This serves the need to maintain data integrity and consistency while transitioning from one event-driven system or other software systems like database, mainframe, etc. to event-driven architecture.


# EDA - specifications  <a id="EDASpecification"></a>

## AsyncAPI spec   <a id="AsyncAPI"></a>

https://www.asyncapi.com/en

The AsyncAPI specification addresses this problem by providing a machine-readable specification to document and describe event-driven applications.

It documents the event producers and consumers of an application along with the events they exchange. That provides a single source of truth for the application in terms of control flow. Apart from that, the specification can be used to generate the implementation code and the validation logic.

```
syncapi: 2.0.0
info:
  title: Account Service
  version: '1.0.0'
  description: This service is responsible for managing user accounts in the system.
...

servers:
  production:
    url: mqtt://test.mosquitto.org
    protocol: mqtt
    description: Test MQTT broker

channels:
  user/signedup:
    subscribe:
      operationId: emitUserSignUpEvent
      message:
        $ref : '#/components/messages/UserSignedUp'

components:
  messages:
    UserSignedUp:
      name: userSignedUp
      title: User signed up event
      summary: Inform about a new user registration in the system
      contentType: application/json
      payload:
        $ref: '#/components/schemas/userSignedUpPayload'

  schemas:
    userSignedUpPayload:
      type: object
      properties:
        firstName:
          type: string
          description: "foo"
...
```

## CloudEvents  <a id="CloudEvents"></a>

https://cloudevents.io/

CloudEvents adds meta-data attributes to any given event. For example, a unique ID for the event and the type of the event.

| Attribute Name 	| Type 	    | Note
|-----------------|-----------|------------------
| id 	            | String 	  | Required. The ID of the event. A CloudEvent is uniquely identified with its source and id.
| source 	        | String    | (URI-reference) 	Required. The source of the event.
| specversion     | String 	  | Required. The version of CloudEvents Specification the Cloud Event uses.
| type 	          | String 	  | Required. The type of the event.

## Serverless Workflow specification  <a id="CServerlessWorkflow"></a>

Serverless Workflow is a specification for describing workflows in a standard way. It provides a vendor-neutral and platform-independent markup for orchestrating services on multiple runtimes and cloud/container platforms.

## Event Catalog <a id="EventCatalog"></a>

https://www.eventcatalog.dev/

help people document their EDA applications powered by markdown files and custom plugins.

# AWS step function patterns  <a id="StepFunctionPatterns"></a>

## Request Response

Step Functions will wait for an HTTP response and then progress to the next state.

## Run a Job (.sync)

Step Functions can wait for a request to complete before progressing to the next state

## Wait for a Callback with Task Token

Callback tasks provide a way to pause a workflow until a task token is returned. A task might need to wait for a human approval, integrate with a third party, or call legacy systems.




# Examples / Use Cases  <a id="EDAExamples"></a>

## Retail and eCommerce Example of Event-Driven Architecture

This use case is often seen in retail or media and entertainment websites that need to scale up to handle unpredictable traffic. A customer visits an ecommerce website and places an order.
The order event is sent to an event router, and all the downstream microservices can pick up the order event for processing—for example, submitting the order, authorizing payment, and
sending the order details to a shipping provider. Because each microservice can scale and fail independently, there are no single points of failure. This pattern has helped LEGO scale its
ecommerce website to meet peak Black Friday traffic.

## Application integration

To unlock siloed data, customers build event-driven architectures that ingest SaaS applications events or send events to their SaaS applications.

## Transforming Order Fulfillment with Event-Driven Architecture

https://aws.amazon.com/blogs/apn/transforming-order-fulfillment-with-event-driven-architecture-a-rapid7-success-story/

Goal was a real-time and seamless approach to order fulfillment.

Challenges to be solved:
- Business Challenges: 
  - Unnecessary complexities and potential failure points. 
  - External middleware, as well as the potential for communication breakdowns or failures between the middleware and Salesforce
- Technical Challenges: 
  - Near real-time events while ensuring no data was lost. scalable, robust, and secure architecture 
  - Improving near real-time error visibility
  - Ability to replay events that had been missed during an error situation to avoid data loss

### Solution

#### Order updates flow:

Dead letter queues, implemented throughout the process, capture problematic updates, enabling efficient error handling, reprocessing, alerts
```
Event Bridge -> StepFunction -> Lambba -> External processors: Sales Order, Fullfillment Record, Licensing Record
```

#### Receiving licensing info

The external processor systems, upon completing the order processing, notifies the EventBridge with the necessary licensing information.
After system is notified of the new license changes and updates the platform accordingly, enabling the requested features for the customer’s order.
Once the order fulfillment process is complete, the fulfillment processor creates a success update message and publishes it back to EventBridge,
The final step involves sending a completed record back to the caller
```
External Event -> API Gateway -> EventBridge -> Strp Function -> SNS - Fulfillment Processor -> SNS -> SQS -> Lambda -> EventBridge
```

## Simple Example

```
API Gateway -> /Create_Account -> Event -> Event Bridge -> AccountService
API Gateway -> /Create_Order -> Event -> Event Bridge -> OrdersService -> DynamoDB
``` 

# References <a id="References"></a>

https://serverlessland.com/

https://www.youtube.com/watch?v=RfvL_423a-I

https://learn.microsoft.com/en-us/archive/msdn-magazine/2018/february/azure-event-driven-architecture-in-the-cloud-with-azure-event-grid

