## Converts scc subtitles to srt
-> Add the path to the file
-> Define the framerate with -f or --fps (you can use the float or rounded version of framerates)
-> Decide if the timecodes are drop frame or not with -df --drop_frame

#### Note on Drop frames
The app automatically detects if the timecode is drop frame or ndf based on the *;* or *:* convention, but they occasionally are not correctly provided.


[x] The app is currently working with a good conversion for 24, 25 and 23.978 framerate files.

[ ] Test with more drop frame titles, specifically 29.97



IMPORTANT NOTE: Some specific conversions may have errors as this project is experimental. I made it to solve some logic problems and test the knowledge I got from these articles:

[http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/CC_CHARS.HTML](http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/CC_CHARS.HTML)

[http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/SCC_FORMAT.HTML](http://www.theneitherworld.com/mcpoodle/SCC_TOOLS/DOCS/SCC_FORMAT.HTML)

[https://www.davidheidelberger.com/2010/06/10/drop-frame-timecode/](https://www.davidheidelberger.com/2010/06/10/drop-frame-timecode/)
