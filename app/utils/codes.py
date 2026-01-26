from datetime import datetime
from app.config import TRACKING_CODE_PREFIX, TRACKING_CODE_PADDING


def _get_prefix() -> str:
    # Default: "PRC"
    prefix = TRACKING_CODE_PREFIX.strip()
    return prefix if prefix else "PRC"


def _get_padding() -> int:
    # Default: 6
    raw = TRACKING_CODE_PADDING.strip()
    try:
        padding = int(raw)
    except ValueError:
        padding = 6

    if padding < 1:
        padding = 1
    return padding


def build_tracking_code(seq: int, prefix: str | None = None, padding: int | None = None) -> str:
    """
    Construiește tracking code-ul pe formatul:
      PREFIX-000123
    """
    if seq < 0:
        raise ValueError("seq must be >= 0")

    if prefix is None:
        prefix = _get_prefix()
    if padding is None:
        padding = _get_padding()

    return f"{prefix}-{seq:0{padding}d}"


def generate_tracking_code(next_id: int) -> str:
    """
    Generează tracking code folosind ID-ul (auto-increment) ca secvență.
    """
    return build_tracking_code(next_id)