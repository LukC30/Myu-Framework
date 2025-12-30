from wsgiref import handlers

class Response():
    def __init__(self):
        pass

class Request():
    def __init__(self, environ):
        self._environ = {} if environ is None else environ
        self._path = self._environ.get("PATH_INFO", "/")
        self._method = self._environ.get("REQUEST_METHOD", 'GET')
        self._content = self._environ.get("wsgi.input").read().decode('utf-8') 
        
    @property
    def path(self):
        return self._path
    
    @property
    def method(self):
        return self._method.upper()
    
    @property
    def content(self):
        return self._content