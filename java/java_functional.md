# Java Functional Programming

Functional programming is a style of writing computer programs that treat computations as evaluating mathematical functions.
In mathematics, a function is an expression that relates an input set to an output set.
Importantly, the output of a function depends only on its input. More interestingly, we can compose two or more functions together to get a new function.

Core Concepts:
- First-Class Functions
- Immutability
- Higher-Order Functions: Takes one or more functions as arguments and returns a function as its result.
- Function Composition
- Declarative Programming
- Lambda Expressions: pass functions as arguments, return them, and store them in variables.
- Functional Interfaces
- Stream
- Optional
- Method References

A programming language is said to have first-class functions if it treats functions as first-class citizens. This means that functions are allowed to support all operations typically available to other entities. 

Higher-order functions are capable of receiving functions as arguments and returning a function as a result.

Example (https://www.baeldung.com/java-functional-programming)

Instead of using this:
```
Collections.sort(numbers, new Comparator<Integer>() {
    @Override
    public int compare(Integer n1, Integer n2) {
        return n1.compareTo(n2);
    }
});
```
Use this:
```
Collections.sort(numbers, (n1, n2) -> n1.compareTo(n2));
```

Behind the syntactic sugar of lambda expressions, Java still wraps these into functional interfaces. So, Java treats a lambda expression as an Object, which is the true first-class citizen in Java.

## Immutability

Immutability is one of the core principles of functional programming, and it refers to the property that an entity can’t be modified after being instantiated.

rules:
- All fields of an immutable data structure must be immutable.
- This must apply to all the nested types and collections (including what they contain) as well.
- There should be one or more constructors for initialization as needed.
- There should only be accessor methods, possibly with no side effects.

Example:
```
final class Student {

    // Member attributes of final class
    private final String name;
    private final int regNo;
    private final Map<String, String> metadata;

    // Constructor of immutable class
    // Parameterized constructor
    public Student(String name, int regNo, Map<String, String> metadata) {

        // This keyword refers to current instance itself
        this.name = name;
        this.regNo = regNo;

        // Creating Map object with reference to HashMap
        // Declaring object of string type
        Map<String, String> tempMap = new HashMap<>();

        // Iterating using for-each loop
        for (Map.Entry<String, String> entry : metadata.entrySet()) {
            tempMap.put(entry.getKey(), entry.getValue());
        }

        this.metadata = tempMap;
    }

    // Method 1 
    public String getName() { return name; }

    // Method 2 
    public int getRegNo() { return regNo; }
  
    // Note that there should not be any setters 

    // Method 3: User -defined type to get meta data
    public Map<String, String> getMetadata() {

        // Creating Map with HashMap reference
        Map<String, String> tempMap = new HashMap<>();

        for (Map.Entry<String, String> entry :
             this.metadata.entrySet()) {
            tempMap.put(entry.getKey(), entry.getValue());
        }
        return tempMap;
    }
}
```

## Functional Interface - Comparator Interface

__A functional interface is an interface that contains exactly one abstract method__.

Example of functional interface:
```
@FunctionalInterface
public interface MathOperation {
    // Single abstract method
    int operate(int a, int b);

    // Optional: default method (can have a body)
    // method defined in an interface that has a method body, can be optionally overridden by implementing classes
    default int addFive(int a) {
        return a + 5;
    }

    // Optional: static method
    static int multiplyByTwo(int a) {
        return a * 2;
    }
}
```

How to use it:
```
public class Main {
    public static void main(String[] args) {
        // Using lambda to define the operate method
        MathOperation addition = (a, b) -> a + b; // Adds two numbers
        MathOperation subtraction = (a, b) -> a - b; // Subtracts two numbers

        // Calling the operate method
        System.out.println("Addition: " + addition.operate(10, 5)); // 15
        System.out.println("Subtraction: " + subtraction.operate(10, 5)); // 5

        // Using default method
        System.out.println("Add Five: " + addition.addFive(10)); // 15

        // Using static method
        System.out.println("Multiply by Two: " + MathOperation.multiplyByTwo(10)); // 20
    }
}
```

The Comparator interface in Java is a functional interface, meaning it has __one abstract method__

The lambda (n1, n2) -> n1.compareTo(n2) is implicitly converted to a Comparator because it matches the compare(T o1, T o2) method signature.

Java infers the types of n1 and n2 from the context, making the lambda fit the Comparator interface.


## Referential Transparency

We call an expression referentially transparent if replacing it with its corresponding value has no impact on the program’s behavior.

## Functional Programming Techniques

### Function Composition

Function composition refers to composing complex functions by combining simpler functions.

```
Function<Double, Double> log = (value) -> Math.log(value);
Function<Double, Double> sqrt = (value) -> Math.sqrt(value);
Function<Double, Double> logThenSqrt = sqrt.compose(log);
logger.log(Level.INFO, String.valueOf(logThenSqrt.apply(3.14)));
// Output: 1.06
Function<Double, Double> sqrtThenLog = sqrt.andThen(log);
logger.log(Level.INFO, String.valueOf(sqrtThenLog.apply(3.14)));
// Output: 0.57
```

### Monads

Monad is an abstraction that allows structuring programs generically. So, a monad allows us to wrap a value, apply a set of transformations, and get the value back with all transformations applied.

There are three laws that any monad needs to follow — left identity, right identity and associativity

In Java, there are a few monads that we use quite often, such as __Optional__ and __Stream__:
```
Optional.of(2).flatMap(f -> Optional.of(3).flatMap(s -> Optional.of(f + s)))
```
- Optional<Integer> opt = Optional.of(2): It creates an Optional that contains the value 2. Optional.of() must NOT receive null.
- to access value use isPresent(): 
```
if (opt.isPresent()) {
    System.out.println(opt.get());
}
```

Why do we call Optional a monad?

Optional allows us to wrap a value using the method of and apply a series of transformations. We’re applying the transformation of adding another wrapped value using the method flatMap.

__Optional__
- Optional<T> is a container object that may or may not contain a value.
- Introduced in Java 8 to reduce NullPointerException
```
Optional<String> name = user.getName();
name.ifPresent(n -> System.out.println(n.toUpperCase()));
OR
opt.ifPresent(System.out::println);
```

### __::__ - method reference

- In Java, :: is called a method reference. It’s a shortcut for writing lambda expressions.
- Use this method as an implementation.
- It works only with __functional interfaces__ (like lambdas).

Instead of:
```
list.forEach(item -> System.out.println(item));
```

use:
```
list.forEach(System.out::println);
```

forEach() can be used on Iterable interface that is part of java.lang and is the root interface on any collection.

Types of method reference:
- Static Method Reference
  - ClassName::staticMethod
- Instance Method of a Particular Object
  - object::instanceMethod
- Instance Method of an Arbitrary Object of a Class
  - ClassName::instanceMethod

Example:
```
PrintStream printer = System.out;
printer.print("Hello");  // prints immediately

Consumer<String> consumer = printer::print;     // printer::print is a method reference. nothing is printed
consumer.accept("Hello"); // prints now

printer::print knows it takes a String because of the target functional interface.
Consumer<String> has one abstract method: void accept(String value);
```

Steps:
- Consumer<String> has one abstract method:
  - Java now asks: “Can printer.print(String) match accept(String)?”
  - If the method signature matches → ✅ compile success
    ```
    void accept(String value);
    ```

- A method reference can have 2 or more arguments — but ONLY if the target functional interface expects them.
  - Method Reference with TWO Arguments: BiConsumer<T, U>
    ```
    BiConsumer<String, Integer> biConsumer = printer::print;
    biConsumer.accept("Hello", 3);
    ```

- Method Reference with RETURN Value
    ```
    Calculator calc = new Calculator();
    BiFunction<Integer, Integer, Integer> addFn = calc::add;
    System.out.println(addFn.apply(2, 3)); // 5
    ```
- Method Reference with THREE Arguments
  - Java doesn’t provide a built-in one — but you can define your own
    ```
    @FunctionalInterface
    interface TriConsumer<A, B, C> {
        void accept(A a, B b, C c);
    }
    class Printer {
        void print(String msg, int count, boolean flag) {
            System.out.println(msg + " " + count + " " + flag);
        }
    }
    TriConsumer<String, Integer, Boolean> tri = printer::print;
    tri.accept("Hello", 2, true);
    ```

### Currying

Currying is a mathematical technique of converting a function that takes multiple arguments into a sequence of functions that take a single argument.

In functional programming, it gives us a powerful composition technique where we don’t need to call a function with all its arguments.

Moreover, a curried function does not realize its effect until it receives all the arguments.

```
Function<Double, Function<Double, Double>> weight = gravity -> mass -> mass * gravity;

Function<Double, Double> weightOnEarth = weight.apply(9.81);
logger.log(Level.INFO, "My weight on Earth: " + weightOnEarth.apply(60.0));

Function<Double, Double> weightOnMars = weight.apply(3.75);
logger.log(Level.INFO, "My weight on Mars: " + weightOnMars.apply(60.0));
```

Meaning of Function<Double, Function<Double, Double>> weight:
- A function that takes a Double, and returns another Function, which takes a Double and returns a Double


### Recursion

Recursion is another powerful technique in functional programming that allows us to break down a problem into smaller pieces. 

Instead of this:
```
Integer factorial(Integer number) {
    return (number == 1) ? 1 : number * factorial(number - 1);
}
```
Notice that we’re making the recursive call before calculating the result at each step or in words at the head of the calculation. 
So, this style of recursion is also known as __head recursion__.

A drawback of this type of recursion is that every step has to hold the state of all previous steps until we reach the base case. This is not really a problem for small numbers, but holding the state for large numbers can be inefficient.

A solution is a slightly different implementation of the recursion known as __tail recursion__. 
Here we ensure that the recursive call is the last call a function makes.

do this:
```
Integer factorial(Integer number, Integer result) {
    return (number == 1) ? result : factorial(number - 1, result * number);
}
```


## Lambda

```
parameter -> expression
OR
(parameter1, parameter2) -> expression
OR
(parameter1, parameter2) -> { code block }
```

### Using Lambda Expressions

#### Runnable
Instead of:
```
public class GFGRun implements Runnable { 
    public void run() { 
        System.out.println( "Running in Runnable thread");
    } 
} 
public class GFG {
    public static void main(String[] args) { 
        new Thread(new GFGRun()).start(); 
    } 
}
```
Use anonymous function (lambda):
```
public class GFG {
    public static void main(String[] args) {
        Runnable r = new Runnable() {
            public void run() {
                System.out.println( "Running in Runnable thread");
            }
        };
 
        r.run();
        System.out.println( "Running in main thread");
    }
}
```
Or better do this:
```
public class GFG {
    public static void main(String[] args) {
        Runnable r  = ()-> System.out.println( "Running in Runnable thread");
 
        r.run();
 
        System.out.println( "Running in main thread");
    }
}
```

#### Iterator

Instead this:
```
public class GFG {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(11, 22, 33, 44, 55, 66, 77, 88, 99, 100);
 
        // External iterator, for Each loop
        for (Integer n : numbers) {
            System.out.print(n + " ");
        }
    }
}
```

Do this:
```
public class GFG {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(11, 22, 33, 44, 55, 66, 77, 88, 99, 100);
 
        // Internal iterator
        numbers.forEach(number -> System.out.print( number + " "));
    }
}
```

And better:
```
public class GFG {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(11, 22, 33, 44, 55, 66, 77, 88, 99, 100);
 
        System.out.println( numbers.stream()
                .filter(number -> number % 2 == 0)
                .mapToInt(e -> e * 2)
                .sum());
    }
}
```

From the above code, we are not mutating any variable. 
Instead, we are transforming the data from one function to another. 
This is another difference between Imperative and Declarative. 
Not only this but also in the above code of declarative style, every function is a pure function and pure functions don’t have side effects


## Built-in java functional interfaces

Java SE 8 included four main kinds of functional interfaces which can be applied in multiple situations as mentioned below:
- __Consumer__: The consumer interface of the functional interface is the one that accepts only one argument or a gentrified argument. The consumer interface has __no return value__. 
```
Consumer<Integer> consumer = (value) -> System.out.println(value);
```
- __Predicate__: function that accepts an argument and, in return, generates a __boolean__ value
```
Predicate predicate = (value) -> value != null;

Predicate<String> p = (s) -> s.startsWith("G");
```
OR
```
Predicate<Integer> greaterThanTen = (i) -> i > 10;
Predicate<Integer> lowerThanTwenty = (i) -> i < 20; 
boolean result = greaterThanTen.and(lowerThanTwenty).test(15); 
```
- __Function__: receives only a single argument and returns a value after the required processing
```
Function<String, String> fun = s1 -> s1 + 2;
```
- __Supplier__:  does not take any input or argument and yet returns a single output.

## Optional

__Minimize the issues with null __

Java Optional is a way of replacing a nullable T reference with a non-null value. 
An Optional may either contain a non-null T reference (in which case we say the value is “present”), or it may contain nothing (in which case we say the value is “absent”).

Example:
```
Optional<Integer> optional = Optional.of(5);
optional.isPresent();          // returns true
optional.get();              // returns 5
 
Optional<Integer> optional1 = Optional.empty();
optional1.isPresent();          // returns false
```

Its purpose is to help design more-comprehensible APIs so that by just reading the signature of a method, we can tell whether we can expect an optional value.

# Java Streams

https://www.baeldung.com/java-8-streams

Stream API is used to process collections of objects. A stream in Java is a sequence of objects that supports various methods that can be pipelined to produce the desired result.

Streams in Java make data processing more efficient by supporting functional-style operations.

Features:
- A stream is not a data structure instead it takes input from the Collections, Arrays or I/O channels.
- Streams don’t change the original data structure, they only provide the result as per the pipelined methods.
- Each intermediate operation is lazily executed and returns a stream as a result, hence various intermediate operations can be pipelined. Terminal operations mark the end of the stream and return the result.

There are two types of Operations in Streams:
- Intermediate Operations
- Terminate Operations

Benefits:
- No Storage
- Pipeline of Functions
- Laziness
- Can be infinite
- Can be parallelized
- Can be created from collections, arrays, Files Lines, Methods in Stream, IntStream etc.

Intermediate Operations:
- map(): The map method is used to return a stream consisting of the results of applying the given function to the elements of this stream.
- filter(): The filter method is used to select elements as per the Predicate passed as an argument.
- sorted(): The sorted method is used to sort the stream.
- flatMap(): The flatMap operation in Java Streams is used to flatten a stream of collections into a single stream of elements. 
- distinct (): Removes duplicate elements.

Terminal Operations:
- collect(): The collect method is used to return the result of the intermediate operations performed on the stream.
- forEach(): The forEach method is used to iterate through every element of the stream.
- reduce(): The reduce method is used to reduce the elements of a stream to a single value
- count(): Returns the count of elements in the stream.

filter()
```
List<Integer> numbers = List.of(1, 2, 3, 4, 5);
numbers.stream()
       .filter(n -> n % 2 == 0)
       .forEach(System.out::println);
```

map()
```
List<String> names = List.of("john", "alice", "bob");
List<String> upper =
    names.stream()
         .map(String::toUpperCase)
         .toList();

System.out.println(upper);
```

reduce()
```
List<Integer> numbers = List.of(1, 2, 3, 4);

int sum =
    numbers.stream()
           .reduce(0, (a, b) -> a + b);

System.out.println(sum); // 10
```

## Streams vs Iterator

Iterator:
- allows you to traverse through a collection (e.g., List, Set, etc.) one element at a time.
- imperative control over iteration
- The Iterator is stateful: It maintains the position in the collection and you manually control its progression with hasNext() and next()
- Eager evaluation: The iterator fetches the next element immediately when next() is called
- Iterators are inherently sequential

Stream:
- sequence of data elements that can be processed in a functional and declarative manner.
- stateless: It represents a sequence of elements that are processed in a pipeline
- immutable: Streams don’t modify the source data; they return a new stream after each transformation
- Declarative processing: You define what you want to do with the elements (e.g., filtering, mapping, reducing), and the Stream API decides how to process them.
- functional-style operations such as map(), filter(), reduce(), and collect().
- lazy evaluation: Streams are evaluated lazily, meaning that intermediate operations (like map(), filter()) are not executed until a terminal operation (like collect(), forEach(), or reduce()) is invoked
- support short-circuiting operations such as findFirst(), anyMatch(), and allMatch()
- Streams have built-in parallelism support. By calling .parallel(), you can process elements in parallel without explicitly managing threads.


# java functional programming interview questions

## Name the four main categories of predefined functional interfaces in java.util.function.

- Function<T,R> → transformation (T → R)
- Predicate<T> → boolean test
- Consumer<T> → accepts T, returns nothing
- Supplier<T> → produces T, takes nothing

## Can a lambda throw a checked exception?

Only if the target functional interface declares it in its abstract method signature. 
Otherwise, you must wrap it in an unchecked exception or handle inside the lambda.

## When is a constructor reference especially useful?

When collecting to a list/set/map of new objects, e.g. list.stream().map(Person::new).collect(Collectors.toList())

```
List<String> names = Arrays.asList("John", "Jane", "Mark", "Sarah");

// Using a constructor reference to create a List of Person objects from a List of Strings
List<Person> persons = names.stream()
    .map(Person::new) // Constructor reference for the Person(String name) constructor
    .collect(Collectors.toList());

// Print the resulting list of Person objects
persons.forEach(System.out::println);
```

## What is the difference between Collection and Stream?

Collection: data structure that holds elements (eager, modifiable).
Stream: pipeline for processing elements lazily, once, not a data structure.

## Intermediate vs terminal operations — examples?

Intermediate (lazy, return Stream): filter, map, flatMap, distinct, sorted, peek
Terminal (trigger computation, return non-Stream): forEach, collect, reduce, count, anyMatch, findFirst

## What happens if you call a terminal operation twice on the same stream?

IllegalStateException — stream has already been operated upon or closed.

## Explain laziness in streams.

Intermediate operations are not executed until a terminal operation is called → allows short-circuiting and optimization.

## Difference between map() and flatMap()?

map() returns a single value for each input, resulting in a stream of the same size, 

flatMap() returns a stream (zero or more values) for each input, which are then merged or "flattened" into a single output stream

map → 1:1 transformation (Stream<T> → Stream<R>)

flatMap → 1:many + flatten (Stream<T> → Stream<Stream<R>> → Stream<R>)

## Explain groupingBy vs partitioningBy.

- partitioningBy() divides elements into exactly two groups based on a Predicate, 
- groupingBy() categorizes elements into multiple groups based on a general Function

groupingBy → groups by arbitrary key → Map<K, List<T>>

partitioningBy → predicate → splits into two groups → Map<Boolean, List<T>>

```
List<Person> people = new ArrayList<>();
people.add(new Person("Kosa", 21));
people.add(new Person("Saosa", 21));
people.add(new Person("Tiuosa", 22));
people.add(new Person("Komani", 22));
people.add(new Person("Kannin", 25));

// Using groupingBy: groups by an Integer key (age)
Map<Integer, List<Person>> peopleByAge = people.stream()
        .collect(Collectors.groupingBy(Person::getAge));

System.out.println("--- GroupingBy result (by age) ---");
System.out.println(peopleByAge);

// Using partitioningBy: partitions by a Boolean key (age >= 22)
Map<Boolean, List<Person>> partitionedPeople = people.stream()
        .collect(Collectors.partitioningBy(p -> p.getAge() >= 22));

System.out.println("\n--- PartitioningBy result (age >= 22) ---");
System.out.println(partitionedPeople);
```

## Common Optional methods chain (2026 style)?

opt.map(...).orElse(...).orElseThrow(...)

opt.filter(...).flatMap(...)

## Can you create a recursive lambda? How?

Yes — use Y combinator pattern or local variable with Supplier/Function.

Example: Function<Integer, Integer> fact = n -> n <= 1 ? 1 : n * fact.apply(n-1); (needs tricky self-reference)

## How to handle exceptions in streams/lambdas?

Wrap in unchecked (RuntimeException), or create custom functional interface that allows throws.

## show me example of java stream reading a large file

```
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class LargeFileReader {

    public static void main(String[] args) {
        Path path = Path.of("largefile.txt");

        try (Stream<String> lines = Files.lines(path)) {

            lines
                .filter(line -> line.contains("ERROR"))
                .forEach(System.out::println);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```