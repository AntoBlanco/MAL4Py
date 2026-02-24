import pytest
import os
from mal4py._utils import Auth
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def client_id():
    cid = os.getenv("MAL_CLIENT_ID")
    if not cid:
        pytest.fail("MAL_CLIENT_ID is missing from the .env file")
    return cid

@pytest.fixture(scope="session")
async def auth_session(client_id):
    """
    Log in only once for the entire test suite.
    """
    user = os.getenv("MAL_USER")
    password = os.getenv("MAL_PASS")
    
    if not user or not password:
        pytest.fail("MAL_USER or MAL_PASS is missing from the .env file")
        
    auth = Auth(client_id)
    # This is where the only real login takes place.
    account = await auth.unstable_login(user, password)
    return account