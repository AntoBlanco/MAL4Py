import pytest
import os
from mal4py._utils import Auth
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def client_id():
    cid = os.getenv("MAL_CLIENT_ID")
    if not cid:
        pytest.fail("Falta MAL_CLIENT_ID en el archivo .env")
    return cid

@pytest.fixture(scope="session")
async def auth_session(client_id):
    """
    Inicia sesión una única vez para toda la suite de pruebas.
    """
    user = os.getenv("MAL_USER")
    password = os.getenv("MAL_PASS")
    
    if not user or not password:
        pytest.fail("Falta MAL_USER o MAL_PASS en el archivo .env")
        
    auth = Auth(client_id)
    # Aquí se hace el único login real
    account = await auth.unstable_login(user, password)
    return account