

### Workflow (that should eventually be automated)
0. User inputs youtube video url with a list of vocab words or timestamps 
1. Download the video 
2. Use ML to rip the subtitles from the movie and put the timestamps of their appearence in a vtt file 
        - example: 
                ```
                00:00:14.000 --> 00:00:17.500
                今天我们要看看

                00:00:18.000 --> 00:00:24.600
                我们喜欢什么样子的男人。
                ```

3. For each vocab word, find where that words in used subtitles, get the timestamp (maybe add buffer if timestamp is < 1 sec) and make a video clip of just that timestamp. 
        - example: 
            Input vocab: 看， 男人
            
            Video clip: 
                - 看：00:00:14.000 --> 00:00:17.500 
                - 男人: 00:00:18.000 --> 00:00:24.600 

4. Make flashcard:
    - examples: 
        - A: 
            - Front: 看
            - Back: subtitles + video clip 
        - B:
            - Front: 看 + *silent* video clip 
            - Back: subtitles + video clip 
        - C:
            - Front: video audio
            - Back: subtitles + video clip  




Lakshya's job:
I need you to make the video parser. It should take in a video from youtube (re-encode as needed w ffmpeg) and create the subtitles in vtt format. 

vtt format is the file format you get when you use yt-dlp to download the CC subtitles (not hard subs). 

For testing, use this youtube video because the CC subtitles seem to be at the exact same timestamps at the hard subs, meaning you can generate a vtt file from the hard subs then compare that hard-sub file directly to the CC-generated vtt file. 

Video: https://www.youtube.com/watch?v=3PLIZA83avs&list=PLWnMeKaZKVEUZbDnqOHc1z3SpjWb8dAOh


For the machine learning: 
https://kerrickstaley.com/2017/05/29/extracting-chinese-subs-part-1

Let me know if you have any questions. 