import os
from kern import video_to_text

def test_video_lib_1_eating():
    file = 'files/food.mp4'
    text = video_to_text(file)
    assert 'eating' in text and 'spaghetti' in text

def test_video_lib_2_kicking():
    file = 'files/kick.mp4'
    text = video_to_text(file)
    assert 'soccer' in text

def test_video_lib_3_playing():
    file = 'files/cello.mp4'
    text = video_to_text(file)
    assert 'cello' in text

def test_video_bin_1_eating():
    text = os.popen("cat files/food.mp4 | video").read()
    assert 'eating' in text and 'spaghetti' in text

def test_video_bin_2_kicking():
    text = os.popen("cat files/kick.mp4 | video").read()
    assert 'soccer' in text

def test_video_bin_3_playing():
    text = os.popen("cat files/cello.mp4 | video").read()
    assert 'cello' in text
