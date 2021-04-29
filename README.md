# rest_framework_simplejwt_RS256
demo project that demonstrates protecting restful endpoints with the rest_framework_simplejwt 4.6.0 AUTH library

Documentation for rest_framework_simplejwt is available at:

https://pypi.org/project/djangorestframework-simplejwt/
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#

Example projects:

https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8
https://blog.miguelgrinberg.com/post/json-web-tokens-with-public-key-signatures
https://www.django-rest-framework.org/api-guide/authentication/

This library is maintained and is a spin-off of the unmaintained framework djangorestframework-jwt by jpadilla.

To run this project:

1. create a virtual environment and activate it
2. Install the following libraries with the command pip install <library-name>:
Django==3.2
  
django-filter==2.4.0

djangorestframework==3.12.4

djangorestframework-simplejwt==4.6.0
  
3. Check out the project
4. Create a database with name <databasename>.  Postgres configuration is in settings.py
5. cd to the directory that contains manage.py
6. run the following commands:
python manage.py makemigrations
  
python manage.py migrate

python manage.py createsuperuser (enter the username & password to use when requesting a token)

python manage.py runserver 8088

The rest_framework_simplejwt_RS256 demo project shows 3 basic AUTH RS256 jwt capabilities:

1. Obtain an access token.( with valid username and password ).  This url will return an access token and a refresh token to refresh the access token when it expires.  Remember that a new access token can be generated using the refresh token if the refresh token has not expired.  The lifetime of a refresh token is typically longer than the lifetime of an access token.  If the refresh token is expired a new access token can be obtained by submitting login credentials on the request token url.  The url for obtaining an access/refresh token (server running at port 8088 ): http://localhost:8088/api/token/

2. Refresh access token ( using the refresh token obtained in step 1 ) The url for a new access token by posting the refresh token (server running at port 8088 ): http://localhost:8088/api/token/refresh/

3. Verify token ( using the access token or the refresh token from step 1 or step 2 ). The url for verifying a token (server running at port 8088 ): http://localhost:8088/api/token/verify/
   If the token is valid or not expired, an empty response is returned.  Otherwise, an error message is returned.

You can easily test if the endpoint returns a response by submitting the following commands in your terminal.  Remember that you must have a user created with the username admin and password password123 for the request to work.  
Create an account with username and password by issuing the command:  
python manage.py createsuperuser in the project directory where manage.py is located.  
Follow the prompts and add a superuser with name admin and password password123.

Test Obtain Token:
$ curl -X POST -d "username=admin&password=password123" http://localhost:8088/api/token/

{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTcxMjM3MiwianRpIjoiMGYyMTUwNmM1ZWE4NGE3M2EyZDMwYzRhMzEwNDQ1ODEiL
CJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1vbmljYSIsInN1YiI6Ik1wZGJVc2VyIiwiYXVkIjoiTXBkYlVzZXJzIiwiaXNzIjoiTXBkYlJlc3RBUEkifQ.FGFY4SjvjqU852IBHAhCpqjww21dvcML8AqgavXY
kRYYShsTH9Egp3vYwHR0DsmQr9chbDuLDyRDxkO_Q9HxoQ","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzExNzcyLCJqdGkiOiI
zODYxODNkMjNhNDY0MTYxOWUwNjZmMmUwMjdkZTAwMyIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoibW9uaWNhIiwic3ViIjoiTXBkYlVzZXIiLCJhdWQiOiJNcGRiVXNlcnMiLCJpc3MiOiJNcGRiUmVzdEFQS
SJ9.kY5kRcT-FKg6z4hfS8Yt7RoNpBsWhptre_f5MMLBxGcD51dPAMs88d2TXi63D2F5LDTaVoQiNvr687rBDxHiiQ"}

Test Obtain Token:
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"password123"}' http://localhost:8088/api/token/

{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTcxMjQ5MCwianRpIjoiY2QzMjAzYTg2MzA5NGRhMmE1NDc2ZmEzYzRmYjY3MzQiL
CJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1vbmljYSIsInN1YiI6Ik1wZGJVc2VyIiwiYXVkIjoiTXBkYlVzZXJzIiwiaXNzIjoiTXBkYlJlc3RBUEkifQ.XL6pk-_eG72xY-rmn8c-zE1d6KI9qkgjv7bvW2q6
jBRjKe4qUcIDhWEssPchYYa79oKAHsPofGPFfxS7FSUNCA","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzExODkwLCJqdGkiOiJ
lNzA3MGM3ZjBkZjM0ZTg1OGRlZmRmY2RiOTQxZDBkMCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoibW9uaWNhIiwic3ViIjoiTXBkYlVzZXIiLCJhdWQiOiJNcGRiVXNlcnMiLCJpc3MiOiJNcGRiUmVzdEFQS
SJ9.DvEd2CnEp6cHR2Oj63jMf66WZ572jkD41qUWY4Iqb4ZrYdSu492TwwxDpV1Lf2l6-XHOpnAiQSAwxkx1f0NpNA"}

Test Token Refresh by posting the refresh token from Otain Token:
$ curl -X POST -H "Content-Type: application/json" -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTcxMjQ5MCwianRpIjoiY2QzMjAzYTg2MzA5NGRhMmE1NDc2ZmEzYzRmYjY3MzQiLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1vbmljYSIsInN1YiI6Ik1wZGJVc2VyIiwiYXVkIjoiTXBkYlVzZXJzIiwiaXNzIjoiTXBkYlJlc3RBUEkifQ.XL6pk-_eG72xY-rmn8c-zE1d6KI9qkgjv7bvW2q6jBRjKe4qUcIDhWEssPchYYa79oKAHsPofGPFfxS7FSUNCA"}' http://localhost:8088/api/token/refresh/

{"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzEyMjY4LCJqdGkiOiIyODlkMjkwY2RiNjY0MTJjYTUzNzVjMDcwMGY0ODUwMCIsIn
VzZXJfaWQiOjEsInVzZXJuYW1lIjoibW9uaWNhIiwic3ViIjoiTXBkYlVzZXIiLCJhdWQiOiJNcGRiVXNlcnMiLCJpc3MiOiJNcGRiUmVzdEFQSSJ9.ppPOSPGZf4tDkijRfBjuMutpu0yhtK2Z_ZdOyTqsbU1
q5tRUZsaciysmFUEKKwjvg4LQaYPF7BPyKeqR6-_U3w","refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTcxMjg2OCwianRpIjoiN
DVkMDJjZmU3YzAzNGEzNmI0N2Y0ODhlOGQwZDlmMDYiLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1vbmljYSIsInN1YiI6Ik1wZGJVc2VyIiwiYXVkIjoiTXBkYlVzZXJzIiwiaXNzIjoiTXBkYlJlc3RBUEk
ifQ.v0_ZHtRGBeaLW1IDcxcJeTDK1YT0Ne4QPgnrYQwnKkj_diDc8LB9SPwmJeN4kBvmH57miHR0QnW26ScA9us74g"}

Test access token verify:
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTcxMjQ5MCwianRpIjoiY2QzMjAzYTg2MzA5NGRhMmE1NDc2ZmEzYzRmYjY3MzQiLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1vbmljYSIsInN1YiI6Ik1wZGJVc2VyIiwiYXVkIjoiTXBkYlVzZXJzIiwiaXNzIjoiTXBkYlJlc3RBUEkifQ.XL6pk-_eG72xY-rmn8c-zE1d6KI9qkgjv7bvW2q6jBRjKe4qUcIDhWEssPchYYa79oKAHsPofGPFfxS7FSUNCA"}' http://localhost:8088/api/token/verify/
{}

Test refresh token verify:
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzEyMjY4LCJqdGkiOiIyODlkMjkwY2RiNjY0MTJjYTUzNzVjMDcwMGY0ODUwMCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoibW9uaWNhIiwic3ViIjoiTXBkYlVzZXIiLCJhdWQiOiJNcGRiVXNlcnMiLCJpc3MiOiJNcGRiUmVzdEFQSSJ9.ppPOSPGZf4tDkijRfBjuMutpu0yhtK2Z_ZdOyTqsbU1q5tRUZsaciysmFUEKKwjvg4LQaYPF7BPyKeqR6-_U3w"}' http://localhost:8088/api/token/verify/
{}

Test an invalid/expired token:
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzEyMjY4LCJqdGkiOiIyODlkMjkwY2RiNjY0MTJjYTUzNzVjMDcwMGY0ODUwMCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoibW9uaWNhIiwic3ViIjoiTXBkYlVzZXIiLCJhdWQiOiJNcGRiVXNlcnMiLCJpc3MiOiJNcGRiUmVzdEFQSSJ9.ppPOSPGZf4tDkijRfBjuMutpu0yhtK2Z_ZdOyTqsbU1q5tRUZsaciysmFUEKKwjvg4LQaYPF7BPyKeqR6-_U3"}' http://localhost:8088/api/token/verify/
{"detail":"Token is invalid or expired","code":"token_not_valid"}


$ curl -X POST -d "username=admin&password=password123" http://localhost:8088/api/token/
Alternatively, you can use all the content types supported by the Django REST framework to obtain the auth token. For example:

$ curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"password123"}' http://localhost:8088/api/token/

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

