# utils.py
from datetime import datetime

def format_date_ymd(dt: datetime) -> str:
    """YYYY-MM-DD"""
    return dt.strftime("%Y-%m-%d")
