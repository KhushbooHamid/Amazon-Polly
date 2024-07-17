import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get AWS credentials and region from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')

# Create a Polly client
polly = boto3.client('polly', region_name=aws_region, 
                     aws_access_key_id=aws_access_key_id, 
                     aws_secret_access_key=aws_secret_access_key)

# Synthesize Speech
response = polly.synthesize_speech(
    Text='aarish nee kaledoud uthaya Hello, this is a test speech from AWS Polly khushi.',
    OutputFormat='mp3',
    VoiceId='Joanna'
)

if "AudioStream" in response:
    with response["AudioStream"] as stream:
        output_file = "output.mp3"
        try:
            with open(output_file, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            print("error", error)

    print("File saved as", output_file)

else:
    print("Could not generate audio file")
