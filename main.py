from pathlib import Path
from scriberry.transcriber import WhisperTranscriber

test_video = Path(__file__).parent / 'whisper_test.mp4'

transcriber = WhisperTranscriber(
    model_size="small",
    device="cpu",
    compute_type="int8"
)

test = transcriber.transcribe(test_video)
print(test)