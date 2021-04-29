# rest_framework_simplejwt_RS256
demo project that demonstrates protecting restful endpoints with the rest_framework_simplejwt 4.6.0 AUTH library

This is a demo project of the django-rest-framework-jwt capabilities by JPadilla. 

Documentation for django-rest-framework-jwt is available at:

https://github.com/jpadilla/django-rest-framework-jwt
https://github.com/jpadilla/django-rest-framework-jwt/issues/484
https://jpadilla.github.io/django-rest-framework-jwt/
https://www.techiediaries.com/django-rest-framework-jwt-tutorial/
https://medium.com/@msum_t/jwt-auth-implemention-with-django-rest-framework-6e9d4b603c1c

This library is unmaintained and is used by the newer framework djangorestframework-simplejwt at:

https://github.com/jazzband/django-rest-framework-simplejwt
The documentation for the maintained version is at:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

The demo projects shows 3 basic RS256 jwt capabilities:
1. Obtain an access token.( with valid username and password ).  This url will return an access token and a refresh token to refresh the access token when it expires.  Remember that a new access token can be generated using the refresh token unless the refresh token has not expired.  The lifetime of a refresh token is typically longer than the lifetime of an access token.  If the refresh token is expired a new access token must be issued by submitting login credentials.  The url for obtaining an access/refresh token (server running at port 8088 ): http://localhost:8088/users/api-token-auth/
2. Refresh access token ( using the refresh token obtained in step 1 ) The url for obtaining a new access token posting the refresh token (server running at port 8088 ): http://localhost:8088/users/api-token-refresh/
3. Verify token ( using the access token from step 1 or step 2 ) The url for obtaining a token (server running at port 8088 ): http://localhost:8088/users/api-token-verify/

You can easily test if the endpoint returns a response by submitting the following commands in your terminal.  Remember that you must have a user created with the username admin and password password123.  
This is done by issuing the command:  python manage.py createsuperuser in the project directory where manage.py is located.  Follow the prompts and add a superuser with name admin and password password123.

$ curl -X POST -d "username=admin&password=password123" http://localhost:8088/users/api-token-auth/
Alternatively, you can use all the content types supported by the Django REST framework to obtain the auth token. For example:

$ curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"password123"}' http://localhost:8088/users/api-token-auth/

Pass in an existing token to the refresh endpoint as follows: {"token": EXISTING_TOKEN}. Note that only non-expired tokens will work. The JSON response looks the same as the normal obtain token endpoint {"token": NEW_TOKEN}.

$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8088/users/api-token-refresh/

Passing a token to the verification endpoint will return a 200 response and the token if it is valid. Otherwise, it will return a 400 Bad Request as well as an error identifying why the token was invalid.

$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8088/users/api-token-verify/

Prerequisite for the obtaining a token:
The username and password for the user requesting a new token must already exist in the django Users database.  For this, run the 'python manage.py createsuperuser' command
to create a user first.

The project also offers 2 services:
1. The hello service ( returns the message Hello )
2. The students service ( view/update/delete/modify students).


Current unresolved capabilities:
The framework will authorize access to the hello and student service in curl commands when the RS256 token is set in the Authorization Bearer header of the request.
The framework DOES NOT authorize access to the hello and student services when when requests for the hello and students resources are submitted via browser.  
The framework WILL NOT automatically authorize users when accessing the endpoints via URL in a web page:

1. http://localhost:8088/hello/
2. http://localhost:8088/students/
3. http://localhost:8088/students/1

When these endpoints are accessed, an error message is returned, even after succesful authentication/authorization.  "detail": "Authentication credentials were not provided."

With curl, the http requests with the token in the Authorization header are susseccuful.  In order to access protected api urls you must include the Authorization: JWT <your_token> header.  JWT to prefix the authorization token is the default prefix.  The default prefix can be overridden in settings.py with JWT_AUTH_HEADER_PREFIX = 'Bearer'.

$ curl -H "Authorization: JWT <your_token>" http://localhost:8088/hello/

$ curl -H "Authorization: JWT <your_token>" http://localhost:8088/students/

$ curl -H "Authorization: JWT <your_token>" http://localhost:8088/students/1/

If in settings.py you have overridden JWT_AUTH_HEADER_PREFIX = 'Bearer', then the api call with curl will be:

$ curl -H "Authorization: Bearer <your_token>" http://localhost:8088/hello/

Read default AUTH settings in the documentation page for djangorestframework-jwt at:

