
# Python Semaphore Exercises

This repository contains Python exercises solving classic synchronization problems using semaphores and threads. Each exercise models a common concurrency problem using threads and semaphores to control shared resource access between processes.

## Content

1. **Queue (queue.py)**  
   Implements a synchronization system between leaders and followers, where both roles must coordinate to perform actions.

2. **Reader-Writer with Reader Priority (rwPR.py)**  
   Solution to the reader-writer problem, giving priority to readers. Readers can access concurrently, but writers must wait until there are no active readers.

3. **Reader-Writer with Writer Priority (rwPW.py)**  
   Similar to the previous one but gives priority to writers. Writers have exclusive access when they need to write.

4. **Unisex Bathroom (unisex.py)**  
   Models a unisex bathroom where men and women cannot be present simultaneously. Semaphores are used to coordinate user entry and exit.

5. **The Sleeping Barber Problem (barber.py)**  
   A classical solution to the sleeping barber problem, where a barber cuts hair for customers, sleeping when there are no customers and waking up when one arrives.

6. **Barrier Synchronization (barrier.py)**  
   Simulates a system where several cars must wait at a barrier until all arrive before proceeding.

7. **The Cannibals and Cook Problem (canival.py)**  
   A group of cannibals feeds from a shared pot. When the pot is empty, the cook is awakened to refill it.

8. **Water Molecule (h2o.py)**  
   Simulates the creation of water molecules from oxygen and hydrogen threads, ensuring each molecule has 2 hydrogen atoms and 1 oxygen atom.

9. **Roller Coaster (montana.py)**  
   Models a roller coaster ride where visitors must wait until enough passengers have boarded before the ride begins.

10. **Producer-Consumer (p_c.py)**  
   Implements the classic producer-consumer problem with a limited buffer. Producers generate data that consumers process.

## Requirements

Python 3.x is required to run the scripts.

## Execution

Each file is independent and can be run directly with Python:

```bash
python filename.py
```

Example:

```bash
python queue.py
```

## Contributions

Feel free to fork this repository and submit pull requests if you have improvements or new implementations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
