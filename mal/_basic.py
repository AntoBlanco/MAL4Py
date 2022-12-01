from typing import Any, Callable
import requests

_api_url = "https://api.myanimelist.net/v2/"
_secondary_api_url = "https://myanimelist.net/v1/"

class _BasicReq:
    def __init__(self, headers: dict[str, str] | None = None):
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
        resp_get = requests.get(_api_url+slug,params=params,headers=self.headers)
        print(resp_get.url)
        return resp_get.json()
    
    def _post(self, slug, data: dict | None = None) -> dict:
        resp_post = requests.post(_api_url+slug,headers=self.headers,data=data)
        return resp_post.json()
    
    def _post_api_v1(self, slug, data: dict | None = None) -> dict:
        resp_post = requests.post(_secondary_api_url+slug,headers=self.headers,data=data)
        print(_secondary_api_url+slug)
        return resp_post.json()
    
    def _put(self, slug) -> dict:
        resp_put = requests.post(_api_url+slug,headers=self.headers)
        return resp_put.json()
    
    def _delete(self, slug) -> dict:
        resp_del = requests.post(_api_url+slug,headers=self.headers)
        return resp_del.json()