#!/usr/bin/env python

# create a loop to loop all the txt files !! 

def run_quickstart():
    
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text="Mit Goethes Faust wird Johann Wolfgang von Goethes Bearbeitung des Fauststoffs bezeichnet. Der Begriff kann sich auf den ersten Teil der von Goethe geschaffenen Tragödie, auf deren ersten und zweiten Teil gemeinsam oder insgesamt auf die Arbeiten am Fauststoff beziehen, die Goethe durch sechzig Jahre hindurch immer wieder neu aufnahm. Er umfasst in diesem letzteren Sinne auch die Entwürfe, Fragmente, Kommentare und Paralipomena des Dichters zu seinem Faustwerk und zum Fauststoff.")

    voice = texttospeech.VoiceSelectionParams(
        #language_code="de-DE", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        name="de-DE-Standard-A"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == "__main__":
    run_quickstart()
