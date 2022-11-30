from typing import Any, Callable
import requests

_apiUrl = "https://api.myanimelist.net/v2/"
_secondaryApiUrl = "https://myanimelist.net/v1/"

class _BasicReq:
    def __init__(self, headers: dict | None = None):
        """
        Add params from API MAL GET and Headers from query
        """
        
        if(headers is None):
            self.headers = {}
            self.headers["Content-Type"] = "application/x-www-form-urlencoded"            
            self.headers["X-MAL-Client-ID"] = "6114d00ca681b7701d1e15fe11a4987e"
        else:
            self.headers = headers

    def _get(self, slug, params) -> dict:
        responseGet = requests.get(_apiUrl+slug,params=params,headers=self.headers)
        print(responseGet.url)
        return responseGet.json()
    
    def _post(self, slug, data: dict | None = None) -> dict:
        responsePost = requests.post(_apiUrl+slug,headers=self.headers,data=data)
        return responsePost.json()
    
    def _postApiV1(self, slug, data: dict | None = None) -> dict:
        responsePost = requests.post(_secondaryApiUrl+slug,headers=self.headers,data=data)
        print(_secondaryApiUrl+slug)
        return responsePost.json()
    
    def _put(self, slug) -> dict:
        responsePut = requests.post(_apiUrl+slug,headers=self.headers)
        return responsePut.json()
    
    def _delete(self, slug) -> dict:
        responseDel = requests.post(_apiUrl+slug,headers=self.headers)
        return responseDel.json()