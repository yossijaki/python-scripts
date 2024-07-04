import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

def main():
    # user-example
    user_name = "user-name"
    page_link = "examplepage.net"
    base_url = f"https://{page_link}/photos/a/e/{user_name}/"
    for i in range(999, 1644):
        if i <= 999:
            image_url = f"{base_url}1000/{user_name}_{i:04d}.jpg"
        else:
            image_url = f"{base_url}2000/{user_name}_{i:04d}.jpg"
        filename = f"{user_name}_{i:04d}.jpg"
        download_image(image_url, filename)

if __name__ == "__main__":
    main()