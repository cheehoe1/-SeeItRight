import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "cea696a9424c4163b2929de8689f65ad", "7f29036657c243f8a0f32b1114abd4fe"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
