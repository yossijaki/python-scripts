import os
import requests
import time

def download_image(url, folder_path, filename):
    response = requests.get(url)
    if response.status_code == 200:
        image_path = os.path.join(folder_path, filename)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

def main():
    # page.com (tfppnngplus)
    page = "thepage.plus"
    username = "some-user"
    #Don't forget to change the url if it's different
    base_url = f"https://{page}/photos/b/e/{username}"
    folder_name = f"{username}"
    os.makedirs(folder_name, exist_ok=True)
    
    #Takes the time before the download process
    start_time = time.time()

    # Number of images found and download process calling download_image function:
    for i in range(5167, 7792):
        if i <= 999:
            url = f"{base_url}/1000/{username}_{i:04d}.jpg"
        elif i <= 1999:
            url = f"{base_url}/2000/{username}_{i:04d}.jpg"
        elif i <= 2999:
            url = f"{base_url}/3000/{username}_{i:04d}.jpg"
        elif i <= 3999:
            url = f"{base_url}/4000/{username}_{i:04d}.jpg"
        elif i <= 4999:
            url = f"{base_url}/5000/{username}_{i:04d}.jpg"
        elif i <= 5999:
            url = f"{base_url}/6000/{username}_{i:04d}.jpg"
        elif i <= 6999:
            url = f"{base_url}/7000/{username}_{i:04d}.jpg"
        elif i <= 7999:
            url = f"{base_url}/8000/{username}_{i:04d}.jpg"
        elif i <= 8999:
            url = f"{base_url}/9000/{username}_{i:04d}.jpg"
        download_image(url, folder_name, f"{username}_{i:04d}.jpg")

    #Takes the time after the downloading process 
    end_time = time.time()
    # Now substracts the end time from the start time
    elapsed_time = end_time - start_time
    print(f"All files downloaded in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
