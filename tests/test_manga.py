import pytest
from mal4py._media import _Media as Media

@pytest.mark.asyncio
async def test_get_manga_details(auth_session):
    # auth_session ya es el objeto 'account' logueado
    search = auth_session.manga.get_details(45)
    
    assert search is not None
    manga = Media(**search.__dict__)
    assert manga.id == 45