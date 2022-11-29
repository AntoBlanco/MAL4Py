import json
from mal._basic import _BasicReq

class _MalToken():
    # __token_type: str
    # __expires_in: int
    # __access_token: str
    # __refresh_token: str

    def __init__(self, tokenType: str,accessToken: str,refreshToken: str,expiresIn: int):
        self.__token_type: str = tokenType
        self.__expires_in: int = expiresIn
        self.__access_token: str = accessToken
        self.__refresh_token: str = refreshToken

    def fromJsonObj(obj: dict["token_type": str,"access_token": str,"refresh_token": str, "expires_in": int ]): 
        """Get MalToken From Token JSON Object"""
        return _MalToken(
            obj["token_type"],
            obj["access_token"],
            obj["refresh_token"],
            obj["expires_in"]
        )

    def fromJsonString(string: str):
        """Get MalToken From Token JSON String"""
        obj = dict[
            "token_type": str,
            "access_token": str,
            "refresh_token": str,
            "expires_in": int,
        ] = json.loads(string)
        return _MalToken(
            obj["token_type"],
            obj["access_token"],
            obj["refresh_token"],
            obj["expires_in"]
        )

    async def fromCredential(clientId: str,username: str,password: str):
        """
        **Unstable!**
        Get MalToken From Login And Password
        """
        DATA = {
            "client_id": clientId,
            "grant_type": "password",
            "username": username,
            "password": password
        }
        # ver ka posibilidad de agregar un try catch para respuestas con error
        REQ = _BasicReq()
        token = REQ._post("auth/token",data=DATA)

        return _MalToken(
            token["token_type"],
            token["access_token"],
            token["refresh_token"],
            token["expires_in"]
        )

    async def fromRefreshToken(clientId: str, refreshToken: str):
        """Get MalToken From Refresh Token"""
        DATA = {
            "client_id": clientId,
            "refresh_token": refreshToken,
            "grant_type": "refresh_token",
        }
        REQ = REQ = _BasicReq()
        token = REQ._postApiV1("oauth2/token",data=DATA)

        return _MalToken(
            token["token_type"],
            token["access_token"],
            token["refresh_token"],
            token["expires_in"]
        )

    async def fromAuthorizationCode(clientId: str,code: str,codeVerifier: str): 
        """Get _MalToken From PKCE Authorization Code"""
        DATA = {
            "client_id": clientId,
            "grant_type": "authorization_code",
            "code": code,
            "code_verifier": codeVerifier,
        }
        REQ = REQ = _BasicReq()
        token = REQ._postApiV1("oauth2/token",data=DATA)

        return _MalToken(
            token["token_type"],
            token["access_token"],
            token["refresh_token"],
            token["expires_in"]
        )

class _MalAcount():
    # __clientId: str
    # __malToken: _MalToken

    def __init_(self, clientId: str, malToken: _MalToken = None):
        self.__clientId: str = clientId
        self.__malToken: _MalToken = malToken
        # self.__user: MalUser = MalUser(self)
        # self.__anime: MalAnime = MalAnime(self)
        # self.__manga: MalManga = MalManga(self)
        # self.__forum: MalForum = MalForum(self)

    async def refreshToken(self):
        if (self.__malToken is None):
            self.__malToken = await _MalToken.fromRefreshToken(
                self.__clientId,
                self.__malToken.refresh_token
            )
        return self

    def getHttpHeaders(self):
        HEADERS: dict[str, str] = {
            "Authorization": None,
            "X-MAL-CLIENT-ID": self.__clientId
        }
        if (self.__malToken is None):
            HEADERS["Authorization"] = "Bearer %s" %(self.__malToken["access_token"])
        return HEADERS

    def stringifyToken(self) -> str:
        if (self.__malToken is None):
            return json.dumps(self.__malToken)
        else:
            return None