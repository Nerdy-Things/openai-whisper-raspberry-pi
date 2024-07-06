import pyaudio
import wave

chunk_size=10.0
form_1 = pyaudio.paInt16  # 16-bit resolution
chans = 1  # 1 channel
samp_rate = 44100  # 44.1kHz sampling rate
chunk = 4096  # 2^12 samples for buffer

class AudioRecord:
    _py_audio = pyaudio.PyAudio()

    def record(self, file_path: str) -> bool:
        usb_mic_found = False
        dev_index = -1
        for i in range(self._py_audio.get_device_count()):
            dev = self._py_audio.get_device_info_by_index(i)
            print((i, dev['name'], dev['maxInputChannels']))
            if "microphone" in dev['name'].lower() :
                usb_mic_found = True
                dev_index = i 
                break

        if usb_mic_found == False or dev_index == -1:
            print("USB MIC NOT FOUND")
            return False

        if usb_mic_found:
            record_secs = int(chunk_size)  # seconds to record

            # create pyaudio stream
            stream = self._py_audio.open(format=form_1, rate=samp_rate, channels=chans,
                            input_device_index=dev_index, input=True,
                            frames_per_buffer=chunk)
            
            frames = []

            # loop through stream and append audio chunks to frame array
            for ii in range(0, int((samp_rate/chunk)*record_secs)):
                if stream.is_stopped() == False :
                    data = stream.read(chunk)
                    frames.append(data)

            # stop the stream, close it, and terminate the pyaudio instantiation

            while stream.is_stopped() == False :
                stream.stop_stream()

            # Save the recorded data as a WAV file
            wf = wave.open(file_path, 'wb')
            wf.setnchannels(chans)
            wf.setsampwidth(self._py_audio.get_sample_size(form_1))
            wf.setframerate(samp_rate)
            wf.writeframes(b''.join(frames))
            wf.close()

            stream.close()
            return True

        def terminate():
            self._py_audio.terminate()
