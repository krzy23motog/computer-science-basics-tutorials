# Java features anfter java 8


## Collection Factory Methods

Allow you to create immutable or mutable collections in a simple, concise, and often more readable manner.
- List.of(): Creates an immutable List
- Set.of(): Creates an immutable Set
- Map.of(): Creates an immutable Map

## var - Local Variable Type Inference

Allows you to declare a local variable without explicitly specifying its type
- type of the variable is automatically inferred. You cannot use var without initializing the variable because the type must be deduce


## Switch Expressions

## Records and Record Patterns

Provide a compact syntax for creating classes whose primary purpose is to hold data. 
The main idea behind records is to provide a lightweight data structure for encapsulating immutable data without the need to manually write boilerplate code (such as constructors, equals(), hashCode(), and toString()).

```
public record Person(String name, int age) {
    public String greet() {
        return "Hello, my name is " + name;
    }
}
```

The record Person automatically defines:
- Final fields (name and age).
- A canonical constructor to initialize those fields.
- Getters for each field (name() and age() methods).
- equals(), hashCode(), and toString() methods automatically.

No Boilerplate Code: Java records automatically generate common methods such as equals(), hashCode(), toString(), and accessors for the fields.

Immutability: The fields in a record are immutable, making them ideal for use cases where data integrity is important.

## Sealed Classes

A sealed class allows you to control the inheritance hierarchy, offering more control over class extensions than traditional classes.

## Virtual Threads

## Sequenced Collections

guarantee the order of elements

# Interview questions

## java Data Structures & Algorithms interview questions

### array and an ArrayList

- Arrays have a fixed size, whereas ArrayLists can dynamically grow or shrink.
- Arrays can store elements of any type, whereas ArrayLists only store objects.

### find the largest element in an array


```
public int findLargest(int[] arr) {
    int largest = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
}
```

with streams
```
int[] arr = {3, 8, 1, 9, 4, 12, 7, 2};
int max = Arrays.stream(arr).max().getAsInt();

// Even shorter (if you're sure array is not empty)
int max2 = Arrays.stream(arr).max().orElseThrow();
```

### HashMap vs TreeMap

A HashMap does not maintain any order of the keys, whereas a TreeMap stores keys in sorted order according to their natural ordering or by a comparator provided at map creation.

### Merge Sort vs Quick Sort vs Bubble Sort

-  Merge Sort is a divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves. It has a time complexity of O(n log n).
-  Quick Sort is a divide-and-conquer algorithm that selects a pivot element, partitions the array into elements less than the pivot and greater than the pivot, and then recursively sorts the two subarrays. Its average time complexity is O(n log n).
- Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps

### Can abstract class have constructor?

Yes — used to initialize common fields for subclasses

### What happens if two default methods in interfaces conflict?

Implementing class must override the conflicting method.

### If two objects are equal according to equals(), must they have the same hashCode()? Vice versa?

Yes — if a.equals(b) → a.hashCode() == b.hashCode() (contract)
No — same hashCode does not imply equal (only reduces collisions)

### Why should you almost always override hashCode() when you override equals()?

Because HashMap/HashSet/etc. use hashCode() first to find bucket → if hashCode is inconsistent with equals, you can get logically duplicate entries or fail to find existing objects.

### Can record classes (Java 16+) override equals(), hashCode(), toString()?

Yes — you can provide custom implementations.
But if you do, you lose the automatic canonical/structural equality behavior — so usually people don't.

### passing in java: is it pass by reference or by value

Java uses only pass-by-value

__Java always passes a copy of the value of the argument to the method.__

What that "value" actually contains depends on whether the argument is a primitive or a reference type:
- primitive: copy of the actual value (int, double, boolean…)
- object reference: copy of the reference (the memory address)
- You cannot reassign the caller's variable to point to a different object

### what are checked and unckecked exceptions

