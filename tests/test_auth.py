import pytest
from mal4py._utils import Auth

@pytest.mark.asyncio
async def test_login_success(auth_session):
    """Verify that the shared session is valid."""
    assert auth_session is not None
    assert hasattr(auth_session, 'anime')

@pytest.mark.asyncio
async def test_login_invalid_credentials(client_id):
    """
    Here we DO create a new instance because we want to
    force a failure with fake credentials.
    """
    auth = Auth(client_id)
    with pytest.raises(Exception):
        await auth.unstable_login("fake_user", "wrong_pass")