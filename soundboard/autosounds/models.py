from django.db import models

# The actual uploaded file and its associated session id from the
# user's browsing session
class SoundboardFile(models.Model):
    session_id = models.CharField(max_length=128)
    uploaded_file = models.FileField()

# Associates a word and timestamp range with a SoundboardFile model object
class SoundboardWord(models.Model):
    soundboard_file = models.ForeignKey(SoundboardFile, on_delete=models.CASCADE)
    word = models.CharField(max_length=64)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
