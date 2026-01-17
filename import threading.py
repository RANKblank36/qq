import threading
import sys

try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"❌ Missing library: {e.name}")
    print("\n📦 Install commands:")
    print("   Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print("   macOS:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    stream = None
    frames = []

    print(f"\n🎤 {label}")
    print("   Press Enter to stop...")
    threading.Thread(target=wait_for_enter, daemon=True).start()

    print("🔴 Recording", end="", flush=True)
    while not stop_event.is_set():

        print(".", end="", flush=True)
    print(" ✅")
    width = 2
    return b''.join(frames), 16000, width
def analyze_audio(data, rate):
    samples = np.array([], dtype=np.int16)
    return {
        'duration': 0,
        'avg_volume': 0,
        'max_volume': 0,
        'samples': samples
    }
def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return "[TODO: transcription]"
    except:
        return "[Could not transcribe]"

def display_stats(stats, text, label):
    print(f"\n{'─' * 35}")
    print(f"📊 {label}")
    print(f"{'─' * 35}")
    print(f"⏱️  Duration:   {stats['duration']:.2f} sec")
    print(f"📈 Avg Volume: {stats['avg_volume']:.0f}")
    print(f"🔊 Max Volume: {stats['max_volume']:.0f}")
    print(f"📝 Text: {text}")

def compare(s1, s2):
    print("\n" + "=" * 40)
    print("🔬 COMPARISON RESULTS")
    print("=" * 40)

    longer = "?"
    
    print(f"⏱️  Recording {longer} is longer ({s1['duration']:.1f}s vs {s2['duration']:.1f}s)")

    louder = "?"
    print(f"🔊 Recording {louder} is louder ({s1['avg_volume']:.0f} vs {s2['avg_volume']:.0f})")

    print("\n💡 In L3, you'll CONTROL rate & volume when AI speaks!")

def plot_both(s1, s2, rate):
    pass
def main():
    print("=" * 40)
    print("🔬 VOICE ANALYSIS LAB")
    print("=" * 40)
    print("Record twice and compare your voice!")

    audio1, rate, width = record_audio("Recording 1: Speak NORMALLY")
    stats1, text1 = analyze_audio(audio1, rate), transcribe(audio1, rate, width)
    display_stats(stats1, text1, "Recording 1")

    input("\n🔄 Press Enter, then speak LOUDER or FASTER...")
    audio2, rate, width = record_audio("Recording 2: CHANGE your voice")
    stats2, text2 = analyze_audio(audio2, rate), transcribe(audio2, rate, width)
    display_stats(stats2, text2, "Recording 2")
    compare(stats1, stats2)
    plot_both(stats1, stats2, rate)

if __name__ == "__main__":
    main()
