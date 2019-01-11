import argparse
import boto3


def extractTextRekognition(source, destination, object_name):
    client = boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': source, 'Name': object_name}})
    text_detection = response['TextDetections']
    print(response)
    print('Detected text')
    for text in text_detection:
        print('Detected text: ' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print('Parent Id: {}'.format(text['ParentId']))
        print('Type:' + text['Type'])


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--source', required=True, help='S3 bucket containing source image files')
    a.add_argument('--dest', required=True, help='Destination path for Rekognition result')
    a.add_argument('--object', required=True, help='Name of the object in S3 bucket that requires text extraction')
    args = a.parse_args()
    print(args)
    extractTextRekognition(args.source, args.dest, args.object)


if __name__ == '__main__':
    main()
