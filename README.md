# Memory-Managment  

The main memory is 4MB which is being allocated for user space. The page size is 8KB. The main memory will be divided into 8 blocks of 4 pages each, 16 blocks of 8 pages each, 16 blocks of 16 pages each, 2 blocks of 32 pages each.

Free Memory Tracking Algorithm: A free bitmap is used to maintain the status of free memory available for use by the set of processes being executed. 
This system is using pages of equal size and one bit or page frame shows the state of each page i.e. whether the page is currently free or not. 
The free memory blocks are monitored by a linked list.

Memory Allocation Algorithm -> Next Fit: Next Fit checks every available block in the main memory starting from the next available after the most recent allocation. 
It treats the blocks as a loop and searches through them until the original block is reached again.

Page Replacement Algorithm->Second Chance: The Second Chance Algorithm allows for the repeated reuse of pages in memory. 
It acts as an extension of the First in First Out algorithm where a page from the head of a queue is allocated to a process. 
A bit known as the accessed bit is examined. If the accessed bit is 0, then the page hasn’t been used in the most recent clock cycle interval and is swapped out. 
If it is 1 then the bit is reset to 0 and the page is added back into the queue at the tail and the page replacement algorithm is repeated. The queue is examined a second time to return data about available pages. 
This algorithm operates under Least Recently Used.
