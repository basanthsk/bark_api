from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from typing import Optional
from fastapi import FastAPI
from fastapi import Response
import soundfile as sf

app = FastAPI()


@app.get("/{prompt}")
def process_prompt(prompt,response_class=Response):

    audio_array = generate_audio(prompt)
    with io.BytesIO() as buf:
        sf.write(buf, audio_array, SAMPLE_RATE, format='wav')
        audio_bytes = buf.getvalue()

    # write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
    headers = {'Content-Disposition': 'inline; filename="bark_generation.wav"'}
    return Response(audio_bytes, headers=headers, media_type='audio/wav')
    
