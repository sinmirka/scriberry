from datetime import timedelta

from scriberry.transcript import TranscriptSegment

def format_timestamp(seconds: float):
    return str(timedelta(seconds=seconds))

def render_markdown(heading: str, segments: list[TranscriptSegment]):
    markdown_heading = f"# {heading}\n"
    lines = []
    lines.append(markdown_heading)
    for segment in segments:
        line = f"- **[{format_timestamp(segment.start)} -> {format_timestamp(segment.end)}]** {segment.text.strip()}\n"
        lines.append(line)

    return "".join(lines)

