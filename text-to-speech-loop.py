from google.cloud import texttospeech
import glob


client = texttospeech.TextToSpeechClient()

#slogans = glob.glob('./generated-txt/20220916_all_slogans_utf8.txt')
slogans = open("./generated-txt/20220916_all_slogans_utf8.txt",'r')
count = 1

uevoices = ['de-DE-Standard-A', 'de-DE-Standard-B', 'de-DE-Standard-C', 'de-DE-Standard-D', 'de-DE-Standard-E', 'de-DE-Standard-F']

while True:
    next_line = slogans.readline()
    if not next_line:
        break;
    
    filename = "./generated-txt/slogans/{0}.txt".format(count)    
    with open(filename, 'w') as f:
        f.write(next_line.strip())
        
    #make audio
        for x in uevoices:
            speak = next_line.strip()
            synthesis_input = texttospeech.SynthesisInput(text=speak)
            
            voice = texttospeech.VoiceSelectionParams(
                language_code="de-DE", name=x)
            
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3)
                
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config)
                
            outputfile = "./mp3/{0}/{1}.mp3".format(x, count)
            
            with open(outputfile, "wb") as out:
                out.write(response.audio_content)
                print("{0}: made file {1}".format(count, outputfile))
            
                 
    count = count + 1
slogans.close()
