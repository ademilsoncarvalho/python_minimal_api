# Python Minimal Api
Python minimal Api using BaseHTTPRequestHandler

### Description

Simple API using native python for server creation.
<br>Project allows the creation of dynamic routes only by creating new files in the controllers directory

## Using 
<br>To create new routes just follow the example of the controller user.
<br>The route will always be /className/Method, the method will always be concatenated using the verb http used.
<br>Example GET :: localhost:5000/user/ to call User.__get
<br>Example GET :: localhost:5000/user/list to call User.list__get

### Getting Started 
    pip install -r requirements.txt

### Prerequisites
    Python >= 3.6
    pip
