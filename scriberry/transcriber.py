from pathlib import Path
from faster_whisper import WhisperModel

from .transcript import TranscriptSegment

class WhisperTranscriber:
    def __init__(
            self,
            model_size: str,
            device: str,
            compute_type: str,
        ):
        self._model = WhisperModel(model_size_or_path=model_size, device=device, compute_type=compute_type)

    def transcribe(self, path: Path) -> list[TranscriptSegment]:
        segments, _ = self._model.transcribe(path)
        tr_segments = []

        for segment in segments:
            tr_segment = TranscriptSegment(
                start=segment.start,
                end=segment.end,
                text=segment.text
            )
            tr_segments.append(tr_segment)

        return tr_segments