from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_ROUTERS=[
    os.path.join(BASE_DIR, 'view', 'common'),
    os.path.join(BASE_DIR, 'view', 'view_account_010'),
    os.path.join(BASE_DIR, 'view', 'view_main_010'),
]