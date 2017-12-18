# Day 18

Part I of day 18 was fairly straight forward. The bulk of the logic I pushed into a Compiler class
that could manage state and be aware of it's own next steps. Part II had some additional complexity
with the need to track messages between two instance of my Compiler--compilers also needed to be
aware of the address of their pair. A simple array served as my message queue. Note: I ran into
several small issues around remove the proper message from the queue and around ensuring that one
compiler could die and they other would continue processing.
