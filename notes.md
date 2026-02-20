
To add video 
- add media via paperclip (beware, anki renames files when saving to db if there are dupes)
- manually add to video field like: https://www.reddit.com/r/Anki/comments/1jwazp1/uploading_videos_to_cards/
This is because paperclip adds video to database and video field is experimental so can't be used via paperclip. 
 cd ~/Library/Application\ Support/Anki2/User\ 1/collection.media


To do 
- check on how genanki handles video 


Resources 
- Github handling videos: https://github.com/kelciour/movies2anki/blob/main/movies2anki.py#L333

# Notes 
- MUST USE av1 codec for video clip (ffmpeg -ss 00:01:00 -i my_input.webm -t 3 -c:v libsvtav1 -crf 30 -c:a copy grace_av1_clip.mp4)



# Large todo 

- Use H's tools to isolate text from video 

- use genanki to add video clips to anki 

- combine w/ yt-dlp

## Reqs 

- Input: 
    - youtube url 
    - timestamp
    - vocab word (in Chinese)

- Output:
    - Front:
        - Silent video without subtitles 
        - sentence with vocab missing
    - Back:
        - Full video with audio 
        - Full sentence
        - pinyin for vocab word 


- Optional:
    Input youtube url and list of vocab words and just generates from first appearance of word.





### movies2anki 
- `subs2srs_video_front_template`
- note["Video"] = video # video is path to 
        - is_add_dir_to_media_path ?





-----------

Julian Sobczak 


Collection  table
    - Deck(s)
    - models (aka Note Types) 
    - Tags

Cards table
    - due (when card should appear again)

Notes table
    - did (deck override. id?)
    - contains the *actual* card info like 水：water.
    - 1 Note may link to multiple cards (think of how you can fill out 1 Add in the and generate both the input and the reversed input as cards)

Revlog table
    - where reviews are registered 








#### `subs2srs_video_front_template`
"""
<video poster="{{Id}}.jpg" playsinline onclick="playVideo();return false;" controlsList="nodownload" disablepictureinpicture disableRemotePlayback>
  <source src="{{Id}}.mp4" type="video/mp4">
  <source src="{{Id}}.webm" type="video/webm">
</video>

<div class="media"><a class="replay-button" href="#" onclick="playVideo();return false;"></a></div>

<div class="snapshot" hidden>{{Snapshot}}</div>

<script>
var video = document.querySelector('video');
var error = false;
var autoplay = true;

function playVideo() {
  if (error) {
    if (typeof pycmd !== 'undefined') {
      pycmd("ankiplay{{Id}}.mp4");
    }
  } else {
    video.currentTime = 0;
    video.play();
  }
}

if (!globalThis.jsReplayButtonHandler) {
  document.addEventListener("keyup", (event) => {
    if (event.code === "KeyR") {
      playVideo();
    }
  });
  globalThis.jsReplayButtonHandler = true;
}

onUpdateHook.push(function () {
  if (document.querySelector("#answer")) {
    autoplay = false;
  }

  let source = document.querySelector('video source:last-child');
  source.addEventListener('error', () => {
    error = true;
    if (autoplay) {
      playVideo();
    }
  });

  if (autoplay) {
    playVideo();
  }
})();
</script>
"""