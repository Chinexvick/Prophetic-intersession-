# Website intro video

Motion-graphics video built as an HTML page (`stage.html`) on one animation timeline,
rendered frame-by-frame at 30fps with Playwright and encoded with ffmpeg.

1. `node capture.js assets` — capture fresh screenshots of the live site into `assets/`
   (also copy `assets/img/logo.png` and `assets/img/gallery/g*.jpg` into `assets/`).
2. `node render.js --stills stills [vertical]` — preview stills of every scene.
3. `node render.js website-intro-16x9.mp4` and `node render.js website-intro-9x16.mp4 vertical`.

The domain shown is propheticintercession.org (scenes 3 and 11).

## Music
`compose_music.py` composes the original worship underscore (key of D, 72 BPM, Bm–G–D–A),
timed to the video's scenes. Needs `pip install numpy scipy pedalboard`.

    python3 compose_music.py                                   # -> music.wav
    ffmpeg -i music.wav -af loudnorm=I=-14:TP=-1.5 music-14.wav
    ffmpeg -i website-intro-16x9.mp4 -i music-14.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest out.mp4
