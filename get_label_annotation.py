#!/user/bin/python
from google.cloud import videointelligence
import io


video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]
with io.open("video.mp4", 'rb') as movie:
    video = movie.read()
operation = video_client.annotate_video(features=features, input_content=video)
print('\nProcessing video for label annotations:')
result = operation.result(timeout=90)
print('\nFinished processing.')

shot_labels = result.annotation_results[0].shot_label_annotations
for i, shot_label in enumerate(shot_labels):
    print('Video label description: {}'.format(
        shot_label.entity.description))
    for category_entity in shot_label.category_entities:
        print('\tLabel category description: {}'.format(
            category_entity.description))

    for i, shot in enumerate(shot_label.segments):
        start_time = (shot.segment.start_time_offset.seconds +
                      shot.segment.start_time_offset.nanos / 1e9)
        end_time = (shot.segment.end_time_offset.seconds +
                    shot.segment.end_time_offset.nanos / 1e9)
        positions = '{}s to {}s'.format(start_time, end_time)
        confidence = shot.confidence
        print('\tSegment {}: {}'.format(i, positions))
        print('\tConfidence: {}'.format(confidence))
    print('\n')

