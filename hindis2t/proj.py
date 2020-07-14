import sounddevice as sd
# import myspsolution as mysp
from listening import recog, aud
# from pydub import AudioSegment
# from pydub.playback import play
# from plotting import plot_sound


# import parselmouth
# from parselmouth.praat import call, run_file

print("welcome")


print("using speech recognition -- online")
while(True):

    text = recog().lower()

    if "sorry" in text:
        # print("kahani")
        # sound = AudioSegment.from_mp3('./audio/story1.mp3')
        # sound = sound[:(10*1000)]
        # play(sound)
        break
    # elif "kavita" in text:
    #     print("kavita")
    #     sound = AudioSegment.from_mp3('./audio/kavita.mp3')
    #     sound = sound[:(10*1000)]
    #     play(sound)
    #     break
    # else:
    #     print("try again")

# print("using speech pattern -- offline")
# aud()


# def filter(m, p):
#     sound = p+"/"+m+".wav"
#     sourcerun = p+"/filter.praat"
#     path = p+"/"
#     try:
#         objects = run_file(sourcerun, -20, 2, 0.3, "yes",
#                            sound, path, 80, 400, 0.01, capture_output=True)

#     except:
#         print("Try again the sound of the audio was not clear")
#     return


# p = "testing"  # Audio File title
# c = r"./audio"  # Path to the Audio_File directory (Python 3.7)
# out = filter(p, c)

# # to plot the sound input for marking sylables
# plot_sound()

# p = "filtered"  # Audio File title
# c = r"./audio"  # Path to the Audio_File directory (Python 3.7)
# out = mysp.myspsyl(p, c)
# if out > 4:
#     print("Kahani")
#     sound = AudioSegment.from_mp3('./audio/story1.mp3')
#     sound = sound[:(10*1000)]
#     play(sound)
# else:
#     print("kavita")
#     sound = AudioSegment.from_mp3('./audio/kavita.mp3')
#     sound = sound[:(10*1000)]
#     play(sound)
print("thank you")
