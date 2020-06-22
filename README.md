# Solving N-Queens using a genetic algorithm

## What?
![image](https://miro.medium.com/max/914/1*SVCP2lIp1jfzJuQn_QUeVg.png "nQueens")  
Here is a [wiki article](https://en.wikipedia.org/wiki/Eight_queens_puzzle) about the problem.
In short, we are trying to place N Queen chess pieces on an N x N board so that none of them can attack each other. 
If you aren't familiar with the game of chess a Queen piece can move horizontally, vertically, and diagonally.  


## How?
An optimal solution uses backtracking on the placement of each queen in order to find an optimal solution.  
But I will roughly follow [this](https://arxiv.org/ftp/arxiv/papers/1802/1802.02006.pdf) research article in order to solve it.
 

## Why?
I apply evolution theory to everything in life even when it doesn't make sense.
Charles Darwin would've wanted it this way.

## Enjoy!

#### Further Improvements
- incorporation of async processing
- ~~time complexity of Individual.get_score()~~
- ~~introduce backtracking algorithm for comparison~~
- ~~random "brute force" method~~
- improve mutation to avoid local minima
- "publish" completion time for each method
- graph the performance of genetic algorithm with matplotlib

#### Known Issue...
- evolution stagnates with high N value and low population
- need a way to quantify results
