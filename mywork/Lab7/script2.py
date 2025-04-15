import requests
import os
import boto3

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")
        return False
    return True

image_url = "https://media1.tenor.com/m/Bb7Di2yH8oMAAAAd/cat-head-shaking.gif"
file = "shaking-cat.gif"
path = os.path.join(os.getcwd(), file)
bucket_name = "ds2002-qxv7jp-bucket2"
expires_in = 604800  #  1week

if download_file(image_url, path):
    s3 = boto3.client("s3", region_name="us-east-1")
    with open(path, "rb") as f:
        s3.put_object(Bucket=bucket_name, Key=file, Body=f, ACL='public-read')

    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": file},
        ExpiresIn=expires_in
    )
    print("Presigned URL:")
    print(url)
