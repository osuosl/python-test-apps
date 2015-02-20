A collection of very tiny Python apps. Used to test the osl-application-python
deployment cookbook (https://github.com/osuosl-cookbooks/osl-application-python).

test_django
===========

The test_django project has three special features used in the tests.

Firstly, it removes syncdb. This is to simulate Django 1.9's removal of the feature,
and to make sure the cookbook continues to work as expected with `migrate`.

Secondly, it adds a custom_collectstatic. When run, this puts a `custom_collectstatic` file
in the root of the django project. (The STATIC_ROOT directory is set to BASE_DIR/static_files.)

Lastly, it contains a `custom_requirements.txt`, containing additional packages. This allows
testing for the existence of these additional packages when using the custom requirements.txt
file command.
