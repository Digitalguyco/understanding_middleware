<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2020/04/django-python-logo.png?w=500&ssl=1" alt="Django logo"></a>
</p>

<h3 align="center">Middleware In Djnago</h3>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [What it is and How it works](#working)
- [Other UseCases](#usage)
- [Built Using](#built_using)
- [End](#end)


## 🏁 Getting Started <a name = "getting_started"></a>
- Clone the repo
- cd into the project directory 
- Create a virtual environment by running `python3 -m venv env` or `virtualenv env`
- Activate the virtual environment by running `source env/bin/activate` or `env/bin/activate`
- Install the requirements by running `pip install -r requirements.txt`
- Generate a secret key by running `python3 secret_key_generator.py` and copy the generated key
- For MacOS and Linux use `export SECRET_KEY=THESECRETKEYYOUJUSTCOPIED` for Windows 10 and lower `Set SECRET_KEY=THESECRETKEYYOUJUSTCOPIED` and for Windows 11 `$ENV:SECRET_KEY = 'THESECRETKEYYOUJUSTCOPIED'`
- Run the make migrations by running `python3 manage.py makemigrations` and then `python3 manage.py migrate`
- Run the server by running `python3 manage.py runserver`


## 🧐 What it is and How it works <a name = "working"></a>
According to the official Django Documentation, Middleware is a framework of hooks into Django's request/response processing. It's a light, low-level “plugin” system for globally altering Django's input or output. Each middleware component is responsible for doing some specific function. in other words, Middleware is simply a framework that allows you to hook into the request/response cycle of a Django application. It is a way to extend the functionality of your application without having to modify the core code.

To get more understanding of Django's request/response processing, here is a diagram of the request/response cycle in Django:

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://learnbatta.com/assets/images/django/request_response_lifecycle_Django.png" alt="Django logo"></a>
    <small>image from [learnbatta.com](https://learnbatta.com/)</small>
</p>

Here we can see the Django request/response cycle. The request is sent to the server, and the server processes the request and sends the response back to the client. The request is processed by the view, and the view returns the response. The response is processed by the template, and the template returns the final response to the client. And in the midst of this, the middleware is used to process the request and response.


The idea of middleware is great in so many as you can improve security, add functionality, and even add features to your application. Django has the following built-in middleware:
- CommonMiddleware: for handling things like the X-Forwarded-Host header.
- CsrfViewMiddleware: for protecting against Cross Site Request Forgery (CSRF) attacks.
- SecurityMiddleware: for setting various security-related HTTP headers.
- SessionMiddleware: for managing user sessions.
and these middlewares are being used every single time a request is sent to the server and the response from the server goes back to the client.


Now do need to create a custom middleware? Well, it depends on what you want to achieve. If you want to add a certain feature to your application, then you can create a custom middleware. If you want to improve security, then you can create a custom middleware. If you want to improve performance, then you can create a custom middleware. If you want to improve the user experience, then you guessed it, you can create custom middleware. 

Now let's see how to create a custom middleware. To create a custom middleware in my case, I created a middleware that will change a user's IP address to a random IP address which isn't so random as it's just '206.71.50.230'. This is just to show how middleware works. So I achieved this by 
- Creating a middleware.py file in the app folder
- Creating a middleware class or function
```python
# middleware.py
# FUNCTION-BASED MIDDLEWARE

def ipchange(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        user_ip = request.META.get('HTTP_X_FORWARDED_FOR') # Shows the IP Address of the user
        print(f'This Now Your Old IP Address: {user_ip}')
        
        request.META['HTTP_X_FORWARDED_FOR'] = '206.71.50.230' # Change the IP Address of the user

        new_user_ip = request.META.get('HTTP_X_FORWARDED_FOR') # Shows the IP Address of the user

        response = get_response(request)

        print(f'This Now Your New IP Address: {new_user_ip}')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware



# CLASS-BASED MIDDLEWARE

class Ipchange:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        user_ip = request.META.get('HTTP_X_FORWARDED_FOR') # Shows the IP Address of the user
        print(f'This Now Your Old IP Address: {user_ip}')
        
        request.META['HTTP_X_FORWARDED_FOR'] = '206.71.50.230' # Change the IP Address of the user

        new_user_ip = request.META.get('HTTP_X_FORWARDED_FOR') # Shows the IP Address of the user

        response = self.get_response(request)

        print(f'This Now Your New IP Address: {new_user_ip}')

        # Code to be executed for each request/response after
        # the view is called.
        
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        pass

    def process_exception(self, request, exception):
        # Code to be executed for each request/response after
        # the view is called.

        pass

    def process_template_response(self, request, response):
        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_response(self, request, response):
        # Code to be executed for each request/response after
        # the view is called.

        return response

```
- Registering the middleware in the settings.py file
```python
# settings.py
MIDDLEWARE = [
    ...
    'app.middleware.Ipchange' # CLASS-BASED MIDDLEWARE
   # 'app.middleware.ipchange' # FUNCTION-BASED MIDDLEWARE
]

```
- Running the server and checking the IP Address of the user
Once you run the server and check the IP Address of the user, you will see that the IP Address of the user has been changed to '206.71.50.230' So with that, I created a custom middleware that does something simple but it's just to show how middleware works. You can create a custom middleware that does something more complex and useful.


## 🎈 Other UseCases <a name = "usage"></a>
You can find other use cases for creating custom middleware in the official Django Documentation [here](https://docs.djangoproject.com/en/3.2/topics/http/middleware/)


## ⛏️ Built Using <a name = "built_using"></a>
- [Django](https://www.djangoproject.com/) - Web Framework



## 🎉 End <a name = "end"></a>
I'm writing all this to help myself and whoever finds it useful to understand djnago core concepts. I hope you find it useful. If you have any questions, feel free to reach out to me on [Twitter](https://twitter.com/khitoTM) or [LinkedIn](https://www.linkedin.com/in/daniel-ikekwem-361658238/)