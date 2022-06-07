def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, os.environ['BUCKET_NAME'], s3_file)

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
