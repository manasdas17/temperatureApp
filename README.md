# temperatureApp

Quick demo with Python and Arduino for the IoT.

### DISCLAIMER
This version is a developer demo. The development is in a very early stage. Take caution.

## Instalation

Clone the repository in your localhost

```
git clone https://github.com/ricveal/temperatureApp.git
```

Install virtualenv:

```
pip install virtualenv
```

Add virtualenv to the cloned repository and enter in the folder using it:

```
virtualenv temperatureApp
cd temperatureApp
source bin/activate
```

You should see (temperatureApp) in front of your prompt.
Install all the required dependencies:

```
pip install -r requirements.txt
```

## Run the demo

You should change the config.json file (in the root directory) with your own properties, leaving "code" blank. It will be filled during the first launch.

Run the app with:

```
cd src
python server.py
```

There is not any implementation that manage the close so you have to exit pressing <ctrl> + c or killing the process.

Thank you!
