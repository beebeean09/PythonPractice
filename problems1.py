Q1: given a graph of nodes, like
A E
A : B C D
B : C
C : E
D : B
Find all the paths from start node (A in the example) to end node (E in the ex).

Q2:
Given an input file, like
(11/01/2015-04:00:00) :: START
(11/01/2015-04:00:00) :: CONNECTED
(11/01/2015-04:30:00) :: DISCONNECTED
(11/01/2015-04:45:00) :: CONNECTED
(11/01/2015-05:00:00) :: SHUTDOWN
Find the portion of connected time.

def connection(time)
