import requests

def main():
    response = requests.get("https://example.com")
    print("Status code:", response.status_code)

if __name__ == "__main__":
    main()
