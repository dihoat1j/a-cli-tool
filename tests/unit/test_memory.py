from a_cli_tool.memory import SharedMemory

def test_memory_roundtrip() -> None:
    m = SharedMemory()
    m.put("k", "v")
    assert m.get("k") == "v"
