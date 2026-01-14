import re
from django import template

register = template.Library()

@register.filter(name='embed_video')
def embed_video(url):
    # Lógica para YouTube
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    yt_match = re.match(youtube_regex, url)
    if yt_match:
        return f"https://www.youtube.com/embed/{yt_match.group(6)}"

    # Lógica para Vimeo
    vimeo_regex = r'https?://(www\.)?vimeo.com/(\d+)'
    vmatch = re.match(vimeo_regex, url)
    if vmatch:
        return f"https://player.vimeo.com/video/{vmatch.group(2)}"

    return url # Si no coincide, devuelve el link original