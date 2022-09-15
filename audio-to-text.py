import os
from google.cloud import speech

#Double check for google application creditials 
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speech_client = speech.SpeechClient()

#max file size 1 minute 
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='de-DE'
)


# 
num_mp3_files = 100

for x in range(num_mp3_files):
  name = "./files/speech2text_"
  media_file_name_mp3 = "{0}{1}.mp3".format(name, x)
  
  
  with open(media_file_name_mp3, 'rb') as f1:
      byte_data_mp3 = f1.read()
      
  audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)
  
  response = speech_client.recognize(
      config=config_mp3,
      audio=audio_mp3
  )
  # each file gets one txt file - use concate later 
  for result in response.results:
    nametxt = "./text/txt_"
    txtfile = "{0}{1}.txt".format(nametxt, x)
    with open(txtfile, 'w') as f:
        f.write("{}".format(result.alternatives[0].transcript))
        print("generated text: {0}".format(x))
        
        
     
