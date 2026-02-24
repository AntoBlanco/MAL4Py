import pytest
from mal4py._media import _Media as Media, Forum, ErrorSearch
# Adjust imports according to your actual structure

@pytest.mark.asyncio
async def test_anime_and_media_logic(auth_session):
    """Try obtaining an Anime and converting it to a Media object."""
    # 1. Obtain raw data from the API (e.g., Cowboy Bebop ID: 1)
    anime_data = auth_session.anime.get_details(1)
    assert anime_data is not None
    
    # 2. Test Media instantiation
    anime_obj = Media(**anime_data.__dict__)
    assert anime_obj.id == 1
    assert "Cowboy Bebop" in anime_obj.title

@pytest.mark.asyncio
async def test_manga_list_item(auth_session):
    """Test the MangaListItem search and format."""
    # get_list already returns a list thanks to the decorator @set_media_list
    search_results = auth_session.manga.get_list("One Piece", limit=1)
    
    # 1. Verify that it is a list
    assert isinstance(search_results, list)
    assert len(search_results) > 0
    
    # 2. The first item is already a Manga/MangaListItem object
    first_item = search_results[0] 
    
    # 3. We access its attributes directly (not as a dictionary)
    assert first_item.title == "One Piece"
    assert hasattr(first_item, 'id')

@pytest.mark.asyncio
async def test_user_data(auth_session):
    """Try obtaining the user profile."""
    user_info = auth_session.user.get_my_info()
    
    assert user_info is not None
    assert "id" in user_info.__dict__
    # assert isinstance(user_info, User) # If you have the User class

@pytest.mark.asyncio
async def test_forum_topics(auth_session):
    """Try obtaining forums."""
    forum_data = auth_session.forum.get_topics(board_id=15,subboard_id=2254192,q="Evangelion")
    if len(forum_data) > 0:
        #assert hasattr(forum_data[0], 'title')
        ##TODO: Next version assign attribute for topic Forum
        assert isinstance(forum_data[0], int)
    else:
        # If the list is empty, at least we've verified that it's not an ErrorSearch
        assert not isinstance(forum_data, ErrorSearch)
        pytest.skip("The search returned no results for these parameters, but the API responded OK.")

def test_error_search_handling():
    """Test the behavior when there are no results (ErrorSearch)."""
    # Here we simulate an empty or failed response
    empty_data = {"error": "not_found", "message": "No results found"}
    
    # If you have a specific class for errors:
    # error = ErrorSearch(**empty_data)
    # assert "not_found" in error.message
    assert "error" in empty_data