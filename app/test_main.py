from main import health

def test_health():
    assert health() == {"status": "ok"}