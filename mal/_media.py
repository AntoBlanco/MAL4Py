

class _Media:
    def __init__(self, **serie):
        self.__dict__.update(serie)
    def __str__(self):
        return f'{self.__dict__}'

class ErrorSearch(_Media):
    def __init__(self, **serie):
        super().__init__(**serie)

class _Anime(_Media):
    def __init__(self, **serie):
        super().__init__(**serie)
        
class _Manga(_Media):
    def __init__(self, **serie):
        super().__init__(**serie)
        
def set_anime(function)-> _Anime | ErrorSearch:
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        try:
            if("message" not in result):
                return _Anime(**result)
            else:
                return ErrorSearch(**result)
        except:
            raise Exception("ERROR", "Error de consulta de datos revise su autenticación...")
    return wrapper

def set_list_anime(function)-> list[_Anime] | ErrorSearch:
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        try:
            if("message" or "error" not in result ):
                aset = []
                for res in result["data"]:
                    aset.append(_Anime(**res["node"]))
                #aset.append(result["paging"])
                return aset
            else:
                return ErrorSearch(**result)
        except:
            raise Exception("ERROR", "Error de consulta de datos revise su autenticación...")
    return wrapper