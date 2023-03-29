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
    