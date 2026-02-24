import pytest
from mal4py._utils import Auth

@pytest.mark.asyncio
async def test_login_success(auth_session):
    """Verifica que la sesión compartida sea válida."""
    assert auth_session is not None
    assert hasattr(auth_session, 'anime')

@pytest.mark.asyncio
async def test_login_invalid_credentials(client_id):
    """
    Aquí SÍ creamos una instancia nueva porque queremos 
    forzar un fallo con credenciales falsas.
    """
    auth = Auth(client_id)
    with pytest.raises(Exception):
        await auth.unstable_login("fake_user", "wrong_pass")