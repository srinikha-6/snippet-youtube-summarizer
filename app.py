# Snippet - AI YouTube Summarizer
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t['text'] for t in transcript])
    return text

def summarize(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("YouTube Summarizer Ready!")