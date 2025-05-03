from matrx_utils.core.initialize_database import init
from matrx_utils.conf import settings

DATABASE_CONFIGURED = False

if not DATABASE_CONFIGURED:
    init()
    DATABASE_CONFIGURED = True