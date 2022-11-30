from mal._basic import _BasicReq
from mal._utils import _MalAccount

#authToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMxY2I2YmVmYjhmZTllMjFjYmQyZTI0MmYzNjk3NjA1ZGYxNmE5YThkZDNlYjFiZDM1OWI4N2QxMDlkOTMyYWIzOTljMTkzNDM3ZWVhOGE5In0.eyJhdWQiOiIxNDI5Njk4M2JiMTg3YTFjMmU1NDU1OGE3MTMyYzg5ZSIsImp0aSI6IjMxY2I2YmVmYjhmZTllMjFjYmQyZTI0MmYzNjk3NjA1ZGYxNmE5YThkZDNlYjFiZDM1OWI4N2QxMDlkOTMyYWIzOTljMTkzNDM3ZWVhOGE5IiwiaWF0IjoxNjY5MjU4MTk5LCJuYmYiOjE2NjkyNTgxOTksImV4cCI6MTY3MTg1MDE5OSwic3ViIjoiNTQwMjcwNyIsInNjb3BlcyI6W119.WtcFQ08-_qqbPDF3BPfYad7LKdXsYAlcL9IfK-Wv9DXlIKZz_A6NOg4xBsJeEKM7sSEmkYMOAzDDtVDW6pQ_sJUcETwtGZfXSod5HTN1Mt7dT5fuT4CGV02TLvZVC53XPUGCVJJf67BXcJY_aX4BQL5_jbYKf8NvzhjuIsexVkB4QeRY44alwTcgAad4dN8akJWR0lXRN2jhXFwM23J-Ej2vyH03w24pIQn5b9san8zmKyU6A8uXeBRMjlv_nHOWh2SBgguIyoP7WdFct-xhUcQtpdAb-QvdzOXlSv3mIeSV9QW4bbz5QqnxYHlqvAz7Ce9eeQ7pKiSlyiLefB4G7A"
# authToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQwM2I1YzRhMGFkNWEwMWZlYmM3OGRhMDM1OTI2Y2IxYmM5ODBjZTZjZjM3MjA4YjA4MzgxMTEyMmEyZmNlYzljY2VjNzViNWUzZWNhNWNlIn0.eyJhdWQiOiI2MTE0ZDAwY2E2ODFiNzcwMWQxZTE1ZmUxMWE0OTg3ZSIsImp0aSI6IjQwM2I1YzRhMGFkNWEwMWZlYmM3OGRhMDM1OTI2Y2IxYmM5ODBjZTZjZjM3MjA4YjA4MzgxMTEyMmEyZmNlYzljY2VjNzViNWUzZWNhNWNlIiwiaWF0IjoxNjY5MjYxMTg1LCJuYmYiOjE2NjkyNjExODUsImV4cCI6MTY3MTg1MzE4NSwic3ViIjoiNTQwMjcwNyIsInNjb3BlcyI6W119.MkAe16mt6D-MuyM0sVhI1QTc9X4eG6UfBVgEG-OYbYjfk3xrTXAlQVVMrjQkIN0RE_LRfLik43B9YR5rc3sy9RStXb213XSDd3CSi3qF9OntxznF7mkYw2JNHZrkXc9bnxYMKRFJjhIvx6TC1dJdJMQhGpBGBac6Ah1YpAZn3D6C2FSM1V3X0ZsSJVa5Bdve8iS2TEt3zRJebZnGUZeTrjAFJNjuY6n40W-OL4u6bUoQ0nyxWxpvzR-XuRr3x8auxMp7MIZ6ss_Lq0dlJkvUzRxSNDWeafyap8du5Fr0OlBYPn04wOjK1DLtQMAZIPsGRVmy2MRM-VQ0-60IC7T3aA"
# headers = {
#         #'Host': 'api.myanimelist.net',
#         'X-MAL-Client-ID': '6114d00ca681b7701d1e15fe11a4987e', #CLient API MAL ANDROIDs
#         'Authorization': 'Bearer ' + authToken,
#         'Content-Type': 'application/json'
#     }
class MalAnime():
    
    def __init__(self, malAccount:_MalAccount):
        self.__slugType = "anime"
        self.__account = malAccount
        self.__query = _BasicReq(self.__account.getHttpHeaders())

    def get_list(self,q,limit=100,offset=0,fields="id,title,main_picture"):
        payload =  {"q" : q, "limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slugType,payload)

    def get_details(self,anime_id: int,fields="id,title,main_picture,my_list_status"):
        payload =  {"fields":fields}
        return self.__query._get(self.__slugType+"/%i"%(anime_id),payload)

    def get_seasonal(self,year: int,season,sort="anime_score",limit=100,offset=0,fields="id,title,main_picture"):
        payload =  {"sort":sort,"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slugType+"/season/%i/%s"%(year,season),payload)

    def get_suggested(self,limit=100,offset=0,fields="id,title,main_picture"):
        payload =  {"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slugType+"/suggestions",payload)
