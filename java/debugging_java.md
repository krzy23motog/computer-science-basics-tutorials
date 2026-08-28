# Setting JVM Arguments

# Remote debugging a Java application

https://www.baeldung.com/java-application-remote-debugging

To debug a Java application Start the JVM with the following options:
```
# windows
java -agentlib:jdwp=transport=dt_shmem,server=y,address=<port> <class>

# unix
java -agentlib:jdwp=transport=dt_socket,server=y,address=<port> <class>
```
Example: 
```
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8000 OurApplication
```

In a separate session, you can attach the debugger to the JVM:
```
jdb -attach <port>
```
# Thread Dumps

https://www.baeldung.com/java-analyze-thread-dumps

## generate java thread dump

jstack -l <process number> > sender-receiver-thread-dump.txt

## thread dump contents

first 2 lines show timestap and jvm data
```
2021-01-04 12:59:29
Full thread dump OpenJDK 64-Bit Server VM (15.0.1+9-18 mixed mode, sharing):
```

then there is list Safe Memory Reclamation (SMR) and non-JVM internal threads:
```
Threads class SMR info:
_java_thread_list=0x00007fd7a7a12cd0, length=13, elements={
0x00007fd7aa808200, 0x00007fd7a7012c00, 0x00007fd7aa809800, 0x00007fd7a6009200,
0x00007fd7ac008200, 0x00007fd7a6830c00, 0x00007fd7ab00a400, 0x00007fd7aa847800,
0x00007fd7a6896200, 0x00007fd7a60c6800, 0x00007fd7a8858c00, 0x00007fd7ad054c00,
0x00007fd7a7018800
}
```

Then, the dump displays the list of threads with information lie: name, priority, javaid, state, stack trace:
```
"Monitor Ctrl-Break" #12 daemon prio=5 os_prio=31 cpu=17.42ms elapsed=11.42s tid=0x00007fd7a6896200 nid=0x6603 runnable  [0x000070000dcc5000]
   java.lang.Thread.State: RUNNABLE
	at sun.nio.ch.SocketDispatcher.read0(java.base@15.0.1/Native Method)
	at sun.nio.ch.SocketDispatcher.read(java.base@15.0.1/SocketDispatcher.java:47)
	at sun.nio.ch.NioSocketImpl.tryRead(java.base@15.0.1/NioSocketImpl.java:261)
	at sun.nio.ch.NioSocketImpl.implRead(java.base@15.0.1/NioSocketImpl.java:312)
	at sun.nio.ch.NioSocketImpl.read(java.base@15.0.1/NioSocketImpl.java:350)
	at sun.nio.ch.NioSocketImpl$1.read(java.base@15.0.1/NioSocketImpl.java:803)
	at java.net.Socket$SocketInputStream.read(java.base@15.0.1/Socket.java:981)
	at sun.nio.cs.StreamDecoder.readBytes(java.base@15.0.1/StreamDecoder.java:297)
	at sun.nio.cs.StreamDecoder.implRead(java.base@15.0.1/StreamDecoder.java:339)
	at sun.nio.cs.StreamDecoder.read(java.base@15.0.1/StreamDecoder.java:188)
	- locked <0x000000070fc949b0> (a java.io.InputStreamReader)
	at java.io.InputStreamReader.read(java.base@15.0.1/InputStreamReader.java:181)
	at java.io.BufferedReader.fill(java.base@15.0.1/BufferedReader.java:161)
	at java.io.BufferedReader.readLine(java.base@15.0.1/BufferedReader.java:326)
	- locked <0x000000070fc949b0> (a java.io.InputStreamReader)
	at java.io.BufferedReader.readLine(java.base@15.0.1/BufferedReader.java:392)
	at com.intellij.rt.execution.application.AppMainV2$1.run(AppMainV2.java:61)

   Locked ownable synchronizers:
	- <0x000000070fc8a668> (a java.util.concurrent.locks.ReentrantLock$NonfairSync)
```

At the end of the dump, we’ll notice there are several additional threads performing background operations such as Garbage Collection (GC) or object termination:
```
"VM Thread" os_prio=31 cpu=1.85ms elapsed=11.50s tid=0x00007fd7a7a0c170 nid=0x3603 runnable  
"GC Thread#0" os_prio=31 cpu=0.21ms elapsed=11.51s tid=0x00007fd7a5d12990 nid=0x4d03 runnable  
"G1 Main Marker" os_prio=31 cpu=0.06ms elapsed=11.51s tid=0x00007fd7a7a04a90 nid=0x3103 runnable  
"G1 Conc#0" os_prio=31 cpu=0.05ms elapsed=11.51s tid=0x00007fd7a5c10040 nid=0x3303 runnable  
"G1 Refine#0" os_prio=31 cpu=0.06ms elapsed=11.50s tid=0x00007fd7a5c2d080 nid=0x3403 runnable  
"G1 Young RemSet Sampling" os_prio=31 cpu=1.23ms elapsed=11.50s tid=0x00007fd7a9804220 nid=0x4603 runnable  
"VM Periodic Task Thread" os_prio=31 cpu=5.82ms elapsed=11.42s tid=0x00007fd7a5c35fd0 nid=0x9903 waiting on condition
```

## analyze it

To understand the threads’ evolution over time, a recommended best practice is to take at least 3 dumps, one at every 10 seconds

We’ll mainly focus on RUNNABLE or BLOCKED threads and eventually TIMED_WAITING ones. Those states will point us in the direction of a conflict between two or more threads:
- In a deadlock situation in which several threads running hold a synchronized block on a shared object
- In thread contention, when a thread is blocked waiting for others to finish. For example, the dump generated in the previous section
- __Focus on long-running or blocked threads__ when issuing abnormal CPU or memory usage

### Use online tools
to analye thread dumps:
- FastThread
- JStack Review
- Thread Dump Analyzer" (TDA)

# Heap Dumps

Identifying the reason for an OutOfMemory error in Java applications with a larger heap size is a nightmare for a developer, because most of the OutOfMemory situations may not be identified during the testing phase.

The space used by the Java Runtime to allocate memory to Objects and JRE Classes is called Heap. The heap space can be configured using the following JVM arguments:
```
-Xmx<size> — Setting maximum Java heap size
-Xms<size> — Setting initial Java heap size
```

The __garbage collection process can be tuned for different applications__ based on the object creation characteristics of the application. This can be achieved through a number of JVM arguments. Following are a few JVM arguments which can be used to tune the garbage collection process:
```
-XX:-UseParallelGC: Use parallel garbage collection for scavenges.
-XX:-UseParallelOldGC: Use parallel garbage collection for the full collections. Enabling this option automatically sets -XX:+UseParallelGC.
-XX:NewRatio: Ratio of old/new generation sizes. The default value is 2.
-XX:SurvivorRatio: Ratio of eden/survivor space size. The default value is 8.
-XX:ParallelGCThreads: Sets the number of threads used during parallel phases of the garbage collectors. The default value varies with the platform on which the JVM is running
```

A java.lang.OutOfMemoryError will occur when the application tries to add more objects into the heap and there is no space left. This will happen when the maximum heap size set in the start of the application is filled with objects and the garbage collector is not able to free up the memory because the all objects in heap still have some references. This may happen because of two reasons:
- The application may need more memory to run; the currently allocated heap size is not enough to accommodate the objects generated during the runtime.
- Due to a coding error in the application which is keeping the references of unwanted objects.

## Take Heap Dump

- A JVM argument can be added to generate heap dump whenever an OutOfMemoryError occurs.
- The -XX:+HeapDumpOnOutOfMemoryError option can be added to generate a heap dump on OutOfMemoryError.
- Using a jmap tool available with JDK. The following command can be executed from the command line:
```
jmap -dump:format=b,file=heap.bin <pid> 
```

## content

## analyze it

Use tools:
- Java VisualVM enables you to visually browse heap dumps

