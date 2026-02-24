import pytest
from mal4py._media import Anime, Manga, User, Forum, ErrorSearch, AnimeListItem

@pytest.mark.asyncio
async def test_anime_details_conversion(auth_session):
    """Verifica que get_details devuelva una instancia de Anime correctamente."""
    # El decorador @set_media ya debería convertir esto en objeto Anime
    anime = auth_session.anime.get_details(1) # Cowboy Bebop
    
    assert isinstance(anime, Anime)
    assert anime.id == 1
    assert hasattr(anime, 'title')
    # Prueba de los métodos de comparación que definiste en _Media
    assert anime == anime 

@pytest.mark.asyncio
async def test_manga_list_conversion(auth_session):
    """Verifica que get_list devuelva una lista de objetos Manga."""
    mangas = auth_session.manga.get_list("Monster", limit=5)
    
    assert isinstance(mangas, list)
    if len(mangas) > 0:
        assert isinstance(mangas[0], Manga)
        assert hasattr(mangas[0], 'title')

@pytest.mark.asyncio
async def test_user_info_conversion(auth_session):
    """Verifica el modelo User."""
    user = auth_session.user.get_my_info()
    
    assert isinstance(user, User)
    assert hasattr(user, 'name')
    assert isinstance(user.id, int)

@pytest.mark.asyncio
async def test_forum_list_conversion(auth_session):
    """Verifica el modelo Forum usando el decorador set_forum_list."""
    # Usamos un ID de anime conocido para buscar temas
    forum_topics = auth_session.forum.get_topics(board_id=10,subboard_id=1,q='love')
    
    assert isinstance(forum_topics, list)
    ##TODO: Next version assign atribute for topic Forum
    # if len(forum_topics): Dissable for next version
    #     assert isinstance(forum_topics[0], Forum)
    #     assert isinstance(repr(forum_topics[0]), Forum)

@pytest.mark.asyncio
async def test_error_search_handling(auth_session):
    """Verifica que un error 404 devuelva un objeto ErrorSearch."""
    # Buscamos un ID que probablemente no exista
    error_res = auth_session.anime.get_details(99999999)
    
    assert isinstance(error_res, ErrorSearch)
    assert hasattr(error_res, 'status')
    assert error_res.status != 200

#TODO: Review listAnime and another media result, 'tuple' object has no attribute 'update'
# @pytest.mark.asyncio
# async def test_anime_list_item_logic(mocker, auth_session):
#     """
#     Prueba que el decorador set_media_list combine correctamente 
#     'node', 'list_status' y 'ranking' en un objeto AnimeListItem.
#     """
#     # Simulación de respuesta cruda de la API de MAL
#     mock_response = [(52991, 'Sousou no Frieren'), (59978, 'Sousou no Frieren 2nd Season'), (5114, 'Fullmetal Alchemist: Brotherhood'), (57555, 'Chainsaw Man Movie: Reze-hen'), (9253, 'Steins;Gate')]

#     # Parcheamos el método de petición (ajusta la ruta según tu proyecto)
#     mocker.patch("mal4py._basic._BasicReq._get", return_value=mock_response)

#     # Ejecutamos la llamada (por ejemplo, obtener el ranking)
#     # Asumiendo que 'get_ranking' usa @set_media_list(AnimeListItem)
#     results = auth_session.anime.get_ranking(ranking_type="all")

#     # Validaciones
#     assert isinstance(results, list[Anime])
#     assert len(results) > 5 if not mocker else len(results) == 1
    
#     item = results[0]
#     assert isinstance(item, Anime)
#     assert item.id == 52991
#     assert item.title == "Sousou no Frieren"
    
@pytest.mark.asyncio
async def test_anime_list_item_real(auth_session):
    """Prueba real consultando el ranking de MAL."""
    results = auth_session.anime.get_ranking(limit=10)
    
    assert isinstance(results, list)
    if len(results) > 0:
        assert isinstance(results[0], Anime)
        assert hasattr(results[0], 'id')
        assert hasattr(results[0], 'title')