# Image Text Extractor

This Python script allows you to extract text from images using Amazon Web Services (AWS) Textract service. It downloads an image from a publicly accessible URL, sends it to AWS Textract, and prints the detected text lines.

## Introduction

The Image Text Extractor is a command-line tool that leverages the power of AWS Textract to extract text from images. It is designed to be easy to use and requires minimal setup. The script is written in Python and uses the `requests` library to download the image and the `boto3` library to interact with the AWS Textract service.

## Prerequisites

Before you can use the Image Text Extractor, you need to have the following:

- Python 3.6 or later
- An AWS account with access keys and a configured region
- A publicly accessible URL of the image you want to extract text from

## Installation

1. Clone the repository or download the source code.
2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory and add your AWS credentials and region:

```
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
```

Replace `your_aws_access_key`, `your_aws_secret_key`, and `your_aws_region` with your actual AWS credentials and region.

## Usage

1. Run the script:

```bash
python main.py
```

2. When prompted, enter the publicly accessible URL of the image you want to extract text from.

3. The script will download the image, send it to AWS Textract, and print the detected text lines with line numbers.

Example output:

```
Please enter the publicly accessible URL of the image: https://example.com/image.jpg
2023-05-24 10:30:00 INFO Downloading image...
2023-05-24 10:30:02 INFO Calling AWS Textract...
2023-05-24 10:30:05 INFO Extracted text:
  1: This is a sample image.
  2: It contains some text.
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

When contributing, please follow these guidelines:

1. Fork the repository and create a new branch for your changes.
2. Make your changes and ensure that the code follows the project's coding style and conventions.
3. Write tests for your changes, if applicable.
4. Update the documentation, if necessary.
5. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).