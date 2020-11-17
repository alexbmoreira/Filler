# Filler

A filler game played against a computer.

## Running the Flask server

Use a virtual environment and pip install dependencies:

```shell
python3 -m venv .venv
source .venv/bin.activate
python3 -m pip install -r requirements.txt
```

Within the virtual environment, run the server:
```shell
export FLASK_APP=run.py
flask run
```

## Testing

```shell
pip install -e .
```

This is equivalent to running

```shell
python setup.py develop
```

and will install filler as a package