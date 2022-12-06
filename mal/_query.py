from mal._basic import _BasicReq
from mal._media import set_anime, set_list_anime

class MalAnime():
    def __init__(self, header_session: dict[str,str]):
        self.__slug_type = "anime"
        self.__HEADERS = header_session
        self.__query = _BasicReq(self.__HEADERS)

    @set_list_anime
    def get_list(self,q:str,limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get Anime List by name"""
        payload =  {"q" : q, "limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type,payload)
    
    @set_anime
    def get_details(self,anime_id: int,fields: str="id,title,main_picture,my_list_status"):
        """Get Anime by ID MAL"""
        payload =  {"fields":fields}
        return self.__query._get(self.__slug_type+"/%i"%(anime_id),payload)

    @set_list_anime
    def get_seasonal(self,year: int,season:str,sort:str="anime_score",limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get a List Anime Seasonal actually"""
        payload =  {"sort":sort,"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type+"/season/%i/%s"%(year,season),payload)

    @set_list_anime
    def get_suggested(self,limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get a List of Anime suggested"""
        payload =  {"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type+"/suggestions",payload)

    @set_list_anime
    def get_ranking(self,ranking_type:str = "all",limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get a List Ranking Anime!"""
        payload =  {"ranking_type":ranking_type,"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type+"/ranking",payload)
    
class MalManga():
    def __init__(self, header_session: dict[str,str]):
        self.__slug_type = "manga"
        self.__HEADERS = header_session
        self.__query = _BasicReq(self.__HEADERS)

    def get_list(self,q:str,limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get Manga List by name"""
        payload =  {"q" : q, "limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type,payload)

    def get_details(self,manga_id:int,fields: str="id,title,main_picture,my_list_status"):
        """Get Manga by ID MAL"""
        payload =  {"fields":fields}
        return self.__query._get(self.__slug_type+"/%i"%(manga_id),payload)

    def get_ranking(self,ranking_type:str = "all",limit:int=100,offset:int=0,fields:str="id,title,main_picture"):
        """Get a List Ranking Manga!"""
        payload =  {"ranking_type":ranking_type,"limit": limit, "offset": offset, "fields": fields}
        return self.__query._get(self.__slug_type+"/ranking",payload)