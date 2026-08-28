# Azure ExpressRoute

Lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. 
With ExpressRoute, you can establish connections to Microsoft cloud services, such as Microsoft Azure and Microsoft 365.

ExpressRoute connections offer more reliability, faster speeds, consistent latencies, and higher security than typical connections over the Internet, because they don’t go over the public Internet.

ExpressRoute connections use a private, dedicated connection through a third-party connectivity provider. The private connection extends your on-premises network into Azure.

https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/expressroute

ExpressRoute connections do not go over the public Internet, and offer more reliability, faster speeds, lower latencies and higher security than typical connections over the Internet.



# Azure Private Link

Azure Private Link enables you to access Azure PaaS Services (for example, Azure Storage and SQL Database) and Azure hosted customer-owned/partner services over a private endpoint in your virtual network.

Traffic between your virtual network and the service travels the Microsoft backbone network. 
Exposing your service to the public internet is no longer necessary. 
You can create your own private link service in your virtual network and deliver it to your customers.

# Private Endpoint

private IP in my VNET that represents a PaaS service.


# Azure to data center conectivity


# Azure Stack Hub

Azure Stack Hub is an extension of Azure that provides a way to run apps in an on-premises environment and deliver Azure services in your datacenter. 

# Connect from On premises to cloud

## HTTP Long Polling
Server keeps the connection hanging till a data is available for client. 
Once data is available, server sends the data closing the connection. 
Once the connection is closed, client has to again establish a new connection. 
Generally, for each long poll request, there is a timeout

Advantages:
- It does not overload the server by sending frequent unnecessary request because in polling sometimes even if we don’t have anything in response.
- Just imagine that If from one app some sending requests 50 times for a single response, then we can avoid this using long polling as we can reuse our resource somewhere else.

In Long polling we can specify the timeout so that our request will not stuck due to some other reasons.

### Example

Publisher:
```
private ExecutorService bakers = Executors.newFixedThreadPool(5);

@GetMapping("/bake/{bakedGood}")
public DeferredResult<String> publisher(@PathVariable String bakedGood, @RequestParam Integer bakeTime) {
    DeferredResult<String> output = new DeferredResult<>( 5000L );
    bakers.execute(() -> {
        try {
            Thread.sleep(bakeTime);
            output.setResult(format("Bake for %s complete and order dispatched. Enjoy!", bakedGood));
        } catch (Exception e) {
            output.setErrorResult("Something went wrong with your order!");
        }
    });
    return output;
}
```
A worker thread from our bakers pool is doing the work and will set the result upon completion. 
When the worker calls setResult, it will allow the container thread to respond to the calling client.

Since long polling is often implemented to handle responses from downstream systems both asynchronously and synchronously, we should add a mechanism to enforce a timeout (5000L) in the case that we never receive a response from the downstream system.

Subscriber:
```
public String callBakeWithRestTemplate(RestTemplateBuilder restTemplateBuilder) {
    RestTemplate restTemplate = restTemplateBuilder
      .setConnectTimeout(Duration.ofSeconds(10))
      .setReadTimeout(Duration.ofSeconds(10))
      .build();

    try {
        return restTemplate.getForObject("/api/bake/cookie?bakeTime=1000", String.class);
    } catch (ResourceAccessException e) {
        // handle timeout
    }
}
```
By catching the ResourceAccessException from our long polling call, we’re able to handle the error upon timeout.

## Websockets
Establish a persistent duplex connection between client and server. 

Advantages:
- Bidirectional: Both server and client can send data.
- Real-time collaboration: Ideal for applications like chat and multiplayer games.
- Efficient data exchange: Supports both text and binary data.

Example Server endpoint:
```
@ServerEndpoint(value="/chat/{username}")
public class ChatEndpoint {
 
    private Session session;
    private static Set<ChatEndpoint> chatEndpoints = new CopyOnWriteArraySet<>();
    private static HashMap<String, String> users = new HashMap<>();

    @OnOpen
    public void onOpen( Session session, @PathParam("username") String username) throws IOException {
        this.session = session;
        chatEndpoints.add(this);
        users.put(session.getId(), username);

        Message message = new Message();
        message.setFrom(username);
        message.setContent("Connected!");
        broadcast(message);
    }

    @OnMessage
    public void onMessage(Session session, Message message) throws IOException {
        message.setFrom(users.get(session.getId()));
        broadcast(message);
    }

    @OnClose
    public void onClose(Session session) throws IOException {
        chatEndpoints.remove(this);
        Message message = new Message();
        message.setFrom(users.get(session.getId()));
        message.setContent("Disconnected!");
        broadcast(message);
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        // Do error handling here
    }

    private static void broadcast(Message message) throws IOException, EncodeException {
        chatEndpoints.forEach(endpoint -> {
            synchronized (endpoint) {
                try {
                    endpoint.session.getBasicRemote().sendObject(message);
                } catch (IOException | EncodeException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}
```

When a new user logs in, (@OnOpen) is immediately mapped to a data structure of active users. 
Then a message is created and sent to all endpoints using the broadcast method.

### Using Redis/ElastiCache for Scaling WebSockets

By leveraging Redis' pub/sub capabilities, you can reduce the load on your primary application server by offloading the message distribution work to Redis

## Server Sent Events (SSE)

Client establishes a long term persistent connection with server. 
This connection is used to send events from server to client. 
There is no timeout and contain remains alive till the client remains on network. 

Advantages:
- Simplicity: Easy to set up and use.
- Periodic updates: Ideal for real-time notifications and feeds.
- Automatic reconnection: Client reconnects if the connection is lost.

SSE is a perfect choice for an application displaying real-time stock price updates because it efficiently pushes updates from the server to the client. 
This code snippet illustrates how SSE can be utilized for such a scenario. 
```
// Create a new EventSource to listen for updates from the server
const stockPriceSource = new EventSource('https://example.com/stock-prices');

// Listen for stock price updates from the server
stockPriceSource.onmessage = function(event) {
  const stockUpdate = JSON.parse(event.data);
  console.log(`New stock price for ${stockUpdate.symbol}: $${stockUpdate.price}`);
  updateStockPriceOnPage(stockUpdate.symbol, stockUpdate.price); // Update the stock price on the web page
};

// Close the connection when done
stockPriceSource.close();
```


