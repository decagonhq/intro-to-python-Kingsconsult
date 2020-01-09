## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing


## Understanding SOLID principles

S.O.L.I.D
- S - SRP: Single Responsibility Principle
- O - OCP: Open-Closed Principle
- L - LSP: Liskov Substitution Principle
- I - ISP: Interface Segregation Principle
- D - DIP: Dependency Inversion Principle

Single Responsibility Principle: 
This principle talks about writing your class or module in such a way that it has one responsibility or functionality
example
1. A dog class should only create a dog not bothering of creating a goat
2. A dog method bark(), should give the dog ability to bark and not running
3. A function add, should bother about adding numbers not adding and subtracting

Open-Closed Principle: 
This principle talks about a function, class or module only give ability to other class, method or module to add more functionalities 
to it, but not giving ability to modify it
example
1. An arithmetic class that have a method add, can allow a method subtract to be added to it, but not telling it to abandon arithmetic 
   and start doing geometric
2. An addition function that only accepts two parameter can be extended to accept three parameters, but not start doing subtraction
3. A dog class can accept speech method, but not modifying its species type to reptile

Liskov Substitution Principle: 
This principle in OOP deals with overriding methods, attributes, class etc
- It states that derived classes must be substitable for thier base classes
- Any derived class should be able to substitute its parent class without distroying the parent
- Every part of the code should get the expected result no matter what instance of a class you send to it
example
1. Given an addition class that adds two parameter, a child can inherit from the parent and override its rules to add more than two parameter
2. Given a cloths class with attributes of price, a child pants can substitute the price for discount_price

Interface Segregation Principle: 
This principle states that do not add additional functionality to an existing interface by adding new methods
- It means that, do not force a function, class, module to depend on methods it does not use
- A client should never depend on anything more than the method it is calling
- Changing one method in a class shouldn't affect classes that don't depend on it 
example
1. The plant class does not need speak mthod, so it should not be added
2. The addition class should not be force to do subtraction

Dependency Inversion Principle: 
This principle states that High-level modules should not depend on low-level modules. Both should depend on abstractions
- Abstractions should not depend on details. Details should depend on abstractions
- Never depend on anything concrete, only depend  on abstractions
- Able to change on implementation easily without altering the high level code
example
1. The window operating system should not depend on microsoft word to power on
2. The Arithmetic class should not depend on addition method to do subtraction