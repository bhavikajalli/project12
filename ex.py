import os
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['QUANDL_KEY'], os.environ['QUANDL_USERNAME'],os.environ['QUANDL_PASSWORD'])
print(s3.quandl_key)
