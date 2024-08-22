import boto3
import pandas as pd

def update_csv(new_df, name, file_path):
    s3 = boto3.client('s3')
    bucket = 'jeans-measurement'
    key = 'measurements.csv'

    df = pd.read_csv(file_path)
    df = pd.concat([df[df['Name'] != name], new_df])
    df.to_csv(file_path, index = False)

    s3.upload_file(file_path, Bucket = bucket, Key = key)
    return True
