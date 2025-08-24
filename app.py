print("Hola Mundo CI/CD")

def test_app():
    assert "Hola" in "Hola Mundo CI/CD"
    print("Test OK ✅")

if __name__ == "__main__":
    test_app()
