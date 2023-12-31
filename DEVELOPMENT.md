# Developers Guide

## Setup

Create a virtual environment

```
python -m venv venv
```

Activate
```
source venv/bin/activate
```

Build library:
```
python setup.py sdist bdist_wheel
```

Install library:
```
./install.sh 
```

## Testing 
Run tests
```
pytest -s tests/
```
This will run all tests in /tests folder.

or run a specific file using:
```
pytest -s tests/<file_name>.py
```

## Tips 

- When new packages are installed, update requirements.txt using:
    ```
    pipreqs --force
    ```
- Make sure to name your branch as: `feature/{issue_number}/{branch-name}`
- Send a pull request to `develop` branch. 
- Write quality commit messages.
- Before merge, the `PR commits must be squashed` first.


## Publish to pypi 
See this [resource](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to learn more about how to publish this package to pypi.org 
