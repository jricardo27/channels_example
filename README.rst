================
Channels Example
================

The intent of this project is to run test examples using
ChannelLiveServerTestCase and Aloe.


Getting Started
---------------
1. Clone repository.

#. Init virtual environment, it will:

   - Create a Python 3.5 virtual environment.
   - Install all pip requirements.
   - Install NPM dependencies (Geckodriver, Chromedriver, PhantomJS)

   Run::

     . ./startenv

#. Create a Postgres database and update the connection details in
   `channels_example/settings.py`.

#. Run tests::

    ./manage.py harvest

   By default tests run using Firefox, it is possible to use Chrome::

    BROWSER_TYPE=chrome ./manage.py harvest

   or PhantomJS::

    BROWSER_TYPE=phantomjs ./manage.py harvest

