# SinequaPy
A python library to handle communication with Sinequa REST API. 
## Development
### Setup

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
pip install dist/<pkg>.tar.gz
```

Run tests
```
pytest -s tests/
```
This will run all tests in /tests folder.

or run a specific file using:
```
pytest -s tests/<file_name>.py
```



When new packages are installed, update requirements.txt using:
```
pipreqs --force
```

chmod +x build_and_install.sh


## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the authors of this repository before making a change.

`Tips:`
Make sure to name your branch as: `feature/{issue_number}/{branch-name}` and send a pull request to `develop` branch. Write quality commit messages. 

## License

Distributed under the terms of the [MIT license][license],
`sinequa_py` is free and open source software.

