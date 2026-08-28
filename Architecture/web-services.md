
# Web Services

Essentially, web services include any software, application, or cloud technology that provides standardized web protocols (HTTP or HTTPS) to interoperate, communicate, and exchange data messaging – usually XML (Extensible Markup Language) – throughout the internet.

XML-centered data exchange systems that use the internet for A2A (application-to-application) communication and interfacing.

A key feature of web services is that applications can be written in various languages and are still able to communicate by exchanging data with one another via a web service between clients and servers. 
A client summons a web service by sending a request via XML, and the service then responses with an XML response. Web services are also often associated with SOA (Service-Oriented Architecture).

It has an interface described in a machine-processable format (specifically WSDL). Other systems interact with the web service in a manner prescribed by its description using SOAP messages, typically conveyed using HTTP with an XML serialization in conjunction with other web-related standards.

web services allow various apps to connect and interact with each other, they are more like the glue that developers use to connect individual apps and build a web services application architecture.

Web services are popular because they allow this exchange of services and data, even when the connecting systems are written in different programming languages or running on different platforms. 

In this way, a web service functions as a bridge–regardless of whether the connection is cloud-to-cloud, server-to-server, server-to-premises, cloud-to-premises, or client-to-server. This makes web services particularly valuable for enterprises that want to connect diverse software components running in different locations. 



To break that down, a web service comprises these essential functions:
- __Available over the internet__ or intranet networks
- Standardized __XML__ messaging system
- __Independent__ of a single operating system or programming language
- __Self-describing via standard XML__ language
- __Discoverable__ through a simple location method

A web service supports communication among numerous apps with __HTML, XML, WSDL, SOAP__, and other open standards. __XML__ tags the data, __SOAP__ transfers the message, and __WSDL__ describes the service’s accessibility.

Types of Web Services:
- __XML-RPC__ (Remote Procedure Call) is the most basic XML protocol to exchange data between a wide variety of devices on a network. It uses HTTP to quickly and easily transfer data and communication other information from client to server.
- __UDDI__ (Universal Description, Discovery, and Integration) is an XML-based standard for detailing, publishing, and discovering web services. It’s basically an internet registry for businesses around the world. 
- __SOAP__ is an XML-based Web service protocol to exchange data and documents over HTTP or SMTP
- __REST__ provides communication and connectivity between devices and the internet for API-based tasks. Most RESTful services use HTTP as the supporting protocol.

## SOAP vs. REST Web Services

A REST web service uses HTTP and supports/repurposes several HTTP methods: GET, POST, PUT or DELETE. 
It is __Lightweight__, human readable, __easier to build__ but allows only for __point-to-point communication__, lack of standards

__SOAP is defined as Simple Object Access Protocol.__ 
This web service protocol exchanges structured data using XML and generally HTTP and SMTP for transmission. 
SOAP also uses WSDL (Web Services Description Language)

## Architecture

The steps to perform this operation are as follows:
- The client program bundles the account registration information into a SOAP message.
- This SOAP message is sent to the web service as the body of an HTTP POST request.
- The web service unpacks the SOAP request and converts it into a command that the application can understand.
- The application processes the information as required and responds with a new unique account number for that customer.
- Next, the web service packages the response into another SOAP message, which it sends back to the client program in response to its HTTP request.
- The client program unpacks the SOAP message to obtain the results of the account registration process.


## Microservices vs. web services

While microservices are an approach to building an application from a set of smaller services, web services are programmable components that communicate with one another using the internet as a conduit.

They are both ways to deliver and share information via APIs. It's common to find applications that use both microservices and web services

Microservices are a distributed architecture with independent, loosely coupled services making up an application. Web services stand on a standardized architecture that enables interoperable communication between systems.

Choose microservices if your application is large and complex, deals with frequent changes, has high availability requirements, or is resource-intensive.

Choose web services if your application needs to integrate with legacy systems, has simple requirements, or has limited resources.

Microservices focus on independent, loosely coupled services, allowing for flexibility, scalability, and faster development cycles.

Web services enable interoperable communication between systems, making them suitable for integrating heterogeneous platforms.

Microservices offer finer scalability and granular control, while web services handle larger loads and have simpler implementation and management.
