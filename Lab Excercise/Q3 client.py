# client.py

import requests

def main():
    response = requests.get("http://localhost:8080")
    print("Response from server:", response.text)

if __name__ == '__main__':
    main()
