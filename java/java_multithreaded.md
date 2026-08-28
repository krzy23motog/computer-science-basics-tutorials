# Java Multithreading

Java supports multithreading through Thread class. Java Thread allows us to create a lightweight process that executes some tasks. We can create multiple threads in our program and start them

## Singleton

### Simple singleton

If your singleton class is not using a lot of resources, this is the approach to use. 
But in most of the scenarios, singleton classes are created for resources such as File System, Database connections, etc. 
We should avoid the instantiation unless the client calls the getInstance method.

```
public class EagerInitializedSingleton {
    private static final EagerInitializedSingleton instance = new EagerInitializedSingleton();
    // private constructor to avoid client applications using the constructor
    private EagerInitializedSingleton(){}
    public static EagerInitializedSingleton getInstance() {
        return instance;
    }
}
```

### Thread Safe Singleton

```
public class ThreadSafeSingleton {
    private static ThreadSafeSingleton instance;
    private ThreadSafeSingleton(){}
    public static synchronized ThreadSafeSingleton getInstance() {
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }
}
```

or better (reduces the performance because of the cost associated with the synchronized method):

```
public static ThreadSafeSingleton getInstanceUsingDoubleLocking() {
    if (instance == null) {
        synchronized (ThreadSafeSingleton.class) {
            if (instance == null) {
                instance = new ThreadSafeSingleton();
            }
        }
    }
    return instance;
}
```

## Create and use Thread in java

### Create thread

Thread life cycle:
- New
- Runnable
- Running
- Blocked/Waiting
- Dead

#### Runnable

```
Thread t = new Thread(new Runnable(){
    @Override
    public void run() {
    }
});
```

OR 

```
Runnable runnable = () -> System.out.println("Hello");
```

OR 

```
public class LiftOff implements Runnable { 
 protected int countDown = 10; // Default 
 private static int taskCount = 0; 
 private final int id = taskCount++; 
 public LiftOff() {} 
 public LiftOff(int countDown) { 
    this.countDown = countDown; 
 } 
 public String status() { 
    return "#" + id + "(" + 
        (countDown > 0 ? countDown : "Liftoff!") + "), "; 
 } 
 public void run() { 
    while(countDown-- > 0) { 
        System.out.print(status()); 
        Thread.yield(); 
    } 
 } 
} 
```

run( ) method usually has some kind of loop that continues until the task is no longer necessary, so you must establish the condition on which to break out of this loop.

The call to the static method Thread.yield( ) inside run( ) is a suggestion to the thread scheduler that says, "I’ve done the important parts of my cycle and this would be a good time to switch to another task for a while.

#### Callable

A __Runnable__ is a separate task that performs work, but it doesn’t return a value. 
If you want the task to produce a value when it’s done, you can implement the __Callable__ interface rather than the Runnable interface

Unlike the Runnable, the Callable instance cannot be passed as an input while creating a thread. 
Instead, __we must wrap it with a future__ (Eg. FutureTask) and pass it to the Thread class.

Callable is a generic with a type parameter representing the return value from the method call( ) (instead of run( )), and must be invoked using an ExecutorService submit( ) method.

```
class TaskWithResult implements Callable<String> { 
 private int id; 
 public TaskWithResult(int id) { 
    this.id = id; 
 } 
 public String call() { 
    return "result of TaskWithResult " + id; 
 } 
} 
```

### Run a thread

#### Runnable

The traditional way to turn a Runnable object into a working task is to hand it to a Thread constructor.

```
public class BasicThreads { 
 public static void main(String[] args) { 
    Thread t = new Thread(new LiftOff()); 
    t.start(); 
    System.out.println("Waiting for LiftOff"); 
 } 
} 
```

Executors provide a layer of indirection between a client and the execution of a task; instead of a client executing a task directly, an intermediate object executes the task. 
Executors allow you to manage the execution of asynchronous tasks without having to explicitly manage the lifecycle of threads

We can use an Executor instead of explicitly creating Thread objects

```
public class CachedThreadPool { 
 public static void main(String[] args) { 
    ExecutorService exec = Executors.newCachedThreadPool(); 
    for(int i = 0; i < 5; i++) 
        exec.execute(new LiftOff()); 
                                                           
    exec.shutdown();
 } 
} 

```

The call to shutdown( ) prevents new tasks from being submitted to that Executor. 
The current thread (in this case, the one driving main( )) will continue to run all tasks submitted before shutdown( ) was called. 
The program will exit as soon as all the tasks in the Executor finish. 

#### Callable

The submit( ) method produces a Future object, parameterized for the particular type of result returned by the Callable. 
You can query the Future with isDone( ) to see if it has completed. 
When the task is completed and has a result, you can call get( ) to fetch the result. 
You can simply call get( ) without checking isDone( ), in which case get( ) will block until the result is ready. 
You can also call get( ) with a timeout.

```
FutureTask<ResultType> futureTask = new FutureTask<>( new TaskWithResult(i) );
Thread t=new Thread(futureTask);
t.start();
// …
ResultType result = futureTask.get(); // will wait for the async completion
```

OR with Executor:

```
public class CallableDemo { 
    public static void main(String[] args) { 
        ExecutorService exec = Executors.newCachedThreadPool(); 
        ArrayList<Future<String>> results = new ArrayList<Future<String>>(); 
        for(int i = 0; i < 10; i++) 
            results.add(exec.submit(new TaskWithResult(i))); 
        for(Future<String> fs : results) {
            try { 
                // get() blocks until completion: 
                System.out.println(fs.get()); 
            } catch(InterruptedException e) { 
                System.out.println(e); 
                return; 
            } catch(ExecutionException e) { 
                System.out.println(e); 
            } finally { 
                exec.shutdown(); 
            } 
        }
    } 
}
```

#### Yielding

When you call yield( ), you are suggesting that other threads of the same priority might be run.

#### Daemon threads

A "daemon" thread is intended to provide a general service in the background as long as the program is running, but is not part of the essence of the program. 
Thus, __when all of the non-daemon threads complete, the program is terminated, killing all daemon threads__ in the process.

If there are any non-daemon threads still running, the program doesn’t terminate.

You must set the thread to be a daemon by calling setDaemon( ) before it is started.

```
public class SimpleDaemons implements Runnable { 
 public void run() { 
    try { 
        while(true) { 
            TimeUnit.MILLISECONDS.sleep(100); 
            print(Thread.currentThread() + " " + this); 
        } 
    } catch(InterruptedException e) { 
        print("sleep() interrupted"); 
    } 
 } 
 public static void main(String[] args) throws Exception { 
    for(int i = 0; i < 10; i++) { 
        Thread daemon = new Thread(new SimpleDaemons()); 
        daemon.setDaemon(true); // Must call before start() 
        daemon.start(); 
    } 
    print("All daemons started"); 
    TimeUnit.MILLISECONDS.sleep(175); 
 } 
}
```

#### Joining a thread

One thread may call join( ) on another thread to wait for the second thread to complete before proceeding. 
If a thread calls t.join( ) on another thread t, then the calling thread is suspended until the target thread t finishes.

#### Catching exceptions

Because of the nature of threads, you can’t catch an exception that has escaped from a thread.

Thread.UncaughtExceptionHandler.uncaughtException( ) is automatically called when that thread is about to die from an uncaught exception.

However it does not work for Executables.

```
class ExceptionThread2 implements Runnable { 
 public void run() { 
    Thread t = Thread.currentThread(); 
    System.out.println("run() by " + t); 
    System.out.println( 
    "eh = " + t.getUncaughtExceptionHandler()); 
    throw new RuntimeException(); 
 } 
} 
class MyUncaughtExceptionHandler implements Thread.UncaughtExceptionHandler { 
    public void uncaughtException(Thread t, Throwable e) { 
    System.out.println("caught " + e); 
 } 
} 
class HandlerThreadFactory implements ThreadFactory { 
 public Thread newThread(Runnable r) { 
    System.out.println(this + " creating new Thread"); 
    Thread t = new Thread(r); 
    System.out.println("created " + t); 
    t.setUncaughtExceptionHandler( new MyUncaughtExceptionHandler()); 
    System.out.println( "eh = " + t.getUncaughtExceptionHandler()); 
    return t; 
 } 
} 
public class CaptureUncaughtException { 
 public static void main(String[] args) { 
    ExecutorService exec = Executors.newCachedThreadPool( 
    new HandlerThreadFactory()); 
    exec.execute(new ExceptionThread2()); 
 } 
}
```

### Resolving shared resource contention

#### Synchronized

All concurrency schemes serialize access to shared resources. This means that only one task at a time is allowed to access the shared resource.

To prevent collisions over resources, Java has built-in support in the form of the synchronized keyword. 
When a task wishes to execute a piece of code guarded by the synchronized keyword, it checks to see if the lock is available, then acquires it, executes the code, and releases it. 

```
public class SynchronizedEvenGenerator extends IntGenerator { 
 private int currentEvenValue = 0; 
 public synchronized int next() { 
    ++currentEvenValue; 
    Thread.yield(); // Cause failure faster 
    ++currentEvenValue; 
    return currentEvenValue; 
 } 
 public static void main(String[] args) { 
    EvenChecker.test(new SynchronizedEvenGenerator()); 
 } 
}
```

#### Atomicity

Atomic operations are thus not interruptible by the threading mechanism.

Changes made by one task, even if they’re atomic in the  sense of not being interruptible, might not be visible to other tasks (the changes might be temporarily stored in a local processor cache, for example), so different tasks will have a different view of the application’s state.

##### Volatile

If you declare a field to be __volatile__, this means that as soon as a write occurs for that field, all reads will see the change. 
This is true even if local caches are involved—volatile fields are immediately written through to main memory, and reads occur from main memory. 

An atomic operation on a non-volatile field will not necessarily be flushed to main memory, and so another task that reads that field will not necessarily see the new value. 
If multiple tasks are accessing a field, that field should be volatile; otherwise, the field should only be accessed via synchronization. Synchronization also causes flushing to main memory, so if a field is completely guarded by synchronized methods or blocks, it is not necessary to make it volatile.

##### Atomiclnteger, AtomicLong etc.

These are for fine-tuning to use machine-level atomicity that is available on some modern processors, so you generally don’t need to worry about using them

##### ThreadLocal

A second way to prevent tasks from colliding over shared resources is to eliminate the sharing of variables. 
Thread local storage is a mechanism that automatically creates different storage for the same variable, for each different thread that uses an object.

If you have five threads using an object with a variable x, thread local storage generates five different pieces of storage for x.

```
// create
ThreadLocal<Integer> threadLocalValue = new ThreadLocal<>();

// use
threadLocalValue.set(1);
Integer result = threadLocalValue.get();
```

OR

```
public class ThreadLocalExp   
{   
     public static class MyRunnable implements Runnable    
   {   
       private ThreadLocal<Integer> threadLocal =   
              new ThreadLocal<Integer>();   
      @Override   
       public void run() {   
           threadLocal.set( (int) (Math.random() * 50D) );   
           try    
           {   
               Thread.sleep(1000);   
           } catch (InterruptedException e) {   
           }   
           System.out.println(threadLocal.get());   
       }   
   }   
   public static void main(String[] args)    
   {   
       MyRunnable runnableInstance = new MyRunnable();    
       Thread t1 = new Thread(runnableInstance);   
       Thread t2 = new Thread(runnableInstance);   
      // this will call run() method    
       t1.start();   
       t2.start();   
   }   
} 

// output:
10
33
10 33
```

### Terminating tasks

Thread.stop(), but it just kills the thread and may leave your application in an inconsistent state. This can be done easier with just calling System.exit().

#### InterruptedException

When a thread is interrupted, it throws an InterruptedException. It's essential to catch this exception and handle it appropriately. 

Thread provides the interrupt() method for interrupting a thread. Some code can call the interrupt() method on our thread.

To query whether a thread has been interrupted, we can use the isInterrupted() method.

Each thread has a boolean property that represents its interrupted status. Invoking Thread.interrupt() sets this flag. When a thread checks for an interrupt by invoking the static method Thread.interrupted(), the interrupt status is cleared.

Someone interrupted your thread. That someone is probably eager to cancel the operation, terminate the program gracefully, or whatever. You should be polite to that someone and return from your method without further ado.

Interruption is a polite request:
- A thread is never forcefully stopped by another thread
- It only receives a signal (the interrupted status flag is set)

##### Solution 1
The best solution here is to let the InterruptedException propagate through the method call stack, by appending each relevant method signature with the throws InterruptedException statement. This might seem like an easy cop-out solution at first glance, but it is, in fact, the correct solution.


##### Solution 2
In the following example, TestThread works periodically after every 2 seconds. It checks if it has been interrupted or not. If not, it continues working, finishes the processing and returns. If it is interrupted in between by another Thread, it can terminate gracefully by throwing InterruptedException to the caller Thread.

```
public class TestThread extends Thread {  
	public void run() {  
		try{
			while(true) {  
                // Check if it is interrupted, if so then throw InterruptedException
				if(Thread.interrupted()) {  
					throw new InterruptedException();
				}  
                // else continue working
				else {  
					System.out.println("Continue working");  
				}  
                Thread.sleep(2000L);
			}
		} catch (InterruptedException e) {
            // Handling InterruptedException and Graceful shutdown of the Thread
			System.out.println("Graceful shutdown"); 
		}
	}  
}
```

#### Shutdown Hooks

The JVM allows registering functions to run before it completes its shutdown. These functions are usually a good place for releasing resources or other similar house-keeping tasks.

```
Thread printingHook = new Thread(() -> System.out.println("In the middle of a shutdown"));
Runtime.getRuntime().addShutdownHook(printingHook);
```

```
package com.tutorialspoint;

class CustomThread extends Thread {
   public void run() {
      System.out.println("JVM is shutting down.");
   }
}

public class TestThread {
   public static void main(String args[]) throws InterruptedException {
      try {
         // register CustomThread as shutdown hook
         Runtime.getRuntime().addShutdownHook(new CustomThread());
         // print the state of the program
         System.out.println("Program is starting...");
         // cause thread to sleep for 3 seconds
         System.out.println("Waiting for 3 seconds...");
         Thread.sleep(3000);
         // print that the program is closing
         System.out.println("Program is closing...");
      } catch (Exception e) {
         e.printStackTrace();
      }
   }
}
```

OR

```
public class TestShutdownHook {  
      // shutdown hook thread can be used to perform cleaning of resources.  
      private static class ShutDownHook extends Thread {  
           public void run() {  
                System.out.println("shutdown hook thread started");  
           }  
      }  
      public static void main(String[] args) {  
           ShutDownHook jvmShutdownHook = new ShutDownHook();  
           Runtime.getRuntime().addShutdownHook(jvmShutdownHook);  
           System.out.println("Register Shutdown Hook");  
           System.out.println("calling System.exit() to close the program");  
           System.exit(0);  
           System.out.println("Program Finished");  
      }  
 }  
```

## wait() 

Object.wait() is a method that:
- Must be called inside a synchronized block (on the same object you're synchronizing on)
- Releases the monitor lock (intrinsic lock) of that object
- Suspends (pauses) the current thread
- Puts the thread into the object's wait set
- The thread stays suspended until one of these happens:
- Another thread calls notify() or notifyAll() on the same object
- Another thread interrupts the waiting thread → throws InterruptedException

# Java Data structures

The collection classes that are thread-safe in Java are __Stack__, __Vector__, __Properties__, __Hashtable__, etc.

## Collections.synchronizedCollection() 

Returns a thread-safe collection backed up by the specified Collection.

```
Collection<Integer> syncCollection = Collections.synchronizedCollection(new ArrayList<>());
    Runnable listOperations = () -> {
        syncCollection.addAll(Arrays.asList(1, 2, 3, 4, 5, 6));
    };
    
    Thread thread1 = new Thread(listOperations);
    Thread thread2 = new Thread(listOperations);
    thread1.start();
    thread2.start();
    thread1.join();
    thread2.join();
    
    assertThat(syncCollection.size()).isEqualTo(12);
}

```
## Collections.synchronizedList()

The method returns a thread-safe view of the specified List:
```
List<Integer> syncList = Collections.synchronizedList(new ArrayList<>());
```


## Collections.synchronizedSortedMap

### ConcurrentHashMap



# Thread Safety in Java

Make our program safe to use in multithreaded environment:
- __Synchronization__ is the easiest and most widely used tool for thread safety in java.
- Use of __Atomic Wrapper classes__ from java.util.concurrent.atomic package. For example AtomicInteger
- Use of __locks__ from java.util.concurrent.locks package.
- Using __thread safe collection__ classes, check this post for usage of ConcurrentHashMap for thread safety.
- Using __volatile__ keyword with variables to make every thread read the data from memory, not read from thread cache.

# Interview questions

## What are the wait() and sleep() methods? 

__wait__(): As the name suggests, it is a non-static method that causes the current thread to wait and go to sleep until some other threads call the notify () or notifyAll() method for the object’s monitor (lock)

__sleep__(): As the name suggests, it is a static method that pauses or stops the execution of the current thread for some specified period. It doesn’t release the lock while waiting and is mostly used to introduce pause on execution

## What’s the purpose of the join() method?

__join__() method is generally used to pause the execution of a current thread unless and until the specified thread on which join is called is dead or completed. To stop a thread from running until another thread gets ended, this method can be used.

## Explain the meaning of the deadlock and when it can occur?

Deadlock, as the name suggests, is a situation where multiple threads are blocked forever. It generally occurs when multiple threads hold locks on different resources and are waiting for other resources to complete their task.

## Explain volatile variables in Java?

This keyword cannot be used with classes and methods, instead can be used with variables. It is simply used to achieve thread-safety. If you mark any variable as volatile, then all the threads can __read its value directly from the main memory__ rather than CPU cache.

## What is thread starvation?

Thread starvation is basically a situation or condition where a thread won’t be able to have regular access to shared resources and therefore is unable to proceed or make progress. This is because other threads have high priority and occupy the resources for too long. This usually happens with low-priority threads that do not get CPU for its execution to carry on.

## What is Livelock?

the state of threads changes between one another without making any progress. Threads are not blocked but their execution is stopped due to the unavailability of resources.

## What is BlockingQueue?

BlockingQueue basically represents a queue that is thread-safe. Producer thread inserts resource/element into the queue using put() method unless it gets full and consumer thread takes resources from the queue using take() method until it gets empty. But if a thread tries to dequeue from an empty queue, then a particular thread will be blocked until some other thread inserts an item into the queue, or if a thread tries to insert an item into a queue that is already full, then a particular thread will be blocked until some threads take away an item from the queue.

## What is a shutdown hook?

A shutdown hook is simply a thread that is invoked implicitly before JVM shuts down. It is one of the most important features of JVM because it provides the capacity to do resource cleanup or save application state JVM shuts down.

## What is race-condition?

When various threads execute simultaneously accessing a shared resource at the same time. The proper use of synchronization can avoid the Race condition.