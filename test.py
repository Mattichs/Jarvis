import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

def capture_audio(device_index, sample_rate=44100, chunk_size=1024, record_seconds=5, output_filename="output.wav"):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=chunk_size)

    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / chunk_size * record_seconds)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    with open(output_filename, "wb") as wf:
        wf.write(b"".join(frames))

# Specify the device index you want to use for capturing audio
device_index = 1  # Change this to the desired device index

# Capture audio
capture_audio(device_index)