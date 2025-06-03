import secrets

def generate_api_key(length: int = 32) -> str:
    """
    Generate a secure API key using secrets module
    """
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    api_key = generate_api_key()
    print("\nGenerated API Key:")
    print("-" * 50)
    print("API_KEY:", api_key)
    print("-" * 50)