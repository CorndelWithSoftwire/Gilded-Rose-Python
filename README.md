# Gilded-Rose-Kata

Edited from https://github.com/emilybache/GildedRose-Refactoring-Kata

## Setup
Everything in this project is part of the Python standard library, so there are no dependencies to install.

To run the tests, run the `golden_master_test.py` file.
```shell script
python golden_master_test.py
```

This should output that it ran 1 test, and the overall result was 'OK'.

## Notes on the "solution"

This is just a possible refactor; there are definitely aspects that can be debated.

But some thoughts:
- The main aim is to make the code clearly map to business logic and generally be a bit easier to read
- A result of that is it's easier to modify the functionality for different item types or add new types
- It is far from a perfect solution, but mostly because of the limitation of only modifying `GildedRose`. In reality you might consider writing subclasses of Item for the different types, or at least put some properties/methods on the Item class.
- The main point of the exercise was not to reach some goal but the process of small incremental improvements, frequently running the test, and frequently making small, self-contained commits)
