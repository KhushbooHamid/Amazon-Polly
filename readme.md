AWS Polly Text-to-Speech Script
This Python script uses AWS Polly to convert text into speech and saves the audio file locally.

Prerequisites
Before running this script, make sure you have the following:

Python 3.x: Ensure you have Python 3.x installed on your system.
AWS Credentials: You need AWS access key ID and secret access key.
Environment Variables: Store your AWS credentials and region in a .env file.
Setup
Install Required Packages
Install the required Python packages using pip:

pip install boto3 python-dotenv flask flask-cors

If you encounter an error:

ModuleNotFoundError: No module named 'urllib3.packages.six.moves'

Install the required following Python packages using pip:

pip install --upgrade urllib3 botocore
Create a .env File
Create a .env file in the same directory as your script and add your AWS credentials and region:

AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_region

Explanation
Load Environment Variables: The script loads AWS credentials and region from a .env file.
Create Polly Client: It creates an AWS Polly client using the provided credentials.
Synthesize Speech: The script sends a request to AWS Polly to synthesize speech from the given text.
Save Audio File: If the response contains an audio stream, the script writes the audio stream to an MP3 file. If there's an error, it prints an error message.
Error Handling
The script handles potential IO errors when writing the audio stream to the file. It also checks if the AudioStream is present in the response to ensure that the synthesis was successful.

Developers
Syed Aarish Shah
Khushboo Hamid
Contribution
We welcome contributors to our project!

Fork the repository.
Create your Feature Branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
📜 License
This project is licensed under the MIT License. For more details, please refer to the LICENSE.md file.