import argparse
import cv2
import boto3
import os


def extract_image(source, destination, step):
    count = 0
    vidcap = cv2.VideoCapture(source)
    success, image = vidcap.read()

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * step * 1000))
        cv2.imwrite(destination + "/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count = count + 1


def s3_upload(bucket, source):
    s3 = boto3.client('s3')
    bucket_name = bucket

    for file in os.listdir(source):
        if file.endswith(".jpg"):
            print(os.path.join(source, file))
            s3.upload_file(os.path.join(source, file), bucket_name, file)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--source', required=True, help='Path to the video source file')
    a.add_argument('--dest', required=True, help='Destination path for images')
    a.add_argument('--s3_bucket', required=True, help='Destination S3 bucket')
    a.add_argument('--step', default=1, help='Step to use in seconds when converting to JPEG. Default is 1 second')
    args = a.parse_args()
    print(args)
    extract_image(args.source, args.dest, args.step)
    s3_upload(args.s3_bucket, args.dest)


if __name__ == '__main__':
    main()
