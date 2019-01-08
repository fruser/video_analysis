import argparse
import cv2
print(cv2.__version__)


def extractImage(source, destination, step):
    count = 0
    vidcap = cv2.VideoCapture(source)
    success, image = vidcap.read()

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * step * 1000))
        cv2.imwrite(destination + "/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count = count + 1


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--source', required=True, help='Path to the video source file')
    a.add_argument('--dest', required=True, help='Destination path for images')
    a.add_argument('--step', default=1, help='Step to use in seconds when converting to JPEG. Default is 1 second')
    args = a.parse_args()
    print(args)
    extractImage(args.source, args.dest, args.step)


if __name__ == '__main__':
    main()
