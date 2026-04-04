Audio Signal Processing Task: Corrupted Transmission Recovery

Objective

The objective of this task was to recover a clean audio signal from a corrupted transmission using signal processing techniques. Since the corruption process was unknown, the approach involved analyzing the signal step-by-step and reversing the transformations applied to it.

Stage 1: Initial Analysis

The corrupted signal was first visualized in the time domain, where it appeared dense and noisy and did not resemble natural audio.

A Fast Fourier Transform (FFT) was then performed to analyze the frequency content. The frequency spectrum showed that the signal energy was not concentrated in the expected speech range (0–4000 Hz). This indicated that the signal had been shifted in frequency.

Stage 2: Frequency Shift Correction

Since natural audio typically lies in the lower frequency range, the observed shift suggested that the signal had undergone modulation during transmission.

To correct this, the signal was demodulated by multiplying it with a cosine wave of an appropriate frequency. This brought the signal back toward the baseband.

After this step, faint traces of speech became audible, confirming that the signal had been successfully shifted back.

Stage 3: Noise Observation and Filtering

Even after demodulation, the signal contained significant noise. The FFT showed that noise was spread across a wide range of frequencies.

A band-pass filter was applied to isolate the useful speech frequency band while removing unwanted frequency components outside this range.

Stage 4: Envelope Recovery

Although the frequency content appeared reasonable after filtering, the audio still sounded distorted. This suggested that the amplitude structure of the signal had been affected.

To address this, envelope detection was performed:

The signal was rectified using the absolute value
A low-pass filter was applied to recover the original amplitude envelope

This step significantly improved the clarity of the signal.

Final Processing

After recovering the envelope, additional filtering was applied to remove residual noise. A tighter band-pass filter focused on speech frequencies was used, followed by additional smoothing using a low-pass filter.

Finally, the signal was normalized to ensure proper amplitude scaling.

Results

The recovered signal contains clearly audible speech compared to the original corrupted input. Noise has been significantly reduced, and the signal structure has been restored. The transformation steps suggest that the signal was likely subjected to frequency shifting, noise addition, and amplitude distortion during transmission.

Conclusion

This task demonstrates how frequency-domain analysis and signal processing techniques can be used to reverse complex signal corruption. By carefully analyzing the FFT and progressively applying demodulation, filtering, and envelope detection, the original signal was successfully recovered.

Tools Used

Python
NumPy
SciPy
Matplotlib
SoundFile

Note

The demodulation frequency and filter parameters were chosen experimentally based on observations from the FFT plots to achieve the best balance between noise removal and signal preservation.