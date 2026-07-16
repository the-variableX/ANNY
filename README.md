# ANNY

A Python toolkit implementing fundamental linear algebra operations from scratch.

## About

It is a collection of functions that perform fundamental matrix operations like row reduction, determinant computation, solving linear system of equations.

This project was built for learning and understanding the implementation of linear algebra algorithms from first principles, without relying on external numerical libraries such as NumPy.

## Features

- Basic matrix operations (addition, subtraction, multiplication)
- Matrix Transpose 
- Row Echelon Form (REF)
- Row Reduced Echelon Form (RREF)
- Rank and nullity
- Matrix inverse
- Linear system solver
- Matrix determinant computation
- Column space basis
- Row space basis
- Null space basis

## Usage

- Import the ANNY Python file and call the required function.
  
  Example:
  
  ```python
  a = ref()
  ```
- Matrices are entered row by row. Use commas to separate elements in a row.

  Example:

  ```python
  your row1:1,2,3
  your row2:4,5,6
  your row3:7,8,9

  This would correspond to:
  
  matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
  ]
  ```
  
## Requirements

- Python 3.14

## License

This project is licensed under the MIT license.
