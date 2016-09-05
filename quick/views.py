from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import json

def index(request):
    """
    This class is for our Index.
    """
    template_name = 'index.html'
    return render(request, template_name, {})


def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    # Commit the user to the database by saving it
    new_user.save()

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    if authenticated_user is not None:
        login(request, authenticated_user)

        data = json.dumps({"success":True})
        return HttpResponse(data, content_type='application/json')

    else:
        data = json.dumps({"success":False})
        return HttpResponse(data, content_type='application/json')


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    print("authenticated_user", authenticated_user)

    # If authentication was successful, log the user in
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)

        data = json.dumps({"success":True})
        return HttpResponse(data, content_type='application/json')

    else:
        data = json.dumps({"success":False})
        return HttpResponse(data, content_type='application/json')


