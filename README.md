# Djangular Authentication

This is a quick & dirty repo that shows code for a bare bones Angular application that invokes XHRs for registering a user, and then logging in a user.

## Setup

1. After you clone the repository, `cd` to the `quick/static` directory.
1. Run `npm install`.
1. Run `cd ../..` to get back to the project root directory.
1. Run `python manage.py migrate` to set up the database.
1. Then run `python manage.py runserver` to start the server.
1. Open your browser and hit `http://localhost:8000`.
1. Click the *Authenticate* link.
1. Click the *Register* button
1. If the registration of the user was successful, you will see a `{"success": true}` response.
1. Click the *Authenticate* link again
1. Click the *Login* button
1. If the authentication of the user was successful, you will see a `{"success": true}` response again

That's it.

