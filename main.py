from faster_whisper import WhisperModel

model_size = "small"

model = WhisperModel(model_size, device='cuda', compute_type='float16')

segments, info = model.transcribe("")