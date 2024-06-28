import boto3
import os

# TODO: Replace with your own AWS credentials
ACCESS_KEY = ''
SECRET_KEY = ''
BUCKET_NAME = ''

languagesToTranslate = [
    'English',
    'Spanish',
    'Chinese',
    'Filipino', #Tagalog
    'Vietnamese',
    'Arabic',
    'Korean',
    'Hindi',
    'Russian',
    'German',
    'Portuguese',
    'Italian',
    'Urdu',
    'Telugu',
    'Persian',
    'Gujarati',
    'Hungarian',
    'Cantonese'
]

category = 'animals'


s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def download_audio_files(bucket_name, folder_path):
    # Adjust folder_path to exclude 'master/' if present
    adjusted_folder_path = folder_path.replace('master/', '')
    
    # Ensure the local directory structure mirrors S3 (excluding 'master/')
    if not os.path.exists(adjusted_folder_path):
        os.makedirs(adjusted_folder_path)
    
    # List all objects within the specified folder in S3
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)
    
    if 'Contents' in response:
        for item in response['Contents']:
            file_name = item['Key']
            # Use adjusted_folder_path for local file path
            local_file_path = os.path.join(adjusted_folder_path, os.path.basename(file_name))
            
            # Download each file
            s3_client.download_file(bucket_name, file_name, local_file_path)
            print(f"Downloaded {file_name} to {local_file_path}")

# Example usage
for language in languagesToTranslate:
    bucket_name = 'babbel-blocks'
    folder_path = f'audio/{language}/{category}/'
    download_audio_files(bucket_name, folder_path)