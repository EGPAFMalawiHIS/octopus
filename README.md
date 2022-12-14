<p align="center">
    <img src="./octopus/static/images/icons/octopus-64.png" alt="Octopus Icon">
    <h3 align="center">Octopus</h3>
    <p align="center">
        System integration solution for regions with unstable connectivity.
    </p>
</p>

# Octopus

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![EGPAF Devs](https://img.shields.io/badge/egpaf-devs-blue)](https://pedaids.org/project/improving-quality-of-care-and-health-impact-through-innovative-systems-and-technologies-in-malawi-health-information-systems-his-cdc/)
![CI](https://github.com/EGPAFMalawiHIS/octopus/actions/workflows/ci.yml/badge.svg)
![What's deployed on dev,stage,prod?](https://img.shields.io/badge/whatsdeployed-dev,stage,prod-green.svg)

License: MIT

## Settings

[TODO] add available settings via .env.

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

        python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    mypy octopus

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    coverage run -m pytest
    coverage html
    open htmlcov/index.html

#### Running tests with pytest

    pytest

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker
