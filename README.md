## Development

**sinequa** : This package allows pythonic communication with Sinequa REST API.



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
