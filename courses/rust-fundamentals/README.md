# Rust Fundamentals

```aiignore
https://app.pluralsight.com/id/signin?redirectTo=https%3A%2F%2Fapp.pluralsight.com%2Flibrary%2Fcourses%2Ffundamentals-rust
```

Rust is a `Static` and `Strong` programing language.

## How programing languages are:

### Data types
- Static - We know all of the data types at compile time
- Dynamic - We only know the data types at run time

### Enforcements
- Strong - Enforces rules on data type assignments
- Weak - Has Few or no enforcement on data type assignments

### Compilation
- Compiled, used to be faster
- Interpreted, slower since bit code in generated on each execution. More portable since they are "compiled" at run time

### Memory
- Stack - pila, last in last out, when stack overflow happens, to many data -> we use the heap
- Heap - has a pointer pointing to the data in memory 

![](./png/stack-heap.png)

## Rust Key concepts

- Most of the variables cannot change their value, you can handle this creating `mutable` variables, but they are not the default one.
- `Ownership and Burrowing`, Core rust memory management
- `Associated methods`, method associated to a data structure
- `Crates`, modules
- `Macros`, (!) primitive functions 

## Rust Toolchain

Toolchain components:

- Rust Compilet
- Cargo (package manager)

[Rustup](https://rustup.rs/), a toolchain management utility

## Bynary command

```
> rustc
```

## Sections:

- [Data Types](#section-data-types)
- [Variables](#section-variables)

### Section: Data Types

#### Scalar, holds a single value

##### Primitives
- Integers
- (u)unsiged 0 - 255
- (i)signed -128 127 
- isize, usize - related to the CPU architecture
- floating points - singed

##### Bolean
- True / False

##### Characters
- A, B, C (ASCII)

Rush uses 4 Bytes, 4.294.967.296, characters in Unicode-32 table, basically support everything

#### Compound, holds multiple values in a single variable

##### Array
- Multiples values of a single data types

##### Tuple
- Multiples values of different data types

Array and Tuples has a FIXED size

#### Strings

We have two alternatives:

##### String, notice the capital S
- mutable
- u8 data vector
- stored on the heap

##### &str (hardcoded string)
- Immutable
- u8 data vector
- stored on the heap/stack or compiled code

### Section: Variables
