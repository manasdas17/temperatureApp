# temperatureApp

Quick demo with Python and Arduino for the IoT.

### DISCLAIMER
This version is a developer demo. The development is in a very earlier stage.

## Instalation

Clone the repository in your localhost

Install virtualenv:

```
pip install virtualenv
```

Add virtualenv to the cloned repository:

```
virtualenv temperatureApp
```

Install all the required dependencies:

```
pip install -r requirements.txt
```

## Run the demo

You should change the config.json file with your own properties, leaving "code" blank. It will be filled during the first launch.

Run the app with:

```
python server.py
```

There is not any implementation that manage the close so you have to exit pressing <ctrl> + c or killing the process.

Thank you!
