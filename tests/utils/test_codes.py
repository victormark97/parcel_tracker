import os

from app.utils.codes import build_tracking_code, generate_tracking_code
from app.config import TRACKING_CODE_PREFIX


def test_build_tracking_code_default_env_values():
    assert build_tracking_code(1) == f"{TRACKING_CODE_PREFIX}-000001"
    assert build_tracking_code(42) == f"{TRACKING_CODE_PREFIX}-000042"
    assert build_tracking_code(123456) == f"{TRACKING_CODE_PREFIX}-123456"


def test_build_tracking_code_custom_env_values():

    assert build_tracking_code(1) == f"{TRACKING_CODE_PREFIX}-000001"
    assert build_tracking_code(42) == f"{TRACKING_CODE_PREFIX}-000042"
    assert build_tracking_code(123456) == f"{TRACKING_CODE_PREFIX}-123456"


def test_build_tracking_code_can_override_directly():
    assert build_tracking_code(7, prefix="X", padding=3) == "X-007"
    assert build_tracking_code(7, prefix="AB", padding=1) == "AB-7"


def test_generate_tracking_code_uses_same_logic_as_build():

    assert generate_tracking_code(5) == f"{TRACKING_CODE_PREFIX}-000005"
    assert generate_tracking_code(99) == f"{TRACKING_CODE_PREFIX}-000099"


def test_negative_seq_raises_value_error():
    try:
        build_tracking_code(-1)
        assert False, "Expected ValueError for negative seq"
    except ValueError:
        assert True