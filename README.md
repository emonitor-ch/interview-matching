# emonitor-interview


## Installation & Running

To run a solver, use:

```
python -m src
```

It will ask for size of square matrix (you can enter 3 for 3x3 matrix, 4 for 4x4 matrix and so on...)

When asked for choice, type `y`

You will see the output as in example below:

```
Please enter size of Square Matrix(for example, 3): 5
Do you want to randomly generate matrix elements? (y/n) y
The applicants matrix is: 
[4, 2, 1, 5, 3]
[2, 5, 3, 4, 1]
[4, 1, 5, 3, 2]
[2, 3, 5, 1, 4]
[4, 5, 1, 2, 3]
The apartments matrix is: 
[2, 1, 5, 3, 4]
[1, 5, 4, 2, 3]
[2, 4, 3, 1, 5]
[1, 4, 3, 5, 2]
[2, 4, 3, 5, 1]
Pairs are:
14
25
32
43
51
```

## Code Style

To stay consistent with development style, install all packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Use `black` to format code, `flake8` to check for warnings and errors and `isort`
to sort imports (*combined into one directive inside Makefile*):

```bash
make lint
```

## Testing

Use:

```bash
python -m unittest discover tests
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
