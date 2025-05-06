import sys
import os
from pathlib import Path
import pytest
from playwright.sync_api import Page

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.signup_fixture import new_user_data
from utils.login_fixture import logged_in_user