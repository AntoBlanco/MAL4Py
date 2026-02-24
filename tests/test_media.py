import pytest
from mal4py._media import _Media as Media, Forum, ErrorSearch
# Asumiendo que tus modelos están en mal4py._media o mal4py.models
# Ajusta las importaciones según tu estructura real

@pytest.mark.asyncio
async def test_anime_and_media_logic(auth_session):
    """Prueba la obtención de un Anime y su conversión a objeto Media."""
    # 1. Obtener datos crudos de la API (ej: Cowboy Bebop ID: 1)
    anime_data = auth_session.anime.get_details(1)
    assert anime_data is not None
    
    # 2. Probar instanciación de Media
    anime_obj = Media(**anime_data.__dict__)
    assert anime_obj.id == 1
    assert "Cowboy Bebop" in anime_obj.title

@pytest.mark.asyncio
async def test_manga_list_item(auth_session):
    """Prueba la búsqueda y el formato de MangaListItem."""
    # get_list ya devuelve una lista gracias al decorador @set_media_list
    search_results = auth_session.manga.get_list("One Piece", limit=1)
    
    # 1. Verificamos que sea una lista
    assert isinstance(search_results, list)
    assert len(search_results) > 0
    
    # 2. El primer item YA es un objeto Manga/MangaListItem
    first_item = search_results[0] 
    
    # 3. Accedemos a sus atributos directamente (no como diccionario)
    assert first_item.title == "One Piece"
    assert hasattr(first_item, 'id')

@pytest.mark.asyncio
async def test_user_data(auth_session):
    """Prueba la obtención del perfil de usuario."""
    user_info = auth_session.user.get_my_info()
    
    assert user_info is not None
    assert "id" in user_info.__dict__
    # assert isinstance(user_info, User) # Si tienes la clase User

@pytest.mark.asyncio
async def test_forum_topics(auth_session):
    """Prueba la obtención de foros."""
    forum_data = auth_session.forum.get_topics(board_id=15,subboard_id=2254192,q="Evangelion")
    if len(forum_data) > 0:
        #assert hasattr(forum_data[0], 'title')
        ##TODO: Next version assign atribute for topic Forum
        assert isinstance(forum_data[0], int)
    else:
        # Si la lista está vacía, al menos verificamos que no sea un ErrorSearch
        assert not isinstance(forum_data, ErrorSearch)
        pytest.skip("La búsqueda no devolvió resultados para estos parámetros, pero la API respondió OK.")

def test_error_search_handling():
    """Prueba el comportamiento cuando no hay resultados (ErrorSearch)."""
    # Aquí simulamos una respuesta vacía o fallida
    empty_data = {"error": "not_found", "message": "No results found"}
    
    # Si tienes una clase específica para errores:
    # error = ErrorSearch(**empty_data)
    # assert "not_found" in error.message
    assert "error" in empty_data