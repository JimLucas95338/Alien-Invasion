import wave
import struct
import math
import random
import os
import numpy as np

def create_wave_file(filename, data, framerate=44100):
    """Save audio data to a WAV file."""
    with wave.open(filename, 'w') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(framerate)
        wave_file.writeframes(data)

def create_pew_sound():
    """Create a 'pew pew' laser sound."""
    sample_rate = 44100
    duration = 0.15  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create a frequency sweep from high to low
    frequency = np.linspace(1500, 500, len(t))
    waveform = np.sin(2 * np.pi * frequency * t)
    
    # Apply envelope for more 'pew' like sound
    envelope = np.exp(-t * 15)
    waveform = waveform * envelope
    
    # Normalize and convert to 16-bit integers
    waveform = waveform * 32767
    return struct.pack('h'*len(waveform), *waveform.astype(int))

def create_crackle_explosion():
    """Create a crackling explosion sound."""
    sample_rate = 44100
    duration = 0.4  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Base explosion sound
    base_freq = 100
    waveform = np.sin(2 * np.pi * base_freq * t)
    
    # Add crackles
    for _ in range(20):
        start = random.uniform(0, duration-0.1)
        crackle_duration = random.uniform(0.02, 0.08)
        crackle_idx = slice(int(start*sample_rate), int((start+crackle_duration)*sample_rate))
        freq = random.uniform(800, 2000)
        crackle = np.sin(2 * np.pi * freq * t[crackle_idx.start-int(start*sample_rate):crackle_idx.stop-int(start*sample_rate)])
        waveform[crackle_idx] += crackle * 0.3

    # Apply envelope
    envelope = np.exp(-t * 8)
    waveform = waveform * envelope
    
    # Normalize and convert to 16-bit integers
    waveform = (waveform / np.max(np.abs(waveform)) * 32767 * 0.7)
    return struct.pack('h'*len(waveform), *waveform.astype(int))

def create_alien_rumble():
    """Create a deep rumbling sound."""
    sample_rate = 44100
    duration = 0.3  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create base rumble with multiple low frequencies
    waveform = np.zeros_like(t)
    for freq in [30, 45, 60, 75]:
        waveform += np.sin(2 * np.pi * freq * t)
    
    # Add some noise for texture
    noise = np.random.random(len(t)) * 0.2
    waveform += noise
    
    # Apply envelope
    envelope = np.exp(-t * 10)
    waveform = waveform * envelope
    
    # Normalize and convert to 16-bit integers
    waveform = (waveform / np.max(np.abs(waveform)) * 32767 * 0.8)
    return struct.pack('h'*len(waveform), *waveform.astype(int))

def create_level_up_sound():
    """Create a two-tone 'do do' level up sound."""
    sample_rate = 44100
    note_duration = 0.15  # duration of each note
    
    # Create two notes
    t1 = np.linspace(0, note_duration, int(sample_rate * note_duration))
    t2 = np.linspace(0, note_duration, int(sample_rate * note_duration))
    
    # First note (lower frequency)
    freq1 = 440  # A4
    wave1 = np.sin(2 * np.pi * freq1 * t1)
    envelope1 = np.exp(-t1 * 8)
    wave1 = wave1 * envelope1
    
    # Second note (higher frequency)
    freq2 = 554.37  # C#5
    wave2 = np.sin(2 * np.pi * freq2 * t2)
    envelope2 = np.exp(-t2 * 8)
    wave2 = wave2 * envelope2
    
    # Combine the notes with a small gap
    gap = np.zeros(int(sample_rate * 0.05))  # 50ms gap
    waveform = np.concatenate([wave1, gap, wave2])
    
    # Normalize and convert to 16-bit integers
    waveform = (waveform / np.max(np.abs(waveform)) * 32767 * 0.8)
    return struct.pack('h'*len(waveform), *waveform.astype(int))

def main():
    # Create sounds directory if it doesn't exist
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sounds_dir = os.path.join(current_dir, 'sounds')
    if not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)

    # Generate and save all sounds
    print("Generating sound effects...")
    
    # Pew pew laser sound
    pew_data = create_pew_sound()
    create_wave_file(os.path.join(sounds_dir, 'shoot.wav'), pew_data)
    print("Created shoot.wav (pew pew sound)")
    
    # Crackling explosion
    explosion_data = create_crackle_explosion()
    create_wave_file(os.path.join(sounds_dir, 'explosion.wav'), explosion_data)
    print("Created explosion.wav (crackling sound)")
    
    # Alien rumble
    rumble_data = create_alien_rumble()
    create_wave_file(os.path.join(sounds_dir, 'alien_explosion.wav'), rumble_data)
    print("Created alien_explosion.wav (rumble sound)")
    
    # Level up do-do
    level_up_data = create_level_up_sound()
    create_wave_file(os.path.join(sounds_dir, 'level_up.wav'), level_up_data)
    print("Created level_up.wav (do-do sound)")
    
    print("\nAll sound effects generated successfully!")

if __name__ == '__main__':
    main()