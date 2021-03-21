import boto3


class S3(object):
    def __init__(self):
        pass

    def upload_file_to_s3(self, body, bucket_name, key, metadata, acl='bucket-owner-full-control'):
        s3 = boto3.resource('s3')
        s3.meta.client.put_object(
            ACL=acl,
            Body=body,
            Bucket=bucket_name,
            Key=key,
            Metadata={
                'string': metadata
            })