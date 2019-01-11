# Video file analysis using AWS Rekognition and Textrack

## Detecting Text using Rekognition and Textrack

A word is one or more ISO basic Latin script characters that aren't separated by spaces. DetectText can detect up to 50 words in an image.

This is proof of concept to show how Rekognition and Textract perform
text extraction from image files.

I've used a sample video file (mp4) which was then split into frames
with one frame per second of the video. These images files were 
then uploaded to AWS S3 bucket for further review.
