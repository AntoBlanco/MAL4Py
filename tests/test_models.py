import pytest
from mal4py._media import Anime, Manga, User, Forum, ErrorSearch, AnimeListItem

@pytest.mark.asyncio
async def test_anime_details_conversion(auth_session):
    """Verify that get_details correctly returns an Anime instance."""
    # The decorator @set_media should already be turning this into an Anime object
    anime = auth_session.anime.get_details(1) # Cowboy Bebop
    
    assert isinstance(anime, Anime)
    assert anime.id == 1
    assert hasattr(anime, 'title')
    # Test the comparison methods you defined in _Media
    assert anime == anime 

@pytest.mark.asyncio
async def test_manga_list_conversion(auth_session):
    """Verify that get_list returns a list of Manga objects."""
    mangas = auth_session.manga.get_list("Monster", limit=5)
    
    assert isinstance(mangas, list)
    if len(mangas) > 0:
        assert isinstance(mangas[0], Manga)
        assert hasattr(mangas[0], 'title')

@pytest.mark.asyncio
async def test_user_info_conversion(auth_session):
    """Check the User model."""
    user = auth_session.user.get_my_info()
    
    assert isinstance(user, User)
    assert hasattr(user, 'name')
    assert isinstance(user.id, int)

@pytest.mark.asyncio
async def test_forum_list_conversion(auth_session):
    """Verify the Forum model using the set_forum_list decorator."""
    # We use a known board_id to search for topics
    forum_topics = auth_session.forum.get_topics(board_id=10,subboard_id=1,q='love')
    
    assert isinstance(forum_topics, list)
    ##TODO: Next version assign attribute for topic Forum
    # if len(forum_topics): Dissable for next version
    #     assert isinstance(forum_topics[0], Forum)
    #     assert isinstance(repr(forum_topics[0]), Forum)

@pytest.mark.asyncio
async def test_error_search_handling(auth_session):
    """Verify that a 404 error returns an ErrorSearch object."""
    # We're looking for an ID that probably doesn't exist.
    error_res = auth_session.anime.get_details(99999999)
    
    assert isinstance(error_res, ErrorSearch)
    assert hasattr(error_res, 'status')
    assert error_res.status != 200

#TODO: Review listAnime and another media result, 'tuple' object has no attribute 'update'
# @pytest.mark.asyncio
# async def test_anime_list_item_logic(mocker, auth_session):
#     """
#     Test that the set_media_list decorator correctly combines
#     'node', 'list_status' and 'ranking' into an AnimeListItem object.
#     """
#     # Raw response simulation of the MAL API
#     mock_response = [(52991, 'Sousou no Frieren'), (59978, 'Sousou no Frieren 2nd Season'), (5114, 'Fullmetal Alchemist: Brotherhood'), (57555, 'Chainsaw Man Movie: Reze-hen'), (9253, 'Steins;Gate')]

#     #TODO: We patched the request method (adjust the route according to your project)
#     mocker.patch("mal4py._basic._BasicReq._get", return_value=mock_response)

#     # We execute the call (for example, to get the ranking)
#     # Assuming 'get_ranking' uses @set_media_list(AnimeListItem)
#     results = auth_session.anime.get_ranking(ranking_type="all")

#     # Validations
#     assert isinstance(results, list[Anime])
#     assert len(results) > 5 if not mocker else len(results) == 1
    
#     item = results[0]
#     assert isinstance(item, Anime)
#     assert item.id == 52991
#     assert item.title == "Sousou no Frieren"
    
@pytest.mark.asyncio
async def test_anime_list_item_real(auth_session):
    """Real test, checking the MAL ranking."""
    results = auth_session.anime.get_ranking(limit=10)
    
    assert isinstance(results, list)
    if len(results) > 0:
        assert isinstance(results[0], Anime)
        assert hasattr(results[0], 'id')
        assert hasattr(results[0], 'title')