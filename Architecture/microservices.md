# Microservices 


Features of microservices architecture

| Feature                    | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| **Single Responsibility**  | Each service focuses on one business capability or domain.                  |
| **Independent Deployment** | Services can be deployed, updated, and scaled independently.                |
| **Loose Coupling**         | Services communicate over well-defined APIs (usually HTTP/REST or gRPC).    |
| **Decentralized Data**     | Each service owns its own database or datastore.                            |
| **Technology Agnostic**    | Teams can choose different languages, frameworks, or databases per service. |
| **Resilience**             | Failure in one service shouldn't bring down the whole system.               |

## Monolith to Microservices 

### Process
Defining service boundaries is an iterative process. 
Because this process is a non-trivial amount of work, you need to __continuously evaluate the cost of decoupling against the benefits__ that you get. 
Following are factors to help you __evaluate how you approach decoupling a monolith__:
- __Avoid refactoring everything all at once.__ To __prioritize__ service decoupling, evaluate cost versus benefits.
- Start with a __Pilot__ Project
- Find the right candidates for refactoring: Services in a __microservice architecture are organized around business concerns__, and __not technical concerns__.
- When you __incrementally__ migrate services, __configure communication between services and monolith to go through well-defined API contracts__.
- __Anticorruption Layer__:  strategy used to ensure that the transition from monolith to microservices does not corrupt the business logic of your system. 
- Implement __API Gateways__ or events
The ACL acts as a barrier between the monolith and the microservices, converting data and requests between the two systems.
- Microservices require much more __automation__: think in advance about __continuous integration (CI), continuous deployment (CD), central logging, and monitoring__.
- Instrument for end-to-end __observability__

#### Decouple by domain-driven design

https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths

Microservices should be designed around business capabilities, not horizontal layers such as data access or messaging.

Microservices are loosely coupled if you can change one service without requiring other services to be updated at the same time.

Domain-driven design (DDD) requires a good understanding of the domain for which the application is written. The necessary domain knowledge to create the application resides within the people who understand it—the domain experts.

You can apply the DDD approach retroactively to an existing application as follows:
- Identify a ubiquitous language—a common vocabulary that is shared between all stakeholders. As a developer, it's important to use terms in your code that a non-technical person can understand. What your code is trying to achieve should be a reflection of your company processes.
- Identify the relevant modules in the monolithic application, and then apply the common vocabulary to those modules.
- Define bounded contexts where you apply explicit boundaries to the identified modules with clearly defined responsibilities. The bounded contexts that you identify are candidates to be refactored into smaller microservices.

#### Prioritize services for migration

An ideal starting point to decouple services is to identify the loosely coupled modules in your monolithic application. 
You can choose a loosely coupled module as one of the first candidates to convert to a microservice. 
To complete a dependency analysis of each module, look at the following:
- The type of the dependency: dependencies from data or other modules.
- The scale of the dependency: how a change in the identified module might impact other modules.

Migrating a module with heavy data dependencies is usually a nontrivial task. 
If you migrate features first and migrate the related data later, you might be temporarily reading from and writing data to multiple databases. 
Therefore, you must account for data integrity and synchronization challenges.

#### Extract a service from a monolith

After you identify the ideal service candidate, you must identify a way for both microservice and monolithic modules to coexist. 
One way to manage this coexistence is to introduce an inter-process communication (IPC) adapter, which can help the modules work together. 
Over time, the microservice takes on the load and eliminates the monolithic component.

#### Manage a monolithic database

Typically, monolithic applications have their own monolithic databases. 
One of the principles of a microservices architecture is to have one database for each microservice. 
Therefore, when you modernize your monolithic application into microservices, you must split the monolithic database based on the service boundaries that you identify.

However, splitting a monolithic database is complex because there might not be clear separation between database objects. 
You also need to consider other issues, such as data synchronization, transactional integrity, joins, and latency. 

##### Share data through an API

When you separate the core functionalities or modules into microservices, you typically use APIs to share and expose data. 
The referenced service exposes data as an API that the calling service needs.

This implementation has obvious performance issues due to additional network and database calls. 
However, sharing data through an API works well when data size is limited.

##### Replicate data

Another way to share data between two separate microservices is to replicate data in the dependent service database. 
The data replication is read-only and can be rebuilt any time. 
This pattern enables the service to be more cohesive. 

##### Static data as configuration

You can inject such static data as a configuration in a microservice.

##### Shared mutable data

Monolithic applications have a common pattern known as shared mutable state. 
In a shared mutable state configuration, multiple modules use a single table.

To migrate a shared mutable state monolith, you can develop a separate ShoppingStatus microservice to manage the ShoppingStatus database table. 
This microservice exposes APIs to manage a customer's shopping status.

##### Distributed transactions

After you isolate the service from the monolith, a local transaction in the original monolithic system might get distributed between multiple services. 
A transaction that spans multiple services is considered a distributed transaction. In the monolithic application, the database system ensures that the transactions are atomic. To handle transactions between various services in a microservice-based system, you need to create a global transaction coordinator. 
The transaction coordinator handles rollback, compensating actions, and other transactions.

##### Data consistency

Consider a multistep transaction in a microservices-based architecture. 
If any one service transaction fails, data must be reconciled by rolling back steps that have succeeded across the other services.

It can be challenging to determine when a step that implements eventual consistency has failed. 

#### Design interservice communication

- One-to-one interaction: each client request is processed by exactly one service.
- One-to-many interactions: each request is processed by multiple services.

Consider whether the interaction is synchronous or asynchronous:
- Synchronous: the client expects a timely response from the service and it might block while it waits. HTTP-based REST, gRPC
- Asynchronous: the client doesn't block while waiting for a response. The response, if any, isn't necessarily sent immediately. AMQP or STOMP

Using asynchronous communication provides the following advantages:
- Loose coupling
- Failure isolation
- Responsiveness: An upstream service can reply faster if it doesn't wait on downstream services.
- Flow control: A message queue acts as a buffer, so that receivers can process messages at their own rate.

Challenges to using asynchronous messaging effectively:
- Latency: If the message broker becomes a bottleneck, end-to-end latency might become high.
- Overhead in development and testing
- Complicates error handling

### Patterns

#### Strangler Fig pattern

We recommend that you incrementally refactor your monolithic application. 
When you incrementally refactor an application, you gradually build a new application that consists of microservices, and run the application along with your monolithic application. 
This approach is also known as the Strangler Fig pattern. 
Over time, the amount of functionality that is implemented by the monolithic application shrinks until either it disappears entirely or it becomes another microservice.

#### Anticorruption Layer

The anticorruption layer (ACL) is a strategy used to ensure that the transition from monolith to microservices does not corrupt the business logic of your system. 
The ACL acts as a barrier between the monolith and the microservices, converting data and requests between the two systems.

### Interservice communication in a microservices setup

After you isolate the service and split it from the monolith, a local transaction in the original monolithic system is distributed among multiple services. 

In the microservice-based system that has a separate database for each service doesn't have a global transaction coordinator that spans the different databases. 
Because transactions aren't centrally coordinated, a failure in processing a payment doesn't roll back changes that were committed in the order service. 
Therefore, the system is in an inconsistent state.

The following patterns are commonly used to handle distributed transactions:
- Two-phase commit protocol (2PC): Part of a family of consensus protocols, 2PC coordinates the commit of a distributed transaction and it maintains atomicity, consistency, isolation, durability (ACID) guarantees.
- Saga: consists of running local transactions within each microservice that make up the distributed transaction. 
An event is triggered at the end of every successful or failed operation. 
All microservices involved in the distributed transaction subscribe to these events. 
If the following microservices receive a success event, they execute their operation. 
If there is a failure, the preceding microservices complete compensating actions to undo changes. 

There are various ways to implement a Saga—for example, you can use task and workflow engines such as Apache Airflow or Apache Camel.

## REST API vs GraphQL

GraphQL and REST API are both web API design approaches.

REST is great for simplicity, caching, and conventional web services.

GraphQL is ideal for flexibility, efficiency, and complex data fetching needs.


| Feature / Aspect      | **REST API**                                                     | **GraphQL**                                                             |
| --------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Design Style**      | Resource-based (e.g., `/users`, `/posts`)                        | Query-based (client defines data shape via queries)                     |
| **Endpoints**         | Multiple endpoints for different resources                       | Single endpoint (`/graphql`) for all queries and mutations              |
| **Data Fetching**     | Fixed responses; often over-fetches or under-fetches             | Client specifies exactly what data it needs                             |
| **Over-fetching**     | Common; returns entire resource even if only one field is needed | Avoided; fetch only requested fields                                    |
| **Under-fetching**    | May require multiple requests to get nested data                 | One request can retrieve deeply nested related data                     |
| **Versioning**        | Versioned URLs (e.g., `/api/v1/`)                                | No need for versioning — schema evolves with optional/nullable fields   |
| **Caching**           | Easy with HTTP (e.g., `ETag`, `304`)                             | Requires custom logic (Apollo, Relay have built-in caching)             |
| **Type System**       | Typically not enforced                                           | Strongly typed schema (defined with SDL)                                |
| **Error Handling**    | Relies on HTTP status codes (e.g., 404, 500)                     | Returns 200 OK with detailed error object in response body              |
| **Batch Requests**    | Requires multiple calls or custom batching                       | One query can retrieve multiple resources                               |
| **Real-time Support** | Not native; needs WebSockets or polling                          | Built-in via **subscriptions**                                          |
| **Tooling**           | Varies; depends on language/framework                            | Excellent tools like GraphiQL, Apollo Studio, schema introspection      |
| **Learning Curve**    | Lower; simpler to get started                                    | Higher; requires understanding of schema, queries, mutations, resolvers |

## Securing mService

### Authentication (Who are you?)

- Use OAuth 2.0, OpenID Connect, or JWT (JSON Web Tokens) for stateless auth.
- Consider API gateways like Kong, Apigee, or AWS API Gateway for centralized auth.

### Authorization (Can you access this?)

- Implement Role-Based Access Control (RBAC) or Attribute-Based Access Control (ABAC).
- Protect routes or methods based on user roles or claims in JWT.

### Transport Layer Security

- Use HTTPS (TLS) for all communication between services and clients.
- Never allow plain HTTP for sensitive endpoints.

### API Gateway / Service Mesh

- Gateways like Kong, Istio, or NGINX can handle: Rate limiting, Auth, Logging, Request validation
- Service meshes (e.g., Istio, Linkerd) provide: Mutual TLS (mTLS) between services, Fine-grained traffic control, Observability and security policies

### Network Security

- Isolate microservices in a private subnet or VPC.
- Use firewalls or security groups to restrict traffic.
- Enable zero-trust networking principles.

## WebSockets

To have your server (on EC2) send updates back to a web browser over HTTPS, you need a form of server push communication.

### WebSockets (most powerful & real-time)
- Allows bi-directional communication between browser and server.
- Ideal for live updates, chats, dashboards, etc.
- Runs over HTTPS (wss://) when using TLS.
- libraries on server: 
- Java: javax.websocket, Jetty, or Spring Boot (spring-websocket)
- Python: websockets, FastAPI + WebSocket
- WebSocket URL must be **wss://**your-ec2-host/ws/updates (not ws://) if you're using HTTPS

#### common mistakes with WebSockets
- Assuming the connection is stable forever:
    - Use onclose and onerror handlers in the client.
    - Implement automatic reconnect logic with exponential backoff.
- Not Scaling WebSocket Connections Properly
    - Keeping state in memory on one server and expecting it to work in a multi-instance deployment (e.g., behind a load balancer).
    - Use sticky sessions
    - Use a pub/sub system like Redis, Kafka, or RabbitMQ to broadcast messages across nodes
- Not Using wss:// for Secure Connections
    - Always use wss:// (WebSocket Secure) if your site uses HTTPS.
- Not Authenticating or Authorizing Clients
    - Require authentication (e.g., JWT token) during the initial WebSocket handshake or immediately after connection
- Failing to Handle Idle Connections or Keep-Alive
    - Use ping/pong frames or custom heartbeats to keep the connection alive.
    - On the server: detect stale connections and close them.
- Blocking the Event Loop (Node.js or Java)
    - Use async/await (Node.js), or non-blocking I/O (Java NIO).
    - Offload heavy work to background workers or threads.
- Not Closing Connections Cleanly
- Ignoring Backpressure and Message Queueing
    - Use throttling/buffering on both ends.
    - Check if session.getBasicRemote().isOpen() before sending (Java).
- Not Using Compression or Binary Frames Efficiently

#### Example:

Server:

```
@ServerEndpoint("/ws/updates")
public class UpdateWebSocket {

    private static Set<Session> sessions = new CopyOnWriteArraySet<>();

    @OnOpen
    public void onOpen(Session session) {
        sessions.add(session);
        System.out.println("New client connected: " + session.getId());
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        System.out.println("Message from client: " + message);
    }

    @OnClose
    public void onClose(Session session) {
        sessions.remove(session);
        System.out.println("Client disconnected: " + session.getId());
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        System.err.println("WebSocket error: " + throwable.getMessage());
    }

    // Send update to all connected clients
    public static void broadcast(String message) {
        for (Session session : sessions) {
            if (session.isOpen()) {
                try {
                    session.getBasicRemote().sendText(message);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

Client:

```
<!DOCTYPE html>
<html>
<head>
  <title>WebSocket Demo</title>
</head>
<body>
  <h2>WebSocket Client</h2>
  <div id="output"></div>

  <script>
    const socket = new WebSocket("wss://your-ec2-host/ws/updates");

    socket.onopen = () => {
      console.log("Connected to WebSocket");
      socket.send("Hello from the client!");
    };

    socket.onmessage = (event) => {
      const output = document.getElementById("output");
      const message = document.createElement("div");
      message.textContent = "Message from server: " + event.data;
      output.appendChild(message);
    };

    socket.onclose = () => {
      console.log("WebSocket closed");
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };
  </script>
</body>
</html>
```

### Server-Sent Events (SSE)

- One-way push from server to browser over HTTP.
- Simpler than WebSockets, but less flexible.
- Only supported over HTTP/HTTPS (not bi-directional).

### Polling (least efficient, but universal)

- Browser sends requests every N seconds.
- Not efficient but easy to implement.