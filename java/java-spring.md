# Table of Contents
- [Java spring](#JavaSpring)
  - [Spring Architecture](#Architecture)
  - [Example](#Example)
  - [IoC Containers](#IoCcontainers)
  - [Bean](#Bean)
  - [Event Handling](#EventHandling)
  - [JDBC Framework](#JDBC)
  - [MVC Framework](#MVC)
  - [AOP](#aop)
  - [Spring Interview](#springinterview)
- [Spring Boot](#Boot)
  - [Spring Boot Architecture](#BootArchitecture)
  - [Spring Boot Project](#BootProject)
  - [Spring Boot Example](#BootExample)
  - [Spring Boot With H2 Database Example](#BootDatabaseExample)

# Java spring <a id="JavaSpring"></a>

https://www.tutorialspoint.com/spring/index.htm

Spring framework is an open source Java platform that provides comprehensive infrastructure support for developing robust Java applications.

Features:
- POJO Based - Spring enables developers to develop enterprise-class applications using POJOs
- Modular - Spring is organized in a modular fashion.
- Integration with existing frameworks
- Testablity - Testing an application written with Spring is simple because environment-dependent code is moved into this framework.
- Web MVC - Spring's web framework is a well-designed web MVC framework, which provides a great alternative to web frameworks such as Struts
- Lightweight - Lightweight IoC containers tend to be lightweight, especially when compared to EJB containers
- Transaction management - Spring provides a consistent transaction management interface

The technology that Spring is most identified with is the __Dependency Injection__ (DI) flavor of __Inversion of Control__. 

When writing a complex Java application, application classes should be as __independent as possible__ of other Java classes to increase the possibility to reuse these classes and to test them independently of other classes while unit testing. __Dependency Injection helps in gluing these classes together and at the same time keeping them independent__

One of the key components of Spring is the __Aspect Oriented Programming__ (AOP) framework. The functions that span multiple points of an application are called cross-cutting concerns and these cross-cutting concerns are conceptually separate from the application's business logic. There are various common good examples of aspects including logging, declarative transactions, security, caching, etc.

## Architecture <a id="Architecture"></a>

Core container:
- The __Core module__ provides the fundamental parts of the framework, including the IoC and __Dependency Injection__ features.
- The __Bean__ module provides BeanFactory, which is a sophisticated implementation of the __factory pattern__.
- The __Context module__ builds on the solid base provided by the Core and Beans modules and it is a medium to access any objects defined and configured. The ApplicationContext interface is the focal point of the Context module.

Data Access/Integration:
- The __JDBC__ module provides a JDBC-abstraction layer that removes the need for tedious JDBC related coding.
- The __ORM__ module provides integration layers for popular object-relational mapping APIs, including __JPA__, JDO, __Hibernate__, and iBatis.
- The __OXM__ module provides an abstraction layer that supports Object/__XML__ mapping implementations for JAXB, Castor, XMLBeans, JiBX and XStream.
- The Java Messaging Service __JMS__ module contains features for __producing and consuming messages__.
- The __Transaction__ module supports programmatic and declarative transaction

Web modules:
- The __Web__ module provides basic __web-oriented integration features__ such as multipart file-upload functionality and the initialization of the IoC container using __servlet__ listeners and a __web-oriented application context__.
- The Web-MVC module contains Spring's __Model-View-Controller__ (MVC) implementation for web applications.
- The __Web-Socket__ module provides support for WebSocket-based, __two-way communication__ between the client and the server in web applications.
- The __Web-Portlet__ module provides

Other modules:
- The __AOP module__ provides an aspect-oriented programming implementation allowing you to define method-interceptors and pointcuts
- The __Aspects module__ provides integration with AspectJ, which is again a powerful and mature AOP framework.
- The __Test module__ supports the testing of Spring components with JUnit or TestNG frameworks.

## Example <a id="Example"></a>

Hello World: HelloWorld.java:
```
package com.tutorialspoint;

public class HelloWorld {
   private String message;

   public void setMessage(String message){
      this.message  = message;
   }
   public void getMessage(){
      System.out.println("Your Message : " + message);
   }
}
```
and MainApp.java:
```
package com.tutorialspoint;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
   public static void main(String[] args) {
      ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
      HelloWorld obj = (HelloWorld) context.getBean("helloWorld");
      obj.getMessage();
   }
}
```

## IoC Containers <a id="IoCcontainers"></a>

__The container will create the objects, wire them together, configure them, and manage their complete life cycle__ from creation till destruction.

The Spring container uses DI to manage the components that make up an application. __These objects are called Spring Beans__

The container gets its instructions on what objects to instantiate, configure, and assemble by reading the configuration metadata provided. The configuration metadata can be represented either by XML, Java annotations, or Java code.

## Bean <a id="Bean"></a>

The objects that form the backbone of your application and that are managed by the Spring IoC container are called beans. A bean is an object that is instantiated, assembled, and otherwise managed by a Spring IoC container. These beans are created with the configuration metadata that you supply to the container. 

Following are the three important methods to provide configuration metadata to the Spring Container −
- XML based configuration file.
- Annotation-based configuration
- Java-based configuration

When defining a <bean> you have the option of declaring a scope for that bean:
- to force Spring to produce a new bean instance each time one is needed, you should declare the bean's scope attribute to be __prototype__.
- if you want Spring to return the same bean instance each time one is needed, you should declare the bean's scope attribute to be __singleton__.
- __request__: This scopes a bean definition to an HTTP request. Only valid in the context of a web-aware Spring ApplicationContext.
- __session__: This scopes a bean definition to an HTTP session. Only valid in the context of a web-aware Spring ApplicationContext.

## Event Handling in Spring <a id="EventHandling"></a>

The ApplicationContext publishes certain types of events when loading the beans. For example, a ContextStartedEvent is published when the context is started and ContextStoppedEvent is published when the context is stopped.

Event handling in the ApplicationContext is provided through the ApplicationEvent class and ApplicationListener interface. Hence, if a bean implements the ApplicationListener, then every time an ApplicationEvent gets published to the ApplicationContext, that bean is notified.

### Listening to Context Events

To listen to a context event, a bean should implement the ApplicationListener interface which has just one method onApplicationEvent()

HelloWorld.java:
```
package com.tutorialspoint;

public class HelloWorld {
   private String message;

   public void setMessage(String message){
      this.message  = message;
   }
   public void getMessage(){
      System.out.println("Your Message : " + message);
   }
}
```
CStartEventHandler.java:
```
package com.tutorialspoint;

import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextStartedEvent;

public class CStartEventHandler 
   implements ApplicationListener<ContextStartedEvent>{

   public void onApplicationEvent(ContextStartedEvent event) {
      System.out.println("ContextStartedEvent Received");
   }
}
```
MainApp.java:
```
package com.tutorialspoint;

import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
   public static void main(String[] args) {
      ConfigurableApplicationContext context = 
         new ClassPathXmlApplicationContext("Beans.xml");

      // Let us raise a start event.
      context.start();
	  
      HelloWorld obj = (HelloWorld) context.getBean("helloWorld");
      obj.getMessage();

      // Let us raise a stop event.
      context.stop();
   }
}
```

 Beans.xml:
 ```
 <?xml version = "1.0" encoding = "UTF-8"?>

<beans xmlns = "http://www.springframework.org/schema/beans"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://www.springframework.org/schema/beans
   http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

   <bean id = "helloWorld" class = "com.tutorialspoint.HelloWorld">
      <property name = "message" value = "Hello World!"/>
   </bean>

   <bean id = "cStartEventHandler" class = "com.tutorialspoint.CStartEventHandler"/>
   <bean id = "cStopEventHandler" class = "com.tutorialspoint.CStopEventHandler"/>

</beans>
 ```

 ## Spring - JDBC Framework Overview <a id="JDBC"></a>

 The JDBC Template class executes SQL queries, updates statements, stores procedure calls, performs iteration over ResultSets, and extracts returned parameter values. It also catches JDBC exceptions and translates them to the generic, more informative, exception hierarchy defined in the org.springframework.dao package.

 A common practice when using the JDBC Template class is to configure a DataSource in your Spring configuration file, and then dependency-inject that shared DataSource bean into your DAO classes, and the JdbcTemplate is created in the setter for the DataSource.

 __DataSource__ to the JDBC Template so it can configure itself to get database access. You can configure the DataSource in the XML file with a piece of code as shown in the following code snippet:
 ```
 <bean id = "dataSource" 
   class = "org.springframework.jdbc.datasource.DriverManagerDataSource">
   <property name = "driverClassName" value = "com.mysql.jdbc.Driver"/>
   <property name = "url" value = "jdbc:mysql://localhost:3306/TEST"/>
   <property name = "username" value = "root"/>
   <property name = "password" value = "password"/>
</bean>
 ```

Query:
```
String SQL = "select count(*) from Student";
int rowCount = jdbcTemplateObject.queryForInt( SQL );
```

### Data Access Object (DAO)

Is used for database interaction. 
DAOs exist to provide a means to read and write data to the database and they should expose this functionality through an interface by which the rest of the application will access them.

StudentDAO.java:
```
package com.tutorialspoint;

import ...

public interface StudentDAO {
   public void setDataSource(DataSource ds);
   public void create(String name, Integer age);
   public Student getStudent(Integer id);
   public List<Student> listStudents();
   public void delete(Integer id);
   public void update(Integer id, Integer age);
}
```

Student.java:
```
package com.tutorialspoint;

public class Student {
   private Integer age;
   private String name;
   private Integer id;

   public void setAge(Integer age) {
      this.age = age;
   }
   public Integer getAge() {
      return age;
   }
   public void setName(String name) {
      this.name = name;
   }
   public String getName() {
      return name;
   }
   public void setId(Integer id) {
      this.id = id;
   }
   public Integer getId() {
      return id;
   }
}
```

StudentMapper.java:
```
package com.tutorialspoint;

import ...

public class StudentMapper implements RowMapper<Student> {
   public Student mapRow(ResultSet rs, int rowNum) throws SQLException {
      Student student = new Student();
      student.setId(rs.getInt("id"));
      student.setName(rs.getString("name"));
      student.setAge(rs.getInt("age"));
      
      return student;
   }
}
```

StudentJDBCTemplate.java:
```
public class StudentJDBCTemplate implements StudentDAO {
   private DataSource dataSource;
   private JdbcTemplate jdbcTemplateObject;
   
   public void setDataSource(DataSource dataSource) {
      this.dataSource = dataSource;
      this.jdbcTemplateObject = new JdbcTemplate(dataSource);
   }
   public void create(String name, Integer age) {
      String SQL = "insert into Student (name, age) values (?, ?)";
      jdbcTemplateObject.update( SQL, name, age);
      System.out.println("Created Record Name = " + name + " Age = " + age);
      return;
   }
   public Student getStudent(Integer id) {
      String SQL = "select * from Student where id = ?";
      Student student = jdbcTemplateObject.queryForObject(SQL, 
         new Object[]{id}, new StudentMapper());
      
      return student;
   }
   public List<Student> listStudents() {
      String SQL = "select * from Student";
      List <Student> students = jdbcTemplateObject.query(SQL, new StudentMapper());
      return students;
   }
   public void delete(Integer id) {
      String SQL = "delete from Student where id = ?";
      jdbcTemplateObject.update(SQL, id);
      System.out.println("Deleted Record with ID = " + id );
      return;
   }
   public void update(Integer id, Integer age){
      String SQL = "update Student set age = ? where id = ?";
      jdbcTemplateObject.update(SQL, age, id);
      System.out.println("Updated Record with ID = " + id );
      return;
   }
}
```
MainApp.java:
```
public class MainApp {
   public static void main(String[] args) {
      ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");

      StudentJDBCTemplate studentJDBCTemplate = 
         (StudentJDBCTemplate)context.getBean("studentJDBCTemplate");
      
      System.out.println("------Records Creation--------" );
      studentJDBCTemplate.create("Zara", 11);
      studentJDBCTemplate.create("Nuha", 2);
      studentJDBCTemplate.create("Ayan", 15);

      System.out.println("------Listing Multiple Records--------" );
      List<Student> students = studentJDBCTemplate.listStudents();
      
      for (Student record : students) {
         System.out.print("ID : " + record.getId() );
         System.out.print(", Name : " + record.getName() );
         System.out.println(", Age : " + record.getAge());
      }

      System.out.println("----Updating Record with ID = 2 -----" );
      studentJDBCTemplate.update(2, 20);

      System.out.println("----Listing Record with ID = 2 -----" );
      Student student = studentJDBCTemplate.getStudent(2);
      System.out.print("ID : " + student.getId() );
      System.out.print(", Name : " + student.getName() );
      System.out.println(", Age : " + student.getAge());
   }
}
```

Beans.xml:
```
<?xml version = "1.0" encoding = "UTF-8"?>
<beans xmlns = "http://www.springframework.org/schema/beans"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" 
   xsi:schemaLocation = "http://www.springframework.org/schema/beans
   http://www.springframework.org/schema/beans/spring-beans-3.0.xsd ">

   <!-- Initialization for data source -->
   <bean id="dataSource" 
      class = "org.springframework.jdbc.datasource.DriverManagerDataSource">
      <property name = "driverClassName" value = "com.mysql.jdbc.Driver"/>
      <property name = "url" value = "jdbc:mysql://localhost:3306/TEST"/>
      <property name = "username" value = "root"/>
      <property name = "password" value = "password"/>
   </bean>

   <!-- Definition for studentJDBCTemplate bean -->
   <bean id = "studentJDBCTemplate" 
      class = "com.tutorialspoint.StudentJDBCTemplate">
      <property name = "dataSource" ref = "dataSource" />    
   </bean>
      
</beans>
```

## Spring - MVC Framework <a id="MVC"></a>

The Spring Web MVC framework provides Model-View-Controller (MVC) architecture and ready components that can be used to develop flexible and loosely coupled web applications. The MVC pattern results in separating the different aspects of the application (input logic, business logic, and UI logic), while providing a loose coupling between these elements.

The __Model__ encapsulates the application data and in general they will consist of POJO.

The __View__ is responsible for rendering the model data and in general it generates HTML output that the client's browser can interpret.

The __Controller__ is responsible for processing user requests and building an appropriate model and passes it to the view for rendering.


### DispatcherServlet

The Spring Web model-view-controller (MVC) framework is designed around a DispatcherServlet that handles all the HTTP requests and responses.

- After receiving an HTTP request, DispatcherServlet consults the HandlerMapping to call the appropriate Controller.
- The Controller takes the request and calls the appropriate service methods based on used GET or POST method. The service method will set model data based on defined business logic and returns view name to the DispatcherServlet.
- The DispatcherServlet will take help from ViewResolver to pickup the defined view for the request.
- Once view is finalized, The DispatcherServlet passes the model data to the view which is finally rendered on the browser.

### Configuration

You need to map requests that you want the DispatcherServlet to handle, by using a URL mapping in the web.xml file:
```
<web-app id = "WebApp_ID" version = "2.4"
   xmlns = "http://java.sun.com/xml/ns/j2ee" 
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://java.sun.com/xml/ns/j2ee 
   http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
    
   <display-name>Spring MVC Application</display-name>
   
   <servlet>
      <servlet-name>HelloWeb</servlet-name>
      <servlet-class>
         org.springframework.web.servlet.DispatcherServlet
      </servlet-class>
      <load-on-startup>1</load-on-startup>
   </servlet>

   <servlet-mapping>
      <servlet-name>HelloWeb</servlet-name>
      <url-pattern>*.jsp</url-pattern>
   </servlet-mapping>

</web-app>
```

<servlet-mapping> tag indicates what URLs will be handled by which DispatcherServlet. Here all the HTTP requests ending with .jsp will be handled by the HelloWeb DispatcherServlet.

HelloWeb-servlet.xml:
```
<beans xmlns = "http://www.springframework.org/schema/beans"
   xmlns:context = "http://www.springframework.org/schema/context"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://www.springframework.org/schema/beans     
   http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
   http://www.springframework.org/schema/context 
   http://www.springframework.org/schema/context/spring-context-3.0.xsd">

   <context:component-scan base-package = "com.tutorialspoint" />

   <bean class = "org.springframework.web.servlet.view.InternalResourceViewResolver">
      <property name = "prefix" value = "/WEB-INF/jsp/" />
      <property name = "suffix" value = ".jsp" />
   </bean>

</beans>
```

The [servlet-name]-servlet.xml file will be used to create the beans defined, overriding the definitions of any beans defined with the same name in the global scope.

### Controller

The DispatcherServlet delegates the request to the controllers to execute the functionality specific to it. The @Controller annotation indicates that a particular class serves the role of a controller. The @RequestMapping annotation is used to map a URL to either an entire class or a particular handler method.

```
@Controller
@RequestMapping("/hello")
public class HelloController { 
   @RequestMapping(method = RequestMethod.GET)
   public String printHello(ModelMap model) {
      model.addAttribute("message", "Hello Spring MVC Framework!");
      return "hello";
   }
}
```

### JSP Views

Spring MVC supports many types of views for different presentation technologies. These include - JSPs, HTML, PDF etc.

simple hello view in /WEB-INF/hello/hello.jsp:
```
<html>
   <head>
      <title>Hello Spring MVC</title>
   </head>
   
   <body>
      <h2>${message}</h2>
   </body>
</html>
```
## Spring AOP <a id="aop"></a>

## Java spring interview questions <a id="springinterview"></a>

### What is Spring Framework?

Spring is a lightweight Java framework for building enterprise applications. It provides inversion of control (IoC), aspect‑oriented programming (AOP), transaction management, and integrates with many technologies.

### What is Inversion of Control (IoC)?

IoC is a design principle where control of object creation and lifecycle is handed over to the container (Spring).

### What is Dependency Injection (DI)?

DI is a pattern where dependencies are provided by the container rather than the object creating them.

```
@Component
public class OrderService {
    private final PaymentService paymentService;

    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}
```

The Spring IoC container (most commonly AnnotationConfigApplicationContext or the one auto-configured in Spring Boot) creates and wires dependencies for your OrderService class using the following step-by-step process:
- Component Scanning: Spring scans your packages (usually starting from the package containing your @SpringBootApplication class) for classes annotated with @Component, @Service, @Repository, @Controller, etc.
- Bean Definition Registration: A BeanDefinition is created for OrderService. Spring sees that:
  - It has exactly one constructor. 
  - That constructor has parameters (PaymentService)
- Dependency Resolution (Constructor Argument Matching): For constructor injection (the recommended and now default style), Spring looks at the parameter types of the constructor. It needs a bean whose type is compatible with PaymentService
- Finding the Dependency Bean: Spring checks the existing bean factory for a bean that matches PaymentService (by type)
- Bean Instantiation Order (Smart Autowiring). Spring creates beans in the right order using a dependency graph:
  - First creates PaymentService bean (if not already created)
  - Then creates OrderService by calling its constructor and passing the already-created PaymentService instance

### What are the types of DI in Spring?

Constructor‑based, Setter‑based, and Field‑based (via annotations).

#### Constructor-based Dependency Injection (Recommended / Best Practice)

```
@Service
public class OrderService {

    private final PaymentService paymentService;
    private final CustomerRepository customerRepo;
    private final OrderValidator validator;

    // Since Spring 4.3 → single constructor = implicit @Autowired
    public OrderService(
            PaymentService paymentService,
            CustomerRepository customerRepo,
            OrderValidator validator) {
        
        this.paymentService  = paymentService;
        this.customerRepo    = customerRepo;
        this.validator       = validator;
    }

    public void placeOrder(Order order) {
        validator.validate(order);
        customerRepo.save(order.getCustomer());
        paymentService.processPayment(order.getTotalAmount());
        // ...
    }
}
```

- Use final fields → immutable, thread-safe
- Dependencies are required (Spring fails fast during startup if missing)
- Easiest to test (just new OrderService(...) in tests)

#### Setter-based Dependency Injection

```
@Service
public class OrderService {

    private PaymentService paymentService;
    private CustomerRepository customerRepo;
    private OrderValidator validator;

    // All setters are called after object is created (but before @PostConstruct)
    @Autowired
    public void setPaymentService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @Autowired
    public void setCustomerRepository(CustomerRepository customerRepo) {
        this.customerRepo = customerRepo;
    }

    @Autowired
    public void setValidator(OrderValidator validator) {
        this.validator = validator;
    }

    // or even bulk variant (less common)
    @Autowired
    public void setDependencies(
            PaymentService paymentService,
            CustomerRepository repo,
            OrderValidator validator) {
        this.paymentService = paymentService;
        this.customerRepo = repo;
        this.validator = validator;
    }

    // business methods...
}
```

#### Field-based Dependency Injection (via @Autowired on fields)

```
@Service
public class OrderService {

    @Autowired
    private PaymentService paymentService;

    @Autowired
    private CustomerRepository customerRepository;

    @Autowired
    @Qualifier("strictOrderValidator")
    private OrderValidator validator;

    // or even (not recommended anymore)
    @Autowired(required = false)
    private NotificationService optionalNotifier;

    public void placeOrder(Order order) {
        // risk: if injection failed → NPE here
        validator.validate(order);
        paymentService.processPayment(order.getAmount());
    }
}
```

### What is a Spring Bean?

An object created, managed, and injected by the Spring IoC container.

### What are Bean Scopes in Spring?

Common scopes: singleton, prototype, request, session, application.

### What is @Component?

A stereotype annotation indicating a Spring‑managed bean.

Marks a class as a Spring bean.

```
@Component
public class InventoryService {}

```

### Difference between @Component, @Service, @Repository, @Controller?

all mark managed beans — but indicate different layers:
- @Service: Service layer
- @Repository: DAO layer (adds exception translation)
- @Controller: MVC controller
- @Component: Generic bean

### What is @Autowired?

Annotation to auto‑inject dependencies.

### Difference between BeanFactory and ApplicationContext?

ApplicationContext extends BeanFactory with more enterprise features (events, i18n, AOP).

### What are the ways to configure Spring?

XML, Java config (@Configuration), and annotations (@ComponentScan, @Bean).

### What does @Configuration do?

Marks a class as a source of bean definitions.

```
@Configuration
public class AppConfig {}
```

### What does @Bean do?

Declares a method as a bean producer.

```
@Bean
public MyService service() {
    return new MyService();
}

```

### What is @ComponentScan?

Scans packages for annotated components.

```
@ComponentScan("com.example")

```

### How do you exclude a package from scanning?

Using @ComponentScan(excludeFilters = @Filter(...)).

### How to define properties file in Spring?

Using @PropertySource and Environment or @Value.

### What is Environment abstraction?

Provides access to properties and profiles.

### What is @Primary vs @Qualifier?

- @Primary: default when multiple beans exist
- @Qualifier: specifies which bean to inject

```
@Autowired
@Qualifier("mysqlRepo")
private UserRepo repo;
```

### What is Environment?

Spring interface to access properties and profiles.

### What is Spring Profile?

Activates environment‑specific beans.

### Bean Lifecycle Callbacks?

- @PostConstruct
- @PreDestroy

### What is AOP?

Aspect‑Oriented Programming — separates cross‑cutting concerns.

### What is JoinPoint?

An executable point (e.g., method call).

### What is Advice?

Action taken at a join point (before, after, around).

### What is @Aspect?

Marks an aspect class.

```
@Aspect
@Component
public class LoggingAspect {}

```








# Spring Boot <a id="Boot"></a>

Spring is widely used for creating scalable applications, but disadvantage of spring projects is that __configuration is really time-consuming__ and can be a bit overwhelming for the new developers.

Spring Boot is built on the top of the spring and contains all the features of spring. It enables the developers to directly focus on the logic instead of struggling with the configuration and set up. __Spring Boot is a microservice-based framework__ and making a production-ready application in it takes very less time. Prerequisite for Spring Boot is the basic knowledge Spring framework. 

Features:
- It allows to avoid heavy configuration of XML. In spring boot __everything is auto-configured.__
- It provides __easy maintenance and creation of REST end points__: Creating a REST API is very easy in Spring Boot. Just the annotation @RestController and @RequestMapping(/endPoint) over the controller class does the work.
- It includes __embedded Tomcat-server__: Unlike Spring MVC project where we have to manually add and install the tomcat server, Spring Boot comes with an embedded Tomcat server, so that the applications can be hosted on it. 
- Deployment is very easy, war and jar file can be easily deployed in the tomcat server:war or jar files can be directly deployed on the Tomcat Server
- Microservice Based Architecture: __Microservice__, as the name suggests is the name given to a module/service which focuses on a single type of feature, exposing an API

## Spring Boot Architecture <a id="BootArchitecture"></a>

Layers in Spring Boot: There are four main layers in Spring Boot:
- __Presentation__ Layer: As the name suggests, it consists of views(i.e. frontend part). __Authentication & Json Translation__
- __Data Access__ Layer: CRUD (create, retrieve, update, delete) operations on the database comes under this category.
  - __Persistence Layer__ – Storage Logic
  - __Database Layer__ – Actual Database
- __Service__ Layer: This consist of service classes and uses services provided by data access layers. __Business Logic, Validation & Authorization__
- __Integration__ Layer: It consists of web different web services(any service available over the internet and uses XML messaging system).


Since Spring boot uses all the features/modules of spring-like Spring data, Spring MVC etc. so __the architecture is almost the same as spring MVC__, __except__ for the fact that __there is no need of DAO and DAOImpl classes__ in Spring boot.

Creating a __data access layer__ needs just a __repository class__ instead which is implementing CRUD operation containing class.

Flow:
- A client makes the https request(PUT/GET)
- Then it goes to controller and the controller mapped with that route as that of request handles it, and calls the service logic if required.
- Business logic is performed in the service layer which might be performing the logic on the data from the database which is mapped through JPA with model/entity class
- Finally, a JSP page is returned in the response if no error occurred.

## Create a Spring Boot Project <a id="BootProject"></a>

Create a Spring Boot Project in Spring Initializr: __https://start.spring.io/__

### Spring Initializr

Spring Initializr is a Web-based tool that provides simple web UI to generate the Spring Boot project structure or we can say it builds the skeleton of the Spring-based application.

It helps you to customize and configure the project requirement and automatically manage the Spring Boot Dependencies using the Maven repository or Gradle.

Configuration:
- Project: Using this one can create Maven or Gradle project i.e; Maven or Gradle can be used as a build tool.
- Language: Spring Initializr provide Java, Kotlin and Groovy as a programming language for the project. 
- Project Dependencies: Dependencies are artifacts that we can add to the project. 

### Application Properties

Write the application-related property src/main/resources/__application.properties__

This file contains the different configuration which is required to run the application in a different environment, and each environment will have a different property defined by it. Inside the application properties file, we define every type of property like changing the port, database connectivity, connection to the eureka server, and many more. 

Example of application.properties:
```
# Log file
logging.file=logs/my-log-file.log

# Server port
server.port=9080

# Servlet context path
server.servlet.context-path=/helloworld

# Custom property
person.name=Java Code Geeks!
person.age=25
person.title=Mr.

## Web error page
server.error.whitelabel.enabled=false
 
## Web HTTPS settings
server.tomcat.remoteip.remote-ip-header=x-forwarded-for
server.tomcat.remoteip.protocol-header=x-forwarded-proto
 
### Web Gzip
server.compression.enabled=true
server.compression.mime-types=application/json,application/xml,text/html,text/xml,text/plain,application/javascript,text/css
 
## Web static resources versioning
spring.web.resources.chain.strategy.content.enabled=true
spring.web.resources.chain.strategy.content.paths=/js/**,/css/**
 
### Web caching
spring.web.resources.cache.cachecontrol.max-age=30d

## DataSource properties
spring.datasource.url=jdbc:mysql://localhost:3306/revogain
spring.datasource.username=${REVOGAIN_DB_USER}
spring.datasource.password=${REVOGAIN_DB_PASSWORD}
 
## HikariCP configuration
spring.datasource.hikari.minimumIdle=0
spring.datasource.hikari.maximum-pool-size=40
spring.datasource.hikari.maxLifetime=900000
spring.datasource.hikari.transaction-isolation=TRANSACTION_READ_COMMITTED
spring.datasource.hikari.auto-commit=false
spring.datasource.hikari.data-source-properties.useServerPrepStmts=false
spring.datasource.hikari.data-source-properties.cachePrepStmts=true
spring.datasource.hikari.data-source-properties.prepStmtCacheSize=500
spring.datasource.hikari.data-source-properties.prepStmtCacheSqlLimit=1024

spring.datasource.hikari.minimumIdle=0
spring.datasource.hikari.maximum-pool-size=40
spring.datasource.hikari.maxLifetime=600000
```

Create separate property files named application-{profile}.properties for each profile you want to define. For example:
- application.properties for common configuration
- application-dev.properties for development

Use the main application.properties file to specify the common settings.

## Create Boot Example <a id="BootExample"></a>

https://www.geeksforgeeks.org/spring-boot-hello-world-example/

https://www.baeldung.com/spring-boot

https://spring.io/guides

### Step 1: Go to Spring Initializr
```
Project: Maven
Language: Java
Spring Boot: 2.2.8
Packaging: JAR
Java: 8
Dependencies: Spring Web
STS IDE
```

### Extract the zip file. Now open IDE

### Example files:

SpringBoot HelloWorldApplication.java - The Spring Initializr creates a simple application class for you.
```
package com.javacodegeeks.examples;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloWorldApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloWorldApplication.class, args);
	}
}
```

HelloController.java - The class is flagged as a @RestController, meaning it is ready for use by Spring MVC to handle web requests. @GetMapping maps / to the index() method.
```
package com.javacodegeeks.examples;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/")
public class HelloController {
	
	@Value("${person.name}")
	private String name;
	
	@Autowired
	private Person person;
	
	@GetMapping("/hello")
	public String hello() {
		return "Hello " + name;
	}

	@PostConstruct
	private void printPerson() {
		System.out.println("name: " + person.name);
		System.out.println("age: " + person.age);
		System.out.println("title: " + person.title);
	}
}
```

Person.java
```
package com.javacodegeeks.examples;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration
@ConfigurationProperties(prefix="person")
public class Person {
	
	String name;
	int age;
	String title;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
}
```

application.properties
```
# Log file
logging.file=logs/my-log-file.log

# Server port
server.port=9080

# Servlet context path
server.servlet.context-path=/helloworld

# Custom property
person.name=Java Code Geeks!
person.age=25
person.title=Mr.
```

To run:
```
./mvnw spring-boot:run
```

## Spring Boot With H2 Database Example <a id="BootDatabaseExample"></a>

https://spring.io/guides/gs/accessing-data-mysql

### Model

Create the entity model, (in src/main/java/com/example/accessingdatamysql/User.java) 
```
package com.example.accessingdatamysql;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class User {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Integer id;
  private String name;
  private String email;

  // getters and setters
}
```

### Repository

Create the repository that holds user records (in src/main/java/com/example/accessingdatamysql/UserRepository.java) 
```
package com.example.accessingdatamysql;

import org.springframework.data.repository.CrudRepository;

import com.example.accessingdatamysql.User;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface UserRepository extends CrudRepository<User, Integer> {

}
```

### Controller

Create a controller to handle HTTP requests to your application (in src/main/java/com/example/accessingdatamysql/MainController.java)
```
package com.example.accessingdatamysql;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // This means that this class is a Controller
@RequestMapping(path="/demo") // This means URL's start with /demo (after Application path)
public class MainController {
  @Autowired // This means to get the bean called userRepository
         // Which is auto-generated by Spring, we will use it to handle the data
  private UserRepository userRepository;

  @PostMapping(path="/add") // Map ONLY POST Requests
  public @ResponseBody String addNewUser (@RequestParam String name
      , @RequestParam String email) {
    // @ResponseBody means the returned String is the response, not a view name
    // @RequestParam means it is a parameter from the GET or POST request

    User n = new User();
    n.setName(name);
    n.setEmail(email);
    userRepository.save(n);
    return "Saved";
  }

  @GetMapping(path="/all")
  public @ResponseBody Iterable<User> getAllUsers() {
    // This returns a JSON or XML with the users
    return userRepository.findAll();
  }
}
```

### Application class

Spring Initializr creates a simple class for the application (src/main/java/com/example/accessingdatamysql/AccessingDataMysqlApplication.java):
```
package com.example.accessingdatamysql;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccessingDataMysqlApplication {

  public static void main(String[] args) {
    SpringApplication.run(AccessingDataMysqlApplication.class, args);
  }

}
```

### Database Configuration

application.yaml:
```
spring:
  datasource:
    url: jdbc:h2:mem:mydb
    username: sa
    password: password
    driverClassName: org.h2.Driver
    url: jdbc:h2:file:/data/demo
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
```


### Run and test

```
curl http://localhost:8080/demo/add -d name=First -d email=someemail@someemailprovider.com
```


### Database Operations

Basic SQL scripts to initialize the database:

src/main/resources/data.sql 
```
INSERT INTO countries (id, name) VALUES (1, 'USA');
INSERT INTO countries (id, name) VALUES (2, 'France');
INSERT INTO countries (id, name) VALUES (3, 'Brazil');
INSERT INTO countries (id, name) VALUES (4, 'Italy');
INSERT INTO countries (id, name) VALUES (5, 'Canada');
```

## Spring AOP example

In Spring AOP, aspects define cross-cutting concerns using advice and pointcuts. 
Spring creates proxy objects around target beans, and the proxy intercepts method calls to apply advice before or after method execution.

Create a Service (Business Logic). This is normal business logic — no logging inside.
```
@Service
public class PaymentService {
    public String processPayment(String user) {
        System.out.println("Processing payment for " + user);
        return "SUCCESS";
    }
}
```

Create an Aspect:
```
@Aspect
@Component
public class LoggingAspect {
    // Pointcut expression
    @Pointcut("execution(* com.example.demo.service.*.*(..))")
    public void serviceMethods() {}

    // Before Advice
    @Before("serviceMethods()")
    public void logBefore() {
        System.out.println("Method execution started");
    }

    // AfterReturning Advice
    @AfterReturning(pointcut = "serviceMethods()", returning = "result")
    public void logAfterReturning(Object result) {
        System.out.println("Method returned: " + result);
    }

    // Around Advice
    @Around("serviceMethods()")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("Before method: " + joinPoint.getSignature().getName());
        Object result = joinPoint.proceed();  // Calls actual method
        System.out.println("After method: " + joinPoint.getSignature().getName());
        return result;
    }
}
```