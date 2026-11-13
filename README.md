# Campus-Library-Manager

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

`LibraryItem` is abstract because it provides common properties and methods for all library items but requires every child class to implement its own `late_fee()` method. If the `DVD` class does not implement `late_fee()`, Python will treat DVD as an abstract class, and creating a DVD object will raise a `TypeError`.

## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access `item.__available` from outside the class, Python raises an `AttributeError` because double underscores trigger name mangling. We use `is_available()` to check availability safely without directly accessing or modifying the private attribute.

## 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the `LibraryItem` child classes, and it keeps track of the total number of items created. In contrast, `self.title` is an instance attribute, meaning each individual object has its own title, which can be different from other objects.
