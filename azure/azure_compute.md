# Table of Contents
- [Azure Functions](#AzureFunctions)
- [Containers](#Containers)
  - Containerized function apps
  - Azure Container Apps
  - Azure App Service
  - Azure Container Instances
  - Azure Kubernetes Service
  - Azure Functions

# Azure Functions <a id="AzureFunctions"></a>

Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs.

Functions provides a comprehensive set of event-driven triggers and bindings that connect your functions to other services without having to write extra code.

## Durable azure functions

Durable Functions is a feature of Azure Functions that lets you write stateful functions in a serverless compute environment. 

The extension lets you define stateful workflows by writing orchestrator functions and stateful entities by writing entity functions using the Azure Functions programming mode

The primary use case for Durable Functions is simplifying complex, stateful coordination requirements in serverless applications.

### Pattern #1: Function chaining

In the function chaining pattern, a sequence of functions executes in a specific order. 
In this pattern, the output of one function is applied to the input of another function. 
The use of queues between each function ensures that the system stays durable and scalable, even though there is a flow of control from one function to the next.

You can use Durable Entities to maintain state across an entire orchestration without making round trips to the database, which is useful for application state management, as opposed to persisting client data


Example:
```
[FunctionName("Chaining")]
public static async Task<object> Run(
    [OrchestrationTrigger] IDurableOrchestrationContext context)
{
    try
    {
        var x = await context.CallActivityAsync<object>("F1", null);
        var y = await context.CallActivityAsync<object>("F2", x);
        var z = await context.CallActivityAsync<object>("F3", y);
        return  await context.CallActivityAsync<object>("F4", z);
    }
    catch (Exception)
    {
        // Error handling or compensation goes here.
    }
}
```

## Use Cases

###  Process file uploads

Run code when a file is uploaded or changed in blob storage.

Trigger Azure Functions on blob containers using an event subscription:

https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-java

### Process data in real time

Capture and transform data from event and IoT source streams on the way to storage.

Azure Event Hubs trigger for Azure Functions:

https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-java&tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2%2Cextensionv5

Azure Functions supports trigger and output bindings for Event Hubs.

```
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="EventHubTrigger1")
@app.event_hub_message_trigger(arg_name="myhub", 
                               event_hub_name="<EVENT_HUB_NAME>",
                               connection="<CONNECTION_SETTING>") 
def test_function(myhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                myhub.get_body().decode('utf-8'))
```

### Infer on data models

Pull text from a queue and present it to various AI services for analysis and classification.

### Build a scalable web API 

Implement a set of REST endpoints for your web applications using HTTP triggers.

An HTTP triggered function defines an HTTP endpoint. These endpoints run function code that can connect to other services directly or by using binding extensions. You can compose the endpoints into a web-based API.

```
import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
        )
```

### Build a serverless workflow 

Create an event-driven workflow from a series of functions using Durable Functions.

### Create reliable message systems 

Process message queues using Queue Storage, Service Bus, or Event Hubs.

## Limits

Consumption plan: Pay for compute resources only when your functions are running
- timeout: 5-10 min
- maximum instances: 100-200
- max memory: 1.5GB

Premium plan: Automatically scales based on demand using prewarmed workers, which run applications with no delay after being idle, runs on more powerful instances, and connects to virtual networks.
- timeout: >30 min
- maximum instances: 20-100
- max memory: 3.5GB

Dedicated plan: Best for long-running scenarios where Durable Functions can't be used
- timeout: >30 min
- maximum instances: 10-100
- max memory: 3.5GB

Container Apps: containerized function apps in a fully managed environment hosted by Azure Container Apps.
- timeout: >30 min
- maximum instances: 300-1000
- max memory: variable

## Containerized function apps

Functions maintains a set of language-specific base images that you can use when creating containerized function apps.

Steps:
- Choose your development language
- Create and test the local functions project
- Build the container image and verify locally
- Publish the container image to a registry
- Create supporting Azure resources for your function
  - A resource group, which is a logical container for related resources.
  ```
  az group create --name AzureFunctionsContainers-rg --location <REGION>
  ```
  - A Storage account, which is used to maintain state and other information about your functions
  ```
  az storage account create --name <STORAGE_NAME> --location <REGION> --resource-group AzureFunctionsContainers-rg --sku Standard_LRS
  ```
  - A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management
  ```
  az functionapp plan create --resource-group AzureFunctionsContainers-rg --name myPremiumPlan --location <REGION> --number-of-workers 1 --sku EP1 --is-linux
  ```
  - Create and configure a function app on Azure with the image
  ```
  az functionapp create --name <APP_NAME> --storage-account <STORAGE_NAME> --resource-group AzureFunctionsContainers-rg --plan myPremiumPlan --image <LOGIN_SERVER>/azurefunctionsimage:v1.0.0 --registry-username <USERNAME> --registry-password <SECURE_PASSWORD>
  ```
  - verify
  ```
  az functionapp function show --resource-group AzureFunctionsContainers-rg --name <APP_NAME> --function-name HttpExample --query invokeUrlTemplate
  ```

# Containers <a id="Containers"></a>

## Azure Container Apps

Azure Container Apps enables you to build serverless microservices based on containers. 
Azure Container Apps doesn't provide direct access to the underlying Kubernetes APIs.

Fully managed experience based on best-practices.

Azure Container Apps provide many application-specific concepts on top of containers, including certificates, revisions, scale, and environments.

## Azure App Service

## Azure Container Instances

Azure Container Instances (ACI) provides a single pod of Hyper-V isolated containers on demand. 
It can be thought of as a lower-level "building block" option compared to Container Apps. 
Concepts like scale, load balancing, and certificates aren't provided with ACI containers.

## Azure Kubernetes Service

Azure Kubernetes Service (AKS) provides a fully managed Kubernetes option in Azure. 
It supports direct access to the Kubernetes API and runs any Kubernetes workload. 
The full cluster resides in your subscription, with the cluster configurations and operations within your control and responsibility.

### Azure Functions

Azure Functions is a serverless Functions-as-a-Service (FaaS) solution. 
It's optimized for running event-driven applications using the functions programming model. 
It shares many characteristics with Azure Container Apps around scale and integration with events, but optimized for ephemeral functions deployed as either code or containers. 
The Azure Functions programming model provides productivity benefits for teams looking to trigger the execution of your functions on events and bind to other data sources. 
If you plan to build FaaS-style functions, Azure Functions is the ideal option. 
The Azure Functions programming model is available as a base container image, making it portable to other container based compute platforms allowing teams to reuse code as environment requirements change.


