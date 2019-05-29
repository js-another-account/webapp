Sample Webapp
======

[![Build Status](https://travis-ci.com/js-another-account/webapp.svg?branch=master)](https://travis-ci.com/js-another-account/webapp)

This is a sample web-api written in Python and Flask. It is meant to be lightweight and extensible.

API
------

  * `/` - returns status 200 and a string
  * `/healthcheck` - returns a JSON with the app version, GIT commit sha and a description

Running locally
------

This repository has continuous integration via Travis CI, which automatically runs Python linter and the tests suite, build a Docker image and pushes it to Docker Hub. To see build status click on the badge above. 

If you desire so, you can run the app locally:

1. Activate you Python virtual environment
2. Run `pip install -r requirements.txt`
3. To run tests execute: `python -m unittest -v`
4. Run the app: `python ./server.py`

Running image from Docker Hub
------

The Docker Hub page for this app you can find at https://hub.docker.com/r/jsanotheraccount/webapp

To run the latest version of the image execute `docker run -p 8000:8000 jsanotheraccount/webapp:latest`

Known issues and risks
------

1. Current version only contains unit tests for the code. It would be nice to have integration testing as well
2. The way how the GIT commit sha gets passed down to the app could be more elegant
3. Docker image needs to be scanned for vulnerabilities