import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='774ec551-661c-4cbe-a671-2d69c0873467',
    password='TM6D3Mq7lLOW',
    x_watson_learning_opt_out=False
)

print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open("/home/icarus/projects/charter-demo/eric.wav",
          'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=True,
        word_confidence=True),
        indent=2))