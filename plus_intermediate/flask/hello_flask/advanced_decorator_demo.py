# This code demonstrate more advanced decorator concepts

class User:
    def __init__(self, name:str):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            user_name = args[0].name
            print(f"{user_name} is not logged in.")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user:User):
    print(f"This is {user.name}'s new blog post.")

user = User('Kerry')
create_blog_post(user)