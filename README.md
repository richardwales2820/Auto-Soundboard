# Auto-Soundboard

A soundboard is usually used for fun to either playback popular quotes from celebrities or characters. The idea behind Auto Soundboard is to feed in any audio file and have a word bank created with audio clips trimmed for each word recognized in the audio file. The user can then use Text to Speech to generate sentences using the speaker's real voice. The audio will probably sound mangled and not continuous, but it is a start.

Content creators that enjoy clipping audio snippets from speeches or videos will be able to take advantage of this to find word occurrences in audio files with audio clips of the word.

Django web application back-end to be created to allow easy user interaction with the audio transcription.

## Current Work in progress
- User file upload and basic HTML page displayed
- Added models for the soundboard uploaded files and their parsed words with timestamps
- Using the request.session.session_key, I can display words for every file associated with the current user's browsing session
- User selects words from the available list, the audio from the uploaded file is then sliced to contain the relevant clips and exported for playback
- Think of ways to speed-up at scale
    - Cut file into snippets on parse and save those as separate files, combining only at the end request when the user selects words?
