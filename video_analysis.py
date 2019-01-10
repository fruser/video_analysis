import argparse
import boto3


def extractText(source, destination):
    client = boto3.client('rekognition')


    # name = 'frame24.jpg'
    # response = client.detect_text(Image={'S3Object': {'Bucket': source, 'Name': name}})
    #



    textDetection = response['TextDetections']
    print(response)
    print('Detected text')
    for text in textDetection:
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
    args = a.parse_args()
    print(args)
    extractText(args.source, args.dest)


if __name__ == '__main__':
    main()
