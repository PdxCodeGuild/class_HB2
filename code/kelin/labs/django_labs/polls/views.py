from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#     Create the following views:

# Register /register/
# form for creating a new user
# redirect to /profile/ after registering
# Login /login/
# form for logging a user in
# redirect to /profile/ after logging in
# Profile /profile/
# a protected page only logged in users can see
# just show a welcome message for now