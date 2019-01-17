# X Total Shapes
> URL: https://practice.geeksforgeeks.org/problems/x-total-shapes/0

## Solution

**Time Complexity**: O(n*m)
**Details**: BFS only when find a X vertex. Enqueue only X vertex not visited.
**Status**: Correct.
**Level**: Medium.

## Description

Given N * M string array of O's and X's.
Return the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

Example (1):
```
OOOXOOO
OXXXXXO
OXOOOXO

answer is 1 , shapes are  :

(i)     X
    X X X X
    X     X
```

Example (2):
```
XXX
OOO
XXX

answer is 2, shapes are

(i)  XXX

(ii) XXX
```

**Input**:
The first line of input takes the number of test cases, T.
Then T test cases follow. Each of the T test cases takes 2 input lines.
The first line of each test case have two integers N and M.The second line of N space separated strings follow which indicate the elements in the array.

**Output**:

Print number of shapes.

**Constraints**:

1<=T<=100

1<=N,M<=50

Example:

Input:
2
4 7
OOOOXXO OXOXOOX XXXXOXO OXXXOOO
10 3
XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO

Output:
4
6