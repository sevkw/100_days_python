# Project Summary

This project comes from the Day 36 of 100 Days of Python on Udemy.
## first_try.py
Note that the first_try.py was a file compiled through my first try. In this try, I do not want to spend too much time on the Twilio, so I just print out the Headline and Brief.

## main.py
This file was my second try after following the video solution. However, I modified the file abit to securely save the secret keys.
In addition, upon taking this project in 2023-07, some API endpoints have changed a bit.
In addition to that, the way to store API keys and tokens are not really the right way to do so.
**YOU SHOULD NEVER SAVE HARDCODED SECRETS INTO SOURCE CODE!!**

Below are some ways to save your secret variables:

# Environment Variables

Here is a great explanation of Environment Variables via ChatGPT:

```
In Python, environment variables are dynamic values that can affect the behavior of a program. They are stored in the operating system's environment and can be accessed by the Python script during runtime.

Environment variables are useful for storing configuration settings, sensitive information (such as API keys or database credentials), or any other values that need to be accessed by multiple processes or scripts.

To access environment variables in Python, you can use the os module, which provides functions for interacting with the operating system. The specific environment variable for Python can vary depending on the operating system, but a common one is PYTHONPATH, which specifies the search path for Python modules.
```
```
import os

# Get the value of an environment variable
my_var = os.getenv('MY_VARIABLE')

# Print the value
print(my_var)
```

Here is a great video on how to set it up: https://youtu.be/DVVYHlGYIHY

# `.env` Files (Recommended!)

Note that if you want the Twilio API code to work you have to set up an `.env` file
Setting environment variables in local machine can have some drawbacks.
According to this article here: https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1 :

```
The process of setting or changing an environment variable is time consuming and over time the number of environment variables you have to manage grows out of control. Eventually naming conflicts becomes an issue and every new variable requires a lengthy prefix to distinguish itself from similar variables.
```
Here is the official site for dot-env package: https://pypi.org/project/python-dotenv/

Also, I find this video to be very helpful in getting me started with `.env` file and the dot-env module: https://youtu.be/8dlQ_nDE7dQ
