# Building-a-maze
Start with a complete n-by-n grid. Repeatedly remove a horizontal or vertical segment from the collection picked randomly, until a path opens up between the upper left and the lower right grid cells


This is a programming exercise. Please submit the source code electronically and a brief description of your approach (an extra description is not needed if the code is well-commented and/or self-explanatory). You should also submit the output (for
some reasonable size, say n = 60).
Start with a complete n-by-n grid, i.e. the collection of horizontal segments between (i; j); (i + 1; j), for i = 0; : : : ; n − 1, j = 0; : : : ; n, and vertical segments between (i; j); (i; j + 1), for i = 0; : : : ; n, j = 0; : : : ; n−1. Repeatedly remove a horizontal or vertical segment from the collection picked randomly (but excluding the segments on the boundary), until a path opens up between the upper left and the lower right grid cells (see figure for example with n = 4).

![image](https://github.com/user-attachments/assets/055bc0c4-7fbd-4fdf-92f3-be26d2aac545)

For extra credit, experiment with ideas that would make the maze more difficult or interesting to solve.
The goal of the exercise is to think about efficient data structures and algorithms for the task. (You can of course use the data structures provided by the programming language/library you use, but think of how they may be implemented at a lower level and how that affects efficiency.) In particular, studying and using a union-find data structure may be helpful.
