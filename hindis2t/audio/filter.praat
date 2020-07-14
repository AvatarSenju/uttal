form Counting Syllables in Sound Utterances
   real Silence_threshold_(dB) 
   real Minimum_dip_between_peaks_(dB) 
   real Minimum_pause_duration_(s) 
   boolean Keep_Soundfiles_and_Textgrids 
   sentence soundin  
   sentence directory 
   positive Minimum_pitch_(Hz) 
   positive Maximum_pitch_(Hz) 
   positive Time_step_(s) 
endform

sound = Read from file... 'soundin$'


# use object ID
   selectObject: sound
   # select "Sound"
   method$ = "Spectral subtraction"
   smoothing = 40
   filtered = Remove noise: 0.0, 0.0, 0.025, 80, 10000, smoothing, method$
   selectObject: filtered
   Save as WAV file: "~/workload/iot-project/audio/filtered.wav"
   # Save as WAV file: './audio/filtered'.wav