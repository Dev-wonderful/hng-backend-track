"""
summary
"""
import os
from dotenv import load_dotenv

load_dotenv(".env")


# pylint: disable=invalid-name
class App_Config:
    """_summary_"""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
    )
