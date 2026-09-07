from faster_whisper import WhisperModel
from pathlib import Path

test_video = Path(__file__).parent / 'whisper_test.mp4'

model_size = "small"

model = WhisperModel(model_size, device='cpu', compute_type='int8')

segments, info = model.transcribe(test_video)
print('started')
for segment in segments:
    print(f"[{segment.start} -> {segment.end}] {segment.text}")