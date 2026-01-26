from app.routers.customers import parse_sort, apply_sort


def test_parse_sort_happy_path():
    raw = "weight_kg,desc"
    allowed_fields = {"weight_kg"}
    default = "tracking_code"

    field, order = parse_sort(raw, allowed_fields, default)

    assert field == "weight_kg"
    assert order == "desc"

def test_parse_sort_not_default():
    raw = "weight_kg,desc"
    allowed_fields = set()
    default = "tracking_code"

    field, order = parse_sort(raw, allowed_fields, default)

    assert field == "tracking_code"
    assert order == "desc"


def test_parse_sort_wrong_raw():
    raw = "desc"
    allowed_fields = {"weight_kg"}
    default = "tracking_code"

    field, order = parse_sort(raw, allowed_fields, default)

    assert field == "tracking_code"
    assert order == "desc"




