## Build and test the application using docker
Use this commands to build a docker image and run it locally to test the application
### Building the image

```docker build . -t fastapi-app-test```

### Running the image locally

```docker run --rm -p 5000:5000 fastapi-app-test```

You should see uvicorn logs in your terminal indicating that the application started successfully

````
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
````

and you may visit the documentation in the browser of your choice to check that everything is working fine

http://localhost:5000/docs