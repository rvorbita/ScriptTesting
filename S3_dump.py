import boto3
import os
from botocore.exceptions import NoCredentialsError
import creds

ACCESS_KEY = creds.ACCESS_KEY
SECRET_KEY = creds.SECRET_ACCESS_KEY


#upload file in s3 bucket
def upload_to_s3_bucket(local_file, bucket_name, s3_file=None):

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    if s3_file is None:
        s3_file = os.path.basename(local_file)


    print("Upload Starting..")

    #upload the file.
    try:
        for root, dirs, files in os.walk(local_file):
            if files:
                for file in files:
                    s3_file = 'data_file/' + file
                    s3.upload_file(file, bucket_name, s3_file)
                    print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("The credentials was not found")
        return False



if __name__ == '__main__':
    
    path = os.getcwd()

    upload_to_s3_bucket(path, 'raymart-dummy-dump', 'data_file')




