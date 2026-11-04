# PAC — Personal AI & Voice Assistant

**PAC** is a multimodal Python desktop voice, vision, and gesture assistant built with Tkinter, OpenCV, MediaPipe, and hybrid AI (Offline Rules + Ollama / Claude LLM brain).

## Key Features

- **Voice & Text Dual Mode**: Continuous background speech recognition (`SpeechRecognition` + `sounddevice`) with natural neural TTS (`edge-tts` + `pyttsx3` fallback) and instant text chat.
- **3D Interactive Wireframe Orb HUD**: Real-time animated 3D particle/wireframe sphere that reacts to listening, thinking, and speaking states.
- **Acoustic Sound Triggers**: Hands-free wake/action via **double-clap** (wake/toggle mic) and **whistle** detection.
- **Hand Gestures & Air Drag-and-Drop**: MediaPipe hand tracking for volume/scroll control and pinching files in mid-air to drop them into the **Phone Shelf**.
- **Phone Link (Wi-Fi QR Transfer & Calls)**: Instant local Wi-Fi file sharing via QR code + ADB/Phone Link call dialing.
- **Face Recognition & Security Guard**: Registers known faces (`LBPHFaceRecognizer`), greets users personally, and alerts or locks the PC when an unknown person sits at the desk.
- **Augmented Reality (AR) Vision**: Live camera HUD with face tagging, object detection, colour analyzer, ruler mode, and virtual sticky notes.
- **Long-Term Memory & Offline Knowledge Base**: Remembers personal facts, notes, reminders, timetable schedules, and answers offline science/history/math (`SymPy`) queries.
- **Gmail OAuth Integration**: Read unread emails and send messages hands-free.

## Quick Start

```bash
pip install -r requirements.txt
python pac.py
```

## License

Licensed under the [MIT License](LICENSE). Made by Ankush.
