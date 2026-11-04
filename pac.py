"""
PAC - your personal voice assistant (Windows first; macOS/Linux mostly work)
==========================================================================

* Two modes, both reachable from the Menu at the top right:
    - TEXT mode  : type commands. No microphone, no speech recognition, no internet needed -
                   PAC runs fully offline (apps, files, notes, your own facts, timers, system
                   controls, spoken replies all work). Only things that are online by nature -
                   Google search, YouTube, WhatsApp, e-mail - need a connection.
    - VOICE mode : speak commands, no wake word. Speech is recognised by Google's Web Speech API
                   through the `SpeechRecognition` library (needs internet). If the connection
                   drops, PAC drops back to Text mode by itself.
* A blue wireframe orb ripples and swells with your voice (and while PAC speaks).
* Clap twice to wake PAC; whistle to open YouTube (Menu > Sound triggers). Analysed on your PC only.
* Say "wake up daddy is home": PAC says Hello sir, tells today's schedule, then reads today's top 20
  international headlines, fetched quietly from Google News in the background (no browser window).
  The same routine also runs by itself once each morning between 5:30 AM and 8:00 AM while PAC is running.
* Say "stop", "stop it" or "mute" (or press Esc) and PAC stops talking at once - even mid-sentence.
* Tells your schedule from a timetable you paste once (Menu > Schedule).
* Hand gestures through the laptop camera (Menu > Gestures): thumbs up, fist, swipes... each runs an action,
  you can teach new gestures, and it keeps working in the background while you use other apps.
* Faces (Menu > Faces): PAC learns the faces you enrol, notices who is at the laptop, welcomes them, flags strangers,
  and can lock commands (shutdown, e-mail, WhatsApp, typing...) to chosen faces. It prefers the laptop's infrared
  camera and falls back to the webcam. Only numbers are kept (~/.pac/faces.json), never pictures.
* Natural female voice through edge-tts when online; falls back to the offline system voice.
* Every feature lives in one dropdown Menu; the window is just the recorder, the chat and a text box.
* Notes open in Notepad, and PAC answers questions from YOUR OWN notes/facts offline
  (see the knowledge folder ~/.pac/knowledge) before it ever bothers Google.
* Can check your inbox and move mails you pick to Trash (needs Email setup once).
* A question PAC can't answer from your own facts is looked up quietly on the web in the background - Google, through
  a hidden copy of your own Chrome / Edge (DuckDuckGo if Google refuses). No "shall I search?" question and no browser
  window: the answer appears in the chat and is read out. Google opens in a new tab only when you say "open in a new
  tab". (This is the one thing that goes online in Text mode; Menu > Assistant switches it off.)
* Hand gestures you don't want can be deleted: Menu > Gestures > Delete gestures, or say "delete the fist gesture".
* Opens any installed app, files and folders, searches Google/YouTube,
  types for you, sends WhatsApp messages (preloaded or custom), controls the laptop.
* Friendly female voice (best female English voice installed on your system).
* Maths, by voice or text, offline: complex-number arithmetic ("(3 + 4i)(2 - i)", "modulus of 3 + 4i"), logarithms
  ("log base 2 of 64", "solve log x + log(x - 3) = 1") and algebra ("solve x squared plus 5x plus 6 equals 0",
  systems, inequalities, factorise, expand, simplify, differentiate, integrate, limits). The working shows in the
  chat and the answer is read out. A problem PAC can't do offline (a word problem) goes to Wolfram|Alpha if you add a
  free AppID, else to Claude when Claude mode is on, else to a quiet web search. Menu > Maths.
* Smarter web answers: after a quiet search PAC opens the top results itself (no browser window), reads them and
  answers from the paragraph that fits your question best, not just the search snippet.

* AI brain (optional): PAC understands ANY phrasing through a language model that picks one of its own tools
  ("it's too loud in here" -> volume down, "wake me when the pasta's done, ten minutes" -> timer). Menu-free: say
  "brain mode llm" (AI first), "brain mode hybrid" (default: built-in commands first, AI for the rest) or "brain off".
  Provider: Claude (online, needs your API key) or Ollama running on this laptop (fully offline):
  install Ollama, run `ollama pull llama3.1:8b`, then say "use ollama brain". Without a key and without Ollama
  chosen, PAC behaves exactly as before. Confirmations and face locks still apply to everything the AI triggers.

* Long-term memory (Menu > Memory): PAC remembers what you tell it about yourself - preferences ("I prefer tea"),
  routines ("every morning I walk"), people ("my wife is Priya"), contacts ("mom's number is 98765 43210") - in
  ~/.pac/memory.json on this laptop, and uses the few that fit each request: they personalise the AI brain's and Claude's
  answers, answer "where do I live" offline, and make "message my wife" work. It improves with use: repeating a thing
  strengthens it, a newer statement replaces an older one, and a command you repeat at the same time of day on three
  days becomes a routine. "What do you remember about me", "forget about tea", "forget everything", "turn off memory".
  Passwords, PINs and card numbers are never kept. Relevant memories reach Claude only if you allow it (Menu > Memory).

* Air drag & drop (Menu > Gestures > Air drag & drop, or say "start air drag"): your hand becomes the mouse through the
  laptop camera. Pinch your thumb and index finger together = press the button (selects the file under the pointer),
  keep pinching and move = drag, let go = drop. Or point and double air-tap to select, close your fist to grab, open your
  palm to drop. It drops onto File Explorer, the desktop and website upload boxes, so there is no "Choose file" step.
  Files you beam from your phone (file transfer) wait on a small shelf you can air-drag from. Each hand keeps its own
  slot even when the tracker's left/right label flips or one hand is reported twice.
* Files by voice or text: "tell me about file report pdf", "read several files on my laptop", "list files in downloads",
  "move report pdf to documents", "move all pdf files from downloads to taxes", "undo move", "create a folder called
  Projects on the desktop", "create a file called todo in documents with text buy milk". Nothing is ever deleted or
  overwritten, system folders are off limits, big moves are confirmed, and the AI brain does the same through its files tool.

* Augmented reality (Menu > Augmented reality, or say "start AR"): a live camera window with overlays. Hold an object in
  the guide box and say "learn this as my keys": PAC learns its look from several angles and recognises it again - it
  outlines it, labels it, and runs a command you tied to it ("when you see my keys say don't forget your wallet").
  PAC also guesses everyday things by outline with no teaching (pen, phone, remote, bottle, card, book, watch - ask
  "what objects can you recognise"). Clean shapes in the box (circle, triangle, square...) are predefined and can trigger commands too ("when you see a
  triangle open chrome"). Needs only opencv-python; nothing leaves the laptop, only numbers are kept (~/.pac/ar_objects.json).

FIRST-TIME SETUP  ->  double-click  setup_pac.bat   (installs everything and
creates a desktop shortcut).  Or manually:
    pip install SpeechRecognition sounddevice pyttsx3 pyautogui psutil pillow edge-tts sympy
    python pac.py --make-shortcut
SpeechRecognition + sounddevice are only needed for Voice mode / clap detection; Text mode starts without them.
edge-tts is optional (a more human voice, needs internet).
sympy is optional too (exact algebra; without it PAC still does arithmetic, complex numbers, logs and real roots).
opencv-python + mediapipe are optional too (only for hand gestures); faces need just opencv-python (4.5.4+).
The microphone is read with sounddevice, so PyAudio is NOT required.
"""

import ast
import base64
import cmath
import collections
import datetime
import difflib
import hashlib
import http.server
import json
import logging
import math
import operator
import os
import platform
import queue
import random
import re
import secrets
import shutil
import struct
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from array import array
from email.header import decode_header, make_header
from email.utils import parseaddr
from html import unescape as html_unescape
from pathlib import Path
from urllib.parse import parse_qs, quote, quote_plus, urlencode, urlparse

OS = platform.system()  # Windows / Darwin / Linux
if OS == "Windows":     # must be set before OpenCV loads: makes Media Foundation cameras start quickly and reliably
    os.environ.setdefault("OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS", "0")
HOME = Path.home()
APP_DIR = Path(__file__).resolve().parent
DATA_DIR = HOME / ".pac"
DATA_DIR.mkdir(exist_ok=True)
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "pac.log"
ICON_FILE = DATA_DIR / "pac_blue.ico"
NOTES_FILE = HOME / "pac_notes.txt"
KNOWLEDGE_DIR = DATA_DIR / "knowledge"
KNOWLEDGE_DIR.mkdir(exist_ok=True)
KNOWLEDGE_FILE = KNOWLEDGE_DIR / "my_facts.txt"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
SEARCH_DIRS = [HOME / d for d in ("Desktop", "Documents", "Downloads", "Pictures", "Videos", "Music")]
FOOTER_TEXT = "Made by Ankush"      # shown at the bottom of PAC's window

logging.basicConfig(filename=str(LOG_FILE), level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("pac")

DEFAULT_MESSAGES = [
    "I'm on my way.",
    "I'll call you back in a few minutes.",
    "Running a little late, please wait for me.",
    "Good morning! Have a wonderful day.",
    "Thank you so much!",
    "I'm in a meeting right now, I'll text you later.",
]
DEFAULT_CONFIG = {
    "country_code": "91",     # added to 10-digit phone numbers
    "contacts": {},           # {"mom": "9876543210"}
    "messages": DEFAULT_MESSAGES,
    "mic": None,              # microphone device index (None = system default)
    "gain": 2.0,              # software mic boost (auto-adjusted unless you move the slider)
    "auto_gain": True,        # automatically raise/lower the boost to keep your voice at a good level
    "rate": 165,              # speaking speed
    "voice_idx": 0,           # which of the female voices found
    "wa_delay": 7,            # seconds to wait for WhatsApp before pressing Enter
    "confirm_send": True,     # ask "shall I send it?" before sending WhatsApp messages
    "online_fallback": "ask", # only used when background_search is off: "ask" = ask before Google, "yes" = just open it, "no" = never
    "background_search": True, # a question with no offline answer is searched on the web quietly: no question, no browser window
    "search_engine": "google", # "google" = Google through a hidden Chrome/Edge (DuckDuckGo if it refuses), "duckduckgo" = DuckDuckGo only
    "mail_address": "",       # your Gmail address - set with the Email setup button
    "mail_client_id": "",     # from your own Google Cloud project (Email setup explains how)
    "mail_client_secret": "",
    "mail_refresh_token": "",  # filled in by "Sign in with Google"; kept in the system credential store if 'keyring' is installed
    "mail_count": 10,         # how many mails to list at a time
    "claude_model": "claude-haiku-4-5-20251001",   # used only when you switch Claude mode on / ask Claude
    "claude_api_key": "",     # only used if 'keyring' isn't installed; Claude mode itself is never remembered
    "transfer_port": 8765,    # port for phone <-> laptop file transfer
    "transfer_max_mb": 500,   # biggest file the phone may send
    "brain": "hybrid",        # rules = built-in patterns only | hybrid = patterns first, then the AI | llm = the AI understands everything first
    "brain_provider": "claude",  # claude (online, needs your key) or ollama (a model running on this laptop, offline)
    "ollama_url": "http://localhost:11434",
    "ollama_model": "llama3.1:8b",   # any Ollama model that supports tools, e.g. qwen2.5:7b
    "mode": "voice",          # "voice" = Google Web Speech (internet), "text" = typing only, fully offline
    "lang": "en-IN",          # language sent to Google\'s speech service
    "speak_replies": True,    # read replies aloud (offline text-to-speech)
    "neural": True,           # use the natural online voice when edge-tts is installed and you are online
    "neural_voice": "en-IN-NeerjaNeural",
    "sound_triggers": True,   # double clap = wake PAC, whistle = open YouTube
    "trigger_sens": "medium", # low / medium / high
    "gesture_enabled": False,  # camera hand gestures (also restarted at launch when left on)
    "gesture_cam": 0,          # which camera
    "gesture_hold": 0.35,      # seconds a pose must be held before it counts (was 0.7)
    "voice_speed": "fast",     # how quickly a finished sentence is sent off: fast / balanced / careful
    "voice_interrupt": True,   # say "stop" / "mute" while PAC is talking and she stops
    "voice_interrupt_sens": "medium",  # low / medium / high: how much louder than her you must be
    "news_count": 20,          # headlines read after "wake up daddy is home"
    "auto_home": True,         # run the "wake up daddy is home" routine by itself, once a morning, inside the window below
    "auto_home_start": "05:30",  # window start (24 h, HH:MM)
    "auto_home_end": "08:00",    # window end   (24 h, HH:MM)
    "auto_home_date": "",      # the day the routine last ran (so it only runs once a day)
    "fast_tuning_v2": False,   # set once the quicker defaults have been applied
    "builtin_knowledge": True,  # keep the built-in facts pack in ~/.pac/knowledge (answers offline)
    "gesture_beep": True,      # short beep when a gesture fires (Windows)
    "gesture_map": {},         # your changes to what the built-in gestures do
    "custom_gestures": [],     # gestures you taught PAC
    "deleted_gestures": [],    # built-in gestures you deleted (PAC ignores them; Delete gestures > Restore brings them back)
    "start_minimized": False,  # open straight into the background
    "math_online": True,       # a maths problem PAC can't do offline (a word problem) is looked up online
    "wolfram_appid": "",       # optional free Wolfram|Alpha AppID - the best online help for word problems
    "read_pages": True,        # after a quiet search, read the top pages for a fuller answer than the snippet
    "face_enabled": False,     # watch the camera for faces (also restarted at launch when left on)
    "face_security": False,    # lock chosen commands to chosen faces (Menu > Faces > People & permissions)
    "face_cam": "auto",        # "auto" prefers the infrared camera, or a camera number
    "face_threshold": 0.40,    # how alike two faces must be (cosine); higher = stricter
    "face_fps": 4,             # pictures looked at per second
    "face_min_px": 70,         # ignore faces narrower than this (people far behind you)
    "face_absent_secs": 45,    # out of sight this long counts as "left"
    "face_greet": True,        # say welcome back when a known face arrives
    "face_lock_on_leave": False,  # lock the laptop when the owner walks away (needs face security on)
    "face_save_unknown": False,   # keep a snapshot of a stranger in ~/.pac/faces (off = no pictures kept)
    "face_rules": {},          # group -> anyone / guest / trusted / owner, overriding the defaults
    "memory_enabled": True,    # long-term memory: PAC remembers what you tell it about yourself (~/.pac/memory.json)
    "memory_learn": "all",     # all = typed and spoken sentences | typed = typed only | explicit = only when you say "remember"
    "memory_habits": True,     # notice commands you repeat at the same time of day and remember them as routines
    "ar_enabled": False,       # augmented reality (also restarted at launch when left on)
    "ar_cam": "auto",          # which camera AR uses
    "ar_announce": True,       # say "I can see your keys" when a learned object appears
    "ar_hud": True,            # time / battery / next-class panel in the AR window
    "ar_min_matches": 12,      # how many matching features count as "the same object" (higher = stricter)
    "memory_share_ai": True,   # let the AI brain / Claude see the few memories relevant to a request (Ollama is local, always allowed)
}


def load_config():
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    try:
        cfg.update(json.loads(CONFIG_FILE.read_text(encoding="utf-8")))
    except Exception:
        pass
    if not cfg.get("fast_tuning_v2"):          # one-off: move an old slow 0.7 s+ hold time to the quicker default
        try:
            if float(cfg.get("gesture_hold", 0.7)) >= 0.7:
                cfg["gesture_hold"] = 0.35
        except (TypeError, ValueError):
            cfg["gesture_hold"] = 0.35
        cfg["fast_tuning_v2"] = True
    return cfg


def save_config(cfg):
    try:
        CONFIG_FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    except Exception:
        logger.exception("could not save config")


# --------------------------------------------------------------- icon + shortcut
def make_icon(path: Path) -> None:
    """Draw a small blue 'P' icon (no image libraries needed)."""
    if path.exists():
        return
    size, scale = 64, 6
    glyph = ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."]
    fw, fh = 5 * scale, 7 * scale
    ox, oy = (size - fw) // 2, (size - fh) // 2
    cx = cy = (size - 1) / 2
    radius = size / 2 - 1.5
    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            alpha = max(0.0, min(1.0, radius + 0.5 - d))
            k = y / (size - 1)
            r, g, b = int(20 * (1 - k)), int(20 * (1 - k)), int(255 + (110 - 255) * k)
            fx, fy = x - ox, y - oy
            if 0 <= fx < fw and 0 <= fy < fh and glyph[fy // scale][fx // scale] == "#":
                r, g, b = 0, 0, 0
            row.append(bytes((b, g, r, int(alpha * 255))))
        rows.append(row)
    pixels = b"".join(b"".join(row) for row in reversed(rows))
    mask = bytes(size * size // 8)
    dib = struct.pack("<IiiHHIIiiII", 40, size, size * 2, 1, 32, 0, len(pixels) + len(mask), 0, 0, 0, 0)
    entry = struct.pack("<BBBBHHII", size, size, 0, 0, 1, 32, len(dib) + len(pixels) + len(mask), 22)
    path.write_bytes(struct.pack("<HHH", 0, 1, 1) + entry + dib + pixels + mask)


def make_shortcut() -> str:
    """Create 'PAC Assistant' on the desktop (Windows)."""
    if OS != "Windows":
        return "Automatic desktop shortcuts are only supported on Windows."
    try:
        make_icon(ICON_FILE)
        exe = Path(sys.executable)
        target = exe.with_name("pythonw.exe")
        if not target.exists():
            target = exe
        script = Path(__file__).resolve()
        q = lambda p: str(p).replace("'", "''")
        ps = (
            "$ws = New-Object -ComObject WScript.Shell; "
            "$lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) 'PAC Assistant.lnk'; "
            "$s = $ws.CreateShortcut($lnk); "
            f"$s.TargetPath = '{q(target)}'; "
            f"$s.Arguments = '\"{q(script)}\"'; "
            f"$s.WorkingDirectory = '{q(script.parent)}'; "
            f"$s.IconLocation = '{q(ICON_FILE)}'; "
            "$s.Description = 'PAC voice assistant'; "
            "$s.Save(); Write-Output $lnk"
        )
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
                           capture_output=True, text=True, timeout=60, creationflags=NO_WINDOW)
        if r.returncode == 0:
            return f"Shortcut created on your desktop: {r.stdout.strip()}"
        return f"Could not create the shortcut: {r.stderr.strip() or r.stdout.strip()}"
    except Exception as e:
        return f"Could not create the shortcut: {e}"


def _startup_shortcut_path() -> str:
    ps = "Write-Output ([Environment]::GetFolderPath('Startup'))"
    r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
                       capture_output=True, text=True, timeout=30, creationflags=NO_WINDOW)
    startup = r.stdout.strip() or str(HOME / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
    return str(Path(startup) / "PAC Assistant.lnk")


def autostart_enabled() -> bool:
    return OS == "Windows" and Path(_startup_shortcut_path()).exists()


def make_autostart(enable: bool = True) -> str:
    """Add or remove a shortcut in the Windows Startup folder, so PAC opens by itself at login."""
    if OS != "Windows":
        return "Automatic startup is only supported on Windows right now."
    try:
        link = _startup_shortcut_path()
        if not enable:
            Path(link).unlink(missing_ok=True)
            return "PAC will no longer open automatically at login."
        make_icon(ICON_FILE)
        exe = Path(sys.executable)
        target = exe.with_name("pythonw.exe")
        if not target.exists():
            target = exe
        script = Path(__file__).resolve()
        q = lambda p: str(p).replace("'", "''")
        ps = (
            "$ws = New-Object -ComObject WScript.Shell; "
            f"$s = $ws.CreateShortcut('{q(link)}'); "
            f"$s.TargetPath = '{q(target)}'; "
            f"$s.Arguments = '\"{q(script)}\"'; "
            f"$s.WorkingDirectory = '{q(script.parent)}'; "
            f"$s.IconLocation = '{q(ICON_FILE)}'; "
            "$s.Description = 'PAC voice assistant'; "
            "$s.Save()"
        )
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
                           capture_output=True, text=True, timeout=60, creationflags=NO_WINDOW)
        if r.returncode == 0:
            return "Done - PAC will open automatically next time you log in to Windows."
        return f"Could not set up automatic startup: {r.stderr.strip() or r.stdout.strip()}"
    except Exception as e:
        return f"Could not set up automatic startup: {e}"


if __name__ == "__main__" and "--make-shortcut" in sys.argv:
    print(make_shortcut())
    sys.exit(0)
if __name__ == "__main__" and "--enable-autostart" in sys.argv:
    print(make_autostart(True))
    sys.exit(0)
if __name__ == "__main__" and "--disable-autostart" in sys.argv:
    print(make_autostart(False))
    sys.exit(0)

# --------------------------------------------------------------- third-party imports
try:
    import psutil
    import pyautogui
    import pyttsx3
except ImportError as _e:
    _msg = (f"PAC needs a few extra packages ({_e}).\n\nOpen Command Prompt and run:\n\n"
            "pip install SpeechRecognition sounddevice pyttsx3 pyautogui psutil pillow")
    try:
        import tkinter as _tk
        from tkinter import messagebox as _mb
        _r = _tk.Tk()
        _r.withdraw()
        _mb.showerror("PAC - missing packages", _msg)
    except Exception:
        print(_msg)
    sys.exit(1)

# Voice input is optional: Text mode needs none of this, so PAC still starts - and works offline - without it.
try:
    import speech_recognition as sr
except Exception:
    sr = None
try:
    import sounddevice as sd
except Exception:          # package missing, or no PortAudio on this machine
    sd = None
VOICE_LIBS_OK = sr is not None and sd is not None
try:
    import edge_tts          # optional: natural neural voices (needs internet)
except Exception:
    edge_tts = None

pyautogui.FAILSAFE = False

# --------------------------------------------------------------- number helpers
NUM_UNITS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen".split())}
NUM_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90}
NUM_WORDS = set(NUM_UNITS) | set(NUM_TENS) | {"hundred", "thousand"}


def words_to_int(words):
    total = cur = 0
    for w in words:
        if w in NUM_UNITS:
            cur += NUM_UNITS[w]
        elif w in NUM_TENS:
            cur += NUM_TENS[w]
        elif w == "hundred":
            cur = (cur or 1) * 100
        elif w == "thousand":
            total += (cur or 1) * 1000
            cur = 0
    return total + cur


def extract_number(text):
    """First number in text, as digits ('5') or words ('twenty five')."""
    m = re.search(r"\d+", text)
    if m:
        return int(m.group())
    run = []
    for w in text.split():
        if w in NUM_WORDS:
            run.append(w)
        elif run:
            break
    return words_to_int(run) if run else None


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod, ast.USub: operator.neg}


def safe_eval(expr):
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            a, b = ev(n.left), ev(n.right)
            if isinstance(n.op, ast.Pow) and abs(b) > 100:
                raise ValueError("exponent too large")
            return _OPS[type(n.op)](a, b)
        if isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.operand))
        raise ValueError("unsupported")
    return ev(ast.parse(expr, mode="eval"))


def spoken_to_expr(text):
    t = " " + text.lower() + " "
    for a, b in ((" multiplied by ", " * "), (" divided by ", " / "), (" to the power of ", " ** "),
                 (" plus ", " + "), (" minus ", " - "), (" times ", " * "), (" over ", " / "),
                 (" into ", " * "), (" x ", " * ")):
        t = t.replace(a, b)
    out, buf = [], []
    for tok in t.split():
        if tok in NUM_WORDS:
            buf.append(tok)
        else:
            if buf:
                out.append(str(words_to_int(buf)))
                buf = []
            out.append(tok)
    if buf:
        out.append(str(words_to_int(buf)))
    return " ".join(out)


# --------------------------------------------------------------- notepad + offline knowledge
KNOWLEDGE_HEADER = (
    "# PAC's private knowledge. PAC answers your questions from this file (and from any other\n"
    "# .txt / .md / .csv file in this folder, and from your notes) WITHOUT going online.\n"
    "# Write one fact per line, or Q: / A: pairs. Lines starting with # are ignored.\n"
    "#\n"
    "# My wifi password is blue-tiger-42.\n"
    "# Q: when is the rent due\n"
    "# A: The rent is due on the 5th of every month.\n\n"
)


def ensure_knowledge_file():
    if not KNOWLEDGE_FILE.exists():
        KNOWLEDGE_FILE.write_text(KNOWLEDGE_HEADER, encoding="utf-8")


def open_in_notepad(path):
    """Open a text file in Notepad (TextEdit on macOS, the default editor on Linux)."""
    path = Path(path)
    if not path.exists():
        path.touch()
    if OS == "Windows":
        subprocess.Popen(["notepad.exe", str(path)])
    elif OS == "Darwin":
        subprocess.Popen(["open", "-a", "TextEdit", str(path)])
    else:
        open_path(path)


STOPWORDS = set(
    "a an the is are was were be been am do does did of to in on at for from with and or my me i you your our "
    "we it its this that these those can could would should will shall please tell about explain define "
    "meaning what whats who whom when where why how which there here have has had s".split())


def _stem(w):
    """Crude but consistent: lives / live / living -> liv, passwords -> password, watches -> watch."""
    if len(w) > 4:
        if w.endswith(("sses", "shes", "ches", "xes", "zes")):
            w = w[:-2]
        elif w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
    if len(w) > 5 and w.endswith("ing"):
        w = w[:-3]
    if len(w) > 3 and w.endswith("e"):
        w = w[:-1]
    return w


def _tokens(text):
    return [_stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS]


KNOWLEDGE_PACK_VERSION = 5
KNOWLEDGE_PACK_FILE = KNOWLEDGE_DIR / "00_pac_builtin.txt"
KNOWLEDGE_PACK = """# PAC built-in knowledge pack - version 5
# PAC rewrites this file when a newer pack ships. Put your own facts in my_facts.txt instead.

# ---------- Using PAC
Q: how do I use gestures
A: Tick Menu, Gestures, Gesture control. Hold a hand sign in front of the camera. Thumbs up raises the volume, a fist plays or pauses, a peace sign takes a screenshot.
Q: can PAC read two hands
A: Yes. Each hand is tracked on its own, so each can make a different gesture at the same time. The same pose in both hands, or moving both open hands apart or together, counts as a two-hand gesture.
Q: two hand gestures
A: Both palms, both fists, both thumbs up, both thumbs down, both peace signs, hands apart and hands together. Set what each one does under Menu, Gestures, Gesture actions.
Q: zoom with hands
A: Open both hands in front of the camera and move them apart to zoom in, or together to zoom out. Both are Ctrl plus and Ctrl minus.
Q: change gesture hold time
A: Menu, Gestures, Hold time. A shorter hold reacts faster but can fire by accident. The default is a third of a second.
Q: change what a gesture does
A: Menu, Gestures, Gesture actions. Pick a gesture and choose an action, such as volume, a PAC command, a website or a key combination.
Q: teach a new gesture
A: Menu, Gestures, Teach a new gesture. Hold your hand shape steady while PAC records it, then choose what it should do.
Q: delete a gesture
A: Say delete gestures, or open Menu, Gestures, Delete gestures, tick the ones you don't want and press Delete selected. You can also say delete the fist gesture. A gesture you taught is erased for good. A built-in one is switched off, and you can bring it back.
Q: restore deleted gestures
A: Say restore gestures, or open Menu, Gestures, Delete gestures and tick the ones to restore. Only built-in gestures can be restored. A gesture you taught and then deleted has to be taught again.
Q: how do i get information about my files
A: Say tell me about file report pdf, or tell me about files notes txt, budget xlsx and letter docx, and I read each one: its type, size, dates, and what's inside, like pages in a PDF, words in a Word document, rows in a CSV, sheets in a spreadsheet, or the size of a picture. Say tell me about all files in downloads to go through a whole folder, read file notes txt to hear the start of it, and list files in documents to see what's there.
Q: how do i move files into folders
A: Say move report pdf to documents, move budget xlsx and letter docx to taxes, or move all pdf files from downloads to documents. If the folder doesn't exist I offer to create it, or say move it to a new folder called Taxes. I ask before a big move and never overwrite anything. Say undo move to put them back.
Q: how do i create a file or folder
A: Say create a folder called Projects on the desktop, create folders Math and Science in documents, or create a file called todo in documents with text buy milk. I can make text files, Word documents, Excel spreadsheets and more. Nothing is ever overwritten.
Q: air drag and drop
A: Say start air drag, or tick Menu, Gestures, Air drag & drop. Your palm becomes the mouse: move your open hand to point at a file, close your fist to grab it, carry it, and open your palm to drop it. It works on File Explorer, the desktop and website upload boxes, so you never have to press Choose file.
Q: how do i air drag a file from my phone
A: Turn on file transfer, open the address on your phone, and tap Pick files to beam. They fly over at once and appear on a small shelf at the right of the laptop screen. Say start air drag, pinch a file with your thumb and finger, move, and let go where you want it. Say show phone files to bring the shelf back.
Q: how do i select and drag a file with air drag
A: With air drag on, hold your hand up so the pointer follows it, then pinch your thumb and index finger together on a file. A pinch is a press: it selects the file, and if you keep pinching and move your hand you drag it. Let go to drop it. A quick pinch is a click and two quick pinches open the file. You can also point with your index finger and bend it twice like pressing a button to select, then close your fist to grab and open your palm to drop.
Q: stop air drag
A: Say stop air drag, or untick Menu, Gestures, Air drag & drop. The mouse is yours again.
Q: how does background search work
A: When I can't answer a question from my own facts, I look it up on the web quietly in the background. I don't ask first and I don't open a browser. Say open in a new tab to see the same search on Google.
Q: open the google results
A: Say open in a new tab, and I open the last search on Google in a new browser tab.
Q: make voice faster
A: Menu, Voice input, Reaction speed. Fast sends your sentence as soon as you stop talking. Careful waits through longer pauses.
Q: change voice
A: Say change voice, or use a name like use Sonia voice or use British voice. Say list voices to hear the options. The natural voices need internet and the edge tts package.
Q: claude mode
A: Claude mode sends what I can't handle myself to Anthropic's Claude. It is off every time PAC starts. Say claude mode on to switch it on, claude mode off to stop, or ask Claude followed by a question for a one-off.
Q: set up claude api key
A: Menu, Assistant, Claude setup. Paste an API key from console dot anthropic dot com, choose a model and press save and test.
Q: add my timetable
A: Say open timetable, paste your classes one per line like Monday 09:00 to 10:00 Maths, Room 204, and save. Then ask what's my schedule or what's next.
Q: add my own facts
A: Say add a fact, or open my facts and write one fact per line, or Q colon question then A colon answer. I search these before anything else.
Q: check my email
A: Set up Email once from the Menu, then say check my mail. I only move mails to Trash when you say yes.
Q: clap to wake
A: Clap twice to wake PAC. Whistle to open YouTube. Change the sensitivity under Menu, Sound triggers.
Q: voice mode and text mode
A: Voice mode listens through the microphone using Google speech recognition and needs internet. Text mode is typing only and works fully offline.
Q: stop listening
A: Say stop listening or go to sleep. Say wake up, or clap twice, to bring me back.
Q: send a whatsapp message
A: Say send message 2 to mom for a saved message, or message mom saying I'll be late. I ask before sending.
Q: take a screenshot
A: Say screenshot, or make a peace sign at the camera. It is saved in your Pictures folder.

Q: what is augmented reality in PAC
A: Say start AR and a camera window opens. PAC outlines and labels objects it has learned, shows the time, battery and your next class, and runs commands when it sees something you taught it.
Q: how do I teach PAC an object
A: Say start AR, hold the object inside the box in the camera window, and say learn this as my keys, or press L in the window. Turn it slowly for three seconds. Show it again later and PAC recognises it.
Q: how do I make PAC do something when it sees an object
A: Say when you see my keys say don't forget your wallet, or when you see a triangle open chrome. Say clear AR action for keys to remove it.
Q: what shapes does PAC know
A: Circle, triangle, square, rectangle, pentagon and hexagon. Draw one on paper and hold it in the box. Say set up AR starter commands to give them ready-made actions.
Q: forget an object in AR
A: Say forget object and its name, or open Menu, Augmented reality, Objects and actions.
Q: why does PAC not recognise my object
A: Teach it again from a few more angles in good light, hold it close inside the box, and avoid shiny or plain objects. A plain object is matched by outline, so hold it inside the box.
Q: how does PAC memory work
A: PAC remembers what you tell it about yourself, like your name, what you prefer, your routines and the people in your life. It keeps them in a small file on this laptop and uses the few that fit each request. Say what do you remember about me to see them.
Q: what does PAC learn about me
A: Only things you say about yourself, such as my name is, I prefer, every morning I, my wife is. It also notices a command you repeat at the same time of day on several days. It never keeps passwords, PINs or card numbers.
Q: how do I make PAC forget something
A: Say forget about, and what to forget. Say forget that to undo what it just learned, forget everything to clear it all, or open Menu, Memory, View and edit memories.
Q: is my memory sent to the internet
A: No, it stays on this laptop. The few memories that fit a request are shown to the AI brain or Claude only when one of those is switched on and Menu, Memory, lets the AI see them. A local Ollama brain never sends anything out.
Q: how do I give a folder a nickname
A: Say my taxes folder is documents slash taxes, or I keep my photos in pictures slash holiday. I check the folder exists, remember the nickname, and then you can say move report pdf to taxes or list files in photos. Say forget about taxes to remove it.
Q: turn off memory
A: Say turn off memory, or untick Menu, Memory, Long-term memory. What is already saved is kept until you forget it.

# ---------- Windows and computer shortcuts
Q: copy shortcut
A: Control and C copies, Control and V pastes, Control and X cuts, Control and Z undoes.
Q: select all shortcut
A: Control and A.
Q: switch between windows shortcut
A: Alt and Tab.
Q: show desktop shortcut
A: Windows key and D.
Q: lock computer shortcut
A: Windows key and L.
Q: screenshot shortcut windows
A: Windows key, Shift and S opens the snipping tool. Print Screen captures the whole screen.
Q: open task manager
A: Press Control, Shift and Escape.
Q: close window shortcut
A: Alt and F4 closes the window. Control and W closes a browser tab.
Q: reopen closed tab
A: Control, Shift and T.
Q: refresh page shortcut
A: F5, or Control and R.
Q: find on page shortcut
A: Control and F.
Q: new browser tab shortcut
A: Control and T.
Q: what is ram
A: RAM is the computer's short-term working memory. Programs use it while they run, and it is cleared when you switch off.
Q: ram versus storage
A: RAM is fast, temporary working memory. Storage, such as an SSD, keeps your files permanently.
Q: what is an ssd
A: A solid state drive. It stores files on flash memory with no moving parts, so it is much faster than an older hard disk.
Q: what is a cpu
A: The central processing unit, the part of the computer that carries out instructions.
Q: what is a gpu
A: The graphics processing unit. It draws images and video and is also good at running many calculations in parallel.
Q: what is wifi
A: A way of connecting devices to a network wirelessly using radio waves, usually through a router.
Q: what is an ip address
A: A number that identifies a device on a network, like a postal address for data.
Q: what is the cloud
A: Computers run by a company that you reach over the internet, used to store files or run programs.
Q: what is an api
A: An application programming interface. It is a set of rules that lets one program ask another program to do something.
Q: what is a vpn
A: A virtual private network. It sends your internet traffic through an encrypted connection to another server.
Q: what is a browser
A: A program for viewing websites, such as Chrome, Edge or Firefox.
Q: what is a password manager
A: A program that stores strong, different passwords for each site, so you only remember one master password.
Q: how to make a strong password
A: Use a long phrase of at least twelve characters, mix words and numbers, never reuse it, and turn on two step verification.
Q: what is two factor authentication
A: A second check besides your password, such as a code sent to your phone, so a stolen password alone is not enough.
Q: what is phishing
A: A fake email or message that tries to trick you into giving away passwords or money. Don't click unexpected links.
Q: what is binary
A: A number system with only zeros and ones, which is how computers store everything.
Q: what is a byte
A: Eight bits. A kilobyte is about a thousand bytes, a megabyte about a million, a gigabyte about a billion.
Q: what is python
A: A popular programming language known for being easy to read. PAC itself is written in Python.
Q: what is artificial intelligence
A: Computer systems that do tasks which normally need human intelligence, such as understanding speech or recognising images.
Q: what is machine learning
A: A way of building software that learns patterns from examples instead of following only hand-written rules.
Q: computer running slow
A: Restart it, close programs you don't use, check Task Manager for anything using lots of memory, and make sure there is free disk space.
Q: wifi not working
A: Turn Wi-Fi off and on, restart the router, restart the laptop, and check whether other devices connect.
Q: laptop battery tips
A: Lower the screen brightness, close background programs, turn on battery saver, and avoid leaving it at full charge or fully empty for long.

# ---------- Full forms
Q: what does gst stand for
A: Goods and Services Tax, the indirect tax charged on most goods and services in India.
Q: gst full form
A: Goods and Services Tax, the indirect tax charged on most goods and services in India.
Q: what does upi stand for
A: Unified Payments Interface, a system for instant bank to bank payments from your phone in India.
Q: upi full form
A: Unified Payments Interface, a system for instant bank to bank payments from your phone in India.
Q: what does ram stand for
A: Random Access Memory, the computer's fast, temporary working memory.
Q: ram full form
A: Random Access Memory, the computer's fast, temporary working memory.
Q: what does cpu stand for
A: Central Processing Unit, the part of the computer that carries out instructions.
Q: cpu full form
A: Central Processing Unit, the part of the computer that carries out instructions.
Q: what does gpu stand for
A: Graphics Processing Unit, the chip that draws images and video.
Q: gpu full form
A: Graphics Processing Unit, the chip that draws images and video.
Q: what does api stand for
A: Application Programming Interface, a set of rules that lets one program ask another to do something.
Q: api full form
A: Application Programming Interface, a set of rules that lets one program ask another to do something.
Q: what does vpn stand for
A: Virtual Private Network, an encrypted connection to another server.
Q: vpn full form
A: Virtual Private Network, an encrypted connection to another server.
Q: what does ssd stand for
A: Solid State Drive, storage built from flash memory with no moving parts.
Q: ssd full form
A: Solid State Drive, storage built from flash memory with no moving parts.
Q: what does bmi stand for
A: Body Mass Index, weight in kilograms divided by height in metres squared.
Q: bmi full form
A: Body Mass Index, weight in kilograms divided by height in metres squared.
Q: what does dna stand for
A: Deoxyribonucleic acid, the molecule that carries genetic information.
Q: dna full form
A: Deoxyribonucleic acid, the molecule that carries genetic information.
Q: what does utc stand for
A: Coordinated Universal Time, the world's reference clock.
Q: utc full form
A: Coordinated Universal Time, the world's reference clock.
Q: what does wifi stand for
A: Wireless Fidelity is the common explanation, though the name is really just a brand name.
Q: wifi full form
A: Wireless Fidelity is the common explanation, though the name is really just a brand name.

# ---------- Maths
Q: value of pi
A: Pi is about 3.14159.
Q: pythagoras theorem
A: In a right angled triangle, the square of the longest side equals the sum of the squares of the other two sides. A squared plus B squared equals C squared.
Q: area of a circle
A: Pi times the radius squared.
Q: circumference of a circle
A: Two times pi times the radius.
Q: area of a triangle
A: Half times the base times the height.
Q: area of a rectangle
A: Length times width.
Q: volume of a cylinder
A: Pi times the radius squared times the height.
Q: volume of a sphere
A: Four thirds times pi times the radius cubed.
Q: quadratic formula
A: x equals minus b, plus or minus the square root of b squared minus four a c, all divided by two a.
Q: what is a prime number
A: A number greater than one that can only be divided evenly by one and itself. Examples are 2, 3, 5, 7 and 11.
Q: first ten prime numbers
A: 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
Q: how many degrees in a triangle
A: The angles of a triangle add up to 180 degrees.
Q: how many degrees in a circle
A: 360 degrees.
Q: how many sides does a hexagon have
A: Six.
Q: how many sides does an octagon have
A: Eight.
Q: what is the square root of 144
A: 12.
Q: what is the square root of 2
A: About 1.414.
Q: what is a percentage
A: A number out of one hundred. To find a percent of a number, multiply the number by the percent and divide by one hundred.
Q: speed distance time formula
A: Speed equals distance divided by time.
Q: simple interest formula
A: Interest equals principal times rate times time, divided by one hundred.
Q: what is the roman numeral for 50
A: L.
Q: roman numerals
A: I is 1, V is 5, X is 10, L is 50, C is 100, D is 500 and M is 1000.

# ---------- Science
Q: speed of light
A: About 300 thousand kilometres per second, or 299,792 kilometres per second in a vacuum.
Q: speed of sound
A: About 343 metres per second in air at room temperature.
Q: boiling point of water
A: 100 degrees Celsius, or 212 Fahrenheit, at sea level.
Q: freezing point of water
A: 0 degrees Celsius, or 32 Fahrenheit.
Q: normal body temperature
A: About 37 degrees Celsius, or 98.6 Fahrenheit.
Q: celsius to fahrenheit formula
A: Multiply by nine fifths, then add 32.
Q: fahrenheit to celsius formula
A: Subtract 32, then multiply by five ninths.
Q: acceleration due to gravity
A: About 9.8 metres per second squared on Earth.
Q: chemical formula of water
A: H two O.
Q: chemical formula of carbon dioxide
A: C O two.
Q: chemical formula of table salt
A: Na Cl, sodium chloride.
Q: chemical symbol for gold
A: Au.
Q: chemical symbol for silver
A: Ag.
Q: chemical symbol for iron
A: Fe.
Q: chemical symbol for sodium
A: Na.
Q: chemical symbol for potassium
A: K.
Q: most abundant gas in the atmosphere
A: Nitrogen, about 78 percent. Oxygen is about 21 percent.
Q: what do plants take in during photosynthesis
A: Carbon dioxide and water, using sunlight, to make glucose and release oxygen.
Q: what is dna
A: Deoxyribonucleic acid, the molecule that carries genetic information in living things.
Q: powerhouse of the cell
A: The mitochondria.
Q: how many bones in the human body
A: An adult has 206 bones.
Q: largest organ of the human body
A: The skin.
Q: how many planets are in the solar system
A: Eight. In order from the sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.
Q: largest planet
A: Jupiter.
Q: closest planet to the sun
A: Mercury.
Q: red planet
A: Mars.
Q: how far is the sun from earth
A: About 150 million kilometres.
Q: how far is the moon from earth
A: About 384 thousand kilometres.
Q: how long does earth take to orbit the sun
A: About 365 and a quarter days, which is why we have a leap year every four years.
Q: how long does light from the sun take to reach earth
A: About 8 minutes and 20 seconds.
Q: what causes the seasons
A: The tilt of the Earth's axis as it orbits the sun, not its distance from the sun.
Q: what causes tides
A: Mainly the gravity of the moon pulling on the oceans, with some effect from the sun.
Q: what is gravity
A: The force that pulls objects with mass towards each other. It keeps us on the ground and the planets in orbit.
Q: newton's first law
A: An object stays at rest or moves in a straight line at constant speed unless a force acts on it.
Q: newton's second law
A: Force equals mass times acceleration.
Q: newton's third law
A: Every action has an equal and opposite reaction.
Q: what is ohm's law
A: Voltage equals current times resistance.
Q: unit of force
A: The newton.
Q: unit of energy
A: The joule.
Q: unit of power
A: The watt.
Q: unit of electrical resistance
A: The ohm.
Q: what is the ph of pure water
A: 7, which is neutral. Below 7 is acid and above 7 is alkaline.
Q: what is an atom
A: The smallest unit of an element. It has a nucleus of protons and neutrons with electrons around it.
Q: states of matter
A: Solid, liquid and gas. Plasma is often counted as a fourth.
Q: what is the hardest natural substance
A: Diamond.
Q: what is the largest ocean
A: The Pacific Ocean.
Q: longest river in the world
A: The Nile and the Amazon are the two candidates. The Nile is traditionally listed as the longest.
Q: highest mountain in the world
A: Mount Everest, about 8,849 metres above sea level.
Q: how many continents are there
A: Seven: Asia, Africa, North America, South America, Antarctica, Europe and Australia, also called Oceania.
Q: how many oceans are there
A: Five: Pacific, Atlantic, Indian, Southern and Arctic.
Q: how many days in a leap year
A: 366.
Q: how many days in a week
A: Seven.

# ---------- India
Q: emergency number in india
A: 112 is the single emergency number. Police is 100, fire is 101 and ambulance is 102 or 108.
Q: police number india
A: 100, or 112 for any emergency.
Q: fire brigade number india
A: 101.
Q: ambulance number india
A: 102 or 108, or 112 for any emergency.
Q: women helpline number india
A: 1091 is the women helpline. 112 works for any emergency.
Q: child helpline number india
A: 1098.
Q: capital of India
A: New Delhi.
Q: when did india get independence
A: On 15 August 1947.
Q: republic day of india
A: 26 January. The Constitution came into effect on 26 January 1950.
Q: national animal of india
A: The Bengal tiger.
Q: national bird of india
A: The Indian peacock.
Q: national flower of india
A: The lotus.
Q: national fruit of india
A: The mango.
Q: national anthem of india
A: Jana Gana Mana.
Q: national song of india
A: Vande Mataram.
Q: currency of india
A: The Indian rupee.
Q: how many states in india
A: 28 states and 8 union territories.
Q: largest state in india by area
A: Rajasthan.
Q: longest river in india
A: The Ganga, also called the Ganges.
Q: highest mountain in india
A: Kangchenjunga, the third highest mountain in the world.
Q: official language of karnataka
A: Kannada.
Q: capital of karnataka
A: Bengaluru.
Q: capital of tamil nadu
A: Chennai.
Q: capital of kerala
A: Thiruvananthapuram.
Q: capital of andhra pradesh
A: Amaravati is the capital of Andhra Pradesh. Hyderabad was the shared capital until June 2024.
Q: capital of telangana
A: Hyderabad.
Q: capital of maharashtra
A: Mumbai.
Q: capital of gujarat
A: Gandhinagar.
Q: capital of rajasthan
A: Jaipur.
Q: capital of uttar pradesh
A: Lucknow.
Q: capital of madhya pradesh
A: Bhopal.
Q: capital of bihar
A: Patna.
Q: capital of west bengal
A: Kolkata.
Q: capital of odisha
A: Bhubaneswar.
Q: capital of punjab
A: Chandigarh.
Q: capital of haryana
A: Chandigarh.
Q: capital of himachal pradesh
A: Shimla.
Q: capital of uttarakhand
A: Dehradun.
Q: capital of jharkhand
A: Ranchi.
Q: capital of chhattisgarh
A: Raipur.
Q: capital of assam
A: Dispur.
Q: capital of goa
A: Panaji.
Q: capital of sikkim
A: Gangtok.
Q: capital of arunachal pradesh
A: Itanagar.
Q: capital of nagaland
A: Kohima.
Q: capital of manipur
A: Imphal.
Q: capital of mizoram
A: Aizawl.
Q: capital of meghalaya
A: Shillong.
Q: capital of tripura
A: Agartala.
Q: when was mahatma gandhi born
A: On 2 October 1869. His birthday is celebrated as Gandhi Jayanti.
Q: first prime minister of india
A: Jawaharlal Nehru.
Q: first president of india
A: Rajendra Prasad.
Q: indian standard time
A: India Standard Time is five and a half hours ahead of UTC, written UTC plus 5:30.

# ---------- World
Q: capital of France
A: Paris.
Q: capital of Germany
A: Berlin.
Q: capital of Italy
A: Rome.
Q: capital of Spain
A: Madrid.
Q: capital of Portugal
A: Lisbon.
Q: capital of the United Kingdom
A: London.
Q: capital of Ireland
A: Dublin.
Q: capital of the Netherlands
A: Amsterdam.
Q: capital of Belgium
A: Brussels.
Q: capital of Switzerland
A: Bern.
Q: capital of Austria
A: Vienna.
Q: capital of Sweden
A: Stockholm.
Q: capital of Norway
A: Oslo.
Q: capital of Denmark
A: Copenhagen.
Q: capital of Finland
A: Helsinki.
Q: capital of Poland
A: Warsaw.
Q: capital of Greece
A: Athens.
Q: capital of Turkey
A: Ankara.
Q: capital of Russia
A: Moscow.
Q: capital of Ukraine
A: Kyiv.
Q: capital of China
A: Beijing.
Q: capital of Japan
A: Tokyo.
Q: capital of South Korea
A: Seoul.
Q: capital of Pakistan
A: Islamabad.
Q: capital of Bangladesh
A: Dhaka.
Q: capital of Nepal
A: Kathmandu.
Q: capital of Bhutan
A: Thimphu.
Q: capital of Sri Lanka
A: Sri Jayawardenepura Kotte is the official capital. Colombo is the largest city and commercial capital.
Q: capital of Afghanistan
A: Kabul.
Q: capital of Iran
A: Tehran.
Q: capital of Iraq
A: Baghdad.
Q: capital of Saudi Arabia
A: Riyadh.
Q: capital of the United Arab Emirates
A: Abu Dhabi.
Q: capital of Egypt
A: Cairo.
Q: capital of South Africa
A: South Africa has three: Pretoria for the government, Cape Town for the parliament and Bloemfontein for the courts.
Q: capital of Nigeria
A: Abuja.
Q: capital of Kenya
A: Nairobi.
Q: capital of Ethiopia
A: Addis Ababa.
Q: capital of the United States
A: Washington, D C.
Q: capital of Canada
A: Ottawa.
Q: capital of Mexico
A: Mexico City.
Q: capital of Brazil
A: Brasilia.
Q: capital of Argentina
A: Buenos Aires.
Q: capital of Chile
A: Santiago.
Q: capital of Peru
A: Lima.
Q: capital of Colombia
A: Bogota.
Q: capital of Australia
A: Canberra.
Q: capital of New Zealand
A: Wellington.
Q: capital of Thailand
A: Bangkok.
Q: capital of Vietnam
A: Hanoi.
Q: capital of Malaysia
A: Kuala Lumpur.
Q: capital of Singapore
A: Singapore is a city state, so it has no separate capital.
Q: capital of the Philippines
A: Manila.
Q: currency of japan
A: The yen.
Q: currency of the united kingdom
A: The pound sterling.
Q: currency of the united states
A: The US dollar.
Q: currency of china
A: The yuan, also called the renminbi.
Q: currency of europe
A: The euro, used by many European Union countries.
Q: largest country by area
A: Russia.
Q: smallest country in the world
A: Vatican City.
Q: most populated country
A: India and China are the two most populated countries, each with over 1.4 billion people.
Q: largest desert
A: Antarctica is the largest desert. The Sahara is the largest hot desert.
Q: largest continent
A: Asia.
Q: who invented the telephone
A: Alexander Graham Bell, in 1876.
Q: who invented the light bulb
A: Thomas Edison made the first practical one, working with others, around 1879.
Q: who discovered gravity
A: Isaac Newton described the law of gravity in the 1600s.
Q: who discovered penicillin
A: Alexander Fleming, in 1928.
Q: who wrote romeo and juliet
A: William Shakespeare.
Q: who wrote the ramayana
A: Valmiki.
Q: who wrote the mahabharata
A: Vyasa, according to tradition.
Q: who wrote the indian constitution
A: A drafting committee chaired by B R Ambedkar prepared it. It was adopted in 1949.
Q: who painted the mona lisa
A: Leonardo da Vinci.
Q: first man on the moon
A: Neil Armstrong, on 20 July 1969.
Q: first person in space
A: Yuri Gagarin, in 1961.
Q: first indian in space
A: Rakesh Sharma, in 1984.
Q: when did world war two end
A: In 1945. It began in 1939.
Q: when did world war one start
A: In 1914. It ended in 1918.
Q: how many players in a cricket team
A: Eleven.
Q: how many players in a football team
A: Eleven on the field.
Q: how many players in a basketball team
A: Five on the court.
Q: how many players in a hockey team
A: Eleven on the field.
Q: how many minutes in a football match
A: Ninety, in two halves of forty five, plus added time.
Q: how many rings on the olympic flag
A: Five.
Q: how often are the olympics held
A: Every four years.

# ---------- Time and calendar
Q: how many days in each month
A: January 31, February 28 or 29, March 31, April 30, May 31, June 30, July 31, August 31, September 30, October 31, November 30, December 31.
Q: how many seconds in a day
A: 86,400.
Q: how many minutes in a day
A: 1,440.
Q: how many hours in a week
A: 168.
Q: how many weeks in a year
A: 52, plus a day or two.
Q: what is a leap year
A: A year with 366 days, with an extra day on 29 February. It comes every four years, except century years not divisible by 400.
Q: what is utc
A: Coordinated Universal Time, the world's reference clock. Time zones are written as hours ahead of or behind it.
Q: time difference between india and uk
A: India is 4 and a half hours ahead of the UK in summer, and 5 and a half hours ahead in winter.
Q: time difference between india and usa
A: India is 9 and a half to 13 and a half hours ahead of the US, depending on the US time zone and daylight saving.
Q: time difference between india and japan
A: Japan is 3 and a half hours ahead of India.
Q: time difference between india and dubai
A: Dubai is 1 and a half hours behind India.
Q: time difference between india and singapore
A: Singapore is 2 and a half hours ahead of India.
Q: time difference between india and australia
A: Sydney is 4 and a half to 5 and a half hours ahead of India, depending on daylight saving.

# ---------- Everyday and study
Q: what is the pomodoro technique
A: Work for 25 minutes with full focus, then rest for 5 minutes. After four rounds, take a longer break.
Q: how to study better
A: Study in short focused sessions, test yourself instead of rereading, space your revision over several days, sleep well and put your phone away.
Q: how many hours of sleep do I need
A: Most adults do best with seven to nine hours a night.
Q: how much water should I drink
A: About two litres a day is a common guide, more when it is hot or you exercise. Needs vary from person to person.
Q: what to do in an emergency
A: Stay calm, move to safety, and call 112 in India. Tell them where you are and what has happened.
Q: first aid for a burn
A: Cool the burn under cool running water for about twenty minutes. Don't use ice, butter or toothpaste. Seek medical help for large or deep burns.
Q: first aid for a nosebleed
A: Sit upright, lean slightly forward, pinch the soft part of your nose for ten minutes and breathe through your mouth.
Q: what is bmi
A: Body mass index: weight in kilograms divided by height in metres squared.
Q: how to calculate percentage
A: Divide the part by the whole and multiply by one hundred.
Q: how to calculate average
A: Add all the numbers and divide by how many there are.
Q: what is gst
A: Goods and Services Tax, the indirect tax charged on most goods and services in India.
Q: what is upi
A: Unified Payments Interface, a system for instant bank to bank payments from your phone in India.
Q: what is an fd
A: A fixed deposit. You put money in a bank for a fixed period and earn a set rate of interest.
Q: what is inflation
A: A general rise in prices over time, so each rupee buys a little less.
Q: parts of speech
A: Noun, pronoun, verb, adjective, adverb, preposition, conjunction and interjection.
Q: what is a noun
A: A word that names a person, place, thing or idea.
Q: what is a verb
A: A word that describes an action or a state, like run or be.
Q: what is an adjective
A: A word that describes a noun, like big or red.
Q: how many letters in the english alphabet
A: Twenty six, of which five are vowels: A, E, I, O and U.
Q: days of the week
A: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.
Q: months of the year
A: January, February, March, April, May, June, July, August, September, October, November and December.
Q: colours of the rainbow
A: Violet, indigo, blue, green, yellow, orange and red. Remember them as VIBGYOR.
Q: primary colours
A: Red, yellow and blue for paint. Red, green and blue for light on screens.
"""


def install_knowledge_pack(cfg):
    """Keep the built-in facts pack in the knowledge folder: written on first run, refreshed when this PAC ships a
    newer pack, removed if you switch it off. Only ever touches 00_pac_builtin.txt - never your own files.
    Returns the number of facts in the pack, or 0 if it is off."""
    try:
        have = KNOWLEDGE_PACK_FILE.exists()
        if not cfg.get("builtin_knowledge", True):
            if have:
                KNOWLEDGE_PACK_FILE.unlink()
            return 0
        if have:
            m = re.search(r"version (\d+)", KNOWLEDGE_PACK_FILE.read_text(encoding="utf-8", errors="ignore")[:200])
            if m and int(m.group(1)) >= KNOWLEDGE_PACK_VERSION:
                return len(re.findall(r"^Q:", KNOWLEDGE_PACK, re.M))
        tmp = KNOWLEDGE_PACK_FILE.with_suffix(".part")
        tmp.write_text(KNOWLEDGE_PACK, encoding="utf-8")
        tmp.replace(KNOWLEDGE_PACK_FILE)
        return len(re.findall(r"^Q:", KNOWLEDGE_PACK, re.M))
    except OSError:
        logger.exception("could not install the built-in knowledge pack")
        return 0


QUALIFIERS = {_stem(w) for w in (
    "first last largest smallest tallest highest longest biggest closest second third oldest newest "
    "latest current present recent new old national".split())}


class Knowledge:
    """Answers questions from text files you control - no internet, no AI service.

    Sources: every .txt/.md/.csv in ~/.pac/knowledge, plus your notes file.
    Format: one fact per line, or 'Q: question' followed by 'A: answer'."""
    EXTS = {".txt", ".md", ".csv"}

    def __init__(self):
        self.sig = None
        self.chunks = []        # (set of key words, text to say, True if it comes from your own files)
        self.idf = {}
        self.max_idf = 1.0

    def _files(self):
        files = [p for p in sorted(KNOWLEDGE_DIR.glob("*")) if p.is_file() and p.suffix.lower() in self.EXTS]
        if NOTES_FILE.exists():
            files.append(NOTES_FILE)
        return files

    @staticmethod
    def split(text, is_notes=False):
        out, pending_q = [], None
        for line in text.splitlines():
            line = line.strip()
            if is_notes:
                line = re.sub(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]\s*", "", line)
            if not line or line.startswith("#"):
                pending_q = None
                continue
            q = re.match(r"(?i)^q\s*[:\-]\s*(.+)$", line)
            if q:
                pending_q = q.group(1)
                continue
            a = re.match(r"(?i)^a\s*[:\-]\s*(.+)$", line)
            if a and pending_q:
                out.append((pending_q, a.group(1)))
                pending_q = None
                continue
            pending_q = None
            if len(line) > 300:        # pasted paragraph: index it two sentences at a time
                sents = re.split(r"(?<=[.!?])\s+", line)
                for i in range(max(1, len(sents) - 1)):
                    piece = " ".join(sents[i:i + 2])
                    out.append((piece, piece))
            else:
                out.append((line, line))
        return out

    def refresh(self):
        files = self._files()
        sig = tuple((str(p), p.stat().st_mtime_ns) for p in files)
        if sig == self.sig:
            return
        self.sig = sig
        raw = []
        for p in files:
            try:
                mine = p.name != KNOWLEDGE_PACK_FILE.name          # the built-in pack is not "yours"
                raw.extend((key, say, mine) for key, say in
                           self.split(p.read_text(encoding="utf-8", errors="ignore"), p == NOTES_FILE))
            except OSError:
                logger.exception("could not read %s", p)
        self.chunks = [(set(_tokens(key)), say, mine) for key, say, mine in raw]
        self.chunks = [(k, say, mine) for k, say, mine in self.chunks if k]
        df = {}
        for keys, _, _ in self.chunks:
            for w in keys:
                df[w] = df.get(w, 0) + 1
        n = len(self.chunks)
        self.idf = {w: math.log(1 + n / c) for w, c in df.items()}
        self.max_idf = math.log(1 + n) if n else 1.0

    def ask(self, query, min_cover=0.6):
        """Best matching line for the question, or None if nothing in your files fits well."""
        self.refresh()
        if not self.chunks:
            return None
        q = []
        for w in _tokens(query):
            if w not in self.idf and len(w) >= 5:      # forgive small mis-hearings
                close = difflib.get_close_matches(w, list(self.idf), n=1, cutoff=0.82)
                w = close[0] if close else w
            if w not in q:
                q.append(w)
        if not q:
            return None
        weight = lambda w: self.idf.get(w, self.max_idf)
        total = sum(weight(w) for w in q)
        best, best_key = None, (0.0, 0)
        for keys, say, mine in self.chunks:
            # "first prime minister" must not answer "who is the prime minister": a line about the first / largest /
            # latest... of something only fits a question that asks for that
            if (keys & QUALIFIERS) - set(q):
                continue
            hit = sum(weight(w) for w in q if w in keys)
            if hit:
                # most of the question covered; on a tie your own line beats the built-in pack; then the tighter line
                key = (round(hit / total, 2), mine, -len(keys))
                if key > best_key:
                    best, best_key = say, key
        return best if best and best_key[0] >= min_cover else None

    def count(self):
        self.refresh()
        return len(self.chunks), sum(1 for _, _, mine in self.chunks if mine)      # (everything, yours)

    @staticmethod
    def add(fact):
        ensure_knowledge_file()
        text = KNOWLEDGE_FILE.read_text(encoding="utf-8", errors="ignore")
        with open(KNOWLEDGE_FILE, "a", encoding="utf-8") as f:
            f.write(("" if text.endswith("\n") else "\n") + fact.strip() + "\n")


# --------------------------------------------------------------- long-term memory: what PAC learns about YOU
# Kept on this laptop in ~/.pac/memory.json. Things you say about yourself ("my name is...", "I prefer...", "every
# morning I...", "my wife is Priya", "mom's number is ...") are noticed and filed, and the few that matter to a
# request are pulled back out: they colour the AI brain's and Claude's answers, answer your own questions offline
# ("where do I live"), and let "message my wife" find the right contact. It improves with use: repeating something
# strengthens it, a newer statement replaces an older one on the same subject, memories that keep proving useful rank
# higher, and a command you repeat at the same time of day on several days becomes a remembered routine.
MEMORY_FILE = DATA_DIR / "memory.json"
MEMORY_MAX_ITEMS = 400
MEMORY_KINDS = ("preference", "routine", "person", "fact")      # contacts live in config["contacts"], where WhatsApp reads them
MEMORY_KIND_LABEL = {"preference": "Preferences", "routine": "Routines and habits", "person": "People", "fact": "Facts about you"}

_SECRET_RE = re.compile(
    r"\b(?:password|passcode|passwd|pin(?! code)|otp|one[- ]time (?:password|code)|cvv|cvc|card number|credit card|"
    r"debit card|account number|ifsc|aadhaar|aadhar|pan (?:card|number)|passport number|social security|ssn|"
    r"secret key|api key|private key|recovery code|security answer)\b", re.I)
_CARD_RE = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)|\b\d{4}[ -]\d{4}[ -]\d{4}\b")


def looks_secret(text):
    """Passwords, PINs, card numbers... PAC never files these: memory can be shared with an AI."""
    return bool(_SECRET_RE.search(text or "") or _CARD_RE.search(text or ""))


_REL_GROUPS = {
    "mom": ("mom", "mother", "mummy", "mommy", "mama", "mum", "amma"),
    "dad": ("dad", "father", "daddy", "papa", "appa"),
    "wife": ("wife",), "husband": ("husband",), "brother": ("brother",), "sister": ("sister",),
    "boss": ("boss", "manager"), "son": ("son",), "daughter": ("daughter",), "friend": ("friend",),
    "best friend": ("best friend",), "girlfriend": ("girlfriend",), "boyfriend": ("boyfriend",),
    "partner": ("partner",), "teacher": ("teacher",), "colleague": ("colleague",), "uncle": ("uncle",),
    "aunt": ("aunt", "aunty"), "grandfather": ("grandfather", "grandpa"), "grandmother": ("grandmother", "grandma"),
    "cousin": ("cousin",), "roommate": ("roommate", "flatmate"), "doctor": ("doctor",),
}
_REL_CANON = {syn: canon for canon, syns in _REL_GROUPS.items() for syn in syns}
_REL_RE = "|".join(sorted(_REL_CANON, key=len, reverse=True))
_NAME = r"[A-Za-z][A-Za-z'.-]*(?: [A-Za-z][A-Za-z'.-]*){0,2}"
_PLACE = r"[A-Za-z][A-Za-z.'-]*(?: [A-Za-z][A-Za-z.'-]*){0,3}"
_NUM = r"\+?\d[\d\s().-]{6,18}\d"
_RX = re.IGNORECASE
_NOT_A_NAME = {"a", "an", "the", "very", "so", "not", "my", "your", "our", "his", "her", "their", "from", "in", "at", "on",
               "going", "coming", "here", "there", "still", "also", "really", "just", "always", "never", "now", "being",
               "sick", "ill", "busy", "home", "out", "away", "late", "early", "angry", "fine", "ok", "okay", "good", "bad",
               "great", "tired", "awake", "asleep", "free", "working", "sleeping", "calling", "waiting", "visiting",
               "back", "later", "tomorrow", "today", "soon", "if", "when", "please", "maybe", "again", "anyway", "tonight"}
_BAD_CONTACT = {"my", "the", "your", "his", "her", "our", "their", "this", "that", "what", "whose", "a", "an", "me", "i",
                "own", "new", "old", "phone", "mobile", "cell"}
_BAD_OBJ_START = re.compile(r"^(?:it|that|this|those|these|them|him|her|you|how|when|what|where|why|who|whom|which|"
                            r"the way|if|there|so|very|more|less|too|much|a lot)\b", _RX)
_NOT_ROUTINE = {"think", "feel", "wonder", "say", "said", "hope", "guess", "believe", "know", "knew", "forget"}
_TRANSIENT_RE = re.compile(r"\b(?:today|tonight|tomorrow|yesterday|later|next|this (?:morning|evening|afternoon|week|"
                           r"weekend)|at \d|need to|have to|has to|should|must|gotta|going to|will|want to|remind)\b", _RX)
_PERSONAL_START = re.compile(r"^(?:my|i|i'm|i am|i've|i have|i'd|we|our|every|each)\b", _RX)

_P_CONTACT1 = re.compile(rf"(?:my\s+)?(?P<n>[a-z][a-z' ]{{0,28}}?)(?:'s)?\s+(?:(?:phone|mobile|cell|whatsapp|contact)\s+)?"
                         rf"(?:number|no|num)\s*(?:is|are|:|=)?\s*(?P<num>{_NUM})", _RX)
_P_CONTACT2 = re.compile(rf"(?:save|store|add|keep)\s+(?:the\s+)?(?:(?:phone\s+)?number\s+)?(?P<num>{_NUM})\s+"
                         rf"(?:as|for|under)\s+(?P<n>[a-z][a-z' ]{{0,28}})", _RX)
_P_CONTACT3 = re.compile(rf"(?:add|save|create|new)\s+(?:a\s+|new\s+)*contact\s+(?:called\s+|named\s+)?"
                         rf"(?P<n>[a-z][a-z' ]{{0,28}}?)\s+(?:with\s+(?:the\s+)?(?:number|phone(?: number)?)\s+|number\s+|at\s+|is\s+)?"
                         rf"(?P<num>{_NUM})", _RX)
_P_FOLDER1 = re.compile(r"my\s+(?P<a>[a-z][a-z ]{0,25}?)\s+(?:folder|directory)\s+(?:is|lives|sits|stays)?\s*(?:in|at|under|called)?\s*(?P<p>\S.{1,100})", _RX)
_P_FOLDER2 = re.compile(r"i\s+(?:keep|store|save|put)\s+(?:all\s+)?(?:my|the)\s+(?P<a>[a-z][a-z ]{0,25}?)(?:\s+(?:files|stuff|documents|docs|pdfs|photos))?\s+(?:in|at|under|inside)\s+(?P<p>\S.{1,100})", _RX)
_P_FOLDER3 = re.compile(r"my\s+(?P<a>[a-z][a-z ]{0,25}?)\s+(?:files|stuff|documents|docs)\s+are\s+(?:in|at|under|inside)\s+(?P<p>\S.{1,100})", _RX)
_P_NAME = re.compile(rf"(?:my name is|my name's|i am called|i'm called|people call me|everyone calls me|friends call me)\s+"
                     rf"(?P<n>{_NAME})", _RX)
_P_ADDRESS = re.compile(r"(?:call me|you can call me|you may call me|please call me|just call me|address me as|refer to me as|"
                        r"i like to be called|i prefer to be called)\s+(?P<n>[A-Za-z][A-Za-z' -]{1,24})", _RX)
_P_REL_A = re.compile(rf"my\s+(?P<rel>{_REL_RE})(?:'s name)?\s+is\s+(?P<n>{_NAME})", _RX)
_P_REL_B = re.compile(rf"(?P<n>{_NAME})\s+is\s+my\s+(?P<rel>{_REL_RE})", _RX)
_P_BIRTHDAY = re.compile(r"my\s+(?:(?P<who>[a-z][a-z ]{0,20}?)'s\s+)?birthday\s+(?:is|falls on)\s+(?:on\s+)?(?P<d>.{3,30})", _RX)
_P_FAV = re.compile(r"my\s+favou?rite\s+(?P<c>[a-z]+(?: [a-z]+)?)\s+is\s+(?P<v>.{1,50})", _RX)
_P_LIVE = re.compile(rf"i\s+(?:live|stay|reside|am living|am staying|'m living|'m staying)\s+in\s+(?P<p>{_PLACE})", _RX)
_P_FROM = re.compile(rf"i(?:'m| am)\s+from\s+(?P<p>{_PLACE})", _RX)
_P_WORK = re.compile(rf"i\s+(?:work|am working|'m working)\s+(?P<w>at|for)\s+(?P<p>{_PLACE})", _RX)
_P_STUDY = re.compile(rf"i\s+(?:study|am studying|'m studying)\s+at\s+(?P<p>{_PLACE})", _RX)
_P_TRAIT = re.compile(r"i(?:'m| am)\s+(?P<d>(?:a\s+|an\s+)?(?:vegetarian|vegan|pescatarian|lactose intolerant|gluten[- ]free|"
                      r"left[- ]handed|right[- ]handed|morning person|night owl|early bird|early riser))", _RX)
_P_ALLERGY = re.compile(r"i(?:'m| am)\s+allergic\s+to\s+(?P<o>.{2,40})", _RX)
_P_EVERY = re.compile(r"(?:every|each)\s+(?P<w>morning|afternoon|evening|night|day|weekday|weekend|week|monday|tuesday|"
                      r"wednesday|thursday|friday|saturday|sunday)\s*,?\s+i\s+(?P<a>.{3,80})", _RX)
_P_USUALLY = re.compile(r"i\s+(?P<adv>usually|normally|always|typically|generally|often|regularly|tend to|mostly)\s+(?P<a>.{3,80})", _RX)
_P_CLOCK = re.compile(r"i\s+(?P<a>(?:wake up|get up|go to bed|go to sleep|go to the gym|go to gym|go to work|go to college|"
                      r"go to school|have breakfast|have lunch|have dinner|start work|finish work|work out|exercise|meditate)"
                      r"\s+(?:at|around|by)\s+(?:\d{1,2}(?::\d\d)?\s*(?:a\.?m\.?|p\.?m\.?)?|noon|midnight)"
                      r"(?:\s+(?:every day|daily|on weekdays|on weekends|every morning))?)", _RX)
_P_PREF = re.compile(r"i\s+(?:(?:really|absolutely|totally|also|just|definitely|truly|still)\s+)*"
                     r"(?P<v>love|like|prefer|enjoy|hate|dislike|can'?t stand|cannot stand|"
                     r"(?:do not|don'?t|dont)\s+(?:really\s+)?(?:like|enjoy|love))\s+(?P<o>.+)", _RX)


def _tidy(text):
    """A statement as it is filed: one line, capital first letter, 'I' capitalised, no trailing full stop."""
    s = " ".join((text or "").replace("\u2019", "'").split()).strip(" .!,;:")
    s = re.sub(r"\bi\b", "I", s)
    return s[:1].upper() + s[1:]


def _nice(s):
    return " ".join(w if w[:1].isupper() else w[:1].upper() + w[1:] for w in s.split())


def _key_of(prefix, text):
    return prefix + ":" + "-".join(_tokens(text)[:4])


def _item(kind, text, key=None, value=None, explicit=False):
    return {"kind": kind, "text": text, "key": key, "value": value, "explicit": explicit}


def _contact_item(m, explicit):
    name, digits = " ".join(m.group("n").lower().split()), re.sub(r"\D", "", m.group("num"))
    if not name or len(name.split()) > 3 or (set(name.split()) & _BAD_CONTACT) or not 8 <= len(digits) <= 15:
        return []
    number = ("+" if m.group("num").strip().startswith("+") else "") + digits
    return [{"kind": "contact", "contact": (name, number), "text": f"{name} {number}", "key": None, "explicit": explicit}]


def _extract_clause(c, explicit):
    if not c:
        return []
    m = _P_CONTACT2.fullmatch(c) or _P_CONTACT3.fullmatch(c)
    if m:
        return _contact_item(m, True)
    m = _P_CONTACT1.fullmatch(c)
    if m:
        got = _contact_item(m, explicit)
        if got:
            return got
    for rx in (_P_FOLDER1, _P_FOLDER2, _P_FOLDER3):
        m = rx.fullmatch(c)
        if m:
            a, p = " ".join(m.group("a").lower().split()), m.group("p").strip(" \"'")
            if a.split()[0] in {"own", "new", "old", "local", "the", "a", "my", "this", "that"} or len(a.split()) > 3:
                continue
            return [{"kind": "folder", "folder": (a, p), "text": f"My {a} folder is {p}", "key": f"folder:{a}",
                     "value": None, "explicit": explicit}]
    m = _P_NAME.fullmatch(c)
    if m and m.group("n").split()[0].lower() not in _NOT_A_NAME:
        n = _nice(m.group("n"))
        return [_item("fact", f"My name is {n}", "name", n, explicit)]
    m = _P_ADDRESS.fullmatch(c)
    if m:
        n = m.group("n").strip()
        if n.split()[0].lower() not in _NOT_A_NAME and len(n.split()) <= 3:
            n = n if n[:1].isupper() else n.lower()
            return [_item("fact", f"I like to be called {n}", "address", n, explicit)]
    for rx in (_P_REL_A, _P_REL_B):
        m = rx.fullmatch(c)
        if m:
            n, rel = m.group("n").strip(), m.group("rel").lower()
            ok = n.split()[0].lower() not in _NOT_A_NAME and len(n) >= 2
            if ok and (explicit or all(w[:1].isupper() for w in n.split())):
                n = _nice(n)
                return [_item("person", f"My {rel} is {n}", f"person:{_REL_CANON[rel]}", n, explicit)]
    m = _P_BIRTHDAY.fullmatch(c)
    if m and re.search(r"\d|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec", m.group("d"), _RX):
        who = (m.group("who") or "").strip().lower()
        d = m.group("d").strip()
        return [_item("fact", f"My {who + chr(39) + 's ' if who else ''}birthday is {d}", f"birthday:{who or 'me'}", d, explicit)]
    m = _P_FAV.fullmatch(c)
    if m:
        cat, v = m.group("c").lower(), m.group("v").strip()
        return [_item("preference", f"My favourite {cat} is {v}", f"fav:{cat}", v, explicit)]
    for rx, key, fmt in ((_P_LIVE, "city", "I live in {}"), (_P_FROM, "origin", "I am from {}"),
                         (_P_STUDY, "study", "I study at {}")):
        m = rx.fullmatch(c)
        if m:
            p = m.group("p").strip()
            if p.split()[0].lower() in {"the", "a", "an", "my", "our", "this", "that", "such", "fear", "hope", "doubt",
                                         "peace", "denial", "harmony", "another", "one"}:
                continue
            return [_item("fact", fmt.format(_nice(p)), key, _nice(p), explicit)]
    m = _P_WORK.fullmatch(c)
    if m:
        p = m.group("p").strip()
        if p.split()[0].lower() not in {"home", "night", "nights", "the", "a", "an", "my", "present", "once", "least",
                                         "all", "times", "most", "weekends", "least"}:
            return [_item("fact", f"I work {m.group('w').lower()} {_nice(p)}", "work", _nice(p), explicit)]
    m = _P_TRAIT.fullmatch(c)
    if m:
        d = m.group("d").lower()
        return [_item("fact", f"I am {d}", "trait:" + re.sub(r"^(?:a|an)\s+", "", d), None, explicit)]
    m = _P_ALLERGY.fullmatch(c)
    if m:
        return [_item("fact", f"I am allergic to {m.group('o').strip()}", _key_of("allergy", m.group("o")), None, explicit)]
    m = _P_EVERY.fullmatch(c)
    if m and m.group("a").split()[0].lower() not in _NOT_ROUTINE:
        return [_item("routine", f"Every {m.group('w').lower()} I {m.group('a').strip()}", _key_of("routine", m.group("a")),
                      None, explicit)]
    m = _P_CLOCK.fullmatch(c)
    if m:
        a = m.group("a").strip()
        return [_item("routine", f"I {a}", "routine:" + "-".join(a.lower().split()[:2]), None, explicit)]
    m = _P_USUALLY.fullmatch(c)
    if m and m.group("a").split()[0].lower() not in _NOT_ROUTINE and len(m.group("a").split()) <= 14:
        return [_item("routine", f"I {m.group('adv').lower()} {m.group('a').strip()}", _key_of("routine", m.group("a")),
                      None, explicit)]
    m = _P_PREF.fullmatch(c)
    if m:
        o = m.group("o").strip()
        if (len(o) >= 2 and len(o.split()) <= 8 and not _BAD_OBJ_START.match(o)
                and not re.search(r"\b(?:you|pac)\b|\?", o, _RX)):
            v = " ".join(m.group("v").lower().split())
            v = re.sub(r"^(?:do not|dont)\b", "don't", v).replace("cannot stand", "can't stand").replace("cant stand", "can't stand")
            return [_item("preference", f"I {v} {o}", _key_of("pref", o), None, explicit)]
    return []


def extract_memories(raw, explicit=False):
    """Statements about the speaker in a sentence -> [{'kind','text','key','value','explicit'} ...]. Questions and
    anything that isn't clearly a lasting fact about the person give []. Contacts come back as kind 'contact'
    with 'contact': (name, number)."""
    s = " ".join((raw or "").replace("\u2019", "'").split())
    s = re.sub(r"^(?:(?:actually|well|okay|ok|so|also|and|btw|fyi|sorry|correction|by the way|just so you know|"
               r"for the record)\b[,:]?\s+|no[,:]\s+)+", "", s, flags=_RX)
    if (not s or len(s) > 240 or s.rstrip().endswith("?")
            or re.match(r"^(?:what|who|when|where|why|how|which|do|does|did|is|are|am|can|could|would|should|will)\b", s, _RX)):
        return []
    s = s.rstrip(" .!,;:")
    out = []
    for n, c in enumerate(re.split(r"\s*(?:[;,]|\band\b|\bbut\b|\balso\b)\s+(?=(?:i|i'm|i've|my|every|each)\b)", s, flags=_RX)[:3]):
        got = _extract_clause(c.strip(" ,;."), explicit)
        if n == 0 and not got:
            return []                       # the sentence must START with the statement: "play jazz, I love it" is a command
        out.extend(got)
    return out


def infer_kind(text):
    if re.search(r"\b(?:usually|always|every|each|daily|normally|tend to|often|regularly)\b", text, _RX):
        return "routine"
    if re.search(r"\b(?:like|love|prefer|hate|dislike|enjoy|favou?rite|allergic)\b", text, _RX):
        return "preference"
    if re.match(rf"^my (?:{_REL_RE})\b", text, _RX):
        return "person"
    return "fact"


_YOU = [(re.compile(p, re.I), r) for p, r in (
    (r"\bI'm\b", "you're"), (r"\bI am\b", "you are"), (r"\bI was\b", "you were"), (r"\bI've\b", "you've"),
    (r"\bI'll\b", "you'll"), (r"\bI'd\b", "you'd"), (r"\bI\b", "you"), (r"\bmy\b", "your"), (r"\bmine\b", "yours"),
    (r"\bmyself\b", "yourself"), (r"\bme\b", "you"))]


def you_form(text):
    """'I like tea. My wife is Priya.' -> 'You like tea. Your wife is Priya.' - for reading a memory back to you."""
    out = text
    for rx, rep in _YOU:
        def sub(m, rep=rep):
            at_start = m.start() == 0 or out[max(0, m.start() - 2):m.start()] in (". ", "! ", "? ")
            return rep[:1].upper() + rep[1:] if m.group(0)[:1].isupper() and at_start else rep
        out = rx.sub(sub, out)
    return out[:1].upper() + out[1:]


def lower_first(s):
    return s[:1].lower() + s[1:] if s and not re.match(r"[A-Z]{2}", s) else s


def day_part(hour):
    return "night" if hour < 5 else "morning" if hour < 12 else "afternoon" if hour < 17 else "evening" if hour < 21 else "night"


class Memory:
    """The store: ~/.pac/memory.json. Thread-safe. Every item is {id, kind, text, key, value, source, created,
    updated, last_used, uses, strength}. `key` names a subject (a name, a city, one preference) so a newer statement
    on the same subject replaces the older one; `source` is said / auto / brain / observed / edited."""

    def __init__(self, path=None):
        self.path = Path(path or MEMORY_FILE)
        self.lock = threading.RLock()
        self.items, self.habits = [], {}
        self._pruned_on = ""
        self._load()
        self.prune()

    # ----- storage
    def _load(self):
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self.items = [i for i in data.get("items", []) if isinstance(i, dict) and i.get("text") and i.get("kind")]
            self.habits = data.get("habits", {}) if isinstance(data.get("habits"), dict) else {}
        except FileNotFoundError:
            pass
        except Exception:
            logger.exception("memory file unreadable - keeping a copy and starting fresh")
            try:
                self.path.replace(self.path.with_suffix(".bad"))
            except OSError:
                pass

    def _save(self):
        tmp = self.path.with_suffix(".part")
        try:
            tmp.write_text(json.dumps({"version": 1, "items": self.items, "habits": self.habits}, indent=1,
                                      ensure_ascii=False), encoding="utf-8")
            try:
                os.chmod(tmp, 0o600)
            except OSError:
                pass
            tmp.replace(self.path)
        except OSError:
            logger.exception("could not save memory")

    def count(self):
        with self.lock:
            return len(self.items)

    # ----- writing
    def _make(self, kind, text, key, value, source):
        now = time.time()
        return {"id": secrets.token_hex(3), "kind": kind if kind in MEMORY_KINDS else "fact", "text": text, "key": key,
                "value": value, "source": source, "created": now, "updated": now, "last_used": 0, "uses": 0, "strength": 1}

    def add(self, text, kind="fact", key=None, source="said", value=None):
        """File a statement. -> (item, 'new' | 'updated' | 'known'), or (None, 'bad')."""
        text = _tidy(text)
        if not text or len(text) > 300 or looks_secret(text):
            return None, "bad"
        with self.lock:
            now = time.time()
            if key:
                for it in self.items:
                    if it.get("key") == key:
                        same = it["text"] == text
                        it.update(text=text, value=value, updated=now)
                        it["kind"] = kind if kind in MEMORY_KINDS else it["kind"]
                        it["strength"] = it.get("strength", 1) + (1 if same else 0)
                        if source in ("said", "brain", "auto"):
                            it["source"] = source
                        self._save()
                        return it, ("known" if same else "updated")
            toks = set(_tokens(text))
            for it in self.items:
                other = set(_tokens(it["text"]))
                if toks and other and len(toks & other) / len(toks | other) >= 0.8:
                    it["strength"] = it.get("strength", 1) + 1
                    it["updated"] = now
                    self._save()
                    return it, "known"
            item = self._make(kind, text, key, value, source)
            self.items.append(item)
            self._trim()
            self._save()
            return item, "new"

    def _trim(self):
        while len(self.items) > MEMORY_MAX_ITEMS:
            rank = {"observed": 0, "auto": 1, "brain": 1, "edited": 2, "said": 3}
            victim = min(self.items, key=lambda i: (rank.get(i.get("source"), 1), i.get("uses", 0), i.get("strength", 1),
                                                    i.get("updated", 0)))
            self.items.remove(victim)

    def remove(self, ids):
        """Forget items by id. -> the items removed. A forgotten habit stays forgotten."""
        ids = set(ids)
        with self.lock:
            gone = [i for i in self.items if i["id"] in ids]
            for it in gone:
                self.items.remove(it)
                k = it.get("key") or ""
                if k.startswith("habit:") and k[6:] in self.habits:
                    self.habits[k[6:]]["muted"] = True
            if gone:
                self._save()
            return gone

    def clear(self):
        with self.lock:
            n = len(self.items)
            self.items, self.habits = [], {}
            self._save()
            return n

    def touch(self, items):
        with self.lock:
            now = time.time()
            for it in items:
                it["uses"] = it.get("uses", 0) + 1
                it["last_used"] = now
            self._save()

    # ----- reading
    def search(self, query, k=6):
        """[(rank, coverage, item)] best first. coverage = how much of the question the item covers (0..1)."""
        qt = []
        for w in _tokens(query):
            if w not in qt:
                qt.append(w)
        with self.lock:
            docs = [(it, set(_tokens(it["text"])) | (set(_tokens("name")) if it["kind"] == "person" else set())) for it in self.items]
        if not qt or not docs:
            return []
        df = collections.Counter(w for _, ts in docs for w in ts)
        vocab = list(df)
        qt = [(difflib.get_close_matches(w, vocab, n=1, cutoff=0.82) or [w])[0] if w not in df and len(w) >= 5 else w
              for w in qt]
        n = len(docs)
        max_idf = math.log(1 + n)
        weight = lambda w: math.log(1 + n / df[w]) if w in df else max_idf
        total = sum(weight(w) for w in qt) or 1.0
        now, scored = time.time(), []
        for it, ts in docs:
            hit = sum(weight(w) for w in qt if w in ts)
            if hit <= 0:
                continue
            age = (now - it.get("updated", now)) / 86400
            boost = (0.12 * min(math.log1p(it.get("uses", 0)), 3) + 0.08 * min(it.get("strength", 1) - 1, 3)
                     + (0.15 if age < 14 else 0.07 if age < 90 else 0))
            scored.append((hit + boost, hit / total, it))
        scored.sort(key=lambda r: -r[0])
        return scored[:k]

    def recall(self, query, k=6):
        """The memories worth showing an AI for this request: what matches it, who you are, and - if that is
        thin - your most-used preferences and routines."""
        found = [it for _, _, it in self.search(query, k)]
        with self.lock:
            have = {it["id"] for it in found}
            core = [it for it in self.items if it.get("key") in ("name", "address") and it["id"] not in have]
            out = core + found
            if len(out) < 3:
                have |= {it["id"] for it in core}
                extra = sorted((it for it in self.items if it["id"] not in have and it["kind"] in ("preference", "routine")),
                               key=lambda it: (-it.get("uses", 0), -it.get("strength", 1), -it.get("updated", 0)))
                out += extra[:3 - len(out)]
        return out

    @staticmethod
    def format_block(items, limit=1000):
        lines, size = [], 0
        for it in items:
            line = "- " + it["text"]
            if size + len(line) > limit:
                break
            lines.append(line)
            size += len(line)
        if not lines:
            return ""
        return ("What the user has told you about themselves, or what you have noticed (first person means the user). "
                "Use it quietly when it genuinely helps; never recite it unprompted, never invent memories, and if one "
                "seems out of date, trust what the user says now:\n" + "\n".join(lines))

    def address(self):
        with self.lock:
            for it in self.items:
                if it.get("key") == "address" and it.get("value"):
                    return str(it["value"])
        return ""

    def folder_aliases(self):
        """{'taxes': 'C:/Users/me/Documents/Taxes'}: folders you have nicknamed ('my taxes folder is documents/taxes')."""
        with self.lock:
            return {i["key"][7:]: str(i["value"]) for i in self.items
                    if (i.get("key") or "").startswith("folder:") and i.get("value")}

    def alias_map(self):
        """{'wife': 'priya', 'mother': 'meera' ...}: who the people in your life are, for 'message my wife'."""
        out = {}
        with self.lock:
            for it in self.items:
                k = it.get("key") or ""
                if k.startswith("person:") and it.get("value"):
                    for syn in _REL_GROUPS.get(k[7:], (k[7:],)):
                        out[syn] = str(it["value"]).lower()
        return out

    def grouped(self, kinds=None):
        with self.lock:
            out = {}
            for it in sorted(self.items, key=lambda i: (-i.get("uses", 0), -i.get("updated", 0))):
                if not kinds or it["kind"] in kinds:
                    out.setdefault(it["kind"], []).append(it)
            return out

    # ----- editing as text (Menu > Memory > View and edit)
    def export_lines(self):
        with self.lock:
            order = {k: n for n, k in enumerate(MEMORY_KINDS)}
            return [f"[{it['kind']}] {it['text']}" for it in
                    sorted(self.items, key=lambda i: (order.get(i["kind"], 9), i.get("created", 0)))]

    def replace_all(self, text):
        """The edited list replaces everything. Unchanged lines keep their history. -> (removed, added)."""
        with self.lock:
            old = {it["text"]: it for it in self.items}
            new, seen = [], set()
            for line in (text or "").splitlines():
                line = line.strip()
                if not line:
                    continue
                m = re.match(r"^\[(preference|routine|person|fact)\]\s*(.*)$", line, _RX)
                kind, body = (m.group(1).lower(), m.group(2)) if m else ("fact", line)
                body = _tidy(body)
                if not body or body in seen or looks_secret(body):
                    continue
                seen.add(body)
                new.append(old.get(body) or self._make(kind, body, None, None, "edited"))
            kept = {id(i) for i in new}
            removed = [i for i in self.items if id(i) not in kept]
            for it in removed:
                k = it.get("key") or ""
                if k.startswith("habit:") and k[6:] in self.habits:
                    self.habits[k[6:]]["muted"] = True
            added = sum(1 for i in new if i not in self.items)
            self.items = new
            self._save()
            return len(removed), added

    # ----- habits: the same command at the same time of day on several days becomes a routine
    def observe(self, phrase, now=None):
        """Note that `phrase` was just carried out. -> the new routine item when this is the third day running
        (within two weeks) that it happens in this part of the day, else None."""
        phrase = " ".join(re.findall(r"[a-z0-9']+", (phrase or "").lower()))
        if not phrase or len(phrase.split()) > 8:
            return None
        now = now or datetime.datetime.now()
        part, day = day_part(now.hour), now.date().isoformat()
        hk = f"{part}|{phrase}"
        with self.lock:
            h = self.habits.setdefault(hk, {"days": []})
            if h.get("muted") or day in h["days"]:
                return None
            h["days"] = (h["days"] + [day])[-30:]
            h["last"] = day
            recent = [d for d in h["days"] if (now.date() - datetime.date.fromisoformat(d)).days <= 14]
            made = None
            if len(recent) >= 3:
                text = f'In the {part} I often say "{phrase}"'
                existed = any(i.get("key") == "habit:" + hk for i in self.items)
                item, _ = self.add(text, "routine", "habit:" + hk, "observed")
                if item:
                    item["strength"] = len(recent)
                    made = None if existed else item
            self._save()
            return made

    def prune(self):
        """Once a day: forget habits that have stopped (nothing for 30 days). Things you said yourself stay."""
        today = datetime.date.today()
        if self._pruned_on == today.isoformat():
            return
        self._pruned_on = today.isoformat()
        cutoff = time.time() - 30 * 86400
        with self.lock:
            stale = [i for i in self.items if i.get("source") == "observed" and i.get("updated", 0) < cutoff]
            for it in stale:
                self.items.remove(it)
            for hk in list(self.habits):
                try:
                    last = datetime.date.fromisoformat(self.habits[hk].get("last", ""))
                except ValueError:
                    last = today - datetime.timedelta(days=99)
                if (today - last).days > 30:
                    del self.habits[hk]
            if stale:
                self._save()


# --------------------------------------------------------------- e-mail (Gmail API over HTTPS)
def _dh(value):
    try:
        return str(make_header(decode_header(str(value or "")))).strip()
    except Exception:
        return str(value or "").strip()


_IDX_WORDS = {**{w: n for w, n in NUM_UNITS.items() if 1 <= n <= 19}, "twenty": 20,
              "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6,
              "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10}


def parse_indices(text):
    """'2' / 'two' / 'the second' / '1 3 and 5' / '2 to 4'  ->  [2] / [1, 3, 5] / [2, 3, 4]"""
    toks = re.findall(r"[a-z]+|\d+", text.lower())
    if len(toks) == 1 and toks[0] in ("to", "too", "for", "won"):   # what speech recognition hears for 2, 2, 4, 1
        return [{"to": 2, "too": 2, "for": 4, "won": 1}[toks[0]]]
    nums = []
    for i, w in enumerate(toks):
        val = int(w) if w.isdigit() else _IDX_WORDS.get(w)
        if val is not None:
            nums.append(val)
        elif w in ("to", "through", "thru", "till", "until") and nums and i + 1 < len(toks) \
                and (toks[i + 1].isdigit() or toks[i + 1] in _IDX_WORDS):
            nums.append("-")
    out, i = [], 0
    while i < len(nums):
        if nums[i] != "-" and i + 2 < len(nums) and nums[i + 1] == "-":
            a, b = nums[i], nums[i + 2]
            out.extend(range(min(a, b), max(a, b) + 1))
            i += 3
        else:
            if nums[i] != "-":
                out.append(nums[i])
            i += 1
    return sorted(set(out))


class MailAuthError(RuntimeError):
    """Google sign-in problem (expired, revoked, cancelled...)."""

    def __init__(self, msg, code=None):
        super().__init__(msg)
        self.code = code


GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
MAIL_SCOPE = "https://www.googleapis.com/auth/gmail.modify"   # read + move to Trash; cannot delete for good
GMAIL_API = "https://gmail.googleapis.com/gmail/v1/users/me"


def _post_form(url, data):
    import urllib.error
    import urllib.request
    req = urllib.request.Request(url, urlencode(data).encode(),
                                 {"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode())
        except Exception:
            err = {}
        raise MailAuthError(err.get("error_description") or err.get("error") or f"HTTP {e.code}", err.get("error"))
    except urllib.error.URLError as e:
        raise ConnectionError(f"could not reach Google's sign-in server ({e.reason})")


def _http(method, url, token, params=None, body=None):
    """One call to the Gmail API (port 443, like any website). Returns the parsed JSON."""
    import urllib.error
    import urllib.request
    if params:
        url += "?" + urlencode(params, doseq=True)
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": "Bearer " + token}
    if data is not None:
        headers["Content-Type"] = "application/json"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data, headers, method=method), timeout=25) as r:
            raw = r.read()
            return json.loads(raw.decode()) if raw else {}
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode()).get("error", {})
        except Exception:
            err = {}
        if not isinstance(err, dict):
            err = {"message": str(err)}
        msg = err.get("message") or f"HTTP {e.code}"
        reason = ((err.get("errors") or [{}])[0]).get("reason", "")
        blob = f"{msg} {reason}".lower()
        if e.code == 403 and ("not been used" in blob or "disabled" in blob or "accessnotconfigured" in blob):
            raise MailAuthError(msg, "api_disabled")
        if "insufficient" in blob:
            raise MailAuthError(msg, "insufficient_scope")
        if e.code == 401:
            raise MailAuthError(msg, "invalid_grant")
        raise MailAuthError(msg, reason or str(e.code))
    except urllib.error.URLError as e:
        raise ConnectionError(f"could not reach Gmail ({e.reason})")


def _secret_get(cfg, name):
    try:
        import keyring
        v = keyring.get_password("pac-mail", f"{cfg.get('mail_address', '')}:{name}")
        if v:
            return v
    except Exception:
        pass
    return cfg.get(name, "")


def _secret_set(cfg, name, value):
    """Keep a token in the system credential store if 'keyring' is installed, else in config.json."""
    try:
        import keyring
        keyring.set_password("pac-mail", f"{cfg.get('mail_address', '')}:{name}", value)
        cfg[name] = ""
        return "in your system credential store"
    except Exception:
        cfg[name] = value
        return "in ~/.pac/config.json (pip install keyring to use the credential store instead)"


def google_sign_in(cfg, timeout=180):
    """Open Google's own sign-in page in the browser and return a refresh token.
    PAC never sees your Google password: Google hands back a one-time code on a local address."""
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    got = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(urlparse(self.path).query)
            body = b""
            if "code" in q or "error" in q:
                got.update({k: v[0] for k, v in q.items()})
                body = ("PAC is connected. You can close this tab." if "code" in q
                        else "Sign-in was cancelled. You can close this tab.").encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), Handler)
    srv.timeout = 3
    redirect = f"http://127.0.0.1:{srv.server_port}"
    webbrowser.open(GOOGLE_AUTH_URL + "?" + urlencode({
        "client_id": cfg["mail_client_id"], "redirect_uri": redirect, "response_type": "code",
        "scope": MAIL_SCOPE, "access_type": "offline", "prompt": "consent", "state": state,
        "code_challenge": challenge, "code_challenge_method": "S256",
        "login_hint": cfg.get("mail_address", "")}))
    end = time.time() + timeout
    try:
        while not got and time.time() < end:
            srv.handle_request()
    finally:
        srv.server_close()
    if not got:
        raise MailAuthError("Sign-in timed out. Try again.")
    if "code" not in got or got.get("state") != state:
        raise MailAuthError("Sign-in was cancelled.")
    tok = _post_form(GOOGLE_TOKEN_URL, {
        "client_id": cfg["mail_client_id"], "client_secret": cfg["mail_client_secret"], "code": got["code"],
        "code_verifier": verifier, "redirect_uri": redirect, "grant_type": "authorization_code"})
    if not tok.get("refresh_token"):
        raise MailAuthError("Google didn't give PAC a long-lived sign-in. Remove PAC at "
                            "myaccount.google.com/permissions, then sign in again.")
    return tok["refresh_token"]


class MailBox:
    """Gmail through Google's web API, signed in with OAuth. Lists the latest mails and moves chosen ones
    to Trash. The permission PAC asks for cannot delete anything permanently."""

    def __init__(self, cfg):
        self.cfg = cfg
        self._tok = None                     # (access token, expiry time)

    def reset(self):
        self._tok = None

    def configured(self):
        return bool(self.cfg.get("mail_address") and self.cfg.get("mail_client_id")
                    and self.cfg.get("mail_client_secret") and _secret_get(self.cfg, "mail_refresh_token"))

    def _access_token(self):
        if self._tok and time.time() < self._tok[1] - 60:
            return self._tok[0]
        d = _post_form(GOOGLE_TOKEN_URL, {
            "client_id": self.cfg["mail_client_id"], "client_secret": self.cfg["mail_client_secret"],
            "refresh_token": _secret_get(self.cfg, "mail_refresh_token"), "grant_type": "refresh_token"})
        self._tok = (d["access_token"], time.time() + int(d.get("expires_in", 3600)))
        return self._tok[0]

    def _api(self, method, path, params=None, body=None):
        return _http(method, GMAIL_API + path, self._access_token(), params, body)

    def test(self):
        self._api("GET", "/profile")

    def recent(self, unread_only=True, limit=10):
        """(total matching, [newest first: {uid, name, addr, subject}]). Reading never marks mails as read."""
        label = self._api("GET", "/labels/INBOX")
        total = label.get("messagesUnread" if unread_only else "messagesTotal", 0)
        found = self._api("GET", "/messages", {"labelIds": ["INBOX", "UNREAD"] if unread_only else ["INBOX"],
                                               "maxResults": limit}).get("messages", [])
        items = []
        for m in found:
            d = self._api("GET", f"/messages/{m['id']}",
                          {"format": "metadata", "metadataHeaders": ["From", "Subject"]})
            hdr = {h.get("name", "").lower(): h.get("value", "") for h in d.get("payload", {}).get("headers", [])}
            name, addr = parseaddr(hdr.get("from", ""))
            items.append({"uid": m["id"], "name": _dh(name) or addr or "unknown sender", "addr": addr,
                          "subject": _dh(hdr.get("subject")) or "no subject"})
        return total, items

    def trash(self, ids):
        """Move mails to Trash one by one (they stay restorable). If one fails, e.done lists the ones that worked."""
        done = []
        try:
            for i in ids:
                self._api("POST", f"/messages/{i}/trash", body={})
                done.append(i)
        except Exception as e:
            e.done = done
            raise
        return done


# --------------------------------------------------------------- misc helpers
def find_top_youtube_result(query):
    """Fetch YouTube's search page and return (video_id, title) for the first
    real video result, or (None, None) if it can't be determined. Needs internet."""
    import urllib.request
    try:
        url = "https://www.youtube.com/results?search_query=" + quote_plus(query)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=6).read().decode("utf-8", errors="ignore")
        m = re.search(r'"videoId":"([\w-]{11})"[^}]*?"title":\{"runs":\[\{"text":"([^"]+)"', html)
        if not m:
            m = re.search(r'"videoId":"([\w-]{11})"', html)
            return (m.group(1), None) if m else (None, None)
        return m.group(1), m.group(2)
    except Exception:
        logger.exception("youtube lookup failed")
        return None, None


def parse_vcf(path):
    """Read a .vcf contacts file (the standard export format from every phone's
    Contacts app) and return {name: phone_number}. WhatsApp has no API that lets
    a desktop script read its contact list directly, but WhatsApp's contacts ARE
    your phone's contacts, so exporting from the phone gets the same list."""
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    out = {}
    for card in re.split(r"(?=BEGIN:VCARD)", text):
        name_m = re.search(r"^FN(?:;[^:]*)?:(.+)$", card, re.M)
        tel_m = re.search(r"^TEL(?:;[^:]*)?:(.+)$", card, re.M)
        if name_m and tel_m:
            name = name_m.group(1).strip()
            digits = re.sub(r"\D", "", tel_m.group(1))
            if name and len(digits) >= 8:
                out[name.lower()] = digits
    return out


def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("_", " ")).strip()


def sh(cmd):
    subprocess.Popen(cmd, shell=True, creationflags=NO_WINDOW)


def open_path(path):
    if OS == "Windows":
        os.startfile(str(path))  # type: ignore[attr-defined]
    elif OS == "Darwin":
        subprocess.Popen(["open", str(path)])
    else:
        subprocess.Popen(["xdg-open", str(path)])


def find_file(query):
    """Fuzzy-search common folders (3 levels deep) for a spoken file name."""
    query = norm(query)
    best, best_score = None, 0.0
    for base in SEARCH_DIRS:
        if not base.exists():
            continue
        depth0 = len(base.parts)
        for root, dirs, files in os.walk(base):
            if len(Path(root).parts) - depth0 >= 3:
                dirs[:] = []
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for f in files:
                stem = norm(Path(f).stem)
                score = difflib.SequenceMatcher(None, query, stem).ratio()
                if query and query in stem:
                    score = max(score, 0.9)
                if score > best_score:
                    best, best_score = Path(root) / f, score
    return best if best_score >= 0.6 else None


def run_power(action):
    cmds = {
        "Windows": {"shutdown": "shutdown /s /t 5", "restart": "shutdown /r /t 5",
                    "lock": "rundll32.exe user32.dll,LockWorkStation",
                    "sleep": "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"},
        "Darwin": {"shutdown": "osascript -e 'tell app \"System Events\" to shut down'",
                   "restart": "osascript -e 'tell app \"System Events\" to restart'",
                   "lock": "pmset displaysleepnow", "sleep": "pmset sleepnow"},
        "Linux": {"shutdown": "systemctl poweroff", "restart": "systemctl reboot",
                  "lock": "loginctl lock-session", "sleep": "systemctl suspend"},
    }
    sh(cmds[OS][action])


def polish(text):
    """Tidy a spoken sentence for sending: capital letters, 'I', full stop."""
    text = text.strip()
    if not text:
        return text
    text = re.sub(r"\bi\b", "I", text)
    text = text[0].upper() + text[1:]
    return text


def protocol_registered(name):
    if OS != "Windows":
        return True
    try:
        import winreg
        winreg.CloseKey(winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, name))
        return True
    except Exception:
        return False


# --------------------------------------------------------------- speech clean-up
# Fix common mis-hearings, then strip polite filler and an optional "PAC".
FIXES = [
    (r"\bwhat'?s ?app\b|\bwhat'?s up\b|\bwatts ?app\b|\bwhats ?up\b|\bwhat sap\b", "whatsapp"),
    (r"\b(?:opened|opens|opening)\b", "open"),
    (r"\bgoogle chrome\b", "chrome"),
    (r"\bnote ?pad\b", "notepad"),
    (r"\bshut ?down\b", "shutdown"),
    (r"\byou tube\b", "youtube"),
]
FILLER_START = r"^(?:hey|ok|okay|please|can you|could you|would you|will you|kindly|pac|pack|pak)\s+"
WAKE_ONLY = {"pac", "pack", "pak"}
DICT_STOP = re.compile(r"\b(?:stop|end|finish)(?: the)? (?:typing|dictation)\b")
CANON = [
    "what time is it", "what is the date", "what is my schedule", "schedule tomorrow", "next class",
    "what class do i have now", "check my mail", "review my mail", "read my notes", "open notes",
    "open my facts", "battery", "volume up", "volume down", "mute volume", "take a screenshot", "tell me a joke",
    "stop listening", "wake up", "help", "list contacts", "list messages", "lock", "show desktop",
    "flip a coin", "roll a dice", "text mode", "voice mode", "open youtube", "open chrome", "open whatsapp",
    "open calculator", "open notepad", "world news", "stop talking", "edit timetable", "speak faster", "speak slower", "change voice",
]
COMMAND_VERBS = {"open", "launch", "start", "type", "write", "search", "google", "send", "message",
                 "text", "whatsapp", "shutdown", "restart", "set", "take", "note", "play", "call",
                 "find", "show", "close", "go", "remind", "move", "create"}

WEB_ALIASES = {
    "google": "https://www.google.com", "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com", "maps": "https://maps.google.com",
    "google maps": "https://maps.google.com", "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com", "twitter": "https://twitter.com",
    "linkedin": "https://www.linkedin.com", "github": "https://github.com",
    "netflix": "https://www.netflix.com", "amazon": "https://www.amazon.in",
}
WEB_FALLBACK = {"whatsapp": "https://web.whatsapp.com"}
WIN_ALIASES = {
    "chrome": "start chrome", "browser": "start msedge", "edge": "start msedge",
    "firefox": "start firefox", "notepad": "notepad", "notes": f'notepad "{NOTES_FILE}"',
    "sticky notes": "start ms-stickynotes:", "calculator": "calc", "paint": "mspaint",
    "word": "start winword", "excel": "start excel", "powerpoint": "start powerpnt",
    "settings": "start ms-settings:", "task manager": "taskmgr", "command prompt": "start cmd",
    "terminal": "start cmd", "file explorer": "explorer", "explorer": "explorer",
    "files": "explorer", "control panel": "control", "camera": "start microsoft.windows.camera:",
    "snipping tool": "snippingtool", "clock": "start ms-clock:", "calendar": "start outlookcal:",
    "mail": "start outlookmail:",
}
KEYS = {
    "enter": ("press", "enter"), "new line": ("press", "enter"), "backspace": ("press", "backspace"),
    "delete": ("press", "backspace"), "tab": ("press", "tab"), "escape": ("press", "esc"),
    "undo": ("hotkey", ("ctrl", "z")), "redo": ("hotkey", ("ctrl", "y")),
    "copy": ("hotkey", ("ctrl", "c")), "paste": ("hotkey", ("ctrl", "v")),
    "cut": ("hotkey", ("ctrl", "x")), "select all": ("hotkey", ("ctrl", "a")),
    "save": ("hotkey", ("ctrl", "s")),
}
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "There are ten kinds of people: those who understand binary and those who don't.",
    "Why did the laptop get cold? It left its Windows open.",
]
HELP_TEXT = (
    "You don't need to say my name. Just speak or type:\n"
    "  - open chrome / whatsapp / notes / calculator / any app\n"
    "  - open file resume  |  open folder downloads\n"
    "  - search for <anything>  |  who is ...  |  play <song> (YouTube)\n"
    "  - any question I can't answer from your facts is looked up quietly on the web (no prompt, no browser window)\n"
    "  - open in a new tab  (shows your last search on Google)  |  search for <anything> in a new tab\n"
    "  - send message 2 to mom  |  message mom saying I'll be late\n"
    "  - type hello world  |  start typing ... stop typing\n"
    "  - shut down / restart / lock (asks first)\n"
    "  - note buy milk  |  open notes (opens Notepad)  |  read my notes\n"
    "  - learn that the wifi password is blue42  |  what is the wifi password  (answered offline)\n"
    "  - open my facts (your knowledge file in Notepad)\n"
    "  - MEMORY: my name is Ankush  |  I prefer tea in the morning  |  every morning I go for a walk  |  my wife is Priya\n"
    "  - my mom's number is 9876543210  (saved to contacts, so 'message my wife saying hi' works)  |  call me boss\n"
    "  - my taxes folder is documents/taxes  (a nickname the file manager understands: 'move report pdf to taxes')\n"
    "  - what do you remember about me  |  forget about tea  |  forget that  |  forget everything  |  turn off memory\n"
    "  - check my mail  |  delete mail 2  |  delete mails from amazon  |  review my mail\n"
    "  - set timer for 5 minutes  |  remind me to call in 10 minutes\n"
    "  - what time is it  |  battery  |  volume up  |  screenshot  |  what is 12 times 7\n"
    "  - MATHS: solve x^2 + 5x + 6 = 0  |  x squared plus 2x plus 5 equals 0  |  solve x + y = 10 and x - y = 2\n"
    "  - calculate (3 + 4i)(2 - i)  |  modulus of 3 + 4i  |  sqrt(-16)  |  convert 1 + i to polar form\n"
    "  - log 1000  |  log base 2 of 64  |  ln 20  |  antilog 2.5  |  solve log x + log(x - 3) = 1  |  solve 2^x = 32\n"
    "  - factorise / expand / simplify ...  |  differentiate x^3 sin x  |  integrate x^2 from 0 to 3  |  lcm of 12 and 18\n"
    "  - what's my schedule  |  schedule tomorrow  |  next class  |  when is maths  |  edit timetable\n"
    "  - remind me to call mom at 5 pm  |  set alarm for 7 am  |  convert 5 km to miles  |  flip a coin\n"
    "  - clap twice to wake me up  |  whistle to open YouTube  (Menu > Sound triggers)\n"
    "  - turn on gestures  |  teach a gesture  |  list my gestures  (camera hand gestures, Menu > Gestures)\n"
    "  - delete gestures  |  delete the fist gesture  |  restore gestures\n"
    "  - start air drag  |  stop air drag  (palm moves the mouse; pinch thumb and index = press the button, let go = drop)\n"
    "  - tell me about file report pdf  |  read file notes txt  |  tell me about files a, b and c  |  tell me about all files in downloads\n"
    "  - list files in downloads  |  how many pdf files are in documents  |  read several files on my laptop  |  show me my files\n"
    "  - move report pdf to documents  |  move all pdf files from downloads to taxes  |  undo move\n"
    "  - create a folder called Projects on the desktop  |  create a file called todo in documents with text buy milk\n"
    "  - air drag: pinch thumb and index together to select and drag a file, let go to drop it (or point + double air-tap, fist to drag, open palm to drop)\n"
    "  - show phone files  |  hide shelf  (files beamed from your phone wait on a shelf you can air-drag from)\n"
    "  - enroll my face  |  enroll my face as Rahul  |  who is there  |  list faces  |  forget face Rahul\n"
    "  - turn on face recognition  |  turn on face security  |  make Rahul trusted  |  face rules  |  face rule mail owner\n"
    "  - when Rahul arrives what's my schedule today   (runs a command when that face shows up; Menu > Faces)\n"
    "  - AR: start AR  |  stop AR  |  learn this as my keys  (hold it in the box)  |  what do you see  |  list objects\n"
    "  - when you see my keys say don't forget your wallet  |  when you see a triangle open chrome  |  forget object keys\n"
    "  - clear AR action for keys  |  set up AR starter commands  (circle, triangle, square... get ready-made actions)\n"
    "  - claude mode on / off  |  ask Claude <question>  (online; stays offline unless you say so)\n"
    "  - wake up daddy is home  (Hello sir, today's schedule, then the top 20 headlines; also runs by itself 5:30-8:00 AM)  |  world news\n"
    "  - stop  |  stop it  |  mute   (PAC stops talking at once, even mid-sentence; Esc does the same)\n"
    "  - change voice  |  speak faster  |  stop listening  |  wake up  |  exit\n"
    "  - text mode  |  voice mode   (text mode works fully offline; voice mode needs internet)"
)


# --------------------------------------------------------------- female voice picker
UK_HINTS = ("en-gb", "en_gb", "en-uk", "british", "english_rp", "united kingdom", "great britain")
FEMALE_NAMES = ("hazel", "susan", "kate", "serena", "stephanie", "libby", "sonia", "fiona", "zira",
                "samantha", "victoria", "karen", "moira", "tessa", "amy", "emma", "heera", "veena",
                "allison", "ava", "aria", "jenny", "eva")
MALE_NAMES = ("david", "mark", "george", "richard", "james", "daniel", "alex", "fred", "ravi",
              "hemant", "guy", "ryan", "oliver", "thomas")


def rank_voices(voices):
    """Female English voices, best first (British before others)."""
    ranked = []
    for v in voices:
        langs = " ".join(l.decode(errors="ignore") if isinstance(l, bytes) else str(l)
                         for l in (getattr(v, "languages", None) or []))
        text = f"{v.name} {v.id} {langs}".lower()
        if not re.search(r"(^|[^a-z])en([-_/ ]|$)|english", text):
            continue
        score = 0
        if any(t in text for t in UK_HINTS):
            score += 2
        if any(n in text for n in FEMALE_NAMES):
            score += 3
        if "female" in text:
            score += 2
        if any(n in text for n in MALE_NAMES) or ("male" in text and "female" not in text):
            score -= 5
        vid = v.id
        if OS == "Linux" and "+" not in vid:
            vid += "+f3"
            score += 1
        if score > 0:
            ranked.append((score, vid, v.name))
    ranked.sort(key=lambda r: -r[0])
    return [(vid, name) for _, vid, name in ranked]


# --------------------------------------------------------------- Claude (optional, only when you ask)
CLAUDE_MODELS = [("claude-haiku-4-5-20251001", "Haiku 4.5 - fast, cheapest"),
                 ("claude-sonnet-5-5", "Sonnet 5.5 - smarter, a bit slower")]
CLAUDE_SYSTEM = (
    "You are PAC, a voice assistant running on the user's laptop. Your replies are read aloud, so answer in short, "
    "natural spoken sentences: no markdown, no bullet points, no headings, no emojis. Keep it to a few sentences "
    "unless the user clearly asks for more. You cannot open apps, files, mail or the web yourself - PAC's own "
    "commands do that - so don't claim to. If you are unsure, say so plainly. Do not add 'sir'; PAC does that.")


def claude_key_get(cfg):
    try:
        import keyring
        v = keyring.get_password("pac-claude", "api-key")
        if v:
            return v
    except Exception:
        pass
    return cfg.get("claude_api_key", "")


def claude_key_set(cfg, key):
    """Keep the key in the system credential store if 'keyring' is installed, else in ~/.pac/config.json."""
    try:
        import keyring
        keyring.set_password("pac-claude", "api-key", key)
        cfg["claude_api_key"] = ""
        return "in your system credential store"
    except Exception:
        cfg["claude_api_key"] = key
        return "in ~/.pac/config.json (pip install keyring to use the credential store instead)"


class ClaudeError(Exception):
    def __init__(self, message, kind="error"):
        super().__init__(message)
        self.kind = kind      # no_key / auth / rate / offline / error


def ask_claude(api_key, model, history, timeout=40, url="https://api.anthropic.com/v1/messages", system_extra=""):
    """One round trip to the Claude Messages API using only the standard library. `history` is a list of
    {"role": "user"|"assistant", "content": str} ending with the user's message. Returns the reply text."""
    import urllib.request
    import urllib.error
    if not api_key:
        raise ClaudeError("no API key set", "no_key")
    system = CLAUDE_SYSTEM + ("\n\n" + system_extra if system_extra else "")
    body = json.dumps({"model": model, "max_tokens": 400, "system": system, "messages": history}).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "content-type": "application/json", "x-api-key": api_key, "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = json.loads(e.read().decode("utf-8", "replace")).get("error", {}).get("message", "")
        except Exception:
            pass
        if e.code in (401, 403):
            raise ClaudeError(f"Claude didn't accept the API key ({detail or e.code})", "auth")
        if e.code == 429:
            raise ClaudeError("Claude is rate-limiting this key right now", "rate")
        raise ClaudeError(f"Claude returned an error ({e.code}) {detail}".strip(), "error")
    except (urllib.error.URLError, OSError) as e:
        raise ClaudeError(f"couldn't reach Claude ({getattr(e, 'reason', e)})", "offline")
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()
    if not text:
        raise ClaudeError("Claude sent back an empty reply", "error")
    return re.sub(r"[*_#`]+", "", text)


# --------------------------------------------------------------- LLM brain (optional): understands any phrasing
# Instead of matching your sentence against fixed patterns, a language model (Claude online, or a local Ollama
# model fully offline) picks one of PAC's tools. The tool is turned into an ordinary PAC command and run through
# the same handlers, confirmations ("shall I send it?") and face locks as before.
BRAIN_MODES = ("rules", "hybrid", "llm")      # rules = old pattern matching only; hybrid = patterns first, LLM for the rest; llm = LLM first
BRAIN_PROVIDERS = ("claude", "ollama")


def _tool(name, desc, props=None, required=None):
    return {"name": name, "description": desc,
            "parameters": {"type": "object", "properties": props or {}, "required": required or list((props or {}).keys())}}


_S = {"type": "string"}
BRAIN_TOOLS = [
    _tool("reply", "Answer in words: chat, questions, explanations, maths, advice. Use this when no laptop action is needed. "
                   "Short natural spoken sentences, no markdown.", {"text": _S}),
    _tool("open_app", "Open an installed application (chrome, notepad, calculator, whatsapp, spotify...).", {"name": _S}),
    _tool("open_website", "Open a website or web address in the browser.", {"site": _S}),
    _tool("web_search", "Look something up on the web (use for current events, prices, scores, anything you cannot know).",
          {"query": _S}),
    _tool("youtube", "Play or search something on YouTube.", {"query": _S}),
    _tool("timer", "Start a countdown timer.", {"amount": {"type": "number"}, "unit": {"type": "string", "enum": ["second", "minute", "hour"]}}),
    _tool("reminder", "Remind the user of something. 'when' is either a clock time like '5:30 pm' or a delay like '10 minutes'.",
          {"what": _S, "when": _S}),
    _tool("take_note", "Save a note to the user's notes file.", {"text": _S}),
    _tool("whatsapp", "Send a WhatsApp message to a saved contact (PAC asks the user to confirm before sending).",
          {"contact": _S, "message": _S}, ["contact"]),
    _tool("volume", "Change the laptop volume.", {"action": {"type": "string", "enum": ["up", "down", "mute"]}}),
    _tool("system", "Laptop controls and quick facts.",
          {"action": {"type": "string", "enum": ["lock", "shutdown", "restart", "sleep_laptop", "screenshot", "minimize",
                                                 "battery", "status", "time", "date", "news", "joke", "schedule", "next_class",
                                                 "check_mail", "read_notes", "stop_listening"]}}),
    _tool("type_text", "Type text into whatever window is focused.", {"text": _S}),
    _tool("files", "Work with files and folders on this laptop. You CAN do all of this, so never say you cannot access files: "
                   "describe or read files ('info', 'read'), look through several files on the laptop ('overview'), list a "
                   "folder ('list'), move files into a folder ('move'), create a file or folder, or undo the last move. "
                   "Names are plain file or folder names such as 'report.pdf', 'downloads', 'documents'. 'names' may hold "
                   "several names separated by commas.",
          {"action": {"type": "string", "enum": ["info", "read", "overview", "list", "move", "create_file", "create_folder", "undo_move"]},
           "names": _S, "folder": _S, "destination": _S, "file_type": _S, "content": _S}, ["action"]),
    _tool("remember", "Keep something lasting the user has just told you about themselves: a preference, a routine, a person in "
                      "their life, how to address them. Write it in the first person, e.g. 'I prefer tea in the morning'. "
                      "Never for passing remarks, tasks, or secrets such as passwords, PINs and card numbers.",
          {"text": _S, "kind": {"type": "string", "enum": ["preference", "routine", "person", "fact"]}}, ["text"]),
    _tool("forget", "Forget something about the user that they asked you to forget.", {"text": _S}),
    _tool("command", "Run any other PAC command by its exact phrase. Known phrases: 'list contacts', 'list messages', "
                     "'change voice', 'speak faster', 'speak slower', 'start gestures', 'stop gestures', 'who is there', "
                     "'what is my schedule tomorrow', 'open my facts', 'review my mail', 'flip a coin', 'roll a dice', "
                     "'help', 'text mode', 'voice mode', 'start file transfer', 'stop file transfer', 'grab file', 'drop file'.", {"phrase": _S}),
]

_SYSTEM_ACTIONS = {
    "lock": "lock", "shutdown": "shutdown", "restart": "restart", "sleep_laptop": "put the laptop to sleep",
    "screenshot": "take a screenshot", "minimize": "show desktop", "battery": "battery", "status": "system status",
    "time": "what time is it", "date": "what is the date", "news": "world news", "joke": "tell me a joke",
    "schedule": "what is my schedule", "next_class": "next class", "check_mail": "check my mail",
    "read_notes": "read my notes", "stop_listening": "go to sleep",
}


def brain_system_prompt(memory_block="", can_remember=False):
    now = datetime.datetime.now().strftime("%A %d %B %Y, %I:%M %p")
    return ("You are PAC, a voice assistant on the user's laptop. It is " + now + ". Every message is a spoken or typed "
            "request. If it asks for an action on the laptop, call the matching tool; never claim you did something "
            "without calling a tool. If it is a question or chat, call 'reply' with a short, natural answer that will be "
            "read aloud: no markdown, no lists, no emojis, no 'sir'. For facts that change or that you do not know, call "
            "'web_search'. When asked to write or compose something (a poem, email, essay, code, plan), call 'reply' with the "
            "complete text, as long as it needs to be. Call exactly one tool per request. Dangerous actions (shutdown, sending messages) are confirmed "
            "by PAC itself, so just call the tool. You CAN read, describe, list, move and create files and folders on this "
            "laptop with the 'files' tool: never say you cannot access files, call the tool instead."
            + (" When the user tells you something lasting about themselves, call 'remember'; when they ask you to forget "
               "something, call 'forget'." if can_remember else "")
            + ("\n\n" + memory_block if memory_block else ""))


def brain_tool_to_phrase(name, a):
    """Turn a tool call into the plain sentence PAC's own command handlers already understand. None = reply only."""
    a = a or {}
    g = lambda k: str(a.get(k, "") or "").strip()
    if name == "reply":
        return None
    if name == "open_app":
        return f"open {g('name')}" if g("name") else ""
    if name == "open_website":
        return f"go to {g('site')}" if g("site") else ""
    if name == "web_search":
        return f"search for {g('query')}" if g("query") else ""
    if name == "youtube":
        return f"play {g('query')} on youtube" if g("query") else ""
    if name == "timer":
        try:
            n = float(a.get("amount"))
        except (TypeError, ValueError):
            return ""
        unit = g("unit") if g("unit") in ("second", "minute", "hour") else "minute"
        n = int(n) if n == int(n) else n
        return f"set a timer for {n} {unit}{'s' if n != 1 else ''}"
    if name == "reminder":
        what, when = g("what"), g("when").lower()
        if not what or not when:
            return ""
        if re.match(r"^\d{1,2}(?::\d\d)?\s*(?:am|pm|a m|p m)?$", when) and (":" in when or re.search(r"[ap]", when)):
            return f"remind me to {what} at {when}"
        return f"remind me to {what} in {when if re.search(r'[a-z]', when) else when + ' minutes'}"
    if name == "take_note":
        return f"take a note {g('text')}" if g("text") else ""
    if name == "whatsapp":
        if not g("contact"):
            return ""
        return f"whatsapp {g('contact')} saying {g('message')}" if g("message") else f"whatsapp {g('contact')}"
    if name == "volume":
        return {"up": "volume up", "down": "volume down", "mute": "mute volume"}.get(g("action"), "")
    if name == "system":
        return _SYSTEM_ACTIONS.get(g("action"), "")
    if name == "files":
        act, names, folder, dest = g("action"), g("names"), g("folder"), g("destination")
        ftype, content = g("file_type").lower().lstrip("."), g("content")
        kind = f"{ftype} " if ftype else ""
        if act == "undo_move":
            return "undo move"
        if act == "overview":
            return f"read several {kind}files in {folder}" if folder else f"read several {kind}files on my laptop"
        if act == "list":
            return f"list {kind}files in {folder}" if folder else f"show me my {kind}files"
        if act in ("info", "read"):
            if names:
                if act == "read" and "," not in names:
                    return f"read file {names}"
                return f"tell me about file {names}" if "," not in names and " and " not in names else f"tell me about files {names}"
            return f"read {kind}files in {folder}" if folder else f"read several {kind}files on my laptop"
        if act == "move":
            if not dest:
                return ""
            if names:
                return f"move {names} from {folder} to {dest}" if folder else f"move {names} to {dest}"
            return f"move all {kind}files from {folder} to {dest}" if folder else ""
        if act == "create_folder":
            return f"create a folder called {names}" + (f" in {folder}" if folder else "") if names else ""
        if act == "create_file":
            if not names:
                return ""
            return (f"create a file called {names}" + (f" in {folder}" if folder else "")
                    + (f" with text {content}" if content else ""))
        return ""
    if name == "type_text":
        return f"type {g('text')}" if g("text") else ""
    if name in ("remember", "forget"):
        return ""                       # handled by the Assistant itself, never turned into a phrase
    if name == "command":
        return g("phrase")
    return ""


_KA = {"conn": None}
_KA_LOCK = threading.Lock()


def _post_keepalive(host, path, body, headers, timeout):
    """POST over a connection that stays open between calls (saves the ~0.3-0.6 s TLS set-up on every question).
    Returns (status, raw bytes). A connection the server closed meanwhile is replaced once, silently."""
    import http.client
    import socket
    data = json.dumps(body).encode()
    with _KA_LOCK:
        for attempt in (0, 1):
            conn = _KA["conn"]
            if conn is None:
                conn = _KA["conn"] = http.client.HTTPSConnection(host, timeout=timeout)
            try:
                conn.timeout = timeout
                if conn.sock is not None:
                    conn.sock.settimeout(timeout)
                conn.request("POST", path, body=data, headers=headers)
                resp = conn.getresponse()
                raw = resp.read()
                if (resp.getheader("Connection") or "").lower() == "close":
                    conn.close()
                    _KA["conn"] = None
                return resp.status, raw
            except socket.timeout:
                conn.close()
                _KA["conn"] = None
                raise
            except (http.client.HTTPException, OSError):
                conn.close()
                _KA["conn"] = None
                if attempt == 1:
                    raise


def warm_ai_connection():
    """Open the secure connection to the AI service ahead of time, so the first question doesn't pay for it."""
    import http.client
    with _KA_LOCK:
        if _KA["conn"] is None:
            try:
                c = http.client.HTTPSConnection("api.anthropic.com", timeout=8)
                c.connect()
                _KA["conn"] = c
            except Exception:
                _KA["conn"] = None


def _api_error(code, raw):
    detail = ""
    try:
        d = json.loads(raw.decode("utf-8", "replace"))
        detail = (d.get("error") or {}).get("message", "") if isinstance(d.get("error"), dict) else str(d.get("error", ""))
    except Exception:
        pass
    if code in (401, 403):
        raise ClaudeError(f"the AI service didn't accept the key ({detail or code})", "auth")
    if code == 429:
        raise ClaudeError("the AI service is rate-limiting right now", "rate")
    raise ClaudeError(f"the AI service returned an error ({code}) {detail}".strip(), "error")


def _post_json(url, body, headers, timeout):
    import urllib.request
    import urllib.error
    try:
        if url.startswith("https://api.anthropic.com/"):
            status, raw = _post_keepalive("api.anthropic.com", url[len("https://api.anthropic.com"):], body, headers, timeout)
            if status >= 400:
                _api_error(status, raw)
            return json.loads(raw.decode("utf-8", "replace"))
        req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        _api_error(e.code, e.read())
    except (urllib.error.URLError, OSError) as e:
        raise ClaudeError(f"couldn't reach the AI service ({getattr(e, 'reason', e)})", "offline")


def brain_decide(cfg, history, timeout=20, memory_block=""):
    """Ask the chosen model what to do. `history` ends with the user's message. Returns (tool_name, args_dict);
    plain text from the model comes back as ('reply', {'text': ...})."""
    can_remember = bool(cfg.get("memory_enabled", True))
    system = brain_system_prompt(memory_block, can_remember)
    tools = [t for t in BRAIN_TOOLS if can_remember or t["name"] not in ("remember", "forget")]
    if cfg.get("brain_provider", "claude") == "ollama":
        base = (cfg.get("ollama_url") or "http://localhost:11434").rstrip("/")
        body = {"model": cfg.get("ollama_model") or "llama3.1:8b", "stream": False,
                "messages": [{"role": "system", "content": system}] + history,
                "tools": [{"type": "function", "function": t} for t in tools]}
        data = _post_json(base + "/api/chat", body, {"content-type": "application/json"}, max(timeout, 60))
        msg = data.get("message") or {}
        calls = msg.get("tool_calls") or []
        if calls:
            fn = calls[0].get("function") or {}
            args = fn.get("arguments") or {}
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except ValueError:
                    args = {}
            return fn.get("name", ""), args
        text = (msg.get("content") or "").strip()
        if not text:
            raise ClaudeError("the local model sent back nothing", "error")
        return "reply", {"text": re.sub(r"[*_#`]+", "", text)}
    key = claude_key_get(cfg)
    if not key:
        raise ClaudeError("no API key set", "no_key")
    body = {"model": cfg.get("claude_model") or CLAUDE_MODELS[0][0], "max_tokens": 400, "system": system,
            "messages": history, "tool_choice": {"type": "any"},
            "tools": [{"name": t["name"], "description": t["description"], "input_schema": t["parameters"]} for t in tools]}
    data = _post_json("https://api.anthropic.com/v1/messages", body,
                      {"content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"}, timeout)
    for block in data.get("content", []):
        if block.get("type") == "tool_use":
            return block.get("name", ""), block.get("input") or {}
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()
    if not text:
        raise ClaudeError("the AI sent back an empty reply", "error")
    return "reply", {"text": re.sub(r"[*_#`]+", "", text)}


# --------------------------------------------------------------- natural voice (optional)
NEURAL_VOICES = [
    ("en-IN-NeerjaNeural", "Neerja (India)"), ("en-US-JennyNeural", "Jenny (US)"),
    ("en-US-AriaNeural", "Aria (US)"), ("en-GB-SoniaNeural", "Sonia (UK)"),
    ("en-AU-NatashaNeural", "Natasha (Australia)"), ("en-GB-LibbyNeural", "Libby (UK)"),
    ("en-US-AvaNeural", "Ava (US)"), ("en-US-EmmaNeural", "Emma (US)"),
    ("en-US-MichelleNeural", "Michelle (US)"), ("en-CA-ClaraNeural", "Clara (Canada)"),
    ("en-IE-EmilyNeural", "Emily (Ireland)"), ("en-NZ-MollyNeural", "Molly (New Zealand)"),
    ("en-ZA-LeahNeural", "Leah (South Africa)"),
]
VOICE_ALIASES = {"UK": "british england", "US": "american usa", "Australia": "australian aussie",
                 "India": "indian", "Canada": "canadian", "Ireland": "irish", "New Zealand": "kiwi zealand",
                 "South Africa": "african"}
_VOICE_FILLER = {"the", "a", "an", "voice", "please", "your", "accent", "one", "to", "use", "with"}
_VOICE_CYCLE_WORDS = {"different", "new", "another", "next", "other", "nicer", "better"}


def voice_first_name(label):
    return label.split(" (")[0]


def voice_query_words(query):
    return [w for w in re.findall(r"[a-z]+", (query or "").lower()) if w not in _VOICE_FILLER]


def voice_search_text(label):
    country = re.search(r"\((.*?)\)", label)
    return (label + " " + VOICE_ALIASES.get(country.group(1) if country else "", "")).lower()


def find_voices(voices, query):
    """The (code, label) voices whose name or accent contains every word of the query ('sonia', 'british')."""
    words = voice_query_words(query)
    if not words:
        return []
    return [(c, n) for c, n in voices if all(w in voice_search_text(n) for w in words)]


def sentence_parts(text, long_enough=90, most=5):
    """Split a long reply into a few sentence-sized pieces, so the first can be spoken while the rest are made.
    Short replies stay in one piece."""
    text = text.strip()
    if len(text) <= long_enough:
        return [text]
    parts = []
    for piece in re.split(r"(?<=[.!?])\s+", text):
        if parts and len(parts[-1]) < 25:                 # don't leave a tiny fragment like "Okay." on its own
            parts[-1] += " " + piece
        else:
            parts.append(piece)
    while len(parts) > most:                              # cap the number of requests
        i = min(range(len(parts) - 1), key=lambda k: len(parts[k]) + len(parts[k + 1]))
        parts[i:i + 2] = [parts[i] + " " + parts[i + 1]]
    if parts and len(parts[0]) > 75:                      # start talking sooner: make the first piece a short clause
        m = re.search(r"[,;:]\s|\s(?:and|but|because|which|so)\s", parts[0][25:75])
        if m:
            cut = 25 + m.end() if m.group(0)[0] in ",;:" else 25 + m.start()
            first, rest = parts[0][:cut].strip(), parts[0][cut:].strip()
            if len(first) >= 20 and len(rest) >= 20:
                parts[0:1] = [first, rest]
    return parts or [text]


def play_audio(path, ctl=None):
    """Play an mp3 and wait until it has finished. `ctl` (the Speaker) is told which player is running, so it
    can pause or stop it from another thread."""
    path = str(path)
    if OS == "Windows":
        import ctypes
        mci = ctypes.windll.winmm.mciSendStringW
        alias = f"pac{os.getpid()}"
        mci(f"close {alias}", None, 0, 0)
        if mci(f'open "{path}" type mpegvideo alias {alias}', None, 0, 0):
            raise RuntimeError("Windows could not open the audio file")
        if ctl is not None:
            ctl.alias = alias
        try:
            mci(f"play {alias} wait", None, 0, 0)
        finally:
            if ctl is not None:
                ctl.alias = None
            mci(f"close {alias}", None, 0, 0)
        return
    players = ([["afplay", path]] if OS == "Darwin" else
               [["mpg123", "-q", path], ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path],
                ["mpv", "--no-video", "--really-quiet", path]])
    for cmd in players:
        if shutil.which(cmd[0]):
            p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if ctl is not None:
                ctl.proc = p
            try:
                p.wait(timeout=120)
            except subprocess.TimeoutExpired:
                p.kill()
            finally:
                if ctl is not None:
                    ctl.proc = None
            return
    raise RuntimeError("no audio player found (install mpg123 or ffmpeg)")


class Speaker:
    """Speaks replies offline. Each reply runs pyttsx3 in its own short-lived
    process, because reusing one engine object for many replies is unreliable
    on Windows (it often stops producing audio after the first one or two)."""

    def __init__(self, cfg, on_info=None):
        self.cfg = cfg
        self.on_info = on_info or (lambda s: None)
        self.q = queue.Queue()
        self.speaking = threading.Event()
        self.ranked = None
        self.last_name = None
        self.rate = int(cfg.get("rate", 165))
        self.volume = 1.0
        self.py = self._python_for_speech()
        self.neural_retry_at = 0.0
        self.warned_neural = False
        self.voices = list(NEURAL_VOICES)        # trimmed to the ones Microsoft really offers on first use
        self.voices_checked = False
        self.on_voice = lambda code: None        # told when the voice changes (keeps the menu tick in step)
        self.gen = 0                 # bumped by stop_now(): anything queued or playing under an older number is dropped
        self.cur_gen = 0
        self.paused = False          # voice held mid-sentence while the listener checks whether you said stop
        self._pause_token = 0
        self.alias = None            # Windows media device now playing, so it can be paused / stopped
        self.proc = None             # offline-voice (or mp3 player) process now running
        self.audible_since = 0.0     # when sound from her really began (the listener compares against it)
        if cfg.get("neural", True) and edge_tts is None:
            self.on_info("Only the voices installed in Windows are available. For several human-sounding voices: "
                         "menu Assistant > Install natural voices.")
        threading.Thread(target=self._worker, daemon=True).start()

    @staticmethod
    def _python_for_speech():
        exe = Path(sys.executable)
        pyw = exe.with_name("pythonw.exe")
        return pyw if OS == "Windows" and pyw.exists() else exe

    def _load_voices(self):
        """One-off, throwaway engine just to list installed voices (safe - it's
        the repeated speaking calls that misbehave, not enumeration)."""
        try:
            eng = pyttsx3.init()
            ranked = rank_voices(eng.getProperty("voices"))
            eng.stop()
            del eng
        except Exception:
            logger.exception("could not list voices")
            ranked = []
        self.ranked = ranked
        if not ranked:
            self.on_info("No female voice found - using the default voice. In Windows: "
                         "Settings > Time & language > Speech > Add voices.")

    def say(self, text):
        if self.cfg.get("speak_replies", True):
            self.q.put((self.gen, text))

    def busy(self):
        return self.speaking.is_set() or not self.q.empty()

    # ----- stopping and pausing
    def _stale(self):
        """True once stop_now() has been called since the sentence now being spoken was queued."""
        return self.cur_gen != self.gen

    def _wait_unpaused(self):
        while self.paused and not self._stale():
            time.sleep(0.03)

    @staticmethod
    def _suspend(pid, on):
        try:
            import psutil as _ps
            proc = _ps.Process(pid)
            proc.suspend() if on else proc.resume()
        except Exception:
            if OS != "Windows":
                import signal
                try:
                    os.kill(pid, signal.SIGSTOP if on else signal.SIGCONT)
                except OSError:
                    pass

    def _media(self, command):
        if OS == "Windows" and self.alias:
            try:
                import ctypes
                ctypes.windll.winmm.mciSendStringW(f"{command} {self.alias}", None, 0, 0)
            except Exception:
                logger.exception("audio device command failed: %s", command)

    def _halt(self):
        """Cut off whatever sound is coming out right now."""
        self._media("stop")
        self._media("close")
        p = self.proc
        if p is not None and p.poll() is None:
            try:
                p.kill()
            except Exception:
                pass

    def stop_now(self):
        """Be quiet RIGHT NOW: drop everything queued, cut the sound that is playing."""
        self.gen += 1
        try:
            while True:
                self.q.get_nowait()
        except queue.Empty:
            pass
        self.paused = False
        self._halt()
        self.audible_since = 0.0
        self.speaking.clear()

    def pause(self):
        """Hold the voice mid-sentence (the listener does this when it hears you start talking over her).
        She carries on by herself after 5 seconds if nobody calls resume()."""
        if self.paused or not self.speaking.is_set():
            return False
        self.paused = True
        self._media("pause")
        p = self.proc
        if p is not None and p.poll() is None:
            self._suspend(p.pid, True)
        self._pause_token += 1
        token = self._pause_token
        timer = threading.Timer(5.0, lambda: self.resume() if (self.paused and self._pause_token == token) else None)
        timer.daemon = True
        timer.start()
        return True

    def resume(self):
        if not self.paused:
            return
        self.paused = False
        self._media("resume")
        p = self.proc
        if p is not None and p.poll() is None:
            self._suspend(p.pid, False)

    def _neural_wanted(self):
        return bool(self.cfg.get("neural", True)) and edge_tts is not None

    def _check_voices(self):
        """Ask Microsoft which of our listed voices exist (once, when online) so a wrong name is never offered."""
        import asyncio

        async def fetch():
            return await asyncio.wait_for(edge_tts.list_voices(), timeout=8)
        try:
            found = {v.get("ShortName") for v in asyncio.run(fetch())}
        except Exception as e:
            logger.warning("couldn't fetch the voice list (%s)", e)
            return False
        keep = [(c, n) for c, n in NEURAL_VOICES if c in found]
        if keep:
            self.voices = keep
        self.voices_checked = True
        return True

    def set_voice_code(self, code, announce=True):
        label = dict(self.voices).get(code) or dict(NEURAL_VOICES).get(code, code)
        self.cfg["neural_voice"] = code
        save_config(self.cfg)
        self.on_info("Voice: " + label)
        self.on_voice(code)
        if announce:
            self.say(f"Hi, I'm {voice_first_name(label)}. How do I sound?")

    def list_labels(self):
        """(names of the voices you can switch between, whether they are the natural online ones)."""
        if self._neural_wanted():
            return [n for _, n in self.voices], True
        if self.ranked is None:
            self._load_voices()
        return [n for _, n in (self.ranked or [])], False

    def pick_voice(self, query):
        """Switch to the voice that matches e.g. 'sonia' or 'british'. Returns its name, or None if none match."""
        if self._neural_wanted():
            hits = find_voices(self.voices, query)
            if not hits:
                return None
            self.set_voice_code(hits[0][0])
            return hits[0][1]
        if self.ranked is None:
            self._load_voices()
        words = voice_query_words(query)
        for i, (_vid, name) in enumerate(self.ranked or []):
            if words and all(w in name.lower() for w in words):
                self.cfg["voice_idx"] = i
                save_config(self.cfg)
                self.say("How about this voice?")
                return name
        return None

    def cycle_voice(self):
        if self._neural_wanted():
            codes = [c for c, _ in self.voices]
            cur = self.cfg.get("neural_voice")
            if cur not in codes:
                cur = codes[0]          # that is the voice she is actually using until one is saved
            nxt = codes[(codes.index(cur) + 1) % len(codes)]
            self.set_voice_code(nxt)
            if time.time() < self.neural_retry_at:
                self.on_info("The online voices couldn't be reached a moment ago, so you may still hear the "
                             "offline voice. Check your internet connection.")
            return
        if self.ranked is None:
            self._load_voices()
        n = len(self.ranked or [])
        if self.cfg.get("neural", True) and edge_tts is None:
            self.on_info("Only the voices installed in Windows are available. For several human-sounding voices: "
                         "menu Assistant > Install natural voices.")
        if n <= 1:
            self.say("I only have one voice on this laptop. The Assistant menu can install more natural ones.")
            return
        self.cfg["voice_idx"] = (int(self.cfg.get("voice_idx", 0)) + 1) % n
        save_config(self.cfg)
        self.say("How about this voice?")

    def change_rate(self, delta):
        self.rate = max(100, min(300, self.rate + delta))
        self.cfg["rate"] = self.rate
        save_config(self.cfg)

    def _speak_in_subprocess(self, text, voice_id):
        code = (
            "import pyttsx3,sys\n"
            "e = pyttsx3.init()\n"
            f"e.setProperty('rate', {self.rate})\n"
            f"e.setProperty('volume', {self.volume})\n"
            + (f"e.setProperty('voice', {voice_id!r})\n" if voice_id else "")
            + f"e.say({text!r})\n"
            "e.runAndWait()\n"
        )
        if self._stale():
            return
        self._wait_unpaused()
        if self._stale():
            return
        p = subprocess.Popen([str(self.py), "-c", code], creationflags=NO_WINDOW,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.proc = p
        self.audible_since = time.time() + 0.6             # python and the voice engine take a moment to start
        try:
            p.wait(timeout=45)
        except subprocess.TimeoutExpired:
            p.kill()
        finally:
            self.proc = None
            self.audible_since = 0.0

    def _neural_ok(self):
        return bool(self.cfg.get("neural", True)) and edge_tts is not None and time.time() >= self.neural_retry_at

    def _speak_neural(self, text):
        """A natural neural voice (Microsoft's online voices through the edge-tts package)."""
        import asyncio
        codes = [c for c, _ in self.voices]
        voice = self.cfg.get("neural_voice")
        if voice not in codes:
            voice = codes[0]
        pct = max(-50, min(100, int(round((self.rate - 165) / 165 * 100))))
        spoken = re.sub(r"[*_#`]+", "", text)

        def synth(part, n):
            path = Path(tempfile.gettempdir()) / f"pac_voice_{os.getpid()}_{n}.mp3"

            async def go():
                comm = edge_tts.Communicate(part, voice, rate=f"{pct:+d}%")
                await asyncio.wait_for(comm.save(str(path)), timeout=12)
            asyncio.run(go())
            return path

        def play(path):
            try:
                if self._stale():
                    return
                self._wait_unpaused()
                if self._stale():
                    return
                self.audible_since = time.time()
                play_audio(path, self)
            finally:
                self.audible_since = 0.0
                try:
                    path.unlink()
                except OSError:
                    pass

        parts = sentence_parts(spoken)
        if len(parts) == 1:
            play(synth(parts[0], 0))
            return
        # A longer reply: start speaking the first sentence while the next one is still being made.
        from concurrent.futures import ThreadPoolExecutor

        def drop(futs):                                    # delete audio that was made but will never be played
            for f in futs:
                def _rm(fut):
                    try:
                        fut.result().unlink()
                    except Exception:
                        pass
                f.add_done_callback(_rm)
        with ThreadPoolExecutor(max_workers=2) as pool:
            futs = {i: pool.submit(synth, parts[i], i) for i in range(min(2, len(parts)))}
            for i in range(len(parts)):
                try:
                    path = futs.pop(i).result()
                except Exception:
                    drop(list(futs.values()))
                    if i == 0:
                        raise                              # nothing spoken yet: the caller falls back to the system voice
                    logger.warning("natural voice failed part-way; finishing with the system voice")
                    self._speak_system(" ".join(parts[i:]))
                    return
                if self._stale():
                    try:
                        path.unlink()
                    except OSError:
                        pass
                    drop(list(futs.values()))
                    return
                if i + 2 < len(parts):                     # keep two sentences being made ahead of the one playing
                    futs[i + 2] = pool.submit(synth, parts[i + 2], i + 2)
                play(path)

    def _speak_one(self, text):
        if self._stale():
            return
        if self._neural_ok():
            try:
                if not self.voices_checked and not self._check_voices():
                    self.neural_retry_at = time.time() + 45      # offline: don't wait on it for every reply
                    raise RuntimeError("can't reach the online voices")
                self._speak_neural(text)
                return
            except Exception as e:
                logger.warning("natural voice failed (%s); using the system voice", e)
                self.neural_retry_at = time.time() + 45      # don't make every reply wait on a dead connection
                if not self.warned_neural:
                    self.warned_neural = True
                    self.on_info("The natural voice needs internet. Using the offline system voice for now.")
        self._speak_system(text)

    def _speak_system(self, text):
        voice_id = None
        if self.ranked:
            voice_id, name = self.ranked[int(self.cfg.get("voice_idx", 0)) % len(self.ranked)]
            if name != self.last_name:
                self.last_name = name
                self.on_info(f"Voice: {name}")
        self._speak_in_subprocess(text, voice_id)

    def _worker(self):
        if self.ranked is None:
            self._load_voices()
        while True:
            gen, text = self.q.get()
            if gen != self.gen:                    # queued before a stop: never say it
                continue
            self.cur_gen = gen
            self.speaking.set()
            try:
                self._speak_one(text)
            except Exception:
                logger.exception("speech output failed")
            finally:
                time.sleep(0.12)
                if self.q.empty():
                    self.speaking.clear()


# --------------------------------------------------------------- timetable
TIMETABLE_FILE = DATA_DIR / "timetable.txt"
TIMETABLE_SAMPLE = (
    "# Your timetable. One class per line:   day   start-end   subject, room\n"
    "# Lines starting with # are ignored. Remove the # in front of the examples to try them, or paste your own.\n"
    "#\n"
    "# Monday 09:00-10:00 Mathematics, Room 204\n"
    "# Monday 10:15-11:15 Physics, Lab 2\n"
    "# Tue/Thu 2 pm - 3 pm Chemistry, Room 12\n"
    "#\n"
    "# You can also group by day:\n"
    "# Friday:\n"
    "# 9:00-10:00 English\n"
    "# 11:00-12:00 Computer Science, Lab 1\n"
    "#\n"
    "# Or paste a grid saved as CSV: days across the top row, time slots down the first column.\n"
)
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
_DAY_EXTRA = {"tues": 1, "thur": 3, "thurs": 3, "weds": 2}
_RANGE = re.compile(r"(\d{1,2}(?:[:.]\d{2})?\s*(?:[ap]\.?m\.?)?)\s*(?:-|\u2013|\u2014|to|until|till)\s*"
                    r"(\d{1,2}(?:[:.]\d{2})?\s*(?:[ap]\.?m\.?)?)", re.I)
_CLOCK = re.compile(r"(\d{1,2})(?:[:. ](\d{2}))?(?:\s*([ap])\.?m\b\.?)?", re.I)


def day_index(word):
    w = (word or "").lower().strip().strip(".:,")
    if w in _DAY_EXTRA:
        return _DAY_EXTRA[w]
    if len(w) >= 3:
        for i, d in enumerate(DAYS):
            if d.startswith(w):
                return i
    return None


def parse_clock(text):
    """'9', '9:30', '2 pm', '17:45' -> (minutes after midnight, whether am/pm was said). None if no time."""
    m = _CLOCK.search(text or "")
    if not m:
        return None
    h, mi, mer = int(m.group(1)), int(m.group(2) or 0), (m.group(3) or "").lower()
    if h > 24 or mi > 59:
        return None
    if mer == "a":
        h = h % 12
    elif mer == "p":
        h = h % 12 + 12
    elif 1 <= h <= 6:          # nobody has a 3 o'clock class at 3 in the morning
        h += 12
    return (h % 24) * 60 + mi, bool(mer)


def parse_range(text):
    m = _RANGE.search(text)
    if not m:
        return None
    a, b = parse_clock(m.group(1)), parse_clock(m.group(2))
    if not a or not b:
        return None
    start, end = a[0], b[0]
    if end <= start and end < 12 * 60:
        end += 12 * 60
    return start, end


def fmt_time(mins):
    h, m = divmod(int(mins) % 1440, 60)
    h12 = h % 12 or 12
    return f"{h12}:{m:02d} {'AM' if h < 12 else 'PM'}" if m else f"{h12} {'AM' if h < 12 else 'PM'}"


def fmt_range(a, b):
    sa, sb = fmt_time(a), fmt_time(b)
    if sa[-2:] == sb[-2:]:
        sa = sa[:-3]
    return f"{sa} to {sb}"


def join_and(items):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1] if items else ""


def _split_subject(rest):
    parts = [p.strip() for p in re.split(r"\s*(?:,|\||;|\s-\s|\s\u2013\s|\s@\s|\s/\s)\s*", rest) if p.strip()]
    if not parts:
        return "Class", ""
    return parts[0], ", ".join(parts[1:])


def _parse_grid(lines):
    import csv
    sample = "\n".join(lines[:6])
    delim = max(",\t;|", key=sample.count)
    if not sample.count(delim):
        return None
    rows = list(csv.reader(lines, delimiter=delim))
    head = next((i for i, r in enumerate(rows)
                 if sum(day_index(c) is not None for c in r) >= 3 and not _RANGE.search(" ".join(r))), None)
    if head is None:
        return None
    cols = {j: day_index(c) for j, c in enumerate(rows[head]) if day_index(c) is not None}
    out = []
    for r in rows[head + 1:]:
        if not r or not parse_range(r[0]):
            continue
        start, end = parse_range(r[0])
        for j, d in cols.items():
            cell = r[j].strip() if j < len(r) else ""
            if cell and cell.lower() not in ("-", "\u2013", "free", "nil", "none", "n/a", "break", "lunch",
                                              "lunch break", "recess", "interval"):
                subj, room = _split_subject(cell)
                out.append({"day": d, "start": start, "end": end, "subject": subj, "room": room})
    return out or None


# ---- CSV timetables. Spreadsheets come in many shapes, so the cells are read by what they CONTAIN (a day name,
# a time, a subject) rather than by exact headings. Layouts understood:
#   days across the top, times down the side   |   days down the side, times across the top
#   a flat list: Day, Start, End, Subject, Room (any column order, headings optional, 'Mon/Wed' allowed)
# plus start-only times ("9:00" - the end is the next slot), 12/24-hour times, '0900-1000', title rows,
# comma / semicolon / tab separators, quoted cells that run over several lines, and Excel's byte-order mark.
_DAY2 = {"mo": 0, "tu": 1, "we": 2, "th": 3, "fr": 4, "sa": 5, "su": 6}
_SKIP_RE = re.compile(r"(?:free|break|lunch|recess|interval|no class|holiday|closed|n/a|nil|none|x)\b")
_TIMES = re.compile(r"(?<![\d:.])(\d{1,2})(?:[:.](\d{2}))?\s*(?:([ap])\.?m\b\.?)?", re.I)
_HDR = (("day", r"\bdays?\b|weekday"), ("start", r"start|from|begin"), ("end", r"\bend|finish|until|\bto\b"),
        ("room", r"room|location|venue|lab|hall|where|place|building"), ("teacher", r"teacher|tutor|instructor|lecturer|faculty|staff|prof"),
        ("subject", r"subject|course|class|module|lesson|title|name|activity|unit|paper|topic"),
        ("time", r"time|slot|hour|period|timing"))


def decode_text_file(raw):
    """Bytes of a text file -> str, whatever Excel or Notepad saved it as."""
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", "replace")
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        try:
            return raw.decode("cp1252")
        except UnicodeDecodeError:
            return raw.decode("latin-1")


def _cell_day(cell):
    """Day index if the cell is a day name: Monday, MON, Mon., Mo, 'Monday (A)', 'Mon 12/10'. Not 'Monday Maths'."""
    c = " ".join((cell or "").split()).strip(" .:,")
    first = re.match(r"[A-Za-z]+", c)
    if not c or len(c) > 22 or not first:
        return None
    w, rest = first.group(0).lower(), c[first.end():]
    if re.search(r"[A-Za-z]{3,}", rest):
        return None
    if w in _DAY2 and not rest.strip(" .:,()-/0123456789"):
        return _DAY2[w] if len(c) <= 3 else None
    return day_index(w)


def _cell_days(cell):
    """All the days named in a cell: 'Mon', 'Mon/Wed/Fri', 'Tue, Thu', 'Mon & Wed', 'Mon-Fri'. [] if it isn't days."""
    c = " ".join((cell or "").split())
    rng = re.fullmatch(r"([A-Za-z]+)\.?\s*(?:-|\u2013|\u2014|to)\s*([A-Za-z]+)\.?", c, re.I)
    if rng and _cell_day(rng.group(1)) is not None and _cell_day(rng.group(2)) is not None:
        a, b = _cell_day(rng.group(1)), _cell_day(rng.group(2))
        return list(range(a, b + 1)) if a <= b else []
    parts = [p for p in re.split(r"[\s/,&+;]+", c) if p and p.lower() != "and"]
    days = [_cell_day(p) for p in parts]
    return days if parts and all(d is not None for d in days) else []


def _times_in(cell):
    out = []
    for m in _TIMES.finditer(cell or ""):
        if m.group(2) or m.group(3):                     # '9:30' or '2 pm' - a bare '1' is a period number, not a time
            pc = parse_clock(m.group(0))
            if pc:
                out.append(pc[0])
    return out


def _cell_span(cell):
    """(start, end or None) minutes if the cell holds a time or a time range, else None."""
    c = " ".join((cell or "").split())
    if not c:
        return None
    dash = r"(?:-|\u2013|\u2014|to|until|till)"
    if re.search(r"\d\s*[:.]\s*\d{2}|\d\s*[ap]\.?m\b", c, re.I) or re.fullmatch(r"\d{1,2}\s*" + dash + r"\s*\d{1,2}", c, re.I):
        r = parse_range(c)
        if r:
            return r
    m4 = re.fullmatch(r"([01]?\d|2[0-3])([0-5]\d)\s*" + dash + r"\s*([01]?\d|2[0-3])([0-5]\d)(?:\s*hrs?)?", c, re.I)
    if m4:
        return int(m4.group(1)) * 60 + int(m4.group(2)), int(m4.group(3)) * 60 + int(m4.group(4))
    t = _times_in(c)
    if len(t) >= 2:
        end = t[1] + (12 * 60 if t[1] <= t[0] and t[1] < 12 * 60 else 0)
        return t[0], end
    return (t[0], None) if t else None


def _row_span(cells):
    spans = [s for s in (_cell_span(c) for c in cells) if s]
    if not spans:
        return None
    if len(spans) >= 2 and spans[0][1] is None and spans[1][1] is None:       # separate Start and End columns
        return spans[0][0], spans[1][0]
    return spans[0]


def _end_for(start, nxt):
    """A class with no stated end runs to the next slot (if that is close), otherwise an hour."""
    return nxt if nxt and start < nxt <= start + 180 else start + 60


def _add_entry(out, day, start, end, cell):
    cell = (cell or "").strip()
    low = re.sub(r"[^a-z/ ]", "", cell.lower()).strip()
    if not cell or (not low and len(cell) <= 3) or _SKIP_RE.match(low) or cell in ("-", "\u2013", "\u2014", "--"):
        return
    if _cell_span(cell) and not re.search(r"[A-Za-z]{3}", cell):
        return
    subj, room = _split_subject(cell)
    out.append({"day": day, "start": start, "end": end, "subject": subj, "room": room})


def _csv_rows(text):
    import csv, io
    text = (text or "").lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    lines = [l for l in text.split("\n") if l.strip()][:60]
    if len(lines) < 2:
        return None
    counts = {d: sum(l.count(d) for l in lines) for d in ",;\t|"}
    delim = max(counts, key=counts.get)
    if not counts[delim]:
        return None
    try:
        raw = list(csv.reader(io.StringIO(text), delimiter=delim))
    except csv.Error:
        raw = [l.split(delim) for l in text.split("\n")]
    rows = []
    for r in raw:
        r = [c.strip().replace("\n", ", ") for c in r]
        if not any(r) or (r[0].startswith("#") and sum(1 for c in r if c) <= 1):
            continue
        rows.append(r)
    if len(rows) < 2:
        return None
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    keep = [j for j in range(width) if any(r[j] for r in rows)]          # drop columns that are empty all the way down
    return [[r[j] for j in keep] for r in rows]


def _grid_days_across(rows):
    best = None
    for i, r in enumerate(rows):
        n = sum(_cell_day(c) is not None for c in r)
        if n >= 2 and not any(_cell_span(c) for c in r) and (best is None or n > best[1]):
            best = (i, n)
    if not best:
        return []
    h = best[0]
    cols = {j: _cell_day(c) for j, c in enumerate(rows[h]) if _cell_day(c) is not None}
    body = [(r, _row_span([c for j, c in enumerate(r) if j not in cols])) for r in rows[h + 1:]]
    timed = [k for k, (_, sp) in enumerate(body) if sp]
    out = []
    for pos, k in enumerate(timed):
        r, (start, end) = body[k]
        if end is None:
            end = _end_for(start, body[timed[pos + 1]][1][0] if pos + 1 < len(timed) else None)
        for j, d in cols.items():
            _add_entry(out, d, start, end, r[j] if j < len(r) else "")
    return out


def _grid_days_down(rows):
    best = None
    for j in range(max(len(r) for r in rows)):
        idx = [i for i, r in enumerate(rows) if j < len(r) and _cell_day(r[j]) is not None]
        if len(idx) >= 2 and (best is None or len(idx) > len(best[1])):
            best = (j, idx)
    if not best:
        return []
    dc, didx = best
    hdr = next((i for i in range(didx[0] - 1, -1, -1) if sum(1 for c in rows[i] if _cell_span(c)) >= 2), None)
    if hdr is None:
        return []
    cols = {}
    for j, c in enumerate(rows[hdr]):
        if j != dc and _cell_span(c):
            cols[j] = _cell_span(c)
    keys = sorted(cols)
    for pos, j in enumerate(keys):
        s, e = cols[j]
        if e is None:
            cols[j] = (s, _end_for(s, cols[keys[pos + 1]][0] if pos + 1 < len(keys) else None))
    out = []
    for i in didx:
        for j, (s, e) in cols.items():
            _add_entry(out, _cell_day(rows[i][dc]), s, e, rows[i][j] if j < len(rows[i]) else "")
    return out


def _flat_rows(rows):
    roles, first = {}, 0
    for i, r in enumerate(rows[:6]):                                      # a heading row, maybe under a title
        found = {}
        for j, c in enumerate(r):
            low = c.lower()
            if _cell_span(c) or _cell_days(c):
                found = {}
                break
            for role, pat in _HDR:
                if re.search(pat, low) and role not in found.values():
                    found[j] = role
                    break
        if len(found) >= 2 and set(found.values()) & {"day", "start", "time"}:
            roles, first = found, i + 1
            break
    col = {role: j for j, role in roles.items()}
    out = []
    for r in rows[first:]:
        days, dj = [], col.get("day")
        if dj is not None and dj < len(r):
            days = _cell_days(r[dj])
        if not days:
            for j, c in enumerate(r):
                if _cell_days(c):
                    days, dj = _cell_days(c), j
                    break
        if not days:
            continue
        span, timecols = None, set()
        sj, ej = col.get("start"), col.get("end")
        if sj is not None and sj < len(r) and _cell_span(r[sj]):
            a = _cell_span(r[sj])
            b = _cell_span(r[ej]) if ej is not None and ej < len(r) else None
            span, timecols = (a[0], b[0] if b else a[1]), {sj, ej}
        if span is None:
            tj = col.get("time")
            cand = [tj] if tj is not None else []
            cand += [j for j in range(len(r)) if j != tj and j != dj]
            span = _row_span([r[j] for j in cand if j < len(r)])
            timecols = {j for j in range(len(r)) if _cell_span(r[j])}
        if not span:
            continue
        start, end = span
        end = end if end is not None else start + 60
        left = [j for j in range(len(r)) if j != dj and j not in timecols and r[j]]
        if "subject" in col and col["subject"] in left:
            sub = r[col["subject"]]
            rest = [r[j] for j in left if j != col["subject"] and col.get("time") != j]
        else:
            nums = [j for j in left if re.fullmatch(r"\d{1,2}", r[j])]
            texts = [j for j in left if j not in nums] or left            # 'Period 1' numbers are not subjects
            if not texts:
                continue
            sub, rest = r[texts[0]], [r[j] for j in left if j != texts[0] and (j not in nums or len(left) == 2)]
        subj, room = _split_subject(sub)
        room = ", ".join(x for x in [room] + [q for q in rest if q] if x)
        for d in days:
            out.append({"day": d, "start": start, "end": end, "subject": subj, "room": room})
    return out


def _csv_timetable(text):
    rows = _csv_rows(text)
    if not rows:
        return []
    for layout in (_grid_days_across, _grid_days_down, _flat_rows):
        try:
            got = layout(rows)
        except Exception:
            logger.exception("timetable layout %s failed", layout.__name__)
            got = []
        if got:
            return got
    return []


def timetable_to_text(entries, source=""):
    """The timetable as plain lines PAC (and you) can read and edit: Monday 09:00-10:00 Maths, Room 204."""
    lines = ["# Timetable" + (f" imported from {source}" if source else "") +
             ". One class per line: day, start-end, subject, room. Lines starting with # are ignored."]
    for e in sorted(entries, key=lambda e: (e["day"], e["start"])):
        a, b = e["start"] % 1440, min(e["end"], 1439)
        lines.append(f"{DAYS[e['day']].capitalize()} {a // 60:02d}:{a % 60:02d}-{b // 60:02d}:{b % 60:02d} {e['subject']}"
                     + (f", {e['room']}" if e.get("room") else ""))
    return "\n".join(lines) + "\n"


def parse_timetable(text):
    """Understands 'Monday 09:00-10:00 Maths, Room 204', 'Mon/Wed 2pm-3pm Physics', day headings with
    times underneath, and CSV grids. Returns a list of {day, start, end, subject, room}."""
    lines = [l.rstrip() for l in (text or "").splitlines() if l.strip() and not l.strip().startswith("#")]
    if not lines:
        return []
    grid = _csv_timetable(text) or _parse_grid(lines)      # the tolerant reader first; the original one as a backstop
    if grid:
        return sorted(grid, key=lambda e: (e["day"], e["start"], e["subject"]))
    out, current = [], []
    for line in lines:
        s, days = line.strip(), []
        while True:
            m = re.match(r"\s*([A-Za-z]+)\.?\s*(?:[/&,:]|\band\b)?\s*", s)
            if m and day_index(m.group(1)) is not None:
                days.append(day_index(m.group(1)))
                s = s[m.end():]
            else:
                break
        rng = parse_range(s)
        if not rng:
            if days and not s.strip():
                current = days            # a heading such as "Friday:"
            continue
        use = days or current
        if not use:
            continue
        rm = _RANGE.search(s)
        rest = (s[:rm.start()] + " " + s[rm.end():]).strip(" ,:-\u2013|\t")
        subj, room = _split_subject(rest)
        for d in use:
            out.append({"day": d, "start": rng[0], "end": rng[1], "subject": subj, "room": room})
    return sorted(out, key=lambda e: (e["day"], e["start"]))


def ensure_timetable_file():
    if not TIMETABLE_FILE.exists():
        try:
            TIMETABLE_FILE.write_text(TIMETABLE_SAMPLE, encoding="utf-8")
        except OSError:
            logger.exception("could not create the timetable file")


class Timetable:
    """Reads ~/.pac/timetable.txt (re-reading whenever you save it) and answers 'what / when'."""

    def __init__(self):
        self.entries, self.stamp = [], None

    def load(self):
        try:
            st = TIMETABLE_FILE.stat().st_mtime
        except OSError:
            self.entries, self.stamp = [], None
            return self.entries
        if st != self.stamp:
            try:
                self.entries = parse_timetable(TIMETABLE_FILE.read_text(encoding="utf-8-sig"))
            except Exception:
                logger.exception("could not read the timetable")
                self.entries = []
            self.stamp = st
        return self.entries

    def on(self, day):
        return sorted((e for e in self.load() if e["day"] == day), key=lambda e: e["start"])

    def now_and_next(self, now):
        mins = now.hour * 60 + now.minute
        today = self.on(now.weekday())
        return (next((e for e in today if e["start"] <= mins < e["end"]), None),
                next((e for e in today if e["start"] > mins), None))

    def next_class(self, now):
        mins = now.hour * 60 + now.minute
        for ahead in range(8):
            for e in self.on((now.weekday() + ahead) % 7):
                if ahead > 0 or e["start"] > mins:
                    return e, ahead
        return None, None

    def find(self, subject):
        key = re.sub(r"[^a-z0-9 ]", "", (subject or "").lower()).strip()
        if len(key) < 3:
            return []
        hits = []
        for e in self.load():
            name = re.sub(r"[^a-z0-9 ]", "", e["subject"].lower())
            if key in name or name in key or difflib.SequenceMatcher(None, key, name).ratio() >= 0.75:
                hits.append(e)
        return sorted(hits, key=lambda e: (e["day"], e["start"]))


# --------------------------------------------------------------- unit conversion
_U = {}


def _unit(family, factor, *names):
    for n in names:
        _U[n] = (family, factor)


_unit("len", 1000.0, "km", "kilometer", "kilometers", "kilometre", "kilometres")
_unit("len", 1.0, "m", "meter", "meters", "metre", "metres")
_unit("len", 0.01, "cm", "centimeter", "centimeters", "centimetre", "centimetres")
_unit("len", 0.001, "mm", "millimeter", "millimeters")
_unit("len", 1609.344, "mile", "miles", "mi")
_unit("len", 0.9144, "yard", "yards", "yd")
_unit("len", 0.3048, "foot", "feet", "ft")
_unit("len", 0.0254, "inch", "inches")
_unit("mass", 1.0, "kg", "kilogram", "kilograms", "kilo", "kilos")
_unit("mass", 0.001, "gram", "grams", "g")
_unit("mass", 0.45359237, "pound", "pounds", "lb", "lbs")
_unit("mass", 0.028349523, "ounce", "ounces", "oz")
_unit("vol", 1.0, "liter", "liters", "litre", "litres", "l")
_unit("vol", 0.001, "ml", "milliliter", "milliliters")
_unit("vol", 3.785411784, "gallon", "gallons")
_unit("vol", 0.2365882, "cup", "cups")
_TEMP = {"c": "c", "celsius": "c", "centigrade": "c", "f": "f", "fahrenheit": "f", "k": "k", "kelvin": "k"}


def convert_units(n, a, b):
    """Returns the converted number, or None if the two units don't go together."""
    a, b = a.strip().lower(), b.strip().lower()
    if a in _TEMP and b in _TEMP:
        c = n if _TEMP[a] == "c" else (n - 32) * 5 / 9 if _TEMP[a] == "f" else n - 273.15
        return c if _TEMP[b] == "c" else c * 9 / 5 + 32 if _TEMP[b] == "f" else c + 273.15
    if a in _U and b in _U and _U[a][0] == _U[b][0]:
        return n * _U[a][1] / _U[b][1]
    return None


# --------------------------------------------------------------- the brain
STOP_SPEAKING = re.compile(
    r"^(?:(?:hey|ok|okay|pac) )?(?:stop|stop it|stop that|stop talking|stop speaking|stop reading|stop the news|"
    r"mute|moot|silence|enough|that'?s enough|enough now)(?: please| now| pac)?$")
HOME_RE = re.compile(r"\bwake up\b.{0,12}\b(?:daddy|dad|papa|father)(?:'?s| is| has)?\b.{0,8}\bhome\b"
                     r"|\b(?:daddy|dad|papa)(?:'?s| is| has) (?:back )?home\b")
NEWS_URL = "https://news.google.com/rss/headlines/section/topic/WORLD?hl={hl}&gl={gl}&ceid={gl}:{lang}"
_NEWS_NUMBERS = {"five": 5, "ten": 10, "fifteen": 15, "twenty": 20}


def fetch_world_news(count=20, lang_code="en-IN", timeout=12):
    """Today's top international headlines from Google News (its public world-news feed), fetched quietly in
    the background - no browser window opens. Returns [(headline, source, link)]."""
    import urllib.request
    import xml.etree.ElementTree as ET
    parts = lang_code.replace("_", "-").split("-")
    lang, gl = parts[0].lower(), (parts[1].upper() if len(parts) > 1 else "US")
    url = NEWS_URL.format(hl=f"{lang}-{gl}", gl=gl, lang=lang)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (PAC voice assistant)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        root = ET.fromstring(r.read())
    items, seen = [], set()
    for it in root.iter("item"):
        title = " ".join((it.findtext("title") or "").split())
        src_el = it.find("source")
        src = " ".join(((src_el.text if src_el is not None else "") or "").split())
        if src and title.endswith(" - " + src):               # Google writes "Headline - Source"
            title = title[:-(len(src) + 3)]
        elif not src and " - " in title:
            title, src = title.rsplit(" - ", 1)
        key = re.sub(r"\W+", " ", title.lower()).strip()[:70]
        if not title or key in seen:                          # the same story from several outlets: once is enough
            continue
        seen.add(key)
        items.append((title, src, (it.findtext("link") or "").strip()))
        if len(items) >= count:
            break
    return items


# --------------------------------------------------------------- quiet web search (no browser window opens)
# Google no longer answers a plain web request (it insists on JavaScript) and its search API is closed to new users.
# So PAC asks Google the way you would - through a hidden copy of your own Chrome / Edge that nobody sees. If Google
# refuses (a captcha, no Chrome / Edge installed, no internet) PAC falls back to DuckDuckGo, which needs no browser.
SEARCH_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/140.0.0.0 Safari/537.36")
SEARCH_PROFILE = DATA_DIR / "search_profile"          # the hidden browser's own profile - never your real one
QUESTION_WORDS = {"who", "whom", "whose", "what", "whats", "when", "where", "why", "how", "which", "is", "are", "was",
                  "were", "do", "does", "did", "can", "could", "will", "would", "should", "shall", "has", "have",
                  "had", "tell", "explain", "define", "meaning"}


def _plain(markup):
    """HTML -> readable text, one block per line."""
    s = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", markup)
    s = re.sub(r"(?i)<br\s*/?>|</(?:div|p|li|h[1-6]|tr)>", "\n", s)
    s = html_unescape(re.sub(r"(?s)<[^>]*>", "", s))
    lines = (" ".join(line.split()) for line in s.splitlines())
    return "\n".join(line for line in lines if line)


def find_browser_exe():
    """A Chrome / Edge / Chromium that can run hidden (headless), or None."""
    cands = []
    if OS == "Windows":
        for env in ("ProgramFiles", "ProgramFiles(x86)", "LocalAppData"):
            base = os.environ.get(env)
            if base:
                cands += [Path(base) / "Google/Chrome/Application/chrome.exe",
                          Path(base) / "Microsoft/Edge/Application/msedge.exe"]
    elif OS == "Darwin":
        cands += [Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
                  Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
                  Path("/Applications/Chromium.app/Contents/MacOS/Chromium")]
    for p in cands:
        if p.exists():
            return str(p)
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    return None


_G_LINK = re.compile(r'(?is)<a\b[^>]*?\bhref="(https?://[^"]+)"[^>]*>(?:(?!</a>).)*?<h3\b[^>]*>(.*?)</h3>')
_G_SKIP = ("accounts.google.", "consent.google.", "policies.google.", "webcache.", "translate.google.", "maps.google.")
_G_ANSWER = ("hgKElc", "kno-rdesc", "Z0LcW")           # classes Google has used for its answer box / info panel


def _google_snippet(chunk):
    """The grey description under one result's title."""
    m = re.search(r'(?is)<[a-z]+\b[^>]*class="[^"]*\bVwiC3b\b[^"]*"[^>]*>', chunk)
    lines = _plain(chunk[m.end():m.end() + 2500] if m else chunk[:3000]).splitlines()
    if m:
        return next((l for l in lines if len(l) >= 20), "")[:400]
    return next((l for l in lines if 50 <= len(l) <= 500 and " \u203a " not in l), "")


def parse_google_dom(dom, limit=5):
    """The answer box (when Google shows one) and the first few results, read out of a rendered results page.
    Returns (answer, [{'title', 'url', 'snippet'}]). Google renames its CSS classes now and then, so this leans on
    the stable part - a link with a heading inside it - and treats the answer box and snippets as a bonus."""
    answer = ""
    for cls in _G_ANSWER:
        m = re.search(r'(?is)<(?:div|span)\b[^>]*class="[^"]*\b' + re.escape(cls) + r'\b[^"]*"[^>]*>', dom)
        if m:
            need = 2 if cls == "Z0LcW" else 25
            answer = next((l for l in _plain(dom[m.end():m.end() + 1500]).splitlines() if len(l) >= need), "")[:400]
        if answer:
            break
    found = list(_G_LINK.finditer(dom))
    results, seen = [], set()
    for i, m in enumerate(found):
        url = html_unescape(m.group(1))
        host = urlparse(url).netloc.lower()
        if (not host or host in ("google.com", "www.google.com") or host.startswith(_G_SKIP)
                or host.endswith("gstatic.com") or url in seen):
            continue
        title = " ".join(_plain(m.group(2)).split())
        if not title:
            continue
        seen.add(url)
        end = found[i + 1].start() if i + 1 < len(found) else len(dom)
        results.append({"title": title, "url": url,
                        "snippet": _google_snippet(dom[m.end():min(end, m.end() + 3000)])})
        if len(results) >= limit:
            break
    return answer, results


def google_hidden_search(query, lang_code="en-IN", limit=5, timeout=20):
    """Ask Google through a hidden Chrome / Edge window (it runs the JavaScript Google insists on). No window is
    shown and your own browser profile is never touched. Returns (answer, results)."""
    exe = find_browser_exe()
    if not exe:
        raise RuntimeError("no Chrome or Edge found to run the hidden search")
    parts = lang_code.replace("_", "-").split("-")
    hl, gl = parts[0].lower(), (parts[1].upper() if len(parts) > 1 else "US")
    url = "https://www.google.com/search?" + urlencode({"q": query, "hl": hl, "gl": gl})
    SEARCH_PROFILE.mkdir(exist_ok=True)
    cmd = [exe, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
           "--disable-extensions", "--mute-audio", "--hide-scrollbars", "--window-size=1280,2400",
           f"--user-data-dir={SEARCH_PROFILE}", f"--user-agent={SEARCH_UA}", f"--lang={hl}-{gl}",
           "--virtual-time-budget=7000", "--dump-dom", url]
    if OS == "Linux" and hasattr(os, "geteuid") and os.geteuid() == 0:
        cmd.insert(1, "--no-sandbox")                     # Chrome refuses to start as root without this
    r = subprocess.run(cmd, capture_output=True, timeout=timeout, creationflags=NO_WINDOW)
    dom = r.stdout.decode("utf-8", "replace")
    answer, results = parse_google_dom(dom, limit)
    if not (answer or results):
        logger.info("hidden Google search came back empty (%d bytes of page)", len(dom))
    return answer, results


def parse_duckduckgo(page, limit=5):
    """Results from DuckDuckGo's plain-HTML page: [{'title', 'url', 'snippet'}]."""
    results = []
    for block in re.split(r'(?=<a\b[^>]*class="[^"]*\bresult__a\b)', page)[1:]:
        m = re.match(r'(?is)<a\b[^>]*?\bhref="([^"]+)"[^>]*>(.*?)</a>', block)
        if not m:
            continue
        url = html_unescape(m.group(1))
        if url.startswith("//"):
            url = "https:" + url
        link = parse_qs(urlparse(url).query).get("uddg")
        if link:
            url = link[0]
        title = " ".join(_plain(m.group(2)).split())
        if not title or not url.startswith("http") or "duckduckgo.com/y.js" in url:
            continue                                       # an advert, not a result
        sn = re.search(r'(?is)class="[^"]*\bresult__snippet\b[^"]*"[^>]*>(.*?)</(?:a|div|td)>', block)
        results.append({"title": title, "url": url,
                        "snippet": " ".join(_plain(sn.group(1)).split()) if sn else ""})
        if len(results) >= limit:
            break
    return results


def duckduckgo_search(query, limit=5, timeout=10):
    import urllib.request
    req = urllib.request.Request("https://html.duckduckgo.com/html/", urlencode({"q": query}).encode(),
                                 {"User-Agent": SEARCH_UA, "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return parse_duckduckgo(r.read().decode("utf-8", "replace"), limit)


def web_search(cfg, query, limit=5):
    """Look a question up on the web without opening a window. Google (hidden browser) and DuckDuckGo are asked AT THE
    SAME TIME and the first useful answer wins (Google gets about a second extra if DuckDuckGo is first, since it is
    preferred). Returns (answer, results, engine name, notes) - the notes say why an engine gave nothing."""
    from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
    engines = []
    if cfg.get("search_engine", "google") == "google":
        engines.append(("Google", lambda: google_hidden_search(query, cfg.get("lang", "en-IN"), limit)))
    engines.append(("DuckDuckGo", lambda: ("", duckduckgo_search(query, limit))))
    order = [n for n, _ in engines]
    notes, ok = [], {}
    pool = ThreadPoolExecutor(max_workers=len(engines))
    futs = {pool.submit(run): name for name, run in engines}

    def collect(done):
        for f in done:
            name = futs[f]
            try:
                answer, results = f.result()
            except Exception as e:
                logger.warning("%s search failed: %s", name, e)
                notes.append(f"{name}: {type(e).__name__}: {e}")
                continue
            if answer or results:
                ok[name] = (answer, results)
            else:
                notes.append(f"{name}: nothing came back")
    try:
        pending = set(futs)
        while pending:
            done, pending = wait(pending, return_when=FIRST_COMPLETED)
            collect(done)
            if ok:
                if order[0] not in ok and pending:          # the preferred engine is still working: a short grace period
                    done, pending = wait(pending, timeout=1.2)
                    collect(done)
                break
    finally:
        pool.shutdown(wait=False)
    for name in order:
        if name in ok:
            return ok[name][0], ok[name][1], name, notes
    return "", [], None, notes


# --------------------------------------------------------------- reading web pages (a fuller answer than a snippet)
# After a quiet search PAC opens the top few results itself - plain HTTP, no browser window - reads their text and
# picks the paragraph that answers the question best. Menu > Assistant > "Read the top web pages" switches it off.
_PAGE_JUNK = re.compile(r"\b(?:cookies?|subscribe|sign (?:in|up)|log ?in|javascript|advertis\w*|all rights reserved|"
                        r"privacy policy|terms of (?:use|service)|newsletter|click here|share this|download (?:the )?app)\b",
                        re.I)
_PAGE_SKIP = ("youtube.com", "youtu.be", "facebook.com", "instagram.com", "twitter.com", "x.com", "tiktok.com",
              "pinterest.", "linkedin.com", "reddit.com/media")


def page_paragraphs(url, timeout=7, max_bytes=1_500_000):
    """The readable paragraphs of one web page (no scripts, menus, headers or footers)."""
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": SEARCH_UA, "Accept": "text/html,*/*;q=0.5",
                                               "Accept-Language": "en-IN,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if "html" not in (r.headers.get("Content-Type") or "text/html").lower():
            return []
        data = r.read(max_bytes)
        charset = r.headers.get_content_charset() or "utf-8"
    page = data.decode(charset, "replace")
    page = re.sub(r"(?is)<(script|style|noscript|nav|header|footer|aside|form|svg|button|select|template)\b.*?</\1\s*>",
                  " ", page)
    out = []
    for m in re.finditer(r"(?is)<(p|li|dd|blockquote)\b[^>]*>(.*?)</\1\s*>", page):
        txt = re.sub(r"\[(?:\d+|[a-z]|citation needed|edit)\]", "", " ".join(_plain(m.group(2)).split()))
        if len(txt) >= 40 and not _PAGE_JUNK.search(txt):
            out.append(txt)
    return out


def best_passage(query, paragraphs, limit=420):
    """The paragraph that covers the most words of the question, trimmed to its best sentences. (text, score)"""
    q = set(_tokens(query))
    if not q:
        return "", 0.0
    best, best_score = "", 0.0
    for idx, p in enumerate(paragraphs[:250]):
        hit = len(q & set(_tokens(p)))
        if not hit:
            continue
        score = hit / len(q) + min(len(p), 400) / 4000 - min(idx, 50) * 0.002
        if score > best_score:
            best, best_score = p, score
    if len(best) > limit:
        sents = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", best)
        hits = [len(q & set(_tokens(s))) for s in sents]
        i = max(range(len(sents)), key=lambda k: (hits[k], -k))
        out, j = sents[i], i + 1
        while j < len(sents) and len(out) + len(sents[j]) < limit:
            out += " " + sents[j]
            j += 1
        best = out if len(out) <= limit + 80 else out[:limit].rsplit(" ", 1)[0] + "..."
    return best, best_score


def read_web_answer(query, results, most=3, timeout=9):
    """Open the top few results at once, read them and return (passage, url) - or ("", "") if none answers well."""
    import concurrent.futures as cf
    urls = []
    for r in results:
        u = r.get("url", "")
        host = urlparse(u).netloc.lower()
        if u.startswith("http") and not any(s in host + urlparse(u).path for s in _PAGE_SKIP) \
                and not urlparse(u).path.lower().endswith(".pdf"):
            urls.append(u)
        if len(urls) >= most:
            break
    if not urls:
        return "", ""
    ex = cf.ThreadPoolExecutor(max_workers=len(urls))
    futs = {ex.submit(page_paragraphs, u): u for u in urls}
    best = ("", "", 0.0)
    try:
        for f in cf.as_completed(futs, timeout=timeout):
            url = futs[f]
            try:
                paras = f.result()
            except Exception as e:
                logger.info("couldn't read %s: %s", url, e)
                continue
            text, score = best_passage(query, paras)
            score += 0.05 * (most - urls.index(url))          # Google's own ranking still counts for something
            if text and score > best[2]:
                best = (text, url, score)
    except cf.TimeoutError:
        logger.info("page reading timed out for %r", query)
    finally:
        ex.shutdown(wait=False)
    return (best[0], best[1]) if best[2] >= 0.6 else ("", "")


def wolfram_short_answer(appid, query, timeout=12):
    """One-line answer from Wolfram|Alpha (free AppID from developer.wolframalpha.com). '' if it has none."""
    import urllib.error
    import urllib.request
    for kind in ("result", "spoken"):
        url = f"https://api.wolframalpha.com/v1/{kind}?" + urlencode({"appid": appid, "i": query, "units": "metric"})
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": SEARCH_UA}),
                                        timeout=timeout) as r:
                txt = r.read().decode("utf-8", "replace").strip()
            if txt:
                return txt
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise RuntimeError("Wolfram|Alpha refused the AppID - check it under Menu > Maths") from None
            if e.code in (400, 501):          # 501 = no short answer for this one; try the spoken form next
                continue
            raise
    return ""


# --------------------------------------------------------------- maths: complex arithmetic, logarithms, algebra
# All offline. With SymPy installed (pip install sympy, or Menu > Maths > Install) PAC gives exact answers and does
# real algebra: equations, systems, inequalities, simplify / expand / factorise, derivatives, integrals, limits.
# Without it PAC still does arithmetic, complex numbers and logarithms, and finds the real roots of a one-variable
# equation numerically. Spoken maths works too: "x squared plus 5 x plus 6 equals 0", "log base 2 of 64".
# Conventions, as on a school calculator: log = base 10, ln = natural log, i = the imaginary unit, e = 2.718...
class MathFail(Exception):
    """PAC couldn't do this one offline. need_sympy: it could, with SymPy installed. final: that IS the answer
    ("that divides by zero") - nothing to look up online."""

    def __init__(self, reason, need_sympy=False, final=False):
        super().__init__(reason)
        self.need_sympy = need_sympy
        self.final = final


_MATH_ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7,
             "eighth": 8, "ninth": 9, "tenth": 10}
_ORD_RE = r"(second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|\d+(?:st|nd|rd|th))"
_OPD = r"(pi\b|-?\d+(?:\.\d+)?|[a-z](?![a-z])|\((?:[^()]|\([^()]*\))*\))"     # a number, one letter or a (bracket)
_FUNC_NAMES = ("sin cos tan cot sec csc cosec asin acos atan acot asec acsc sinh cosh tanh asinh acosh atanh "
               "sqrt cbrt nroot log ln exp abs floor ceil re im arg conjugate gcd lcm factorial").split()
_MATH_WORDS = set(_FUNC_NAMES) | {"pi", "oo"}
_NOT_VARIABLES = {"is", "it", "be", "an", "as", "at", "to", "in", "on", "by", "of", "or", "if", "so", "we", "me",
                  "my", "do", "no", "up", "us", "am", "he", "go", "hi", "ok", "km", "cm", "mm", "kg", "mg", "ml",
                  "hr", "rs", "kb", "mb", "gb"}
_UNICODE_MATH = (("\u00d7", "*"), ("\u00f7", "/"), ("\u2212", "-"), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u207b\u00b9", "^(-1)"), ("\u00b2", "^2"), ("\u00b3", "^3"), ("\u2074", "^4"), ("\u221a", " sqrt "),
                 ("\u221b", " cbrt "), ("\u03c0", " pi "), ("\u221e", " oo "), ("\u2264", "<="), ("\u2265", ">="),
                 ("\u00b7", "*"), ("[", "("), ("]", ")"), ("{", "("), ("}", ")"),
                 ("\u00bd", "(1/2)"), ("\u00bc", "(1/4)"), ("\u00be", "(3/4)"), ("\u00b0", " degrees "),
                 ("**", "^"))


def _ord(word):
    return _MATH_ORD.get(word) or int(re.match(r"\d+", word).group())


# Spoken maths -> symbols, applied in this order (roots before "square", logs before "of" is dropped, ...).
_SPOKEN_MATH = [
    (r"\b(?:is )?greater than or equal to\b|\bat least\b", " >= "),
    (r"\b(?:is )?less than or equal to\b|\bat most\b", " <= "),
    (r"\b(?:is )?(?:greater|more|bigger) than\b", " > "),
    (r"\b(?:is )?(?:less|smaller) than\b", " < "),
    (r"\b(?:is equal to|is equals to|equal to|equals to|equals|equal|is equals)\b", " = "),
    (r"\b(?:open(?:ing)?|left)\s+(?:round\s+|curly\s+|square\s+)?(?:brackets?|parenthes[ie]s|parens?|braces?)\b"
     r"|\bbracket open\b", " ( "),
    (r"\b(?:close[ds]?|closing|right)\s+(?:round\s+|curly\s+|square\s+)?(?:brackets?|parenthes[ie]s|parens?|braces?)\b"
     r"|\bbracket close\b", " ) "),
    (r"\b(?:the\s+)?(?:square\s+root|sq\s+root|under\s*root|root\s+over)(?:\s+of)?\b", " sqrt "),
    (r"\b(?:the\s+)?cube\s+root(?:\s+of)?\b", " cbrt "),
    (r"\b(?:the\s+)?square\s+of\s*" + _OPD, r" (\1)^2 "),
    (r"\b(?:the\s+)?cube\s+of\s*" + _OPD, r" (\1)^3 "),
    (r"\b(?:the\s+)?" + _ORD_RE + r"\s+root\s+of\s*" + _OPD, lambda m: f" nroot({m.group(2)}, {_ord(m.group(1))}) "),
    (r"\broot\b(?=\s*[\d(a-z])", " sqrt "),
    (r"\b(?:natural\s+log(?:arithm)?|log(?:arithm)?\s+(?:to\s+)?(?:the\s+)?base\s+e)\b(?:\s+of)?", " ln "),
    (r"\blog(?:arithm)?\s+(?:to\s+)?(?:the\s+)?base\s+(\d+(?:\.\d+)?|[a-z](?![a-z]))\s+(?:of\s+)?" + _OPD,
     r" log(\2, \1) "),
    (r"\blog_?\{?(\d+)\}?\s*" + _OPD, r" log(\2, \1) "),            # log2(64), log_2 x, log10 1000
    (r"\blog_\{?([a-z])\}?\s*" + _OPD, r" log(\2, \1) "),
    (r"\blog(?:arithm)?\b(?:\s+of)?", " log "),
    (r"\bln\b(?:\s+of)?", " ln "),
    (r"\banti\s*-?\s*log(?:arithm)?\s+(?:of\s+)?" + _OPD, r" 10^(\1) "),
    (r"\b(?:the\s+)?exponential(?:\s+of)?\b", " exp "),
    (r"\b(?:sin|sine)\s+inverse\b|\binverse\s+(?:sin|sine)\b|\barc\s*sine?\b", " asin "),
    (r"\b(?:cos|cosine)\s+inverse\b|\binverse\s+(?:cos|cosine)\b|\barc\s*cos(?:ine)?\b", " acos "),
    (r"\b(?:tan|tangent)\s+inverse\b|\binverse\s+(?:tan|tangent)\b|\barc\s*tan(?:gent)?\b", " atan "),
    (r"\bsine\b", " sin "), (r"\bcosine\b", " cos "), (r"\btangent\b", " tan "), (r"\bcosecant\b", " cosec "),
    (r"\bsecant\b", " sec "), (r"\bcotangent\b", " cot "),
    (r"\b(sin|cos|tan|cot|sec|cosec|csc|asin|acos|atan|sqrt|cbrt|exp|abs)\s+of\b", r" \1 "),
    (r"\b(?:absolute value|modulus|mod)\s+of\s*" + _OPD, r" abs(\1) "),
    (r"(\d+(?:\.\d+)?)\s*(?:degrees?|deg)\b", r" (\1*pi/180) "),
    (r"\b(?:raised\s+)?to\s+the\s+power\s+of\b|\braised\s+to\s+the\s+power\b|\bto\s+the\s+power\b|\braised\s+to\b"
     r"|\bpower\b", " ^ "),
    (r"\bto\s+the\s+" + _ORD_RE + r"(?:\s+power)?\b", lambda m: f" ^ {_ord(m.group(1))} "),
    (r"\bto\s+the\b(?=\s*[\da-z(-])", " ^ "),                       # "e to the x"
    (r"\bsquared?\b", " ^2 "),                                      # "x squared", Indian "x square"
    (r"\bcubed?\b", " ^3 "),
    (r"\b(?:the\s+)?factorial\s+(?:of\s+)?" + _OPD, r" (\1)! "),
    (_OPD + r"\s*factorial\b", r" (\1)! "),
    (r"(\d+(?:\.\d+)?)\s*(?:%|percent\b|per\s+cent\b)\s*of\b", r" (\1/100)* "),
    (r"(\d+(?:\.\d+)?)\s*(?:percent|per\s+cent)\b", r" (\1/100) "),
    (r"(\d+(?:\.\d+)?)\s*%(?=\s*(?:$|[+\-*/)=<>]))", r" (\1/100) "),
    (r"\bmod(?:ulo)?\b", " % "),
    (r"\b(?:multiplied\s+by|times|into|multiply)\b", " * "),
    (r"\b(?:divided\s+by|divide\s+by|over)\b", " / "),
    (r"(\d)\s+by\s+(?=\d)", r"\1 / "),                              # Indian "10 by 2"
    (r"\bplus\b", " + "),
    (r"\b(?:minus|negative)\b", " - "),
    (r"\binfinity\b", " oo "),
    (r"\bpie\b", " pi "),
]
_SPOKEN_MATH = [(re.compile(p), r) for p, r in _SPOKEN_MATH]
_NUMWORD_RUN = re.compile(r"\b(?:(?:%s)\b(?:\s+|-)?)+" % "|".join(sorted(NUM_WORDS, key=len, reverse=True)))
_CNUM = r"-?\s*\d+(?:\.\d+)?\s*[+-]\s*(?:\d+(?:\.\d+)?\s*)?\*?\s*i\b"


def to_math(text, x_is_times=False):
    """What you typed or said -> a maths expression, e.g. 'log base 2 of 64' -> 'log(64, 2)'."""
    s = " " + text.lower() + " "
    for a, b in _UNICODE_MATH:
        s = s.replace(a, b)
    s = _NUMWORD_RUN.sub(lambda m: " " + str(words_to_int(m.group().replace("-", " ").split())) + " ", s)
    s = re.sub(r"(\d)\s+point\s+(\d)", r"\1.\2", s)
    for pat, rep in _SPOKEN_MATH:
        s = pat.sub(rep, s)
    if x_is_times:                                   # "5 x 3" in plain arithmetic means 5 times 3
        s = re.sub(r"(?<=[\d)])\s+x\s+(?=[\d(])", " * ", s)
    s = re.sub(r"\b(?:the|of|value)\b", " ", s)
    s = re.sub(r"\b(%s)\s+\(" % "|".join(_FUNC_NAMES), r"\1(", s)
    s = re.sub(r"\b(log|nroot)\(\(([^()]*)\),", r"\1(\2,", s)
    s = re.sub(r"\s+", " ", s).strip()
    m = re.fullmatch(rf"({_CNUM})\s*([*/])\s*({_CNUM})", s)   # spoken "2 + 3i times 4 - 5i": two whole numbers
    if m:
        s = f"({m.group(1)}) {m.group(2)} ({m.group(3)})"
    return s


def _wordy(s):
    """True when words are left that aren't maths - a word problem, not an expression."""
    for w in re.findall(r"[a-z]+", s):
        if w in _MATH_WORDS or len(w) == 1:
            continue
        if len(w) == 2 and w not in _NOT_VARIABLES:
            continue                                  # "xy" = x times y
        return True
    return False


def _safe_math(s):
    """Only maths characters and maths words - so nothing but maths ever reaches the parser."""
    return bool(re.fullmatch(r"[0-9a-z+\-*/^().,!%<>=; ]*", s)) and not re.search(r"\.(?!\d)", s) and not _wordy(s)


def _too_big(s):
    """Refuse numbers that would eat all the memory (9^9^9, 10^1000000, 100000!) - letters are fine."""
    for b, c in re.findall(r"\^\s*\(?\s*(\d+(?:\.\d+)?)\s*\^\s*\(?\s*(\d+(?:\.\d+)?)", s):
        try:
            if float(b) ** float(c) > 100000:
                return True
        except OverflowError:
            return True
    if any(float(n) > 100000 for n in re.findall(r"\^\s*\(?\s*(\d+(?:\.\d+)?)", s)):
        return True
    return any(float(n) > 5000 for n in re.findall(r"(\d+(?:\.\d+)?)\s*\)?\s*!", s))


def _pretty_input(s):
    """The problem as PAC understood it, written the way you'd write it."""
    s = re.sub(r"\blog\(([^(),]+),\s*([^()]+)\)", r"log_\2(\1)", s)
    s = re.sub(r"\bnroot\(([^(),]+),\s*(\d+)\)", r"\2√(\1)", s)
    s = re.sub(r"\bsqrt\s*", "√", s).replace("cbrt", "∛").replace("pi", "π").replace("oo", "∞")
    s = re.sub(r"\s*\*\s*", "·", s)
    s = re.sub(r"(\d)·(?=[a-zπ√(])", r"\1", s)
    s = re.sub(r"(\d)\s+(?=[a-z](?![a-z]))", r"\1", s)                    # spoken "5 x" -> 5x
    s = re.sub(r"\(\s+", "(", re.sub(r"\s+\)", ")", s)).replace(" ; ", ",  ")
    return re.sub(r"\s*\^\s*", "^", s)


_ASK = r"(?:(?:find|what is|what's|whats|what are|calculate|compute|get|evaluate|work out|determine)\s+)?(?:the\s+)?"
_MATH_OPS = [
    (rf"(?:solve|{_ASK}(?:solutions?|roots?|zeros?|zeroes)\s+of)\b(?:\s+for\s+(?P<v>[a-z])\b)?(?:\s+the)?"
     r"(?:\s+(?:following\s+)?(?:equations?|inequalit(?:y|ies)|system(?:\s+of\s+equations)?|expression|problem|question))?"
     r"(?:\s+for\s+(?P<v2>[a-z])\b)?[\s:,]*", "solve"),
    (r"(?:find|what is|what's|whats|calculate|compute|get|determine|work out)\s+(?:the\s+)?(?:value\s+of\s+)?"
     r"(?P<v>[a-z])\b\s*(?:if|when|where|given(?:\s+that)?|such that|from|for)?[\s:,]*"
     r"(?=.*(?:[=<>]|\bequals?\b|\bequal to\b|\bgreater\b|\bless\b))", "solve"),
    (rf"{_ASK}(?:simplify|simplification\s+of)\b[\s:,]*", "simplify"),
    (rf"{_ASK}(?:expand|expansion\s+of)\b[\s:,]*", "expand"),
    (rf"(?:factori[sz]e|factor|{_ASK}(?:prime\s+)?(?:factors|factori[sz]ation)\s+of)\b[\s:,]*", "factor"),
    (rf"{_ASK}(?P<k>l\.?\s?c\.?\s?m\.?|least common multiple|lowest common multiple|h\.?\s?c\.?\s?f\.?|g\.?\s?c\.?\s?d\.?|"
     r"highest common factor|greatest common (?:divisor|factor))\s+of\b[\s:,]*", "gcdlcm"),
    (rf"{_ASK}(?P<ord>first|second|third|fourth|1st|2nd|3rd|4th)?\s*(?:derivative|differentiation|"
     r"differential coefficient)\s+of\b[\s:,]*", "diff"),
    (r"(?:differentiate|derive)\b(?:\s+(?P<twice>twice))?[\s:,]*", "diff"),
    (r"d(?:\^?(?P<n>\d))?\s*/\s*d(?P<v>[a-z])(?:\^?\d)?\s*(?:of\s+)?", "diff"),
    (rf"{_ASK}(?:definite\s+|indefinite\s+)?(?:integral|integration|anti-?derivative)\s+of\b[\s:,]*", "integrate"),
    (r"integrate\b[\s:,]*", "integrate"),
    (rf"{_ASK}limit\s+of\b[\s:,]*|lim\b[\s:,]*", "limit"),
    (rf"{_ASK}(?:modulus|absolute\s+value|magnitude|mod)\s+of\b[\s:,]*", "abs"),
    (rf"{_ASK}(?:argument|arg|amplitude|phase)\s+of\b[\s:,]*", "arg"),
    (rf"{_ASK}(?:complex\s+)?conjugate\s+of\b[\s:,]*", "conjugate"),
    (rf"{_ASK}real\s+part\s+of\b[\s:,]*", "re"),
    (rf"{_ASK}imaginary\s+part\s+of\b[\s:,]*", "im"),
    (rf"{_ASK}polar\s+form\s+of\b[\s:,]*", "polar"),
    (r"(?:convert|write|express|put)\s+(?=.*\s(?:in|to|into)\s+polar(?:\s+form)?$)", "polar"),
    (r"(?:is it true that|is|does|do|check(?:\s+(?:if|whether|that))?|verify(?:\s+that)?|true or false)\s+"
     r"(?=.*(?:[=<>]|\bequals?\b|\bequal to\b))", "solve"),
    (r"(?:calculate|compute|evaluate|work out|find|what is|what's|whats|how much is|what does|what do)\b"
     r"(?:\s+the)?(?:\s+value\s+of)?[\s:,]*", "eval"),
]
_MATH_OPS = [(re.compile(p), op) for p, op in _MATH_OPS]
_MATH_LEAD = re.compile(r"^(?:(?:hey|ok|okay|please|kindly|pac|pack|pak|so|now|then|also|quickly|can you|could you|"
                        r"would you|will you|help me|i want to|i need to|i want you to|let'?s|lets|i'd like to|"
                        r"tell me|show me|give me|just)\b[\s,:]*)+")
_NOT_MATH_START = re.compile(r"^(?:type|write|dictate|send|message|text|whatsapp|launch|start|run|search|google|"
                             r"youtube|play|remind|set|note|take|remember|learn|convert|go|visit|ask|claude|call|"
                             r"delete|remove|read|review|list|show|switch|turn|use|"
                             r"open(?!\s+(?:round\s+|square\s+|curly\s+)?(?:brackets?|parenthes|parens?|braces?))|"
                             r"check(?!\s+(?:if|whether|that)\b))\b")
_STRONG_EVAL = re.compile(r"^(?:calculate|compute|evaluate|work out)\b")
_HAS_OPERATOR = re.compile(r"[=<>^*/+%!]|\d\s*-\s*[\d(a-z]|\b(?:sqrt|cbrt|nroot|log|ln|exp|sin|cos|tan|cot|sec|csc|"
                           r"cosec|asin|acos|atan|abs)\b|\d\s*i\b|\bi\s*\^")


def parse_math_request(text):
    """Is this a maths problem? -> {"op", "expr", "var", ...} or None. Regexes only: it is cheap, so it can run on
    every sentence; the actual maths happens later, on another thread."""
    s = " ".join(text.strip().split())
    s = re.sub(r"(?i)\s+(?:please|for me|pac|pack|now|quickly)\s*[?!.]*$", "", s)
    s = re.sub(r"\?+$|(?<=[a-zA-Z]{2})!+$|(?<=\D)\.$", "", s).strip()
    low = _MATH_LEAD.sub("", s.lower()).strip()
    if not low or (_NOT_MATH_START.match(low) and not re.match(r"convert\s.+\spolar(?:\s+form)?$", low)):
        return None
    op, body, info = None, low, {}
    for pat, name in _MATH_OPS:
        m = pat.match(low)
        if m and (name != "eval" or m.end() < len(low)):
            op, body, info = name, low[m.end():].strip(), {k: v for k, v in m.groupdict().items() if v}
            break
    if not body:
        return None
    req = {"op": op or "auto", "text": s, "var": info.get("v") or info.get("v2"), "order": 1}
    if info.get("ord") or info.get("twice") or info.get("n"):
        req["order"] = {"first": 1, "1st": 1, "second": 2, "2nd": 2, "twice": 2, "third": 3, "3rd": 3,
                        "fourth": 4, "4th": 4}.get(info.get("ord") or info.get("twice"), int(info.get("n") or 1))
    if op == "gcdlcm":
        nums = [int(n) for n in re.findall(r"\d+", body)]
        if len(nums) < 2 or _wordy(re.sub(r"\band\b|,", " ", body)):
            return None
        req.update(op="lcm" if info["k"].replace(".", "").replace(" ", "")[0] in "l" else "gcd", nums=nums,
                   expr=" and ".join(map(str, nums)))
        return req
    # what the problem says about itself: "... for y", "... with respect to t", "... from 0 to 3", "... as x -> 0"
    m = re.search(r"\s+(?:in|to|into)\s+polar(?:\s+form)?$", body)
    if m:
        body, req["op"] = body[:m.start()], "polar"
    if req["op"] in ("auto", "eval", "simplify", "expand", "factor", "solve"):
        m = re.search(r"[\s,]+(?:where|when|if|at|with|given|for|putting|substituting)\s+"
                      r"((?:[a-z]\s*(?:=|equals|is)\s*[^,;=]+?)(?:\s*(?:,|;|\band\b)\s*[a-z]\s*(?:=|equals|is)\s*[^,;=]+?)*)$",
                      body)
        if m and (req["op"] != "solve" or len(re.findall(r"=|\bequals\b", body[:m.start()])) >= 1):
            subs = re.findall(r"([a-z])\s*(?:=|equals|is)\s*([^,;=]+?)(?=\s*(?:,|;|\band\b|$))", m.group(1))
            req["subs"] = [(k, to_math(v)) for k, v in subs]
            body = body[:m.start()]
    if req["op"] in ("solve", "auto", "eval"):
        m = re.search(r"[\s,]+(?:solve\s+)?for\s+([a-z])$", body)
        if m:
            body, req["var"] = body[:m.start()], m.group(1)
        body = re.sub(r"^(?:if|when|where|given(?:\s+that)?)\s+", "", body)
    if req["op"] in ("diff", "integrate", "limit"):
        m = re.search(r"\s+(?:with respect to|w\.?\s?r\.?\s?t\.?)\s+([a-z])$", body)
        if m:
            body, req["var"] = body[:m.start()], m.group(1)
    if req["op"] == "integrate":
        for _ in range(2):
            m = re.search(r"\s*\bd([a-z])$", body)
            if m:
                body, req["var"] = body[:m.start()], req["var"] or m.group(1)
            m = re.search(r"\s+(?:from|between)\s+(.+?)\s+(?:to|and)\s+(.+)$", body)
            if m:
                body, req["limits"] = body[:m.start()], (to_math(m.group(1)), to_math(m.group(2)))
    if req["op"] == "limit":
        m = re.search(r"\s+(?:as|when|where)\s+([a-z])\s*(?:approaches|tends to|goes to|->|→|=)\s*(.+)$", body) \
            or re.search(r"^(?:as\s+)?([a-z])\s*(?:approaches|tends to|goes to|->|→)\s*(\S+)\s+(?:of\s+)?", body)
        if not m:
            return None if op is None else {**req, "expr": "", "bad": "say what x approaches, e.g. as x approaches 0"}
        req["var"], req["point"] = m.group(1), to_math(m.group(2))
        body = body[:m.start()] if m.start() > 0 else body[m.end():]
    if req["op"] == "diff":
        body = re.sub(r"^(?:the\s+)?(?:function\s+)?", "", body)
    expr = to_math(body, x_is_times=req["op"] in ("eval", "auto"))
    if req["op"] in ("solve", "auto", "eval") and len(re.findall(r"<=|>=|=|<|>", expr)) >= 2:
        expr = re.sub(r"\s+and\s+", " ; ", expr)          # "x + y = 10 and x - y = 2": a system
    req["expr"] = expr
    wordy = not _safe_math(expr)
    if req["op"] == "auto":
        if wordy or not _HAS_OPERATOR.search(expr):
            return None
        letters = set(re.findall(r"(?<![a-z])[a-z](?![a-z])",
                                 re.sub(r"\b(?:%s)\b" % "|".join(_MATH_WORDS), " ", expr))) - {"i", "e"}
        if letters and not re.search(r"[=<>]", expr) and not req.get("subs"):
            return None                                  # "2x + 3" on its own: nothing to do
        req["op"] = "eval"
    elif op == "eval":
        if wordy and not _STRONG_EVAL.match(low):
            return None                                  # "what is the capital of France" - not maths
        if not wordy and not _HAS_OPERATOR.search(expr) and not re.search(r"\d", expr) and expr not in ("pi", "e"):
            return None
    if wordy:
        req["wordy"] = True
    elif _too_big(expr):
        req["bad"] = "that number is too big to work out"
    return req


# ---- numbers in, numbers out
def _fmt_real(x, sig=10):
    if x != x:
        return "undefined"
    if x in (math.inf, -math.inf):
        return "∞" if x > 0 else "-∞"
    if abs(x) < 1e-12:
        return "0"
    if abs(x - round(x)) < 1e-9 * max(1.0, abs(x)) and abs(x) < 1e15:
        return str(int(round(x)))
    s = f"{x:.{sig}g}"
    if "e" in s:
        mant, exp = s.split("e")
        return f"{mant} × 10^{int(exp)}"
    return s


def _fmt_num(z, sig=10):
    """1.5, 3 - 4i, i, -2i ... (a real number stays real)."""
    z = complex(z)
    re_, im_ = z.real, z.imag
    if abs(im_) <= 1e-12 * max(1.0, abs(re_)):
        return _fmt_real(re_, sig)
    ims = _fmt_real(abs(im_), sig)
    ims = "i" if ims == "1" else ims + "i"
    if abs(re_) <= 1e-12 * max(1.0, abs(im_)):
        return ("-" if im_ < 0 else "") + ims
    return f"{_fmt_real(re_, sig)} {'-' if im_ < 0 else '+'} {ims}"


def _polar_line(z):
    z = complex(z)
    return (f"Polar form: |z| = {_fmt_real(abs(z), 6)}, angle = {_fmt_real(math.degrees(cmath.phase(z)), 6)}° "
            f"({_fmt_real(cmath.phase(z), 6)} rad)")


def speak_math(s):
    """'x^2 - 5x + 6 = 0' -> 'x squared minus 5 x plus 6 equals 0' (for the voice)."""
    t = re.sub(r"log_(\w+)\(", r" log base \1 of (", s)
    t = re.sub(r"(\d+)√", r" \1th root of ", t)
    t = t.replace("√", " root ").replace("∛", " cube root ").replace("× 10^", " times 10 to the power ")
    t = re.sub(r"\^(?:2|\(2\))(?![\d.])", " squared ", t)
    t = re.sub(r"\^(?:3|\(3\))(?![\d.])", " cubed ", t)
    t = t.replace(")(", ") times (")
    for a, b in (("^", " to the power "), ("π", " pi "), ("∞", " infinity "), ("±", " plus or minus "),
                 ("≈", " about "), ("≤", " less than or equal to "), ("≥", " greater than or equal to "),
                 ("<=", " less than or equal to "), (">=", " greater than or equal to "), ("<", " less than "),
                 (">", " greater than "), ("·", " times "), ("*", " times "), ("/", " over "), ("=", " equals "),
                 ("+", " plus "), ("-", " minus "), ("°", " degrees "), ("|", " "), ("(", " "), (")", " "),
                 ("[", " "), ("]", " "), (";", ", "), ("!", " factorial ")):
        t = t.replace(a, b)
    t = re.sub(r"(\d)(?=[a-z])", r"\1 ", t)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"\s+,", ",", t).strip(" ,")


# ---- without SymPy: complex-number arithmetic and real roots, in plain Python
def _real_part(z):
    z = complex(z)
    if abs(z.imag) > 1e-9 * max(1.0, abs(z.real)):
        raise ValueError("needs a real number")
    return z.real


def _factorial(n):
    n = _real_part(n)
    if n < 0 or abs(n - round(n)) > 1e-9:
        raise ValueError("factorial needs a whole number that isn't negative")
    return math.factorial(int(round(n)))


def _nroot(z, n):
    n = int(_real_part(n))
    z = complex(z)
    if abs(z.imag) < 1e-15 and z.real < 0 and n % 2:
        return -((-z.real) ** (1.0 / n))           # the real cube root of -8 is -2
    return z ** (1.0 / n)


_NUM_FUNCS = {
    "sin": cmath.sin, "cos": cmath.cos, "tan": cmath.tan, "cot": lambda z: 1 / cmath.tan(z),
    "sec": lambda z: 1 / cmath.cos(z), "csc": lambda z: 1 / cmath.sin(z), "cosec": lambda z: 1 / cmath.sin(z),
    "asin": cmath.asin, "acos": cmath.acos, "atan": cmath.atan, "acot": lambda z: cmath.atan(1 / z),
    "asec": lambda z: cmath.acos(1 / z), "acsc": lambda z: cmath.asin(1 / z),
    "sinh": cmath.sinh, "cosh": cmath.cosh, "tanh": cmath.tanh, "asinh": cmath.asinh, "acosh": cmath.acosh,
    "atanh": cmath.atanh, "sqrt": cmath.sqrt, "cbrt": lambda z: _nroot(z, 3), "nroot": _nroot,
    "log": lambda z, b=10: cmath.log(z) / cmath.log(b), "ln": cmath.log, "exp": cmath.exp, "abs": abs,
    "arg": cmath.phase, "re": lambda z: complex(z).real, "im": lambda z: complex(z).imag,
    "conjugate": lambda z: complex(z).conjugate(), "floor": lambda z: math.floor(_real_part(z)),
    "ceil": lambda z: math.ceil(_real_part(z)),
    "factorial": _factorial,
    "gcd": lambda a, b: math.gcd(int(_real_part(a)), int(_real_part(b))),
    "lcm": lambda a, b: abs(int(_real_part(a)) * int(_real_part(b))) // (math.gcd(int(_real_part(a)),
                                                                                 int(_real_part(b))) or 1),
}
_NUM_CONST = {"pi": math.pi, "e": math.e, "i": 1j, "oo": math.inf}
_FN_ALT = "|".join(sorted(_NUM_FUNCS, key=len, reverse=True))


def _py_math(s):
    """'2x^2 + sin x + 3(4i)' -> '2*x**2 + sin(x) + 3*(4*i)' for the plain-Python evaluator."""
    s = re.sub(r"(\d+(?:\.\d+)?|\b[a-z]\b)\s*!", r"factorial(\1)", s)
    s = re.sub(r"(\((?:[^()]|\([^()]*\))*\))\s*!", r"factorial\1", s)
    s = re.sub(rf"\b({_FN_ALT})\s+(-?(?:[\d.]+[a-z]?|[a-z])\b(?:\s*\^\s*-?[\d.]+)?)", r"\1(\2)", s)   # sin 2x
    s = re.sub(r"\b([a-z]{2,3})\b", lambda m: m.group(1) if m.group(1) in _NUM_FUNCS or m.group(1) in _NUM_CONST
               else "*".join(m.group(1)), s)                          # "xy" -> x*y
    s = re.sub(r"(\d)\s*(?=[a-z(])", r"\1*", s)                       # 2x, 2(...), 4i
    s = re.sub(r"\)\s*(?=[\w(])", ")*", s)                            # (...)(...), (...)x
    s = re.sub(rf"\b(?!(?:{_FN_ALT})\b)([a-z])\s*(?=\()", r"\1*", s)   # x(...) -> x*(...)
    s = re.sub(r"\b([a-z])\s+(?=[a-z(\d])", r"\1*", s)                # "x y" -> x*y
    return s.replace("^", "**")


def _num_compile(s):
    tree = ast.parse(_py_math(s), mode="eval")

    def ev(n, env):
        if isinstance(n, ast.Expression):
            return ev(n.body, env)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return n.value
        if isinstance(n, ast.Name):
            if n.id in env:
                return env[n.id]
            if n.id in _NUM_CONST:
                return _NUM_CONST[n.id]
            raise MathFail(f"I don't know what {n.id} is")
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            a, b = ev(n.left, env), ev(n.right, env)
            if isinstance(n.op, ast.Pow) and abs(b) > 10000:
                raise OverflowError("number too large")
            if isinstance(n.op, ast.Mod):
                return _real_part(a) % _real_part(b)
            if isinstance(n.op, ast.Pow) and isinstance(a, (int, float)) and a < 0 and isinstance(b, float) \
                    and not b.is_integer():
                return complex(a) ** b                                    # (-8)^0.5 is complex, not an error
            return _OPS[type(n.op)](a, b)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            v = ev(n.operand, env)
            return -v if isinstance(n.op, ast.USub) else v
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in _NUM_FUNCS and not n.keywords:
            return _NUM_FUNCS[n.func.id](*[ev(a, env) for a in n.args])
        raise MathFail("I couldn't read that as maths")
    return lambda **env: ev(tree, env)


def _real_roots(f, most=12):
    """Real x where f(x) = 0, found by scanning -20000..20000 and narrowing in on every sign change."""
    def g(x):
        try:
            v = complex(f(x))
        except Exception:                      # outside the domain (log of -1, 1/0, ...): no value here
            return None
        if v != v or abs(v.imag) > 1e-9 * (1 + abs(v.real)) or abs(v.real) == math.inf:
            return None
        return v.real
    grid = [k * 0.01 for k in range(2001)] + [20 + k * 0.1 for k in range(1, 1801)] + \
           [200 + k for k in range(1, 1801)] + [2000 + k * 10 for k in range(1, 1801)]
    pts = sorted(set([-p for p in grid] + grid))
    vals = [g(p) for p in pts]
    roots = []

    def add(r):
        r = round(r) if abs(r - round(r)) < 1e-9 else float(f"{r:.12g}")
        if all(abs(r - q) > 1e-7 * max(1, abs(r)) for q in roots):
            roots.append(r)
    for (a, fa), (b, fb) in zip(zip(pts, vals), zip(pts[1:], vals[1:])):
        if fa is None or fb is None:
            continue
        if fa == 0:
            add(a)
        elif fa * fb < 0:
            lo, hi, flo = a, b, fa
            for _ in range(80):
                mid = (lo + hi) / 2
                fm = g(mid)
                if fm is None:
                    break
                if (fm < 0) == (flo < 0):
                    lo, flo = mid, fm
                else:
                    hi = mid
            r = (lo + hi) / 2
            fr = g(r)
            if fr is not None and abs(fr) < 1e-6:            # a real root, not a jump like 1/x at 0
                add(r)
        if len(roots) >= most:
            break
    if vals[-1] == 0:
        add(pts[-1])
    return sorted(roots)


def _split_rel(s):
    """'2x + 1 >= 7' -> ('2x + 1', '>=', '7')"""
    m = re.search(r"<=|>=|=|<|>", s)
    if not m:
        return s.strip(), None, None
    return s[:m.start()].strip(), m.group(), s[m.end():].strip()


def _split_system(s):
    parts, depth, cur = [], 0, ""
    for ch in s:
        depth += (ch == "(") - (ch == ")")
        if ch in ",;" and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def _numeric_math(req):
    """The answer without SymPy (arithmetic, complex numbers, logs, real roots of one equation)."""
    op, expr = req["op"], req["expr"]
    if op == "eval" and len(re.findall(r"<=|>=|=|<|>", expr)) == 1:
        op = "solve"
    if op in ("eval", "abs", "arg", "conjugate", "re", "im", "polar"):
        if re.search(r"[=<>]", expr):
            raise MathFail("that needs the algebra engine", need_sympy=True)
        try:
            env = {k: _num_compile(v)() for k, v in req.get("subs", [])}
            raw = _num_compile(expr)(**env)
            if isinstance(raw, int) and op == "eval" and abs(raw) >= 10 ** 15:      # exact, however long
                digits = str(abs(raw))
                shown = ("-" if raw < 0 else "") + (digits if len(digits) <= 300 else
                                                    f"{digits[0]}.{digits[1:7]} × 10^{len(digits) - 1}")
                return {"lines": [f"Problem: {_pretty_input(expr)}", f"Answer: {shown}  ({len(digits)} digits)"],
                        "say": f"It's a {len(digits)} digit number, about {digits[0]} point {digits[1:3]} times "
                               f"10 to the power {len(digits) - 1}."}
            val = complex(raw)
        except MathFail:
            raise
        except (SyntaxError, TypeError):
            raise MathFail("I couldn't read that as maths") from None
        except ZeroDivisionError:
            raise MathFail("that divides by zero, so it's undefined", final=True) from None
        except OverflowError:
            raise MathFail("that number is too big to work out", final=True) from None
        except ValueError as e:
            raise MathFail("that's undefined" if "domain" in str(e) else str(e), final=True) from None
        if val != val:
            raise MathFail("that's undefined", final=True)
        lines = [f"Problem: {_pretty_input(expr)}"]
        if op == "eval":
            ans = _fmt_num(val)
            lines.append(f"Answer: {ans}")
            if abs(val.imag) > 1e-12 * max(1.0, abs(val.real)):
                lines.append(_polar_line(val))
            return {"lines": lines, "say": f"The answer is {speak_math(_fmt_num(val, 6))}."}
        if op == "abs":
            r = abs(val)
            lines.append(f"Modulus |z| = {_fmt_real(r)}")
            return {"lines": lines, "say": f"The modulus is {speak_math(_fmt_real(r, 6))}."}
        if op == "arg":
            th = cmath.phase(val)
            lines.append(f"Argument = {_fmt_real(th)} rad = {_fmt_real(math.degrees(th))}°")
            return {"lines": lines, "say": f"The argument is {speak_math(_fmt_real(math.degrees(th), 5))} degrees."}
        if op == "conjugate":
            c = _fmt_num(val.conjugate())
            lines.append(f"Conjugate: {c}")
            return {"lines": lines, "say": f"The conjugate is {speak_math(c)}."}
        if op in ("re", "im"):
            part = _fmt_real(val.real if op == "re" else val.imag)
            lines.append(f"{'Real' if op == 're' else 'Imaginary'} part: {part}")
            return {"lines": lines, "say": f"The {'real' if op == 're' else 'imaginary'} part is {speak_math(part)}."}
        lines.append(_polar_line(val))
        r, th = _fmt_real(abs(val), 6), _fmt_real(math.degrees(cmath.phase(val)), 6)
        return {"lines": lines, "say": f"In polar form that's {speak_math(r)} at an angle of {speak_math(th)} degrees."}
    if op == "solve":
        if req.get("subs"):
            raise MathFail("that needs the algebra engine", need_sympy=True)
        rels = _split_system(expr)
        if len(rels) != 1:
            raise MathFail("systems of equations need the algebra engine", need_sympy=True)
        lhs, rel, rhs = _split_rel(rels[0])
        if rel != "=":
            raise MathFail("inequalities need the algebra engine", need_sympy=True)
        letters = set(re.findall(r"\b[a-z]\b", re.sub(r"\b(?:%s)\b" % _FN_ALT, " ", _py_math(lhs + " + " + rhs)))) \
            - set(_NUM_CONST)
        if len(letters) != 1:
            raise MathFail("that needs the algebra engine", need_sympy=True)
        v = letters.pop()
        try:
            fl, fr = _num_compile(lhs), _num_compile(rhs)
        except SyntaxError:
            raise MathFail("I couldn't read that as maths") from None
        roots = _real_roots(lambda x: fl(**{v: x}) - fr(**{v: x}))
        lines = [f"Problem: {_pretty_input(expr)}"]
        if not roots:
            lines.append("No real solution found between -20000 and 20000.")
            return {"lines": lines, "say": "I couldn't find a real solution.",
                    "hint": "(Install the algebra engine - Menu > Maths - for exact answers and complex roots.)"}
        shown = [_fmt_real(r) for r in roots]
        lines.append("Answer: " + "  or  ".join(f"{v} = {s}" for s in shown) + "   (numerical, real roots only)")
        return {"lines": lines, "say": f"{v} equals {' or '.join(speak_math(_fmt_real(r, 6)) for r in roots[:6])}.",
                "hint": "(Install the algebra engine - Menu > Maths - for exact answers and complex roots.)"}
    raise MathFail("that needs the algebra engine", need_sympy=True)


# ---- with SymPy: exact answers and real algebra
_SYMPY = None


def _sympy():
    """(sympy, parse) when SymPy is installed, else None. Imported on first use so PAC still starts quickly."""
    global _SYMPY
    if _SYMPY is None:
        try:
            import sympy as S
            from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                                    parse_expr, standard_transformations)
        except Exception as e:
            logger.info("SymPy not available (%s) - plain-Python maths only", e)
            _SYMPY = False
            return None
        tr = standard_transformations + (implicit_multiplication_application, convert_xor)
        names = {"i": S.I, "e": S.E, "pi": S.pi, "oo": S.oo, "ln": S.log, "log": lambda x, b=10: S.log(x, b),
                 "sqrt": S.sqrt, "cbrt": S.cbrt, "nroot": S.root, "exp": S.exp, "abs": S.Abs, "arg": S.arg,
                 "re": S.re, "im": S.im, "conjugate": S.conjugate, "factorial": S.factorial, "floor": S.floor,
                 "ceil": S.ceiling, "gcd": S.gcd, "lcm": S.lcm, "cosec": S.csc, "csc": S.csc}
        for n in ("sin cos tan cot sec asin acos atan acot asec acsc sinh cosh tanh asinh acosh atanh").split():
            names[n] = getattr(S, n)

        def parse(text):
            if not _safe_math(text):
                raise MathFail("I couldn't read that as maths")
            try:
                return parse_expr(text, local_dict=dict(names), transformations=tr)
            except MathFail:
                raise
            except Exception:
                raise MathFail("I couldn't read that as maths") from None
        _SYMPY = (S, parse)
    return _SYMPY or None


def reset_sympy():
    global _SYMPY
    _SYMPY = None


def _pretty(S, v):
    """A SymPy answer written for people: x^2 - 5x + 6, 3 + 4i, √2, π/6, log_2(x), e^x."""
    if getattr(v, "is_number", False) and not v.free_symbols:
        if v.has(S.CRootOf) or v.has(S.Float) or len(str(v)) > 90:
            return _fmt_num(complex(S.N(v, 15)))
        if v.has(S.I):
            re_, im_ = S.re(v), S.im(v)
            if im_ != 0 and re_.is_number and im_.is_number and len(str(re_)) + len(str(im_)) < 60:
                r, i = _pretty(S, re_), _pretty(S, abs(im_))
                i = "i" if i == "1" else (i + "i" if re.fullmatch(r"[\d.]+|π|e", i) else f"({i})i")
                return ("-" if im_ < 0 else "") + i if re_ == 0 else f"{r} {'-' if im_ < 0 else '+'} {i}"
    s = S.sstr(v)
    s = re.sub(r"\blog\(([^()]+)\)/log\((\d+)\)", r"log_\2(\1)", s)
    s = re.sub(r"\blog\(", "ln(", s)                   # SymPy's log is the natural log; PAC's 'log' is base 10
    s = re.sub(r"\bexp\(", "e^(", s)
    s = s.replace("**", "^").replace("sqrt(", "√(")
    s = re.sub(r"√\(([\w.]+)\)", r"√\1", s)
    s = re.sub(r"e\^\(([\w.]+)\)", r"e^\1", s)
    s = re.sub(r"\bE\b", "e", s)
    s = re.sub(r"\bI\b", "i", s)
    s = re.sub(r"\bpi\b", "π", s).replace("zoo", "∞").replace("oo", "∞")
    s = s.replace(")*(", ")(")
    s = re.sub(r"(?<![\^.\d])(\d+)\*(?=[a-zA-Zπ√(])", r"\1", s)       # 3*x -> 3x, but x^3*cos(x) keeps its dot
    return s.replace("*", "·")


def _approx(S, v):
    """'  (≈ 1.414213562)' when an exact answer isn't already a plain number; '  (= 3.5)' for a fraction."""
    if not getattr(v, "is_number", False) or v.free_symbols or v.has(S.Float):
        return ""
    try:
        re_, im_ = v.as_real_imag()
        z = _fmt_num(complex(S.N(v, 15)))
    except Exception:
        return ""
    if re_.is_Integer and im_.is_Integer:
        return ""
    if re_.is_Rational and im_.is_Rational:
        return f"  (= {z})"
    return f"  (≈ {z})"


def _choose_vars(S, exprs, hint, count=1):
    syms = set()
    for e in exprs:
        syms |= e.free_symbols
    pref = {"x": 0, "y": 1, "z": 2, "t": 3, "n": 4, "m": 5}
    order = sorted(syms, key=lambda s: (pref.get(s.name, 9), s.name))
    if hint:
        h = [s for s in order if s.name == hint]
        if not h:
            raise MathFail(f"there's no {hint} in that")
        return h + [s for s in order if s.name != hint][:count - 1]
    return order[:count]


def _log_domain_ok(S, expr, v, sol):
    """log(negative) is undefined for real answers: x = -2 doesn't solve log x + log(x - 3) = 1."""
    for f in expr.atoms(S.log):
        a = S.N(f.args[0].subs(v, sol))
        if a.free_symbols:
            continue
        if not (a.is_real and a > 0):
            return False
    return True


def _is_real_number(S, v):
    try:
        z = complex(S.N(v, 15))
    except Exception:
        return False
    return abs(z.imag) <= 1e-10 * max(1.0, abs(z.real))


def _fmt_set(S, st, name, words=False):
    """An answer set as text: 'x > 2', '2 < x ≤ 5', 'x < 2  or  x > 3' - or in words for the voice."""
    lt, le, gt, ge = ((" is less than ", " is at most ", " is greater than ", " is at least ") if words
                      else (" < ", " ≤ ", " > ", " ≥ "))
    join = " or " if words else "  or  "
    if st == S.S.Reals:
        return f"every real {name}" if not words else f"every real {name} works"
    if st is S.S.EmptySet:
        return "no real solution" if not words else "there's no real solution"
    if isinstance(st, S.Union):
        return join.join(_fmt_set(S, a, name, words) for a in st.args)
    if isinstance(st, S.Interval):
        a, b = st.start, st.end
        pa, pb = (speak_math(_pretty(S, a)), speak_math(_pretty(S, b))) if words else (_pretty(S, a), _pretty(S, b))
        if a == -S.oo and b == S.oo:
            return f"every real {name}"
        if a == -S.oo:
            return f"{name}{lt if st.right_open else le}{pb}"
        if b == S.oo:
            return f"{name}{gt if st.left_open else ge}{pa}"
        if words:
            return f"{name} is between {pa} and {pb}"
        return f"{pa}{lt if st.left_open else le}{name}{lt if st.right_open else le}{pb}"
    if isinstance(st, S.FiniteSet):
        return join.join(f"{name} = {_pretty(S, x)}" for x in st)
    return _pretty(S, st)


def _sentence(text):
    text = " ".join(text.split()).strip(" .")
    if not text:
        return ""
    return (text if re.match(r"[a-z]\b", text) else text[:1].upper() + text[1:]) + "."


def _say_answer(prefix, shown, already_words=False):
    """'The derivative is' + 'x^2·cos(x)' -> 'The derivative is x squared times cos x.' (long ones aren't read)"""
    spoken = shown if already_words else speak_math(shown)
    if len(spoken) > 150:
        return "It's a long answer - it's on the screen."
    return _sentence(f"{prefix} {spoken}")


def _big_int_text(S, n):
    digits = str(abs(n))
    if len(digits) <= 300:
        return str(n), len(digits)
    return ("-" if n < 0 else "") + f"{digits[0]}.{digits[1:7]} × 10^{len(digits) - 1}", len(digits)


def _sympy_math(S, P, req):
    op, expr = req["op"], req["expr"]
    shown_in = _pretty_input(expr)
    lines = [f"Problem: {shown_in}" + ("   with " + ", ".join(f"{k} = {_pretty_input(v)}" for k, v in req["subs"])
                                       if req.get("subs") else "")]
    if re.search(r"\blog\b", expr) and not re.search(r"\blog\([^()]*,", expr):
        lines.append("(log means log base 10 here - say ln for the natural log)")
    rels = _split_system(expr) if re.search(r"<=|>=|=|<|>", expr) else [expr]
    if op in ("eval", "solve") and any(_split_rel(r)[1] for r in rels):
        op = "solve"
    if op == "solve":
        return _sympy_solve(S, P, req, rels, lines)
    e = P(expr)
    if op == "eval" and e.free_symbols:
        op = "simplify"
    if op == "eval":
        if e.has(S.zoo, S.nan) or (e.is_number and e.is_finite is False):
            raise MathFail("that's undefined - it divides by zero or runs off to infinity", final=True)
        if e.is_Integer:
            shown, ndig = _big_int_text(S, int(e))
            lines.append(f"Answer: {shown}" + (f"  ({ndig} digits)" if ndig > 15 else ""))
            if ndig > 15:
                return {"lines": lines, "say": f"It's a {ndig} digit number, about {shown[0]} point {shown[2:4]} "
                                               f"times 10 to the power {ndig - 1}." if ndig > 300 else
                                               f"It's a {ndig} digit number - it's on the screen."}
            return {"lines": lines, "say": _say_answer("The answer is", shown)}
        exact = e if isinstance(e, S.Float) else S.simplify(e)
        if exact.has(S.I) and exact.is_number:
            exact = S.expand_complex(exact)
        if exact.has(S.zoo, S.nan) or (exact.is_number and exact.is_finite is False):
            raise MathFail("that's undefined - it divides by zero or runs off to infinity", final=True)
        z = complex(S.N(exact, 15))
        shown = _pretty(S, exact)
        lines.append(f"Answer: {shown}{_approx(S, exact)}")
        if abs(z.imag) > 1e-12 * max(1.0, abs(z.real)):
            lines.append(_polar_line(z))
        if exact.is_Integer or exact.has(S.Float) or len(speak_math(shown)) > 40 or re.search(r"[a-z]{2,}", shown):
            spoken = _fmt_num(z, 6) if not _approx(S, exact) else f"about {_fmt_num(z, 6)}"
        elif _approx(S, exact) and exact.has(S.I):
            spoken = _fmt_num(z, 6)
        elif _approx(S, exact):
            spoken = f"{shown}, that's {'about ' if not exact.is_Rational else ''}{_fmt_num(z, 5)}"
        else:
            spoken = shown
        return {"lines": lines, "say": _say_answer("The answer is", spoken)}
    if op in ("abs", "arg", "conjugate", "re", "im", "polar"):
        if e.free_symbols:
            raise MathFail("give me a number, like 3 + 4i", final=True)
        if op == "abs":
            r = S.simplify(S.Abs(e))
            lines.append(f"Modulus |z| = {_pretty(S, r)}{_approx(S, r)}")
            spoken = _pretty(S, r) if not _approx(S, r) else f"{_pretty(S, r)}, about {_fmt_num(complex(S.N(r)), 5)}"
            return {"lines": lines, "say": _say_answer("The modulus is", spoken)}
        if e == 0:
            raise MathFail("zero has no argument", final=True)
        if op == "arg":
            th = S.simplify(S.arg(e))
            deg = math.degrees(float(S.N(th)))
            lines.append(f"Argument = {_pretty(S, th)} rad  (= {_fmt_real(deg)}°)")
            return {"lines": lines, "say": f"The argument is {speak_math(_fmt_real(deg, 5))} degrees."}
        if op == "conjugate":
            c = S.expand_complex(S.conjugate(e))
            lines.append(f"Conjugate: {_pretty(S, c)}")
            return {"lines": lines, "say": _say_answer("The conjugate is", _pretty(S, c))}
        if op in ("re", "im"):
            part = S.simplify(S.re(e) if op == "re" else S.im(e))
            word = "Real" if op == "re" else "Imaginary"
            lines.append(f"{word} part: {_pretty(S, part)}")
            return {"lines": lines, "say": _say_answer(f"The {word.lower()} part is", _pretty(S, part))}
        r, th = S.simplify(S.Abs(e)), S.simplify(S.arg(e))
        lines.append(f"Polar form: {_pretty(S, r)}(cos({_pretty(S, th)}) + i·sin({_pretty(S, th)}))  =  "
                     f"{_pretty(S, r)}·e^(i·{_pretty(S, th)})")
        lines.append(_polar_line(complex(S.N(e, 15))))
        return {"lines": lines, "say": f"In polar form that's {speak_math(_fmt_real(float(S.N(r)), 5))} at an angle "
                                       f"of {speak_math(_fmt_real(math.degrees(float(S.N(th))), 5))} degrees."}
    if op == "factor":
        if e.is_Integer and abs(e) > 1:
            fs = S.factorint(e)
            shown = " × ".join(f"{p}^{k}" if k > 1 else str(p) for p, k in sorted(fs.items()))
            lines.append(f"Prime factors: {e} = {shown}")
            return {"lines": lines, "say": _say_answer(f"{e} is", shown.replace("×", "times"))}
        f = S.factor(e)
        lines.append(f"Factorised: {_pretty(S, f)}")
        try:
            g = S.factor(e, gaussian=True) if e.is_polynomial() and not e.has(S.I) else f
        except Exception:
            g = f
        if g != f:
            lines.append(f"Over the complex numbers: {_pretty(S, g)}")
        if f == e and g == f:
            lines.append("(It doesn't factorise any further.)")
        return {"lines": lines, "say": _say_answer("That factorises as", _pretty(S, f))}
    if op == "expand":
        x = S.expand(e)
        lines.append(f"Expanded: {_pretty(S, x)}")
        return {"lines": lines, "say": _say_answer("Expanded, that's", _pretty(S, x))}
    if op == "simplify":
        x = S.simplify(e)
        if x.has(S.log):
            x = min((x, S.logcombine(x, force=True), S.expand_log(x, force=True)), key=lambda q: len(str(q)))
        lines.append(f"Simplified: {_pretty(S, x)}{_approx(S, x)}")
        return {"lines": lines, "say": _say_answer("It simplifies to", _pretty(S, x))}
    vs = _choose_vars(S, [e], req.get("var"))
    v = vs[0] if vs else S.Symbol(req.get("var") or "x")
    if op == "diff":
        n = req.get("order", 1)
        raw = S.diff(e, v, n)
        simp = S.simplify(raw)
        d = simp if len(str(simp)) < 0.7 * len(str(raw)) else raw
        tag = "d/d" + v.name if n == 1 else f"d^{n}/d{v.name}^{n}"
        lines.append(f"{tag} [{shown_in}] = {_pretty(S, d)}")
        word = {1: "derivative", 2: "second derivative", 3: "third derivative"}.get(n, f"{n}th derivative")
        return {"lines": lines, "say": _say_answer(f"The {word} is", _pretty(S, d))}
    if op == "integrate":
        if req.get("limits"):
            a, b = P(req["limits"][0]), P(req["limits"][1])
            res = S.integrate(e, (v, a, b))
            if res.has(S.Integral):
                res = S.N(S.Integral(e, (v, a, b)), 12)
            if res.has(S.zoo, S.nan) or (res.is_number and res.is_finite is False):
                lines.append("The integral diverges - the area is infinite.")
                return {"lines": lines, "say": "That integral diverges - the area under it is infinite."}
            lines.append(f"∫ from {_pretty(S, a)} to {_pretty(S, b)} of {shown_in} d{v.name} = {_pretty(S, res)}"
                         f"{_approx(S, res)}")
            spoken = _pretty(S, res) if len(_pretty(S, res)) < 30 else _fmt_num(complex(S.N(res, 15)), 6)
            return {"lines": lines, "say": _say_answer("The integral is", spoken)}
        res = S.integrate(e, v)
        if res.has(S.Integral):
            raise MathFail("I couldn't find that integral")
        lines.append(f"∫ {shown_in} d{v.name} = {_pretty(S, res)} + C")
        return {"lines": lines, "say": _say_answer("The integral is", _pretty(S, res) + " + C")}
    if op == "limit":
        pt = P(req["point"])
        try:
            lim = S.limit(e, v, pt, dir="+-") if pt not in (S.oo, -S.oo) else S.limit(e, v, pt)
        except ValueError:
            left, right = S.limit(e, v, pt, dir="-"), S.limit(e, v, pt, dir="+")
            lines.append(f"From the left: {_pretty(S, left)},  from the right: {_pretty(S, right)}  ->  no limit")
            return {"lines": lines, "say": "The limit doesn't exist - the two sides disagree."}
        lines.append(f"lim {v.name} → {_pretty(S, pt)} of {shown_in} = {_pretty(S, lim)}{_approx(S, lim)}")
        return {"lines": lines, "say": _say_answer("The limit is", _pretty(S, lim))}
    raise MathFail("I don't know how to do that one")


def _sympy_solve(S, P, req, rels, lines):
    eqs, ineqs = [], []
    for r in rels:
        lhs, rel, rhs = _split_rel(r)
        if not rel:
            eqs.append(P(lhs))                                   # "roots of x^2 - 4": "= 0" is understood
            continue
        L, R = P(lhs), P(rhs)
        if rel == "=":
            eqs.append(L - R)
        else:
            ineqs.append((L, rel, R))
    allx = eqs + [L - R for L, _, R in ineqs]
    if not any(x.free_symbols for x in allx):                     # "is 2^10 = 1024" - just check it
        try:
            ok = all(S.simplify(x) == 0 for x in eqs) and all(
                bool({"<": L < R, ">": L > R, "<=": L <= R, ">=": L >= R}[rel]) for L, rel, R in ineqs)
        except TypeError:
            raise MathFail("complex numbers can't be compared with < or >", final=True) from None
        lines.append("That's true." if ok else "That's false.")
        return {"lines": lines, "say": "Yes, that's true." if ok else "No, that's false."}
    if ineqs:
        if eqs:
            raise MathFail("I can't mix equations and inequalities in one go", final=True)
        v = _choose_vars(S, allx, req.get("var"))[0]
        vr = S.Symbol(v.name, real=True)
        sol = S.S.Reals
        for L, rel, R in ineqs:
            cond = {"<": S.Lt, ">": S.Gt, "<=": S.Le, ">=": S.Ge}[rel](L.subs(v, vr), R.subs(v, vr))
            sol = sol.intersect(S.solve_univariate_inequality(cond, vr, relational=False))
        lines.append(f"Answer: {_fmt_set(S, sol, v.name)}")
        return {"lines": lines, "say": _say_answer("", _fmt_set(S, sol, v.name, words=True), already_words=True)}
    if len(eqs) > 1:
        vs = _choose_vars(S, eqs, req.get("var"), count=len(eqs))
        sols = S.solve(eqs, vs, dict=True)
        if not sols:
            lines.append("No solution - the equations contradict each other.")
            return {"lines": lines, "say": "There's no solution - those equations contradict each other."}
        outs = [", ".join(f"{k} = {_pretty(S, d[k])}" for k in vs if k in d) for d in sols[:6]]
        free = [k.name for k in vs if k not in sols[0]]
        lines.append("Answer: " + "   or   ".join(outs) + (f"   ({', '.join(free)} can be anything)" if free else ""))
        if any(_approx(S, d[k]) for d in sols[:6] for k in d):
            lines.append("Decimal: " + "   or   ".join(", ".join(f"{k} ≈ {_fmt_num(complex(S.N(d[k], 15)), 6)}"
                                                                   for k in vs if k in d and not d[k].free_symbols)
                                                         for d in sols[:6]))
        return {"lines": lines, "say": _say_answer("", " or ".join(o.replace(", ", " and ").replace(" = ", " equals ")
                                                                    for o in outs[:3]))}
    expr = eqs[0]
    v = _choose_vars(S, [expr], req.get("var"))[0]
    if S.simplify(expr) == 0:
        lines.append(f"Every value of {v} works - both sides are always equal.")
        return {"lines": lines, "say": f"Every value of {v} works - both sides are always equal."}
    poly = expr.is_polynomial(v)
    others = expr.free_symbols - {v}
    if poly and not others:
        p = S.Poly(expr, v)
        if p.degree() == 2:
            a, b, c = p.all_coeffs()
            disc = S.simplify(b ** 2 - 4 * a * c)
            if disc.is_real:
                kind = ("two real roots" if disc > 0 else "one repeated real root" if disc == 0
                        else "no real roots - two complex roots")
                lines.append(f"Discriminant b² - 4ac = {_pretty(S, disc)}  ->  {kind}")
    numeric = False
    try:
        sols = S.solve(expr, v)
    except NotImplementedError:
        sols = []
    if any(s.has(S.CRootOf) for s in sols):
        sols = [S.N(s, 12) for s in sols]
    rejected = []
    if expr.has(S.log):
        keep = [s for s in sols if _log_domain_ok(S, expr, v, s)]
        rejected = [s for s in sols if s not in keep]
        sols = keep
    dropped = []
    if not poly:                                                  # exp / log / trig: real answers first
        real = [s for s in sols if s.free_symbols or _is_real_number(S, s)]
        if real and len(real) < len(sols):
            dropped = [s for s in sols if s not in real]
        sols = real or sols
    if not sols and not others and not poly:                     # SymPy gave up: hunt for real roots numerically
        roots = _real_roots(S.lambdify(v, expr, modules=["mpmath"]))
        sols = [S.Integer(r) if isinstance(r, int) else S.Float(r, 12) for r in roots]
        numeric = bool(sols)
    if not sols:
        lines.append("No solution." if poly else "No real solution.")
        for s in rejected:
            lines.append(f"({v} = {_pretty(S, s)} was rejected: it makes a log of a number that isn't positive)")
        return {"lines": lines, "say": "There's no solution." if poly else "There's no real solution."}
    shown = [_pretty(S, s) for s in sols[:10]]
    approx = [_approx(S, s).strip(" ()≈=") for s in sols[:10]]
    lines.append("Answer: " + "  or  ".join(f"{v} = {s}" for s in shown) + ("   (numerical)" if numeric else ""))
    if any(approx) and len(sols) <= 6:
        lines.append("Decimal: " + "  or  ".join(f"{v} ≈ {a or s}" for a, s in zip(approx, shown)))
    for s in rejected:
        lines.append(f"({v} = {_pretty(S, s)} was rejected: it makes a log of a number that isn't positive)")
    if dropped:
        lines.append(f"(Complex solutions left out: {',  '.join(_pretty(S, s) for s in dropped[:4])})")
    if expr.has(S.sin, S.cos, S.tan, S.cot, S.sec, S.csc) and not numeric:
        lines.append("(These are the principal solutions - add whole periods for the rest.)")
    if len(sols) > 10:
        lines.append(f"... and {len(sols) - 10} more")
    dec = [_fmt_num(complex(S.N(s, 15)), 5) if not s.free_symbols else "" for s in sols[:10]]
    each = [d if (d and (s != d and (len(speak_math(s)) > 25 or re.search(r"[a-z]{2,}", s) or "." in d)))
            else s for d, s in zip(dec, shown)]
    say = _say_answer(f"{v} equals", " or ".join(each)) if len(sols) <= 6 else ""
    if not say or say.startswith("It's a long") or (len(say) > 90 and any(not _is_real_number(S, s) for s in sols)):
        real = [d for s, d in zip(sols[:10], dec) if d and _is_real_number(S, s)]
        rest = len(sols) - len(real)
        if real and rest:
            say = _sentence(f"{v} equals {' or '.join(speak_math(d) for d in real[:3])}, and there are {rest} "
                            f"complex {'roots' if rest > 1 else 'root'} - all on the screen")
        else:
            say = f"There are {len(sols)} solutions - they're on the screen."
    return {"lines": lines, "say": say}


def solve_math(req):
    """Work the problem out offline. -> {"lines": [...], "say": "...", "hint"?: "..."}, or raises MathFail."""
    if req.get("bad"):
        raise MathFail(req["bad"], final=True)
    if req.get("wordy"):
        raise MathFail("that's a word problem, not an expression I can work out offline")
    if req["op"] in ("gcd", "lcm"):
        nums = req["nums"]
        val = nums[0]
        for n in nums[1:]:
            val = math.gcd(val, n) if req["op"] == "gcd" else abs(val * n) // (math.gcd(val, n) or 1)
        name = "HCF" if req["op"] == "gcd" else "LCM"
        return {"lines": [f"{name} of {', '.join(map(str, nums))} = {val}"],
                "say": f"The {' '.join(name)} is {val}."}
    sym = _sympy()
    if sym is None:
        return _numeric_math(req)
    S, P = sym
    if req.get("subs"):
        base, values = P, {S.Symbol(k): P(v) for k, v in req["subs"]}
        P = lambda text: base(text).subs(values)          # noqa: E731 - every parsed piece gets the values
    try:
        return _sympy_math(S, P, req)
    except MathFail:
        raise
    except (ZeroDivisionError, OverflowError) as e:
        raise MathFail("that's undefined" if isinstance(e, ZeroDivisionError) else "that number is too big",
                       final=True) from None
    except (NotImplementedError, ValueError, TypeError, AttributeError) as e:
        logger.info("SymPy couldn't do %r: %s", req.get("expr"), e)
        raise MathFail("I couldn't work that one out offline") from None


# --------------------------------------------------------------- phone <-> laptop file transfer (same Wi-Fi)
# PAC serves one small private page on your local network. Your phone opens it (address shown in the chat) and can
# send files to the laptop or download the file the laptop is "holding". Gestures/voice only trigger the steps.
TRANSFER_PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>PAC Transfer</title>
<style>body{font-family:system-ui,sans-serif;background:#060a12;color:#d6e6f3;margin:0 auto;padding:18px;max-width:560px}
h1{color:#4da6ff;font-size:22px}.card{border:1px solid #1f4f7a;border-radius:12px;padding:14px;margin:14px 0}
button,a.btn,label.btn{background:#4da6ff;color:#060a12;border:0;border-radius:8px;padding:12px 16px;font-size:16px;font-weight:600;
text-decoration:none;display:inline-block}.muted{color:#88b}progress{width:100%;margin-top:10px}ul{padding-left:18px}
input[type=file]{width:100%;margin:10px 0}</style></head><body>
<h1>PAC Transfer</h1>
<div class="card"><b>Beam to laptop</b><label class="btn" style="display:block;text-align:center;margin:10px 0">Pick files to beam<input id="f" type="file" multiple hidden onchange="up()"></label><div class="muted">They fly over the moment you pick them and appear on the laptop shelf, ready to air-drag.</div><progress id="p" value="0" max="1" hidden></progress><div id="m" class="muted"></div></div>
<div class="card"><b>From laptop</b><div id="held" class="muted">Nothing held. Grab a file on the laptop.</div></div>
<div class="card"><b>Recently received by laptop</b><ul id="rx"></ul></div>
<script>
const T=new URLSearchParams(location.search).get('t')||'';let MAXMB=500;
const q=s=>s+(s.includes('?')?'&':'?')+'t='+encodeURIComponent(T);
function msg(s){document.getElementById('m').textContent=s}
async function poll(){try{const s=await (await fetch(q('/state'))).json();MAXMB=s.max_mb;
const h=document.getElementById('held');h.textContent='';
if(s.held){const a=document.createElement('a');a.className='btn';a.href=q('/get');a.textContent='Download '+s.held+' ('+s.size+')';h.appendChild(a);}
else h.textContent='Nothing held. Grab a file on the laptop.';
const u=document.getElementById('rx');u.textContent='';
s.received.forEach(n=>{const li=document.createElement('li');li.textContent=n;u.appendChild(li)});}catch(e){}}
function up(){const list=[...document.getElementById('f').files];if(!list.length){msg('Choose a file first.');return}
const p=document.getElementById('p');p.hidden=false;
const next=()=>{if(!list.length){msg('All sent. Grab them from the laptop shelf.');p.hidden=true;document.getElementById('f').value='';poll();return}
const f=list.shift();if(f.size>MAXMB*1048576){msg(f.name+' is bigger than the '+MAXMB+' MB limit.');next();return}const x=new XMLHttpRequest();
x.open('POST',q('/up?name='+encodeURIComponent(f.name)));
x.upload.onprogress=e=>{if(e.lengthComputable)p.value=e.loaded/e.total};
x.onload=()=>{if(x.status==200){msg('Sent '+f.name);next()}else{msg('Failed: '+f.name+' ('+x.status+')');p.hidden=true}};
x.onerror=()=>{msg('Connection lost while sending '+f.name);p.hidden=true};
x.send(f)};next()}
poll();setInterval(poll,2500);
</script></body></html>"""
_WIN_RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}


def safe_filename(name):
    """A file name from the phone, made harmless: no folders, no odd characters, no Windows device names."""
    name = Path(str(name).replace("\\", "/")).name
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" .")
    if Path(name).stem.upper() in _WIN_RESERVED:
        name = "_" + name
    return name[:150] or "file"


def zip_paths(paths, dest):
    import zipfile
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for p in paths:
            if p.is_dir():
                for root, _d, files in os.walk(p):
                    for f in files:
                        fp = Path(root) / f
                        z.write(fp, str(Path(p.name) / fp.relative_to(p)))
            elif p.is_file():
                z.write(p, p.name)
    return dest


# --------------------------------------------------------------- file manager: look at, move and create files
USER_FOLDER_NAMES = {
    "desktop": "Desktop", "documents": "Documents", "document": "Documents", "docs": "Documents",
    "downloads": "Downloads", "download": "Downloads", "pictures": "Pictures", "picture": "Pictures",
    "photos": "Pictures", "pics": "Pictures", "images": "Pictures", "videos": "Videos", "video": "Videos",
    "movies": "Videos", "music": "Music", "songs": "Music",
}
SKIP_DIRS = {"appdata", "node_modules", "__pycache__", "$recycle.bin", "system volume information",
             "windows", "program files", "program files (x86)", "programdata"}
EXT_WORDS = {"txt", "pdf", "docx", "doc", "xlsx", "xls", "pptx", "ppt", "csv", "tsv", "json", "md", "py", "png", "jpg",
             "jpeg", "gif", "bmp", "webp", "zip", "rar", "mp3", "wav", "mp4", "mkv", "mov", "avi", "html", "css", "js",
             "xml", "log", "rtf", "exe", "ini", "bat", "odt", "ods", "svg", "heic", "flac", "m4a", "webm", "yaml", "yml"}
TEXT_EXTS = {"txt", "md", "log", "csv", "tsv", "json", "py", "js", "html", "css", "xml", "ini", "cfg", "yaml", "yml",
             "bat", "ps1", "java", "c", "cpp", "h", "sql", "rtf", "tex", "toml", "sh"}
IMAGE_EXTS = {"png", "jpg", "jpeg", "gif", "bmp", "webp", "tif", "tiff", "ico"}
KIND_NAMES = {
    "pdf": "PDF document", "docx": "Word document", "doc": "Word document", "xlsx": "Excel spreadsheet",
    "xls": "Excel spreadsheet", "pptx": "PowerPoint presentation", "ppt": "PowerPoint presentation",
    "txt": "text file", "md": "Markdown file", "csv": "CSV table", "tsv": "table", "json": "JSON file",
    "py": "Python script", "js": "JavaScript file", "html": "web page", "css": "stylesheet", "xml": "XML file",
    "log": "log file", "zip": "ZIP archive", "rar": "RAR archive", "mp3": "MP3 audio", "wav": "WAV audio",
    "flac": "FLAC audio", "m4a": "audio file", "mp4": "MP4 video", "mkv": "MKV video", "mov": "MOV video",
    "avi": "AVI video", "webm": "WebM video", "exe": "program", "lnk": "shortcut", "png": "PNG image",
    "jpg": "JPEG image", "jpeg": "JPEG image", "gif": "GIF image", "bmp": "bitmap image", "webp": "WebP image",
    "svg": "SVG image", "heic": "HEIC photo", "ini": "settings file", "bat": "batch script", "rtf": "rich text file",
}
KIND_GROUPS = {                                   # "all images", "every video", ...
    "images": {"jpg", "jpeg", "png", "gif", "bmp", "webp", "heic", "svg"}, "photos": {"jpg", "jpeg", "png", "heic"},
    "pictures": {"jpg", "jpeg", "png", "gif", "bmp", "webp", "heic"},
    "videos": {"mp4", "mkv", "mov", "avi", "webm"}, "music": {"mp3", "wav", "flac", "m4a", "aac"},
    "songs": {"mp3", "wav", "flac", "m4a", "aac"},
    "documents": {"pdf", "doc", "docx", "txt", "rtf", "odt", "xlsx", "xls", "pptx", "ppt", "csv"},
    "pdfs": {"pdf"}, "spreadsheets": {"xlsx", "xls", "csv"}, "presentations": {"pptx", "ppt"},
}
MAKE_KINDS = {"text": "txt", "plain text": "txt", "notepad": "txt", "word": "docx", "excel": "xlsx",
              "spreadsheet": "xlsx", "markdown": "md", "python": "py", "html": "html", "csv": "csv", "json": "json"}


def _plural(n, word):
    return f"{n:,} {word}" + ("" if n == 1 else "s")


def human_size(n):
    n = float(n)
    for unit in ("bytes", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{int(n)} bytes" if unit == "bytes" else f"{n:.1f} {unit}"
        n /= 1024


def human_age(ts):
    d = time.time() - ts
    if d < 90:
        return "just now"
    if d < 3600:
        return f"{int(d // 60)} minutes ago"
    if d < 86400:
        return _plural(int(d // 3600), "hour") + " ago"
    days = int(d // 86400)
    if days == 1:
        return "yesterday"
    if days < 60:
        return f"{days} days ago"
    if days < 700:
        return _plural(days // 30, "month") + " ago"
    return _plural(days // 365, "year") + " ago"


def _when(ts):
    return time.strftime("%d %b %Y, %I:%M %p", time.localtime(ts)).lstrip("0")


def _mtime(p):
    try:
        return Path(p).stat().st_mtime
    except OSError:
        return 0.0


def _protected(p):
    """True for places PAC must never move things from or into: system folders, a drive root, your home folder itself."""
    try:
        rp = Path(p).resolve()
    except OSError:
        return True
    if len(rp.parts) <= 1 or rp == HOME.resolve():
        return True
    s = str(rp).lower().replace("\\", "/")
    if OS == "Windows":
        for key in ("SystemRoot", "ProgramFiles", "ProgramFiles(x86)", "ProgramData"):
            v = os.environ.get(key)
            if v:
                v = v.lower().replace("\\", "/")
                if s == v or s.startswith(v + "/"):
                    return True
        return False
    if s.startswith(str(HOME.resolve()).lower().replace("\\", "/") + "/"):
        return False
    return any(s == x or s.startswith(x + "/") for x in ("/bin", "/boot", "/dev", "/etc", "/lib", "/lib64", "/proc",
                                                        "/sys", "/usr", "/var", "/sbin", "/opt", "/root",
                                                        "/system", "/library", "/applications"))


def _bases():
    bases = [HOME]
    try:
        bases += [p for p in HOME.glob("OneDrive*") if p.is_dir()]
    except OSError:
        pass
    v = os.environ.get("OneDrive")
    if v and Path(v).is_dir() and Path(v) not in bases:
        bases.append(Path(v))
    return bases


MEMORY_PATH_LOOKUP = None          # set by the Assistant: a nickname from memory -> the folder it names


def user_folder(name):
    """'downloads', 'my documents', 'the desktop', 'home' -> that folder (OneDrive-moved ones included)."""
    key = re.sub(r"^(?:the|my)\s+", "", norm(name))
    key = re.sub(r"\s+(?:folder|directory)$", "", key)
    if key in ("home", "user", "user folder", "home folder", "my files"):
        return HOME
    hook = MEMORY_PATH_LOOKUP
    if hook:                                   # a folder you named yourself wins ("my taxes folder is documents/taxes")
        named = hook(key)
        if named:
            return named
    real = USER_FOLDER_NAMES.get(key)
    if not real:
        return None
    for b in _bases():
        if (b / real).is_dir():
            return b / real
    return None


def default_parent():
    return user_folder("desktop") or user_folder("documents") or HOME


def search_roots():
    roots, seen = [], set()
    for real in dict.fromkeys(USER_FOLDER_NAMES.values()):
        for b in _bases():
            p = b / real
            if p.is_dir() and p not in seen:
                seen.add(p)
                roots.append((p, 3))
    roots.append((HOME, 1))
    return roots


def scan_index(roots=None, cap=40000):
    """Every file and folder (path, is_folder) in your usual places, a few levels deep."""
    out, seen = [], set()
    for base, depth in (roots or search_roots()):
        base = Path(base)
        d0 = len(base.parts)
        for root, dirs, files in os.walk(base):
            rel = len(Path(root).parts) - d0
            keep = [d for d in dirs if not d.startswith(".") and d.lower() not in SKIP_DIRS]
            dirs[:] = keep if rel < depth else []
            for d in keep:
                p = Path(root) / d
                if p not in seen:
                    seen.add(p)
                    out.append((p, True))
            for f in files:
                p = Path(root) / f
                if not f.startswith(".") and p not in seen:
                    seen.add(p)
                    out.append((p, False))
            if len(out) >= cap:
                return out
    return out


def spoken_name(s):
    """'notes dot txt' / 'notes txt' -> 'notes.txt'."""
    s = re.sub(r"\s+dot\s+", ".", s.strip(), flags=re.I)
    s = re.sub(r"\s+underscore\s+", "_", s, flags=re.I)
    m = re.fullmatch(r"(.+?)\s+([A-Za-z0-9]{2,5})", s)
    if m and m.group(2).lower() in EXT_WORDS and not re.search(r"\.[A-Za-z0-9]{1,5}$", m.group(1)):
        s = m.group(1) + "." + m.group(2)
    return s.strip()


def as_path(text):
    t = text.strip().strip("\"'")
    if re.match(r"^(?:[a-zA-Z]:[\\/]|[\\/]{2}|/|~)", t):
        try:
            p = Path(t).expanduser()
            return p if p.exists() else None
        except OSError:
            return None
    return None


def pick_item(query, index, want=None, fuzzy=True):
    """The file or folder you mean -> (path, exact). want: 'file', 'folder' or None."""
    pick_item.same_name = 0
    q = spoken_name(query)
    q = re.sub(r"^(?:the |my |a |an )+", "", q.strip().strip("\"'"), flags=re.I)
    q = re.sub(r"^(?:file|folder|document|directory)\s+", "", q, flags=re.I)
    if not q:
        return None, False
    p = as_path(q)
    if p is not None:
        return (p, True) if want is None or p.is_dir() == (want == "folder") else (None, False)
    low = q.lower().rstrip("/\\")

    def ok(isd):
        return want is None or isd == (want == "folder")
    exact = [p for p, isd in index if ok(isd) and (p.name.lower() == low or (not isd and p.stem.lower() == low))]
    pick_item.same_name = len(exact)                   # how many things carry exactly this name
    if exact:
        return max(exact, key=_mtime), True
    if not fuzzy:
        return None, False
    qext = Path(low).suffix.lower().lstrip(".") if re.search(r"\.[a-z0-9]{1,5}$", low) else ""
    qn = norm(Path(low).stem if qext else low)
    best, bs = None, 0.0
    for p, isd in index:
        if not ok(isd) or (qext and not isd and p.suffix.lower().lstrip(".") != qext):
            continue
        s = norm(p.name if isd else p.stem)
        if not s:
            continue
        sc = difflib.SequenceMatcher(None, qn, s).ratio()
        if len(qn) >= 3 and qn in s:
            sc = max(sc, 0.9)
        if sc > bs or (sc == bs and best is not None and _mtime(p) > _mtime(best)):
            best, bs = p, sc
    return (best, False) if bs >= 0.65 else (None, False)


def find_child_folder(parent, name):
    try:
        kids = [c for c in Path(parent).iterdir() if c.is_dir()]
    except OSError:
        return None
    q = norm(name)
    for c in kids:
        if norm(c.name) == q:
            return c
    best = max(kids, key=lambda c: difflib.SequenceMatcher(None, q, norm(c.name)).ratio(), default=None)
    if best is not None and difflib.SequenceMatcher(None, q, norm(best.name)).ratio() >= 0.85:
        return best
    return None


def resolve_folder(text, index, strict=False):
    """An existing folder from what you said: 'downloads', 'documents slash taxes', 'taxes', a full path."""
    q = re.sub(r"^(?:the |my |a )+", "", text.strip().strip("\"'"), flags=re.I)
    q = re.sub(r"\s+(?:folder|directory)$", "", q, flags=re.I)
    q = re.sub(r"^(?:folder|directory)\s+", "", q, flags=re.I).strip()
    if not q:
        return None
    p = as_path(q)
    if p is not None:
        return p if p.is_dir() else None
    parts = [x.strip() for x in re.split(r"\s+slash\s+|[\\/]", q) if x.strip()]
    if len(parts) > 1:
        cur = resolve_folder(parts[0], index, strict)
        for part in parts[1:]:
            cur = find_child_folder(cur, part) if cur is not None else None
        return cur
    uf = user_folder(q)
    if uf:
        return uf
    return pick_item(q, index, want="folder", fuzzy=not strict)[0]


def unique_path(folder, name):
    """folder/name, or folder/'name (1)' - never an existing path, so nothing is ever overwritten."""
    folder = Path(folder)
    cand = folder / name
    stem, suffix, n = Path(name).stem, Path(name).suffix, 1
    while cand.exists():
        cand = folder / f"{stem} ({n}){suffix}"
        n += 1
    return cand


# ----- looking inside files
def _text_of(p, limit=2_000_000):
    with open(p, "rb") as f:
        raw = f.read(limit)
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", "ignore")
    return raw.decode("utf-8-sig", "ignore")


def _xml_text(xml):
    xml = re.sub(r"</w:p>|<w:br\s*/>|<w:tab\s*/>", "\n", xml)
    txt = re.sub(r"<[^>]+>", "", xml)
    return re.sub(r"&amp;", "&", re.sub(r"&lt;", "<", re.sub(r"&gt;", ">", txt)))


def _pdf_reader(p):
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader
    r = PdfReader(str(p))
    if getattr(r, "is_encrypted", False):
        raise ValueError("encrypted")
    return r


def extract_text(p, limit=1500):
    """The start of a file's text, or None when it isn't something PAC can read."""
    p = Path(p)
    ext = p.suffix.lower().lstrip(".")
    try:
        if ext in TEXT_EXTS:
            return _text_of(p, limit * 4).strip()[:limit]
        if ext == "pdf":
            r, out = _pdf_reader(p), ""
            for page in r.pages[:6]:
                out += (page.extract_text() or "") + "\n"
                if len(out) >= limit:
                    break
            return re.sub(r"\s+", " ", out).strip()[:limit] or None
        if ext == "docx":
            import zipfile
            with zipfile.ZipFile(p) as z:
                return re.sub(r"[ \t]+", " ", _xml_text(z.read("word/document.xml").decode("utf-8", "ignore"))).strip()[:limit]
    except Exception:
        logger.exception("couldn't read %s", p)
    return None


def _extras(p, ext, size):
    """(short facts for speech, detail lines, one-line preview) for a file."""
    short, lines, preview = [], [], ""
    try:
        if ext in TEXT_EXTS:
            text = _text_of(p)
            n = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
            words = len(text.split())
            note = " (counted the first 2 MB)" if size > 2_000_000 else ""
            short.append(f"{_plural(n, 'line')}, {_plural(words, 'word')}")
            lines.append(f"Contents: {_plural(n, 'line')}, {_plural(words, 'word')}, {len(text):,} characters{note}")
            body = [l for l in text.splitlines() if l.strip()]
            if ext in ("csv", "tsv") and body:
                cols = [c.strip().strip('"') for c in re.split(r"\t" if ext == "tsv" else ",", body[0])]
                short[-1] = f"{_plural(max(len(body) - 1, 0), 'row')}, {_plural(len(cols), 'column')}"
                lines.append(f"Columns: {', '.join(cols[:8])}" + (" ..." if len(cols) > 8 else ""))
            elif ext == "json":
                try:
                    data = json.loads(text)
                    desc = (f"an object with {_plural(len(data), 'key')}: {', '.join(list(data)[:6])}" if isinstance(data, dict)
                            else f"a list of {_plural(len(data), 'item')}" if isinstance(data, list) else "a single value")
                    lines.append(f"JSON holds {desc}")
                    short.append(desc)
                except ValueError:
                    lines.append("JSON: this file isn't valid JSON")
            elif ext == "py":
                fn, cl = len(re.findall(r"^\s*def ", text, re.M)), len(re.findall(r"^\s*class ", text, re.M))
                lines.append(f"Python: {_plural(fn, 'function')}, {_plural(cl, 'class')}")
            preview = " ".join(l.strip() for l in body[:4])[:160]
        elif ext == "pdf":
            try:
                r = _pdf_reader(p)
                pages = len(r.pages)
                meta = getattr(r, "metadata", None)
                title = getattr(meta, "title", None) if meta else None
                short.append(_plural(pages, "page"))
                lines.append(f"Pages: {pages}")
                if title:
                    lines.append(f"Title: {title}")
                preview = re.sub(r"\s+", " ", (r.pages[0].extract_text() or ""))[:160].strip() if pages else ""
            except ValueError:
                short.append("password protected")
                lines.append("This PDF is password protected, so I can't look inside it")
            except Exception:
                data = open(p, "rb").read(30_000_000)
                pages = len(re.findall(rb"/Type\s*/Page(?![s\w])", data))
                if pages:
                    short.append(_plural(pages, "page"))
                    lines.append(f"Pages: about {pages}")
        elif ext in ("docx", "xlsx", "pptx"):
            import zipfile
            with zipfile.ZipFile(p) as z:
                names = z.namelist()
                if ext == "docx":
                    text = _xml_text(z.read("word/document.xml").decode("utf-8", "ignore"))
                    words = len(text.split())
                    paras = len([x for x in text.split("\n") if x.strip()])
                    short.append(_plural(words, "word"))
                    lines.append(f"Contents: {_plural(words, 'word')} in {_plural(paras, 'paragraph')}")
                    if "docProps/app.xml" in names:
                        pm = re.search(r"<Pages>(\d+)</Pages>", z.read("docProps/app.xml").decode("utf-8", "ignore"))
                        if pm:
                            short.append(_plural(int(pm.group(1)), "page"))
                            lines.append(f"Pages: {pm.group(1)}")
                    preview = re.sub(r"\s+", " ", text).strip()[:160]
                elif ext == "xlsx":
                    sheets = re.findall(r'<sheet [^>]*?name="([^"]+)"', z.read("xl/workbook.xml").decode("utf-8", "ignore"))
                    short.append(_plural(len(sheets), "sheet"))
                    lines.append(f"Sheets: {', '.join(sheets[:8])}")
                else:
                    slides = [n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
                    short.append(_plural(len(slides), "slide"))
                    lines.append(f"Slides: {len(slides)}")
        elif ext in IMAGE_EXTS:
            from PIL import Image
            with Image.open(p) as im:
                short.append(f"{im.width} by {im.height} pixels")
                lines.append(f"Dimensions: {im.width} x {im.height} pixels ({im.mode})")
        elif ext in ("zip", "jar", "whl"):
            import zipfile
            with zipfile.ZipFile(p) as z:
                infos = z.infolist()
                total = sum(i.file_size for i in infos)
                short.append(f"{_plural(len(infos), 'item')} inside")
                lines.append(f"Inside: {_plural(len(infos), 'item')}, {human_size(total)} unpacked")
        elif ext in ("mp3", "wav", "flac", "m4a", "mp4", "mkv", "mov", "avi", "webm"):
            lines.append("Length and tags need an audio/video tool, so I only report the size")
    except Exception:
        logger.exception("couldn't look inside %s", p)
    return short, lines, preview


def describe(p):
    """Everything PAC can tell about a file or folder: {name, kind, short, headline, lines, preview}."""
    p = Path(p)
    st = p.stat()
    created = getattr(st, "st_birthtime", None) or (st.st_ctime if OS == "Windows" else st.st_mtime)
    lines = [f"Location: {p.parent}"]
    if p.is_dir():
        try:
            kids = [k for k in p.iterdir() if not k.name.startswith(".")]
        except OSError:
            kids = []
        nfiles = sum(1 for k in kids if k.is_file())
        nfold = len(kids) - nfiles
        total = seen = 0
        for root, _d, fs in os.walk(p):
            for f in fs:
                try:
                    total += (Path(root) / f).stat().st_size
                except OSError:
                    pass
                seen += 1
            if seen > 5000:
                break
        newest = max(kids, key=_mtime, default=None)
        kind = "folder"
        short = ([f"{_plural(nfiles, 'file')} and {_plural(nfold, 'folder')}", f"about {human_size(total)}"] if kids else ["empty"])
        lines += [f"Type: folder", f"Holds: {_plural(nfiles, 'file')} and {_plural(nfold, 'subfolder')}",
                  f"Total size: about {human_size(total)}" + (" (counted the first 5,000 files)" if seen > 5000 else "")]
        if newest is not None:
            lines.append(f"Newest item: {newest.name} ({human_age(_mtime(newest))})")
        preview = ""
    else:
        ext = p.suffix.lower().lstrip(".")
        kind = KIND_NAMES.get(ext) or (f"{ext.upper()} file" if ext else "file")
        ex_short, ex_lines, preview = _extras(p, ext, st.st_size)
        short = [human_size(st.st_size)] + ex_short
        lines += [f"Type: {kind}", f"Size: {human_size(st.st_size)} ({st.st_size:,} bytes)"] + ex_lines
    lines += [f"Created: {_when(created)}", f"Last changed: {_when(st.st_mtime)} ({human_age(st.st_mtime)})"]
    if preview:
        lines.append(f"Starts with: {preview}")
    first = kind.split()[0]
    article = "an" if (first[:1].lower() in "aeiou" or (first.isupper() and first[:1] in "FHLMNRSX")) else "a"
    headline = f"{p.name} is {article} {kind}, " + ", ".join(short) + f", last changed {human_age(st.st_mtime)}."
    return {"name": p.name, "kind": kind, "short": f"{p.name}: {kind}, " + ", ".join(short), "headline": headline,
            "lines": lines, "preview": preview}


# ----- making things
def _docx_bytes(text=""):
    import io
    import zipfile
    from xml.sax.saxutils import escape
    paras = "".join(f'<w:p><w:r><w:t xml:space="preserve">{escape(l)}</w:t></w:r></w:p>' for l in (text.splitlines() or [""]))
    parts = {
        "[Content_Types].xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>',
        "_rels/.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>',
        "word/document.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>' + paras + "<w:sectPr/></w:body></w:document>",
    }
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)
    return buf.getvalue()


def _xlsx_bytes(text=""):
    import io
    import zipfile
    from xml.sax.saxutils import escape
    cell = f'<row r="1"><c r="A1" t="inlineStr"><is><t>{escape(text)}</t></is></c></row>' if text else ""
    parts = {
        "[Content_Types].xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>',
        "_rels/.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>',
        "xl/workbook.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Sheet1" sheetId="1" r:id="rId1"/></sheets></workbook>',
        "xl/_rels/workbook.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>',
        "xl/worksheets/sheet1.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>' + cell + "</sheetData></worksheet>",
    }
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)
    return buf.getvalue()


def make_folder(parent, name):
    """Create parent/name (a/b/c nests). Returns (path, created); an existing folder is left alone."""
    parts = [safe_filename(x) for x in re.split(r"\s+slash\s+|[\\/]", name) if x.strip()]
    target = Path(parent).joinpath(*parts)
    existed = target.is_dir()
    target.mkdir(parents=True, exist_ok=True)
    return target, not existed


def make_file(parent, name, content="", default_ext="txt"):
    """Create a new file without ever overwriting one. Returns the path."""
    name = safe_filename(spoken_name(name))
    if not Path(name).suffix:
        name += "." + default_ext
    target = unique_path(parent, name)
    ext = target.suffix.lower().lstrip(".")
    if ext == "docx":
        target.write_bytes(_docx_bytes(content))
    elif ext == "xlsx":
        target.write_bytes(_xlsx_bytes(content))
    else:
        target.write_text(content + ("\n" if content else ""), encoding="utf-8")
    return target


def move_items(items, dest):
    """Move files/folders into dest. Never overwrites (a clash becomes 'name (1)'). -> (moved [(from, to)], failed [(path, why)])"""
    moved, failed = [], []
    dest = Path(dest)
    for src in items:
        src = Path(src)
        try:
            if _protected(src) or _protected(dest):
                failed.append((src, "that's a protected place"))
            elif not src.exists():
                failed.append((src, "it isn't there any more"))
            elif src.parent.resolve() == dest.resolve():
                failed.append((src, "it's already there"))
            elif src.is_dir() and (src.resolve() == dest.resolve() or src.resolve() in dest.resolve().parents):
                failed.append((src, "a folder can't go inside itself"))
            else:
                target = unique_path(dest, src.name)
                shutil.move(str(src), str(target))
                moved.append((src, target))
        except PermissionError:
            failed.append((src, "Windows won't allow it (no permission, or it's open in a program)"))
        except OSError as e:
            failed.append((src, str(e)))
    return moved, failed


# ----- the spoken side
_PFX = r"(?:the |my |these |those |all the |all |some )*"
FS_INFO = [
    r"^(?:(?:tell|give|show) me |can you |could you )?(?:the )?(?:info(?:rmation)?|details?|properties|stats|facts|summary)\s+(?:about|on|of|for)\s+" + _PFX + r"(?:(?P<ext>[a-z0-9]{2,5}) )?(?P<kind>files?|folders?|documents?|directory)\s*(?P<what>.*)$",
    r"^(?:tell me about|describe|inspect|analy[sz]e|examine|check|summari[sz]e|review|read(?: out)?)(?: me)?\s+" + _PFX + r"(?:(?P<ext>[a-z0-9]{2,5}) )?(?P<kind>files?|folders?|documents?)\s*(?P<what>.*)$",
    r"^(?P<kind>file|folder) (?:info|information|details|properties)(?: (?:of|about|for|on))?\s*(?P<what>.+)$",
    r"^what(?:'s| is| are)(?: (?:in|inside))\s+" + _PFX + r"(?P<kind>files?|folders?|documents?)\s+(?P<what>.+)$",
    r"^how (?:big|large) (?:is|are)\s+" + _PFX + r"(?P<kind>files?|folders?|documents?)\s+(?P<what>.+)$",
]
_EXTS = "|".join(sorted(EXT_WORDS))
FS_INFO.append(r"^(?:read(?: out)?|inspect|describe|analy[sz]e|summari[sz]e|tell me about|info(?:rmation)? (?:about|on)|what(?:'s| is) (?:in|inside)|how (?:big|large) is)\s+(?:the |my )?(?P<what>.+?\.(?:" + _EXTS + r")|.+?\s(?:dot\s)?(?:" + _EXTS + r"))$")
FS_LIST = [
    r"^(?:list|show|display|what(?:'s| is| are)|how many)(?: me)?\s+" + _PFX + r"(?:(?P<ext>[a-z0-9]{2,8}) )?(?:files|items|documents|things|folders)\s+(?:are |is )?(?:in|inside|on|from|under|of)\s+(?:the |my )?(?P<where>.+?)(?: folder| directory)?$",
    r"^(?:list|show|display)(?: me)?\s+(?:the )?(?:contents?) (?:of|in)\s+(?:the |my )?(?P<where>.+?)(?: folder| directory)?$",
    r"^what(?:'s| is| are)\s+(?:in|inside)\s+(?:the |my )?(?P<where>.+?)(?: folder| directory)?$",
    r"^(?:list|show|display|read|check)(?: me)?\s+(?:what(?:'s| is) in\s+)?(?:the |my )?(?P<where>.+?) (?:folder|directory)$",
]
FS_MOVE = r"^move\s+(?:the |my |these |those )*(?P<what>.+)\s+(?:to|into|in|inside|onto)\s+(?:the |my )?(?P<dest>.+?)(?: folder| directory)?$"
FS_MOVE2 = r"^(?:put|shift|relocate)\s+(?=.*\b(?:files?|folders?|directory|documents|pdfs?|photos|images|videos|[a-z0-9]+\.(?:" + _EXTS + r")|(?:" + _EXTS + r"))\b)(?:the |my |these |those )*(?P<what>.+)\s+(?:to|into|in|inside|onto)\s+(?:the |my )?(?P<dest>.+?)(?: folder| directory)?$"
FS_ANY = r"^(?:please )?(?:(?:can|could|would) you )?(?:read|show|list|display|tell|give|find|check|get|fetch|scan|look|what|which|how many|are there|do i have|i want|i need|let me|open and read|go through)\b.*\b(?:files|folders|directories)\b"
FS_ANY_CUE = re.compile(r"\b(?:my|our|this|have|there|device|laptop|computer|pc|system|machine|desktop|downloads?|documents|pictures|videos|music|home|several|some|few|any|all|\d+)\b", re.I)
FS_NOT_FILES = re.compile(r"\bfile (?:a |an |my |the |for |your |our )?(?:complaints?|claims?|tax(?:es)?|returns?|reports?|lawsuit|case|application|appeal|petition|police|fir|suit|papers)\b|\bfiling\b|\bfile cabinet\b|\byou (?:remember|know|learned|learnt)\b|\bmemor(?:y|ies)\b|\bforget\b", re.I)
DEVICE_WORDS = r"(?:the |my |this )?(?:device|laptop|computer|pc|system|machine|drive|hard ?drive|disk)"
FS_UNDO = r"^(?:undo|reverse|revert)(?: the)?(?: last)?(?: file)? (?:move|moves|moving)$|^(?:put|move) (?:them|it|those|the files?) back$"
FS_NEWDIR = r"^(?:create|make|add|new|build)(?: me)?(?: a| an| the| some)?(?: new)?\s+(?:folders?|directory|directories)(?:\s+(?:called|named|with the name|name))?\s*(?P<what>.*)$"
FS_NEWFILE = r"^(?:create|make|add|new)(?: me)?(?: a| an| the| some)?(?: new)?(?: (?P<ktype>text|plain text|word|excel|spreadsheet|markdown|python|html|csv|json|empty|blank|notepad))?\s+(?P<noun>files?|documents?|docs?|spreadsheets?|workbooks?|scripts?)(?:\s+(?:called|named|with the name|name))?\s*(?P<what>.*)$"
FS_SCOPE = re.compile(r"^(?:in|inside|from|under|of|on|at)\s+(?:the |my )?(?P<where>.+?)(?: folder| directory)?$", re.I)
FS_BULK = re.compile(r"^(?:all|every|each|everything)\b(?:\s+(?:the|of the|of my|my))*\s*(?:(?P<ext>[a-z0-9]{2,5}) )?(?P<noun>files?|documents|images|photos|pictures|videos|music|songs|pdfs|spreadsheets|presentations|items|things|stuff)?(?:\s+(?:from|in|inside|of|under|on)\s+(?:the |my )?(?P<src>.+?)(?: folder| directory)?)?$", re.I)
FS_NAMES = re.compile(r"^(?P<names>.+?)(?:\s+(?:from|in|inside|out of)\s+(?:the |my )?(?P<src>.+?)(?: folder| directory)?)?$", re.I)
FS_NEWDEST = re.compile(r"^(?:an? |the )?new (?:folder|directory)(?:\s+(?:called|named))?\s+(?P<name>.+)$", re.I)
FS_DESTIN = re.compile(r"^(?P<d>.+?)\s+(?:in|inside|under|within|on)\s+(?:the |my )?(?P<p>.+?)(?: folder| directory)?$", re.I)
FS_TAIL = re.compile(r"^(?P<names>.+?)(?:\s+(?:in|on|inside|under|within|at|into)\s+(?:the |my )?(?P<where>.+?)(?: folder| directory)?)?(?:\s+(?:with|containing|saying|that says)(?: the)?(?: text| content| contents| words)?\s+(?P<content>.+))?$", re.I)
FS_INFO_RXS = [re.compile(x, re.I) for x in FS_INFO]
FS_LIST_RXS = [re.compile(x, re.I) for x in FS_LIST]
FS_MOVE_RX, FS_MOVE2_RX, FS_UNDO_RX = re.compile(FS_MOVE, re.I), re.compile(FS_MOVE2, re.I), re.compile(FS_UNDO, re.I)
FS_NEWDIR_RX, FS_NEWFILE_RX = re.compile(FS_NEWDIR, re.I), re.compile(FS_NEWFILE, re.I)


class FileAssistant:
    """Looks at, lists, moves and creates files and folders when you ask. It never deletes or overwrites anything,
    refuses system folders, asks before a big move, and can undo the last move.
    `owner` supplies say(), emit(), ask(), awaiting and raw (PAC's assistant)."""
    BIG_MOVE = 5                                  # more than this many items: ask first

    def __init__(self, owner):
        self.o = owner
        self.history = []                         # one list of (from, to) per move, newest last
        self.notes = []                           # things worth saying along with the answer

    # ----- small helpers
    def _raw(self, t):
        s = re.sub(r"\s+", " ", (getattr(self.o, "raw", "") or t or "").strip())
        for _ in range(3):
            s = re.sub(FILLER_START, "", s, flags=re.I)
        s = re.sub(r"\s+(?:please|for me|now|pac|pack)\s*[.!?]*$", "", s, flags=re.I)
        return s.strip().rstrip(".!?;,")

    def _match(self, rxs, t):
        for s in (self._raw(t), t):
            for i, rx in enumerate(rxs):
                m = rx.match(s)
                if m:
                    return m, s, i
        return None, "", -1

    @staticmethod
    def _ext(word):
        w = (word or "").lower().strip().rstrip("s") if (word or "").lower() not in EXT_WORDS else (word or "").lower()
        return w if w in EXT_WORDS else ""

    @staticmethod
    def _names(text):
        parts = [x.strip() for x in re.split(r"\s*(?:,|&|\band\b|\bplus\b)\s*", text) if x.strip()]
        return parts or [text.strip()]

    def _gather(self, what, idx):
        """Turn 'report pdf and notes txt' / 'all pdf files from downloads' into a list of paths -> (items, missing, bulk)."""
        what = re.sub(r"^(?:the |my |these |those )+", "", what.strip(), flags=re.I)
        bm = FS_BULK.match(what)
        if bm:
            src = bm.group("src")
            folder = resolve_folder(src, idx) if src else None
            if folder is None:
                return [], [src or "the folder you mean"], True
            ext = self._ext(bm.group("ext"))
            noun = (bm.group("noun") or "").lower()
            allowed = {ext} if ext else KIND_GROUPS.get(noun)
            try:
                kids = [k for k in folder.iterdir() if not k.name.startswith(".")]
            except OSError:
                kids = []
            if noun == "folders":
                items = [k for k in kids if k.is_dir()]
            else:
                items = [k for k in kids if k.is_file() and (allowed is None or k.suffix.lower().lstrip(".") in allowed)]
            return sorted(items, key=_mtime, reverse=True), ([] if items else [what]), True
        nm = FS_NAMES.match(what)
        src = nm.group("src") if nm else None
        whole, exact = pick_item(what, idx, fuzzy=False)
        if whole is not None and exact:                          # e.g. "log in guide.pdf" is one file name
            if pick_item.same_name > 1:
                self.notes.append(f"There are {pick_item.same_name} items called {whole.name}; I used the newest, in {whole.parent.name}.")
            return [whole], [], False
        if src:
            folder = resolve_folder(src, idx)
            if folder is not None:
                idx = scan_index([(folder, 3)])
            else:
                src = None
        names = self._names(nm.group("names") if nm and src else what)
        items, missing = [], []
        for n in names:
            p, _ex = pick_item(n, idx)
            if p is None:
                missing.append(n)
            elif p not in items:
                items.append(p)
                if pick_item.same_name > 1:
                    self.notes.append(f"There are {pick_item.same_name} items called {p.name}; I used the newest, in {p.parent.name}.")
        return items, missing, False

    # ----- looking
    def info(self, t):
        self.notes = []
        mm, s, pi = self._match(FS_INFO_RXS, t)
        if not mm:
            return False
        gd = mm.groupdict()
        kind = (gd.get("kind") or "file").lower()
        what = re.sub(r"^(?:called|named)\s+", "", (gd.get("what") or "").strip(), flags=re.I)
        what = re.sub(r"\s+(?:and|then)\s+(?:tell|give|show|read|list|describe|summari[sz]e|explain)\b.*$", "", what, flags=re.I)
        ext = self._ext(gd.get("ext"))
        reading = bool(re.match(r"^read\b", s, re.I))
        idx = scan_index()
        if not what and kind.startswith("document") and user_folder("documents") and not ext:
            return False                                       # "check my documents": not a file question
        if (not what and kind in ("files", "documents")) or re.match(r"^(?:(?:in|on|at|from|inside)\s+)?" + DEVICE_WORDS + r"\b", what, re.I):
            return self.overview(t, force=True)                # "read files", "read some files on my laptop"
        if re.fullmatch(r"(?:folder|directory)", what, re.I) and user_folder(kind):
            if pi == 3:                                          # "what is in my documents folder": list it
                return self.listing(t)
            items, missing = [user_folder(kind)], []
        elif not what:
            self.o.say("Which one? For example: tell me about file report pdf.")
            return True
        else:
            scope = FS_SCOPE.match(what)
            folder = resolve_folder(scope.group("where"), idx) if scope else None
            if scope and folder is None and kind.startswith("file"):
                self.o.say(f"I couldn't find a folder called {scope.group('where')}.")
                return True
            if folder is not None:                              # "all files in downloads", "pdf files in documents"
                try:
                    kids = [k for k in folder.iterdir() if k.is_file() and not k.name.startswith(".")]
                except OSError:
                    kids = []
                if ext:
                    kids = [k for k in kids if k.suffix.lower().lstrip(".") == ext]
                items, missing = sorted(kids, key=_mtime, reverse=True), []
                if not items:
                    self.o.say(f"There are no {ext + ' ' if ext else ''}files in {folder.name}.")
                    return True
            elif kind.startswith("folder"):
                f = resolve_folder(what, idx)
                items, missing = ([f], []) if f is not None else ([], [what])
            else:
                items, missing, _b = self._gather(what, idx)
        if not items:
            self.o.say(f"I couldn't find {', '.join(missing)}." if missing else "I couldn't find that.")
            return True
        self._report(items, missing, reading)
        return True

    def _nickname_in(self, low):
        """True when the sentence names a folder you gave a nickname to ('what files are in receipts')."""
        try:
            return self.o.mem_on() and any(re.search(r"\b" + re.escape(a) + r"\b", low) for a in self.o.memory.folder_aliases())
        except Exception:
            return False

    def overview(self, t, force=False):
        """'read several files on my laptop', 'show me my files', 'what files do I have', 'how many pdf files are on my
        desktop': looks in the folders you name, or in all your usual ones, and tells you about the newest files."""
        self.notes = []
        s = self._raw(t)
        low = s.lower()
        if FS_NOT_FILES.search(low) or not (force or FS_ANY_CUE.search(low) or self._nickname_in(low)):
            return False
        folders = []
        for key in USER_FOLDER_NAMES:
            if re.search(r"\b" + re.escape(key) + r"\b", low):
                f = user_folder(key)
                if f and f not in folders:
                    folders.append(f)
        try:
            if self.o.mem_on():
                for alias in self.o.memory.folder_aliases():
                    if re.search(r"\b" + re.escape(alias) + r"\b", low):
                        f = user_folder(alias)
                        if f and f not in folders:
                            folders.append(f)
        except Exception:
            logger.exception("folder nickname lookup failed")
        named = bool(folders)
        if not folders:
            folders = [f for f in (user_folder(n) for n in ("desktop", "documents", "downloads", "pictures", "videos", "music")) if f]
        ext = next((w for w in re.findall(r"[a-z0-9]{2,5}", low) if w in EXT_WORDS and w not in ("exe", "ini", "log")), "")
        group = next((g for g in KIND_GROUPS if re.search(r"\b" + g + r"\b", low)), "")
        allowed = {ext} if ext else (KIND_GROUPS[group] if group else None)
        files = []
        for f in folders:
            try:
                files += [k for k in f.iterdir() if k.is_file() and not k.name.startswith(".")
                          and k.name.lower() not in ("desktop.ini", "thumbs.db")]
            except OSError:
                pass
        if allowed:
            files = [k for k in files if k.suffix.lower().lstrip(".") in allowed]
        files.sort(key=_mtime, reverse=True)
        names = [f.name for f in folders]
        where = (" and ".join(names) if len(names) <= 2 else ", ".join(names[:-1]) + " and " + names[-1]) if named else \
            "your usual folders (" + ", ".join(names) + ")"
        kind_word = (ext + " " if ext else group + " " if group else "")
        if not files:
            self.o.say(f"I didn't find any {kind_word}files in {where}.")
            return True
        words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
                 "several": 5, "some": 5, "few": 5}
        nm = re.search(r"\b(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|several|some|few)\b(?:\s+\w+){0,2}?\s+(?:files|documents)\b", low)
        limit = min(int(nm.group(1)) if nm and nm.group(1).isdigit() else words.get(nm.group(1), 5) if nm else 5, 12)
        counting = re.search(r"\bhow many\b", low)
        reading = nm or re.search(r"\b(?:read|tell|describe|info|information|details|inspect|analy[sz]e|summari[sz]e|about|several|some|few|review|examine|look at|go through)\b", low)
        if reading and not counting:
            self._report(files[:limit], [], reading=bool(re.search(r"\bread\b", low)))
            return True
        lines = []
        for k in files[:30]:
            lines.append(f"{k.name}  ({k.parent.name}, {human_size(k.stat().st_size)}, {human_age(_mtime(k))})")
        if len(files) > 30:
            lines.append(f"... and {len(files) - 30} more.")
        self.o.emit("sys", "\n".join(lines))
        if counting:
            self.o.say(f"There are {_plural(len(files), kind_word + 'file')} in {where}.")
        else:
            top = [k.name for k in files[:3]]
            self.o.say(f"I found {_plural(len(files), kind_word + 'file')} in {where}. The newest "
                       f"{'is' if len(top) == 1 else 'are'} {', '.join(top[:-1]) + ' and ' + top[-1] if len(top) > 1 else top[0]}. "
                       "The full list is in the chat. Say read several files to hear about them.")
        return True

    def _report(self, items, missing, reading=False):
        shown = items[:12]
        block, facts = [], []
        for p in shown:
            try:
                d = describe(p)
            except OSError as e:
                block.append(f"{p.name}: I can't open it ({e})\n")
                continue
            facts.append((p, d))
            block.append(d["name"] + "\n  " + "\n  ".join(d["lines"]) + "\n")
        if len(items) > len(shown):
            block.append(f"... and {len(items) - len(shown)} more.")
        self.o.emit("sys", "\n".join(block).strip())
        if not facts:
            self.o.say("I couldn't open " + ("those." if len(items) > 1 else "that."))
            return
        if len(facts) == 1:
            p, d = facts[0]
            if reading and p.is_file():
                text = extract_text(p, 600)
                if text:
                    self.o.say(f"{p.name} starts: {text}")
                    return
            speak = d["headline"] + (f" It starts: {d['preview']}" if reading and d["preview"] else "")
        else:
            speak = f"I looked at {len(items)} items. " + " ".join(d["short"] + "." for _p, d in facts[:4])
            if len(items) > 4:
                speak += f" And {len(items) - 4} more, listed in the chat."
        if missing:
            speak += f" I couldn't find {', '.join(missing)}."
        self.o.say(" ".join([speak] + self.notes))

    def listing(self, t):
        mm, s, i = self._match(FS_LIST_RXS, t)
        if not mm:
            return False
        where = mm.group("where")
        ext = self._ext(mm.groupdict().get("ext"))
        if re.match(r"^" + DEVICE_WORDS + r"\b", where, re.I) or \
                (i == 0 and re.search(r"\b(?:\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)\s+(?:\w+\s+)?files\b", s, re.I)):
            return self.overview(t, force=True)
        if i == 2 and not re.search(r"\b(?:folder|directory)\b", s, re.I) \
                and norm(where) not in ("downloads", "documents", "desktop", "pictures", "videos", "music", "home"):
            return False                                         # "what is in the picture" is not a folder question
        folder = resolve_folder(where, scan_index(), strict=(i == 2))
        if folder is None:
            if i == 2:
                return False                                     # "what is in the news": not about a folder
            self.o.say(f"I couldn't find a folder called {where}.")
            return True
        try:
            kids = [k for k in folder.iterdir() if not k.name.startswith(".") and k.name.lower() not in ("desktop.ini", "thumbs.db")]
        except OSError as e:
            self.o.say(f"I can't open {folder.name}: {e}")
            return True
        files = [k for k in kids if k.is_file()]
        if ext:
            files = [k for k in files if k.suffix.lower().lstrip(".") == ext]
        folders = [k for k in kids if k.is_dir()] if not ext else []
        shown = sorted(files + folders, key=_mtime, reverse=True)
        lines = []
        for k in shown[:30]:
            if k.is_dir():
                lines.append(f"[folder]  {k.name}  ({human_age(_mtime(k))})")
            else:
                lines.append(f"{k.name}  ({human_size(k.stat().st_size)}, {human_age(_mtime(k))})")
        if len(shown) > 30:
            lines.append(f"... and {len(shown) - 30} more.")
        self.o.emit("sys", f"{folder}\n" + ("\n".join(lines) if lines else "(nothing here)"))
        if not shown:
            self.o.say(f"There's nothing {'of that type ' if ext else ''}in {folder.name}.")
            return True
        if ext:
            self.o.say(f"{folder.name} has {_plural(len(files), ext + ' file')}. The newest is {shown[0].name}.")
            return True
        kinds = collections.Counter((KIND_NAMES.get(k.suffix.lower().lstrip(".")) or "other") for k in files)
        top = kinds.most_common(1)[0] if kinds else None
        mostly = f" Mostly {top[0]}s." if top and top[1] >= 3 and top[1] >= 0.4 * len(files) and top[0] != "other" else ""
        self.o.say(f"{folder.name} has {_plural(len(files), 'file')} and {_plural(len(folders), 'folder')}." + mostly + f" The newest is {shown[0].name}. The full list is in the chat.")
        return True

    # ----- moving
    def move(self, t):
        self.notes = []
        mm, s, _i = self._match([FS_MOVE_RX, FS_MOVE2_RX], t)
        if not mm:
            return False
        what, dest_txt = mm.group("what").strip(), mm.group("dest").strip()
        idx = scan_index()
        items, missing, bulk = self._gather(what, idx)
        if bulk and not items:
            if missing and missing[0] == "the folder you mean":
                self.o.say("Tell me which folder to take them from, for example: move all pdf files from downloads to documents.")
            else:
                self.o.say(f"I couldn't find anything matching {what}.")
            return True
        if not items:
            self.o.say(f"I couldn't find {', '.join(missing)} to move." if missing else "I couldn't find that to move.")
            return True
        nm = FS_NEWDEST.match(dest_txt)
        dest, create, asked = None, None, False
        if nm:                                                   # "to a new folder called Taxes": you asked for it
            create = items[0].parent / safe_filename(nm.group("name"))
            asked = True
            if create.is_dir():
                dest, create = create, None
        else:
            dm = FS_DESTIN.match(dest_txt)
            if dm and resolve_folder(dm.group("p"), idx) is not None and resolve_folder(dest_txt, idx, strict=True) is None:
                parent = resolve_folder(dm.group("p"), idx)
                dest = find_child_folder(parent, dm.group("d"))
                if dest is None:
                    create = parent / safe_filename(dm.group("d"))
            else:
                dest = resolve_folder(dest_txt, idx)
                if dest is None:
                    create = items[0].parent / safe_filename(dest_txt)
        n = len(items)
        label = (create or dest).name

        def go():
            target = dest
            try:
                if create is not None:
                    create.mkdir(parents=True, exist_ok=True)
                    target = create
            except OSError as e:
                self.o.say(f"I couldn't create {create.name}: {e}")
                return
            self._do_move(items, target, missing, created=create is not None)
        if create is not None and not asked:
            self.o.ask(f"There's no folder called {label}. Shall I create it in {create.parent.name} and move "
                       f"{'it' if n == 1 else _plural(n, 'item')} there?", go)
        elif bulk or n > self.BIG_MOVE:
            self.o.ask(f"Move {_plural(n, 'item')} to {label}? Say yes to go ahead.", go)
        else:
            go()
        return True

    def _do_move(self, items, dest, missing, created=False):
        moved, failed = move_items(items, dest)
        if moved:
            self.history = (self.history + [moved])[-10:]
        lines = [f"{a.name}  ->  {b}" for a, b in moved] + [f"{p.name}: not moved, {why}" for p, why in failed]
        if lines:
            self.o.emit("sys", "\n".join(lines))
        if not moved:
            self.o.say("I didn't move anything: " + "; ".join(f"{p.name} {why}" for p, why in failed[:2]) + ".")
            return
        msg = (f"Moved {moved[0][0].name}" if len(moved) == 1 else f"Moved {len(moved)} items") + f" to {dest.name}"
        msg += " (a new folder)." if created else "."
        if failed:
            msg += f" {_plural(len(failed), 'item')} couldn't be moved, see the chat."
        if missing:
            msg += f" I couldn't find {', '.join(missing)}."
        self.o.say(" ".join([msg] + self.notes + ["Say undo move to put them back."]))

    def undo(self, t):
        if not self.history:
            self.o.say("There's no move to undo.")
            return True
        batch = self.history.pop()
        back, failed = 0, []
        for src, target in reversed(batch):
            try:
                if not target.exists():
                    failed.append(target.name)
                    continue
                src.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(unique_path(src.parent, src.name)))
                back += 1
            except OSError:
                failed.append(target.name)
        self.o.say(f"Put {_plural(back, 'item')} back where they were." + (f" I couldn't restore {', '.join(failed)}." if failed else ""))
        return True

    # ----- creating
    def _where_name(self, what, idx):
        """'Taxes in documents' -> (parent folder, 'Taxes', content)."""
        tm = FS_TAIL.match(what.strip())
        names, where, content = (tm.group("names"), tm.group("where"), tm.group("content")) if tm else (what, None, None)
        parent = resolve_folder(where, idx) if where else None
        if where and parent is None:                             # "in" was part of the name after all
            names, content = what, None
            tm2 = re.match(r"^(?P<n>.+?)\s+(?:with|containing|saying)(?: the)?(?: text| content| contents)?\s+(?P<c>.+)$", what, re.I)
            if tm2:
                names, content = tm2.group("n"), tm2.group("c")
        return parent or default_parent(), names.strip(), (content or "").strip()

    def create_folder(self, t):
        mm, s, _i = self._match([FS_NEWDIR_RX], t)
        if not mm:
            return False
        what = (mm.group("what") or "").strip()
        lm = re.match(r"^(?:in|on|inside|under|at)\s+(?:the |my )?(?P<w>.+?)(?: folder| directory)?$", what, re.I)
        if lm and resolve_folder(lm.group("w"), scan_index()) is not None:       # only a place was given
            self.o.say("What should the folder be called?")
            self.o.awaiting = lambda ans, w=lm.group("w"): self._make_folders(ans.strip().rstrip(".!?") + " in " + w)
            return True
        if not what:
            self.o.say("What should the folder be called?")
            self.o.awaiting = lambda ans: self._make_folders(ans.strip().rstrip(".!?"))
            return True
        self._make_folders(what)
        return True

    def _make_folders(self, what):
        parent, names, _c = self._where_name(what, scan_index())
        made, existed = [], []
        for n in self._names(names):
            try:
                if _protected(parent):
                    self.o.say(f"I won't create things in {parent.name}, it's a protected place.")
                    return
                path, created = make_folder(parent, n)
                (made if created else existed).append(path)
            except OSError as e:
                self.o.say(f"I couldn't create {n}: {e}")
                return
        where = f"in {parent.name}" if parent != user_folder("desktop") else "on the Desktop"
        parts = []
        if made:
            rel = [str(p.relative_to(parent)) for p in made]
            parts.append(f"Created {'the folder ' + rel[0] if len(made) == 1 else _plural(len(made), 'folder') + ': ' + ', '.join(rel)} {where}.")
        if existed:
            parts.append(f"{', '.join(p.name for p in existed)} already {'exists' if len(existed) == 1 else 'exist'}.")
        self.o.emit("sys", "\n".join(str(p) for p in made + existed))
        self.o.say(" ".join(parts))

    def create_file(self, t):
        mm, s, _i = self._match([FS_NEWFILE_RX], t)
        if not mm:
            return False
        gd = mm.groupdict()
        ktype = (gd.get("ktype") or "").lower()
        noun = (gd.get("noun") or "file").lower()
        default_ext = (MAKE_KINDS.get(ktype) or ("xlsx" if noun.startswith(("spreadsheet", "workbook")) else
                       "py" if noun.startswith("script") else "docx" if noun.startswith("doc") else "txt"))
        what = (gd.get("what") or "").strip()
        lm = re.match(r"^(?:in|on|inside|under|at)\s+(?:the |my )?(?P<w>.+?)(?: folder| directory)?$", what, re.I)
        if lm and resolve_folder(lm.group("w"), scan_index()) is not None:       # only a place was given
            self.o.say("What should the file be called?")
            self.o.awaiting = lambda ans, w=lm.group("w"): self._make_files(ans.strip().rstrip(".!?") + " in " + w, default_ext)
            return True
        if not what:
            self.o.say("What should the file be called?")
            self.o.awaiting = lambda ans: self._make_files(ans.strip().rstrip(".!?"), default_ext)
            return True
        self._make_files(what, default_ext)
        return True

    def _make_files(self, what, default_ext):
        parent, names, content = self._where_name(what, scan_index())
        if _protected(parent):
            self.o.say(f"I won't create things in {parent.name}, it's a protected place.")
            return
        made = []
        for n in ([names] if content else self._names(names)):
            try:
                made.append(make_file(parent, n, content, default_ext))
            except OSError as e:
                self.o.say(f"I couldn't create {n}: {e}")
                return
        where = f"in {parent.name}" if parent != user_folder("desktop") else "on the Desktop"
        self.o.emit("sys", "\n".join(str(p) for p in made))
        what_made = made[0].name if len(made) == 1 else f"{len(made)} files: " + ", ".join(p.name for p in made)
        self.o.say(f"Created {what_made} {where}" + (f", with your text in it." if content else "."))


SHELF_PS = r"""
param([string]$list)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$files = @(Get-Content -LiteralPath $list -Raw -Encoding UTF8 | ConvertFrom-Json)
$bg   = [System.Drawing.Color]::FromArgb(4,6,12)
$tile = [System.Drawing.Color]::FromArgb(14,30,70)
$red  = [System.Drawing.Color]::FromArgb(77,166,255)
$form = New-Object System.Windows.Forms.Form
$form.Text = 'Phone files'
$form.TopMost = $true
$form.ShowInTaskbar = $false
$form.FormBorderStyle = 'FixedToolWindow'
$form.StartPosition = 'Manual'
$form.BackColor = $bg
$form.AutoScroll = $true
$wa = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$w = 320
$rows = [Math]::Min($files.Count, 6)
$h = [int](48 + $rows * 66 + 44)
$form.ClientSize = New-Object System.Drawing.Size($w, $h)
$x = [int]($wa.Right - $w - 30)
$y0 = [int]($wa.Top + 60)
$form.Location = New-Object System.Drawing.Point($x, $y0)
$hint = New-Object System.Windows.Forms.Label
$hint.Text = 'Pinch a file = grab. Let go = drop.'
$hint.ForeColor = $red
$hint.Font = New-Object System.Drawing.Font('Segoe UI', 10, [System.Drawing.FontStyle]::Bold)
$hint.Location = New-Object System.Drawing.Point(12, 14)
$hint.Size = New-Object System.Drawing.Size(($w - 24), 24)
$form.Controls.Add($hint)
$mouseDown = {
  param($s, $e)
  if ($e.Button -ne [System.Windows.Forms.MouseButtons]::Left) { return }
  if (-not (Test-Path -LiteralPath $s.Tag)) { return }
  $d = New-Object System.Windows.Forms.DataObject
  $d.SetData([System.Windows.Forms.DataFormats]::FileDrop, [string[]]@([string]$s.Tag))
  $eff = $s.DoDragDrop($d, [System.Windows.Forms.DragDropEffects]::Copy)
  if ($eff -ne [System.Windows.Forms.DragDropEffects]::None) {
    $s.BackColor = [System.Drawing.Color]::FromArgb(20,80,35)
    $s.Text = 'Dropped: ' + [System.IO.Path]::GetFileName([string]$s.Tag)
  }
}
$y = 48
foreach ($p in $files) {
  $p = [string]$p
  if (-not (Test-Path -LiteralPath $p)) { continue }
  $item = Get-Item -LiteralPath $p
  $kb = [Math]::Max(1, [int]($item.Length / 1024))
  if ($kb -ge 1024) { $size = ('{0:N1} MB' -f ($kb / 1024)) } else { $size = "$kb KB" }
  $l = New-Object System.Windows.Forms.Label
  $l.Tag = $p
  $l.Text = $item.Name + "`r`n" + $size
  $l.AutoEllipsis = $true
  $l.BackColor = $tile
  $l.ForeColor = [System.Drawing.Color]::White
  $l.Font = New-Object System.Drawing.Font('Segoe UI', 10)
  $l.Padding = New-Object System.Windows.Forms.Padding(10, 8, 6, 4)
  $l.Cursor = [System.Windows.Forms.Cursors]::Hand
  $l.Location = New-Object System.Drawing.Point(12, $y)
  $l.Size = New-Object System.Drawing.Size(($w - 24), 58)
  $l.Add_MouseDown($mouseDown)
  $form.Controls.Add($l)
  $y += 66
}
$btn = New-Object System.Windows.Forms.Button
$btn.Text = 'Close shelf'
$btn.Dock = 'Bottom'
$btn.Height = 36
$btn.FlatStyle = 'Flat'
$btn.BackColor = $red
$btn.ForeColor = [System.Drawing.Color]::Black
$btn.Add_Click({ $form.Close() })
$form.Controls.Add($btn)
[System.Windows.Forms.Application]::Run($form)
"""


class PhoneShelf:
    """A small always-on-top window that lists the files from your phone. Each tile is a real Windows drag source,
    so it can be dragged by mouse or by PAC's air drag (pinch = grab, let go = drop) into File Explorer, the
    desktop or a website's upload box."""

    def __init__(self):
        self.proc = None

    def alive(self):
        return self.proc is not None and self.proc.poll() is None

    def show(self, paths):
        paths = [str(p) for p in paths if Path(p).exists()]
        if not paths or OS != "Windows":
            return False
        self.close()
        try:
            lst = DATA_DIR / "shelf.json"
            lst.write_text(json.dumps(paths), encoding="utf-8")
            ps = DATA_DIR / "shelf.ps1"
            ps.write_text(SHELF_PS, encoding="utf-8-sig")
            self.proc = subprocess.Popen(
                ["powershell", "-NoProfile", "-Sta", "-ExecutionPolicy", "Bypass", "-WindowStyle", "Hidden",
                 "-File", str(ps), str(lst)], creationflags=NO_WINDOW)
            return True
        except Exception:
            logger.exception("shelf failed to start")
            return False

    def close(self):
        if self.alive():
            try:
                self.proc.terminate()
            except Exception:
                pass
        self.proc = None




# ---------------------------------------------------------------- understanding the sentence, not just the keyword
_NOUNS = (r"(?:poems?|poetry|stor(?:y|ies)|essays?|articles?|letters?|e-?mails?|mails?|speech(?:es)?|paragraphs?|"
          r"summar(?:y|ies)|songs?|lyrics|jokes?|scripts?|code|programs?|functions?|captions?|bios?|resumes?|cv|"
          r"cover letters?|reports?|plans?|outlines?|lists?|ideas?|slogans?|taglines?|posts?|tweets?|blogs?|reviews?|"
          r"explanations?|descriptions?|sentences?|quotes?|haiku|limericks?|rhymes?|applications?|proposals?|"
          r"presentations?|slides?|abstracts?|conclusions?|introductions?|assignments?|recipes?|itinerary|agenda|"
          r"schedules?|routines?|questions?|quiz(?:zes)?|answers?)")
_COMPOSE = re.compile(
    r"^(?:please )?(?P<v>write|compose|draft|generate|come up with|put together|prepare|produce|create|make|build|"
    r"type(?: out)?)\s+(?:me |us |him |her |them )?(?P<rest>.+)$")
_ARTICLE_NOUN = re.compile(rf"^(?:an?|some|another)\s+(?:[\w'-]+\s+){{0,3}}?{_NOUNS}\b")
_BARE_NOUN = re.compile(rf"^(?:[\w'-]+\s+)?{_NOUNS}\s+(?:about|on|regarding|for|of|that|which|explaining|describing)\b")
_TYPE_NOUN = re.compile(rf"^an?\s+(?:[\w'-]+\s+){{0,2}}?{_NOUNS}\s+(?:about|on|regarding|for|that|which|explaining|describing)\b")
_DOC_NOUN = re.compile(r"^(?:an?|the|another)\s+(?:[\w'-]+\s+){0,2}?(?:document|doc|spreadsheet|workbook|sheet|presentation|report)\b")
_CONTENT_MARK = re.compile(r"\b(?:about|on|regarding|explaining|describing|containing|that (?:says|explains|describes|lists|covers)|with (?:text|content|details))\b")
_NAMED = re.compile(r"\b(?:called|named|name)\b")


def compose_intent(t):
    """True when the sentence asks PAC to THINK UP new content ("write a poem about my dog", "create a document about
    my trip") rather than to run a command ("type hello", "create a file called notes.txt"). The verb alone decides nothing."""
    m = _COMPOSE.match(t)
    if not m:
        return False
    v, rest = m.group("v"), m.group("rest").strip()
    if v.startswith("type"):
        return bool(_TYPE_NOUN.match(rest))
    if v in ("create", "make", "build", "prepare", "produce") and _NAMED.search(rest):
        return False                                   # "create a document called plan": a named file, not a request
    if _ARTICLE_NOUN.match(rest) or _BARE_NOUN.match(rest):
        return True
    if v in ("create", "make", "build", "prepare", "produce", "generate") and _DOC_NOUN.match(rest):
        return bool(_CONTENT_MARK.search(rest)) and not _NAMED.search(rest)
    return False


_EXPLAIN_Q = re.compile(
    r"^(?:how (?:does|do|did|is|are|can|come|would|could)\b|why\b|explain\b|describe\b|define\b|"
    r"what (?:is|are|was|were) (?:a|an|the (?:meaning|history|point|purpose|difference|cause|reason|use))\b|"
    r"what does\b|who (?:invented|made|created|discovered|wrote)\b|tell me (?:about|how|why)\b|"
    r"history of\b|meaning of\b|difference between\b|should i\b|is it (?:safe|bad|okay|ok|good)\b)")


def reads_as_command(t):
    """For handlers triggered by a single keyword anywhere in the sentence (restart, battery, timer, joke...):
    only act if the sentence is short and is not a how/why/explain question about that word."""
    return len(t.split()) <= 9 and not _EXPLAIN_Q.match(t)



_SEP = re.compile(r"\s+(?:and then|and also|then|after that|and)\s+")
_NO_SPLIT = re.compile(r"^(?:type|write|dictate|note|take (?:a )?note|remember|message|text|whatsapp|send|call|compose|draft|"
                       r"create|make|add|learn|teach|my |i |remind)\b")


def compound_parts(t, understands):
    """"open chrome and search for cats" -> ["open chrome", "search for cats"], but only when EVERY piece is a
    sentence PAC already understands on its own. "salt and pepper", "type this and that" are never split."""
    if len(t.split()) < 4 or _NO_SPLIT.match(t):
        return None
    pieces = [p.strip() for p in _SEP.split(t) if p.strip()]
    if not 2 <= len(pieces) <= 4:
        return None
    return pieces if all(understands(p) for p in pieces) else None


# ---------------------------------------------------------------- phone link: QR pairing, events, contacts, calls
DISCOVERY_PORT = 8766                     # UDP: the phone shouts here to find this PC again if its Wi-Fi address changes
PHONEBOOK_FILE = DATA_DIR / "phone_contacts.json"

QR_WINDOW_SCRIPT = r"""
import sys, tkinter as tk
import segno
url = sys.argv[1]
m = segno.make(url, error="m").matrix
n, border, px = len(m), 4, 8
size = (n + 2 * border) * px
root = tk.Tk()
root.title("PAC - pair your phone")
root.configure(bg="white")
tk.Label(root, text="On your phone: open PAC and type  pair  (or Settings > Scan QR code)",
         bg="white", fg="black", font=("Segoe UI", 11)).pack(padx=16, pady=(14, 6))
cv = tk.Canvas(root, width=size, height=size, bg="white", highlightthickness=0)
cv.pack(padx=16, pady=6)
for y, row in enumerate(m):
    for x, v in enumerate(row):
        if v:
            cv.create_rectangle((x + border) * px, (y + border) * px, (x + border + 1) * px, (y + border + 1) * px,
                                fill="black", outline="black")
tk.Label(root, text="Anyone who sees this code can link to this PC. It closes by itself once your phone connects.",
         bg="white", fg="#555", font=("Segoe UI", 9)).pack(padx=16, pady=(0, 6))
tk.Button(root, text="Close", command=root.destroy).pack(pady=(0, 12))
root.attributes("-topmost", True)
root.after(300000, root.destroy)
root.mainloop()
"""


def clean_phone_text(s, limit=300):
    """Text that came from the phone is shown and spoken, so strip control characters, hide one-time codes, cap length."""
    s = re.sub(r"[\x00-\x1f\x7f]+", " ", str(s or "")).strip()
    if re.search(r"\b(?:otp|one[- ]time|verification|verify|passcode|security code|login code|code)\b", s, re.I):
        s = re.sub(r"\d(?:[\s-]?\d){3,7}", "[code hidden]", s)
    return s[:limit]


def load_phonebook():
    try:
        rows = json.loads(PHONEBOOK_FILE.read_text(encoding="utf-8"))
        return [(str(a), str(b)) for a, b in rows]
    except (OSError, ValueError, TypeError):
        return []


def save_phonebook(rows):
    PHONEBOOK_FILE.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")


def find_contacts(book, query):
    """People matching a spoken name, best match first: exact, starts with, every word found, contains, then spelling-tolerant."""
    norm = lambda x: re.sub(r"\s+", " ", re.sub(r"[^\w ]", " ", x.lower())).strip()
    q = norm(query)
    if not q:
        return []
    rows = [(norm(n), n, num) for n, num in book]
    words = q.split()

    def close(w, nw):
        return any(x.startswith(w) or difflib.SequenceMatcher(None, w, x).ratio() >= (0.7 if len(w) > 4 else 0.8 if len(w) > 3 else 1.0) for x in nw)
    tiers = [lambda r: r[0] == q,
             lambda r: r[0].startswith(q),
             lambda r: all(any(x.startswith(w) for x in r[0].split()) for w in words),
             lambda r: q in r[0],
             lambda r: all(close(w, r[0].split()) for w in words)]
    for t in tiers:
        hit = [r for r in rows if t(r)]
        if hit:
            seen, out = set(), []
            for _, n, num in hit:
                if n not in seen:
                    seen.add(n)
                    out.append((n, num))
            return out
    return []


class PhoneTransfer:
    def __init__(self, cfg, on_receive=None, on_event=None, on_contacts=None):
        self.cfg = cfg
        self.on_receive = on_receive
        self.on_event = on_event            # called with the dict the phone POSTs to /event (missed call, sms, hello)
        self.on_contacts = on_contacts      # called with the dict the phone POSTs to /contacts
        self.outbox = queue.Queue()         # commands for the phone; it long-polls /poll to collect them
        self.last_poll = 0.0
        self.udp = None
        self.root = HOME / "PAC_Transfer"
        self.inbox = self.root / "Received"
        self.token = ""
        self.port = 0
        self.held = None            # the one file the phone may download
        self.received = []          # everything the phone sent (newest last)
        self.unplaced = []          # received but not yet "dropped" somewhere
        self.server = None

    def running(self):
        return self.server is not None

    @staticmethod
    def lan_ip():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.255.255.255", 1))          # no packet is sent; it just picks the Wi-Fi/LAN address
            return s.getsockname()[0]
        except OSError:
            return "127.0.0.1"
        finally:
            s.close()

    def url(self, host=None):
        return f"http://{host or self.lan_ip()}:{self.port}/?t={self.token}"

    def start(self):
        if self.server:
            return self.url()
        self.inbox.mkdir(parents=True, exist_ok=True)
        # The secret is kept between sessions, so a phone paired once by QR stays paired. "unpair my phone" replaces it.
        self.token = str(self.cfg.get("phone_token") or "")
        if len(self.token) < 8:
            self.token = secrets.token_urlsafe(12)
            self.cfg["phone_token"] = self.token
            try:
                save_config(self.cfg)
            except Exception:
                logger.exception("could not save the phone token")
        owner = self
        max_bytes = int(self.cfg.get("transfer_max_mb", 500)) * 1024 * 1024

        class Handler(http.server.BaseHTTPRequestHandler):
            timeout = 60

            def log_message(self, *a):
                pass

            def _ok(self):
                q = parse_qs(urlparse(self.path).query)
                good = secrets.compare_digest(q.get("t", [""])[0].encode(), owner.token.encode())
                if not good:
                    self._send(403, b"Forbidden", "text/plain")
                return good, q

            def _send(self, code, body, ctype="application/json", extra=None):
                self.send_response(code)
                self.send_header("Content-Type", ctype + ("; charset=utf-8" if ctype.startswith("text") else ""))
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                for k, v in (extra or {}).items():
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                good, q = self._ok()
                if not good:
                    return
                path = urlparse(self.path).path
                if path == "/":
                    self._send(200, TRANSFER_PAGE.encode("utf-8"), "text/html")
                elif path == "/state":
                    h = owner.held
                    ok = bool(h and h.is_file())
                    size = h.stat().st_size if ok else 0
                    pretty = f"{size / 1048576:.1f} MB" if size >= 1048576 else f"{max(1, size // 1024)} KB"
                    self._send(200, json.dumps({"held": h.name if ok else None, "size": pretty, "max_mb": max_bytes // 1048576,
                                                "received": [p.name for p in owner.received[-8:]][::-1]}).encode())
                elif path == "/poll":
                    owner.last_poll = time.time()
                    try:
                        cmd = owner.outbox.get(timeout=25)        # hold the request open until PAC has something to say
                    except queue.Empty:
                        cmd = {}
                    owner.last_poll = time.time()
                    self._send(200, json.dumps(cmd).encode())
                elif path == "/get":
                    h = owner.held
                    if not (h and h.is_file()):
                        return self._send(404, b"Nothing is being held", "text/plain")
                    ascii_name = re.sub(r'[^A-Za-z0-9._-]', "_", h.name) or "file"
                    self.send_response(200)
                    self.send_header("Content-Type", "application/octet-stream")
                    self.send_header("Content-Length", str(h.stat().st_size))
                    self.send_header("Content-Disposition",
                                     f"attachment; filename=\"{ascii_name}\"; filename*=UTF-8''{quote(h.name)}")
                    self.end_headers()
                    try:
                        with open(h, "rb") as f:
                            shutil.copyfileobj(f, self.wfile, 65536)
                    except (BrokenPipeError, ConnectionError, OSError):
                        pass
                else:
                    self._send(404, b"Not found", "text/plain")

            def do_POST(self):
                good, q = self._ok()
                if not good:
                    return
                route = urlparse(self.path).path
                if route in ("/event", "/contacts"):
                    try:
                        n = int(self.headers.get("Content-Length", "0"))
                    except ValueError:
                        n = 0
                    if n <= 0 or n > 4 * 1024 * 1024:
                        return self._send(400, b"Bad size", "text/plain")
                    try:
                        data = json.loads(self.rfile.read(n).decode("utf-8", "replace"))
                        if not isinstance(data, dict):
                            raise ValueError
                    except ValueError:
                        return self._send(400, b"Bad JSON", "text/plain")
                    self._send(200, b'{"ok": true}')
                    cb = owner.on_event if route == "/event" else owner.on_contacts
                    if cb:
                        try:
                            cb(data)
                        except Exception:
                            logger.exception("phone callback failed")
                    return
                if route != "/up":
                    return self._send(404, b"Not found", "text/plain")
                try:
                    length = int(self.headers.get("Content-Length", "0"))
                except ValueError:
                    length = 0
                if length <= 0:
                    return self._send(400, b"Empty upload", "text/plain")
                if length > max_bytes:
                    self.close_connection = True
                    return self._send(413, b"File is too big", "text/plain", {"Connection": "close"})
                name = safe_filename((q.get("name") or ["file"])[0])
                dest = owner.inbox / name
                n = 1
                while dest.exists():
                    dest = owner.inbox / f"{Path(name).stem} ({n}){Path(name).suffix}"
                    n += 1
                part = dest.with_name(dest.name + ".part")
                got = 0
                try:
                    with open(part, "wb") as f:
                        while got < length:
                            chunk = self.rfile.read(min(65536, length - got))
                            if not chunk:
                                break
                            f.write(chunk)
                            got += len(chunk)
                    if got != length:
                        part.unlink(missing_ok=True)
                        return self._send(400, b"Upload was cut off", "text/plain")
                    part.replace(dest)
                except OSError as e:
                    logger.warning("transfer write failed: %s", e)
                    try:
                        part.unlink(missing_ok=True)
                    except OSError:
                        pass
                    return self._send(500, b"Could not save the file", "text/plain")
                owner.received.append(dest)
                owner.unplaced.append(dest)
                self._send(200, json.dumps({"ok": True, "name": dest.name}).encode())
                if owner.on_receive:
                    try:
                        owner.on_receive(dest)
                    except Exception:
                        logger.exception("on_receive failed")

        base = int(self.cfg.get("transfer_port", 8765))
        err = None
        for port in range(base, base + 10):
            try:
                srv = http.server.ThreadingHTTPServer(("0.0.0.0", port), Handler)
                break
            except OSError as e:
                err = e
        else:
            raise err
        srv.daemon_threads = True
        self.port = srv.server_address[1]
        self.server = srv
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        self._start_discovery()
        return self.url()

    def _start_discovery(self):
        """Answers the phone's "is this PAC?" shout, so it can find this PC again when the Wi-Fi address changes."""
        import socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1.0)
            sock.bind(("0.0.0.0", DISCOVERY_PORT))
        except OSError as e:
            logger.warning("phone discovery port unavailable: %s", e)
            return
        self.udp = sock
        want = b"PAC?" + hashlib.sha256(self.token.encode()).hexdigest()[:16].encode()

        def loop():
            while self.server is not None:
                try:
                    data, addr = sock.recvfrom(128)
                except socket.timeout:
                    continue
                except OSError:
                    break
                if data.strip() == want:
                    try:
                        sock.sendto(f"PAC!{self.port}".encode(), addr)
                    except OSError:
                        pass
        threading.Thread(target=loop, daemon=True).start()

    def connected(self):
        """True while the phone's service is waiting on /poll (it re-asks every ~25 seconds)."""
        return self.server is not None and (time.time() - self.last_poll) < 45

    def send_command(self, cmd):
        self.outbox.put(cmd)

    def stop(self):
        srv, self.server = self.server, None
        if self.udp is not None:
            try:
                self.udp.close()
            except OSError:
                pass
            self.udp = None
        if srv:
            try:
                srv.shutdown()
                srv.server_close()
            except Exception:
                pass
        self.held = None


class Assistant:
    """Understands a sentence and does something about it. No GUI code in here."""

    def __init__(self, cfg, speak, emit, notify=None, request_quit=None, speaker=None):
        self.cfg = cfg
        self._speak = speak
        self.emit = emit                      # emit(who, text): who = you / pac / sys
        self.notify = notify or (lambda *a: None)
        self.request_quit = request_quit or (lambda: None)
        self.speaker = speaker
        self.pending = None                   # yes/no question waiting for an answer
        self._last_sir_style = None           # varies how 'sir' is worked into replies
        self.awaiting = None                  # waiting for free text (e.g. message body)
        self.dictating = False
        self.asleep = False
        self.source = "text"
        self.app_index = {}
        self.raw = ""                         # the sentence exactly as typed / heard
        self.kb = Knowledge()
        self.memory = Memory()                # what PAC has learned about you (~/.pac/memory.json)
        self._mem_last = None                 # (ids, time) of what was learned last, for "forget that"
        self._mem_hint_shown = False
        self._mem_shared_note = False
        self._install_memory_hooks()          # lets the file manager understand folder nicknames
        self.mailbox = MailBox(cfg)
        self.timetable = Timetable()
        self.last_reply = ""                  # for "say that again"
        self.news_token = 0                   # bumped by stop_speaking(): cancels a news reading in progress
        self.claude_on = False                # always starts OFF: nothing goes to Claude unless you say so
        self.claude_history = []              # this Claude conversation only; forgotten when the mode ends
        self.brain_history = []               # recent turns, so the AI brain understands follow-ups
        self._in_brain = False
        self.transfer = None                  # PhoneTransfer, created the first time it is needed
        self._qr_proc = None                  # the QR window, while it is open
        threading.Thread(target=self._prewarm, daemon=True).start()
        if cfg.get("phone_token"):            # a phone has been paired: keep the link listening from the start
            _t = threading.Timer(4.0, lambda: self.transfer_start(announce=False))
            _t.daemon = True
            _t.start()
        self.brain_token = 0                  # bumped by stop_speaking(): drops an AI answer still on its way
        self.search_token = 0                 # bumped by stop_speaking(): drops a quiet web search still on its way
        self.last_search = None               # {"query", "time"} - what "open in a new tab" opens
        self.mail_list = []                   # the mails last shown, so "delete mail 2" knows which one
        self.math_token = 0                   # bumped by stop_speaking(): drops a maths answer still being worked out
        self.faces = None                     # the FaceEngine, set by the window
        self.ar = None                        # the ARVision engine, set by the window
        self._last_greet = {}                 # face key -> when "welcome back" was last said
        C = lambda p, fn: (re.compile(p), fn)
        self.commands = [
            C(STOP_SPEAKING.pattern, self.c_stop),
            C(HOME_RE.pattern, self.c_home),
            C(r"^(?:please )?(?:enrol|enroll|register|remember|learn|save|add|scan)\s+(?:my |a |this |the |new |another )?face(?:\s+(?:as|for|named|called)\s+(?P<n>[a-z][a-z' -]*?))?(?:\s+as\s+(?P<r>owner|trusted|guest|family))?$", self.c_face_enroll),
            C(r"^(?:forget|delete|remove|erase)\s+(?:all |the |my )?faces?(?:\s+(?:of|for|named|called))?\s*(?P<n>[a-z][a-z' -]*)?$", self.c_face_forget),
            C(r"^(?:who(?:'s| is| are)(?: there| here| around| in front of (?:me|you|the (?:laptop|camera|screen))| at the (?:laptop|camera|screen))|who (?:do you see|can you see)|do you see (?:anyone|anybody|someone)|is (?:anyone|anybody|someone) (?:there|here|around)|look around)$", self.c_face_who),
            C(r"^(?:list|show|which)\s+(?:the |my )?(?:known |saved |enrolled )?(?:faces|people)$|^who do you know$", self.c_face_list),
            C(r"^(?:(?P<on>turn on|enable|start|activate|switch on)|(?P<off>turn off|disable|stop|deactivate|switch off))\s+(?:the )?face (?:recognition|detection|watch|scanning)$", self.c_face_watch),
            C(r"^(?:(?P<on>turn on|enable|start|activate|switch on)|(?P<off>turn off|disable|stop|deactivate|switch off))\s+(?:the )?face (?:security|lock|protection|guard|authentication|verification)$", self.c_face_security),
            C(r"^(?:make|set)\s+(?P<n>[a-z][a-z' -]*?)\s+(?:an? |as (?:an? )?|to )?(?P<r>owner|trusted|guest|family)$", self.c_face_role),
            C(r"^when\s+(?P<n>[a-z][a-z' -]*?)\s+(?:arrives?|comes in|comes home|is seen|shows up|walks in|appears|gets home|is here)\s*,?\s*(?:then )?(?P<cmd>.+)$", self.c_face_arrival),
            C(r"^(?:clear|remove|delete|cancel)\s+(?:the )?arrival (?:command|action)(?: for (?P<n>[a-z][a-z' -]*))?$", self.c_face_arrival_clear),
            C(r"^face rules?$|^(?:list|show) (?:the )?face rules$", self.c_face_rules_list),
            C(r"^face rule\s+(?P<g>[a-z]+)\s+(?P<lvl>anyone|guest|trusted|owner)$", self.c_face_rule),
            C(r"^(?:(?P<on>turn on|enable|start|activate|switch on|open|launch)|(?P<off>turn off|disable|stop|deactivate|switch off|close))\s+(?:the |my )?(?:ar|a r|augmented reality)(?: mode| vision| view| window| camera)?$", self.c_ar_toggle),
            C(r"^(?:learn|remember|memori[sz]e|scan|save|teach yourself|teach you)\s+(?:this|that|what i(?:'m| am) (?:showing|holding))(?:\s+(?:object|thing|item|shape))?\s+(?:as|called|named)\s+(?P<n>[a-z0-9][a-z0-9' -]{0,40})$", self.c_ar_learn),
            C(r"^this (?:object |thing |item )?is (?:called |named )?(?P<n>(?:my |a |an |the |your )?[a-z0-9][a-z0-9' -]{0,40})$", self.c_ar_learn),
            C(r"^(?:what do you see|what can you see|what(?:'s| is) (?:this|that)|what am i (?:holding|showing(?: you)?)|what(?:'s| is) in (?:front of (?:me|you)|the box)|identify (?:this|that)|do you (?:recogni[sz]e|know) (?:this|that))$", self.c_ar_what),
            C(r"^(?:list|show|which|what are)\s+(?:my |the |all )*(?:learned |known |saved )?(?:ar )?(?:objects|things you know)$|^what (?:objects |things |shapes )?(?:can you|do you) recogni[sz]e$|^what objects do you know$", self.c_ar_list),
            C(r"^(?:unlearn|forget (?:the )?object|delete (?:the )?object|remove (?:the )?object)\s+(?P<n>.+)$", self.c_ar_forget),
            C(r"^when you (?:see|spot|notice|recogni[sz]e|detect|find)\s+(?P<n>.+?)\s*,?\s*(?:then )?(?P<cmd>(?:open|say|tell|play|remind|set|start|send|message|text|search|google|type|take|note|what|what's|lock|volume|mute|screenshot|battery|check|show|read|run|launch|turn|news|world|flip|roll)\b.+)$", self.c_ar_bind),
            C(r"^(?:clear|remove|cancel)\s+(?:the )?(?:sight|ar) (?:action|command)(?: for (?P<n>.+))?$", self.c_ar_unbind),
            C(r"^(?:which|what) (?:objects|things|items) (?:can|do) you (?:already )?(?:recogni[sz]e|know)(?: already)?$", self.c_ar_presets),
            C(r"^(?:set up|setup|add|load|install)\s+(?:the )?(?:ar )?(?:starter|default|preset|predefined) (?:shape )?(?:commands|pack|actions)$", self.c_ar_starter),
            C(r"^(?:give me |tell me |read |read out |show |what(?:'s| is) )?(?:me )?(?:the )?(?:today'?s |latest |top )*(?:(?P<n>\d+|five|ten|fifteen|twenty) )?(?:international |world |global )?(?:news|headlines)(?: today)?$", self.c_news),
            C(r"^(?:set |switch to |use |turn )?(?:the )?(?:ai )?brain(?: mode)?\s*(?:to |is )?(?P<m>llm|hybrid|rules|off|on)$", self.c_brain),
            C(r"^(?:use|switch to|set)\s+(?P<p>ollama|claude)(?: as)?(?: the)? brain$|^brain (?:provider )?(?P<p2>ollama|claude)$", self.c_brain),
            C(r"^(?:pair|connect|link)\s+(?:with\s+)?(?:my |the )?phone(?: with (?:a )?(?:qr|code))?$|^(?:show|open)\s+(?:the )?(?:phone )?qr(?: code)?$", self.c_pair_qr),
            C(r"^(?:unpair|unlink|forget)\s+(?:my |the )?phone$", self.c_unpair_phone),
            C(r"^(?:start|turn on|enable|begin|open)\s+(?:the )?(?:phone |file )?(?:file )?transfer$", self.c_transfer_on),
            C(r"^(?:stop|turn off|disable|end|close)\s+(?:the )?(?:phone |file )?(?:file )?transfer$|^disconnect (?:my |the )?phone$", self.c_transfer_off),
            C(r"^(?:grab|hold|pick up)\s+(?:this |the |that |selected )*(?:file|files|folder|selection)$|^(?:grab|hold) (?:it|this|that)$", self.c_grab_file),
            C(r"^(?:send|share|transfer|put)\s+(?:the |my )?(?:file |document |photo |picture |video )?(?P<n>.+?)\s+to (?:my |the )?phone$|^send (?:this|that|the selected|selected)(?: file| files)? to (?:my |the )?phone$", self.c_send_phone),
            C(r"^drop(?: the| this| that| my)?(?: file| files| it| here)?$|^(?:paste|put) (?:the )?(?:received |phone )?files? here$|^get (?:the )?files? from (?:my )?phone$", self.c_drop_file),
            C(r"^(?:open|show)\s+(?:the |my )?(?:received|phone|transfer)(?: files| folder)?(?: folder)?$", self.c_transfer_folder),
            C(r"^(?:use|set up|setup|enable)\s+(?:the )?(?:fist and (?:open )?palm|gestures?)\s+for\s+(?:phone |file )?(?:file )?transfer$", self.c_transfer_gestures),
            C(r"^(?:reset|undo|restore)\s+(?:the )?(?:file |phone )?transfer gestures$", self.c_transfer_gestures_reset),
            C(r"^(?:call|phone|ring|dial)\s+(?!me\b)(?P<n>[a-z][a-z' .-]*)$", self.c_phone_call),
            C(r".", self.c_math),          # maths of any kind - it says no (returns False) to anything that isn't
            C(r"^(?:stop listening|go to sleep|sleep mode|be quiet|quiet mode|mute yourself|pause listening)\b", self.c_sleep),
            C(r"^(?:exit|quit|goodbye|bye|close pac)\b", self.c_exit),
            C(r"^(?:help|what can you do|what are your commands|show commands)\b", self.c_help),
            C(r"^(?:switch to |go to |use |turn on |enable |start |activate )?(?P<m>voice|text|offline) mode$", self.c_mode),
            C(r"^(?:switch to|go to|use|turn on|enable|start|activate|connect to|go online with)\s+claude(?: api)?(?: mode)?$"
              r"|^claude(?: api)? mode(?: on)?$", self.c_claude_on),
            C(r"^(?:switch off|turn off|disable|stop|exit|leave|end|disconnect(?: from)?|go offline from|quit)\s+claude(?: api)?(?: mode)?$"
              r"|^claude(?: api)? mode off$|^(?:go offline|stay offline|stop using claude)$", self.c_claude_off),
            C(r"^(?:forget (?:this|our|the) (?:conversation|chat)|new (?:conversation|chat)|clear claude)$", self.c_claude_forget),
            C(r"^(?:(?:ask|tell|hey|ok|okay) claude(?: to| that)?|claude)\s+(?P<q>.+)$", self.c_claude_ask),
            C(r"^(?:(?P<on>start|enable|turn on|activate|begin)|(?P<off>stop|disable|turn off|deactivate|end))(?: the| my)? (?:hand )?(?:gestures?|gesture control|gesture sensing|gesture detection)$", self.c_gesture),
            C(r"^(?:(?P<on>start|enable|turn on|activate|begin)|(?P<off>stop|disable|turn off|deactivate|end))(?: the| my)? (?:air|hand|palm) (?:drag(?: ?(?:and|&|n) ?drop)?|dragging|mouse)(?: mode)?$", self.c_air_drag),
            C(r"^(?:show|open|bring up|pull up)(?: me)?(?: the| my)? (?:phone files|phone shelf|shelf)$", self.c_show_shelf),
            C(r"^(?:hide|close|dismiss)(?: the| my)? (?:phone )?shelf$", self.c_hide_shelf),
            *[C(pat, self.c_file_info) for pat in FS_INFO],
            *[C(pat, self.c_file_list) for pat in FS_LIST],
            C(FS_MOVE, self.c_file_move),
            C(FS_MOVE2, self.c_file_move),
            C(FS_UNDO, self.c_file_undo),
            C(FS_NEWDIR, self.c_file_new_folder),
            C(FS_NEWFILE, self.c_file_new_file),
            C(r"^(?:teach|add|create|record|learn|make)(?: me)?(?: a| an| new| another)*(?: new)? (?:hand )?gesture\b", self.c_gesture_teach),
            C(r"^(?:list|show|what are|which|tell me)(?: me)?(?: my| the| all)? (?:hand )?gestures\b|^what gestures\b", self.c_gesture_list),
            C(r"^(?:delete|remove|erase)(?: a| an| the| my| some| any| all)?(?: hand)? gestures?(?: signs?)?$", self.c_gesture_delete_dialog),
            C(r"^(?:delete|remove|erase|forget|get rid of|drop)(?: the| my| this| that)?\s+(?:(?:hand )?gestures?(?: sign)?\s+(?P<a>.+)|(?P<b>.+?)\s+(?:hand )?gestures?(?: sign)?)$", self.c_gesture_delete),
            C(r"^(?:restore|bring back|undelete|re-?enable|get back)(?: all| the| my| those)*(?: deleted| removed)* (?:hand )?gestures?(?: signs?)?(?: back)?$", self.c_gesture_restore),
            C(r"^(?:repeat that|say that again|say it again|what did you say|come again)$", self.c_repeat),
            C(r"^(?:import|upload|load)(?: my| the| a| new)? (?:time ?table|schedule)(?: from)?(?: a| my)?(?: file| csv| spreadsheet)?$|^(?:import|upload|load)(?: a| my| the)? (?:time ?table |schedule )?(?:csv|spreadsheet)(?: file)?$", self.c_timetable_import),
            C(r"^(?:open|edit|change|update|fix)(?: my| the)? (?:timetable|time table|schedule)(?: file| editor)?$", self.c_timetable_edit),
            C(r"^when (?:is|do i have|are|will i have) (?:my |the )?(?P<subj>.+?)(?: class| classes| lecture| lectures| period| periods)?$", self.c_when_class),
            C(r"\b(?:schedule|timetable|time table|classes|lectures)\b|\bwhat do i have\b|\bdo i have (?:a |any )?(?:class|lecture|period)|\b(?:next|current) (?:class|lecture|period)\b|\bwhat(?:'s| is) next\b|\bam i free\b|\bwhat (?:class|lecture|period)\b|\b(?:class|lecture|period)s? (?:now|right now|today|tomorrow)\b", self.c_schedule),
            C(r"\b(?:change|switch|next)(?: your)? voice\b", self.c_voice),
            C(r"\b(?:list|show|which|what)\b.*\bvoices\b", self.c_voice_list),
            C(r"^(?:use|switch to|change to|set|pick|try|select|give me)(?: the| a| an| your)?\s+(?P<v>.+?)\s+voice$"
              r"|^(?:use|switch to|change to|pick|try|select)\s+voice\s+(?P<v2>.+)$", self.c_voice_pick),
            C(r"\b(?:speak|talk)\b.*\b(?:faster|quicker|slower|slowly|louder|up|quieter|softer|lower)\b", self.c_speak_ctl),
            C(r"\b(?:shutdown|power off|turn off (?:the )?(?:laptop|computer|pc|system))\b", self.c_shutdown),
            C(r"\b(?:cancel|abort|stop) (?:the )?(?:shutdown|restart)\b", self.c_cancel_shutdown),
            C(r"\b(?:restart|reboot)\b", self.c_restart),
            C(r"^lock(?: the)?(?: laptop| computer| screen| pc)?$", self.c_lock),
            C(r"\b(?:put (?:the )?(?:laptop|computer|pc) to sleep|sleep (?:the )?(?:laptop|computer|pc)|hibernate)\b", self.c_laptop_sleep),
            C(r"^(?:start|begin|turn on)(?: the)? (?:typing|dictation)\b|^dictate$", self.c_dictate_on),
            C(r"^(?:stop|end|finish)(?: the)? (?:typing|dictation)\b", self.c_dictate_off),
            C(r"^(?:send|whatsapp|text|message)\s+(?:the )?(?:preloaded |preset |saved |quick )?(?:message|text|option|number|template)?\s*(?P<num>[a-z0-9]+(?: [a-z]+)?)\s+to\s+(?P<who>.+)$", self.c_wa_preset),
            C(r"^(?:send (?:a )?(?:whatsapp )?(?:message|text)(?: on whatsapp)?(?: to)?|whatsapp(?: message| text)?(?: to)?|message|text|write (?:a )?(?:whatsapp )?(?:message|text)(?: to)?)\s+(?P<rest>.+)$", self.c_wa_compose),
            C(r"\b(?:list|show|read|what are)(?: my| the)?(?: preloaded| preset| saved| quick)? messages\b", self.c_list_messages),
            C(r"\b(?:list|show|read)(?: my| the)? contacts\b", self.c_list_contacts),
            C(r"^(?:press )?(?P<key>enter|new line|backspace|delete|tab|escape|undo|redo|copy|paste|cut|select all|save)(?: that| this| it)?$", self.c_key),
            C(r"^(?:type|write|dictate)\s+(?P<txt>.+)$", self.c_type),
            C(r"^(?:open|show|view|launch|bring up|take me to|see)\s+(?:(?:it|that|this|them|these|the (?:search )?(?:results?|answer|page)|google|google results?|the google (?:results?|search))\s+)?(?:in|on|using|with)\s+(?:a |the )?(?:new )?(?:google )?(?:browser|tab|window|chrome|google)$", self.c_open_search),
            C(r"^(?:open|show|view)\s+(?:it|that|the (?:search )?results?|the google (?:search|results?)|google results?)$", self.c_open_search),
            C(r"^(?:search )?youtube(?: for)?\s+(?P<q>.+)$|^play\s+(?P<p>.+?)(?: on youtube)?$", self.c_youtube),
            C(r"^(?:search(?: google)?(?: for)?|google(?: search)?(?: for)?|look up|search on google(?: for)?)\s+(?P<q>.+)$", self.c_google),
            C(r"^(?:go to|visit|open (?:the )?(?:website|site|page))\s+(?P<site>.+)$", self.c_website),
            C(r"^open (?:the )?(?:file|document)\s+(?P<name>.+)$", self.c_open_file),
            C(r"^open (?:the )?(?:folder|directory)\s+(?P<name>.+)$", self.c_open_folder),
            C(FS_ANY, self.c_file_any),            # anything else about "files" / "folders": never goes to the AI brain
            C(r"^(?:open|show|edit)(?: my| the)? (?:notes|notes file|note file|notepad notes)$", self.c_open_notes),
            C(r"^(?:open|show|edit)(?: my| the| your)? (?:knowledge|facts)(?: file| base)?$", self.c_open_knowledge),
            C(r"^how (?:many|much)(?: facts| things| answers)?(?: do| can)? (?:you|pac) (?:know|remember)(?: about)?(?: facts)?$"
              r"|^how many facts(?: do you know| have you learned)?$", self.c_fact_count),
            C(r"^(?:please )?(?:remember|memori[sz]e|keep in mind|don'?t forget|do not forget)(?: that)?\s+(?P<txt>.+)$", self.c_mem_remember),
            C(r"^(?:what|tell me what|show me what)(?: do| did| have)? you (?:know|remember|learned|learnt|noticed)(?: about (?:me|my (?P<topic>[a-z ]+?)))?$|^(?:show|list|read)(?: me)?(?: my| the| your)?(?: long[- ]term)? (?:memory|memories)$", self.c_mem_show),
            C(r"^(?:please )?forget\s+(?:about\s+|that\s+|what i (?:said|told you) about\s+)(?P<q>.+?)(?:\s+from (?:your |my )?memory)?$", self.c_mem_forget),
            C(r"^(?:please )?forget (?:that|this|the last (?:thing|one)|what i (?:just )?(?:said|told you))$|^(?:that'?s|that is) (?:wrong|not right|incorrect|not true|a mistake)$", self.c_mem_forget_last),
            C(r"^forget (?:everything|all)(?: you (?:know|remember|learned|learnt))?(?: about me)?$|^(?:forget|erase|wipe|delete|clear) (?:everything|all) (?:you (?:know|remember|learned|learnt) )?about me$|^(?:forget|erase|wipe|delete|clear|reset) (?:your |my |the )?(?:long[- ]term )?(?:memory|memories)$", self.c_mem_clear),
            C(r"^(?:(?P<on>turn on|enable|start|switch on|activate)|(?P<off>turn off|disable|stop|switch off|pause|deactivate))\s+(?:your |the |my )?(?:long[- ]term )?memory$|^(?:(?P<on2>start)|(?P<off2>stop))\s+learning(?: about me| from me)?$", self.c_mem_toggle),
            C(r"^(?:open|edit|manage|view)(?: my| the| your)?(?: long[- ]term)? (?:memory|memories)(?: editor| list)?$", self.c_mem_open),
            C(r"^(?:learn|memori[sz]e|teach yourself|add to (?:your )?(?:knowledge|facts)|save (?:this )?fact)(?: that| this)?\s+(?P<txt>.+)$", self.c_learn),
            C(r"^(?:take (?:a )?note|note(?: down)?|remember)(?: that)?\s+(?P<txt>.+)$", self.c_note),
            C(r"\b(?:read|what are)(?: my)? notes\b", self.c_read_notes),
            C(r"^(?:review|go through|go over|clean(?: up)?|sort(?: out)?)(?: my| the)?(?: new| unread)*\s*(?:e-?mails?|mails?|inbox)\b", self.c_mail_review),
            C(r"^(?:delete|remove|trash|bin|erase)(?: the| my)?\s+(?P<a>.*?)\s*(?:e-?mails?|mails?)\b\s*(?P<b>.*)$", self.c_mail_delete),
            C(r"^(?:(?:check|read|show|get|fetch)(?: me)?(?: my| the| all| any)?(?: new| unread| latest| recent)*\s+(?:e-?mails?|mails?|inbox)|do i have (?:any )?(?:new |unread )?(?:e-?mails?|mails?)|any (?:new |unread )?(?:e-?mails?|mails?))\b", self.c_mail_check),
            C(r"^remind me (?:to )?(?P<what>.+?) (?:at|by) (?P<when>\d.*)$", self.c_remind_at),
            C(r"^(?:set (?:an |the |my )?alarm|wake me up)(?: for| at)?\s*(?P<when>\d.*)$", self.c_alarm),
            C(r"^remind me (?:to )?(?P<what>.+?) in (?P<amt>.+)$", self.c_remind),
            C(r"\b(?:timer|countdown)\b", self.c_timer),
            C(r"\bjoke\b", self.c_joke),
            C(r"\b(?:flip|toss)\b.*\bcoin\b", self.c_coin),
            C(r"\b(?:roll|throw)\b.*\b(?:dice|die)\b", self.c_dice),
            C(r"\brandom number(?: between (?P<a>\d+) and (?P<b>\d+))?", self.c_random),
            C(r"\b(?:volume up|increase (?:the )?volume|turn (?:it )?up|louder)\b", self.c_vol_up),
            C(r"\b(?:volume down|decrease (?:the )?volume|turn (?:it )?down|quieter)\b", self.c_vol_down),
            C(r"\b(?:mute|unmute)\b", self.c_mute),
            C(r"\bscreenshot\b|\bscreen shot\b|\bcapture (?:the )?screen\b", self.c_screenshot),
            C(r"\b(?:minimi[sz]e|show desktop)\b", self.c_minimize),
            C(r"^close (?:this |the )?window$", self.c_close_window),
            C(r"\bbattery\b", self.c_battery),
            C(r"\b(?:cpu|memory|ram|system status)\b", self.c_system),
            C(r"^(?:what(?:'s| is) the time|what time is it|tell me the time|current time|time)$|\bwhat time\b", self.c_time),
            C(r"\b(?:what day|which day|date|day)\b.*\b(?P<w>tomorrow|yesterday)\b", self.c_date_offset),
            C(r"\b(?:today'?s date|what(?:'s| is) the date|what day is it|what is today|date today|the date)\b|^date$", self.c_date),
            C(r"^(?:hello|hi|hey|good (?:morning|afternoon|evening|night))\b", self.c_greet),
            C(r"\bhow are you\b", self.c_how_are_you),
            C(r"\b(?:who are you|your name|what are you)\b", self.c_who),
            C(r"^(?:thanks|thank you)\b", self.c_thanks),
            C(r"^(?:open|launch|start|run)\s+(?:the )?(?:app |application |program )?(?P<name>.+)$", self.c_open_app),
            C(r"^google$", self.c_open_google),
            C(r"^(?:convert|what is|what'?s|how much is)?\s*(?P<n>-?\d+(?:\.\d+)?)\s*(?P<a>[a-z]+)\s+(?:to|in|into)\s+(?P<b>[a-z]+)$", self.c_convert),
            C(r"^(?:calculate|compute|what is|what'?s|whats|how much is)\s+(?P<expr>.+)$", self.c_calc),
            C(r"^(?:who|what|when|where|why|how|which|whom|tell me about|explain|define|meaning of)\b.*", self.c_question),
        ]

    # ---------- output helpers
    def _sirify(self, text):
        """Weave 'sir' into a reply the way a person would: usually trailing
        ('...done, sir.'), sometimes leading ('Sir, ...'), never both, and
        never twice in a row in the same style so it doesn't sound scripted."""
        text = text.strip()
        title = self.mem_title()
        if not text or re.search(r"\bsir\b", text, re.I) or (title != "sir" and re.search(r"\b" + re.escape(title) + r"\b", text, re.I)):
            return text
        use_prefix = random.random() < 0.3
        if self._last_sir_style == "prefix":
            use_prefix = False  # don't lead with "Sir," two times running
        self._last_sir_style = "prefix" if use_prefix else "suffix"
        if use_prefix:
            first_word_is_i = bool(re.match(r"^I['\s]", text))
            body = text if first_word_is_i or not text[0].isupper() else text[0].lower() + text[1:]
            return title[:1].upper() + title[1:] + ", " + body
        m = re.match(r"^(.*)([.!?])$", text, re.S)
        return f"{m.group(1)}, {title}{m.group(2)}" if m else text + f", {title}"

    def say(self, text, plain=False):
        text = text if plain else self._sirify(text)       # plain: no "sir" (used when talking to a named person)
        self.last_reply = text
        self.emit("pac", text)
        self._speak(text)

    def ask(self, prompt, action):
        self.pending = {"action": action}
        self.say(prompt)

    def clean(self, raw):
        t = re.sub(r"[?!.,;:]+", " ", raw.lower())
        t = re.sub(r"\s+", " ", t).strip()
        for pat, rep in FIXES:
            t = re.sub(pat, rep, t)
        for _ in range(3):
            t = re.sub(FILLER_START, "", t)
        t = re.sub(r"\s+(?:please|for me|now|pac|pack)$", "", t).strip()
        return t

    # ---------- main entry
    def process(self, raw, source="voice"):
        self.source = source
        raw = (raw or "").strip()
        self.raw = raw
        if not raw:
            return
        t = self.clean(raw)
        if not t:
            return
        if STOP_SPEAKING.match(t) and self._stop_applies():        # "stop" / "stop it" / "mute": be quiet at once
            self.emit("you", raw)
            self.c_stop(None, t)
            return
        if HOME_RE.search(t):                                      # "wake up daddy is home": works even when asleep
            self.emit("you", raw)
            self.wake_home()
            return
        if self.asleep:
            if source == "text" or re.search(r"\b(?:wake up|wake|are you there|listen|come back)\b", t):
                self.asleep = False
                self.notify("asleep", False)
                self.emit("you", raw)
                self.say("I'm awake. What can I do for you?")
            return
        if not getattr(self, "_compound", False):
            self.emit("you", raw)
        if t in WAKE_ONLY:
            self.say("Yes, I'm listening.")
            return
        if self.pending:
            pend, self.pending = self.pending, None
            words = set(t.split())
            if words & {"yes", "yeah", "yep", "confirm", "sure", "proceed", "okay", "ok", "send", "affirmative"} \
                    or "go ahead" in t or "do it" in t:
                pend["action"]()
                return
            if words & {"no", "nope", "cancel", "stop", "dont", "don't", "negative"}:
                self.say("Okay, cancelled.")
                return
            # anything else: treat as a fresh command
        if self.awaiting:
            fn, self.awaiting = self.awaiting, None
            if re.match(r"^(?:cancel|never mind|nevermind|stop)$", t):
                self.say("Okay, cancelled.")
            else:
                fn(polish(raw))
            return
        if self.dictating and source == "voice" and not DICT_STOP.search(t):
            self.type_text(raw)
            return
        if not getattr(self, "_compound", False):
            parts = compound_parts(t, self.understands)
            if parts:                                    # two jobs in one sentence: do them one after the other
                self._compound = True
                try:
                    for p in parts:
                        self.process(p, source)
                finally:
                    self._compound = False
                return
        if self.memory_learn(raw, t, source):            # "my name is...", "I prefer...": kept, not run as a command
            return
        if self.memory_question(t):                      # "where do I live", "who is my wife": from memory
            return
        for pat, fn in self.commands:                    # brain controls always run locally, never through the AI
            if fn == self.c_brain:
                mm = pat.search(t)
                if mm:
                    self.c_brain(mm, t)
                    return
        if compose_intent(t) and self.compose_request(raw, t, source):     # "write a poem about..." is a request, not "type"
            return
        if self.cfg.get("brain", "hybrid") == "llm" and self.brain_active():
            for pat, fn in self.commands:                # so do the memory controls (forget, show, turn off...)
                if getattr(fn, "__name__", "") in self.MEMORY_CONTROLS:
                    mm = pat.search(t)
                    if mm:
                        if not self.guard(fn) or fn(mm, t) is not False:
                            return
            if self.try_files(t):                           # reading, listing, moving, creating files: handled here
                return
            if self.answer_offline_first(t) or self.brain_route(raw, t, source):
                return
        if self.dispatch(t):
            return
        if source == "text" and self.answer_offline(t):   # typed sentence that isn't a command: try your own notes
            return
        if self.claude_on and (source == "text" or len(t.split()) >= 3):   # not a stray word picked up from the room
            self.claude_answer(raw)
            return
        if self.brain_active() and (source == "text" or len(t.split()) >= 3) and self.brain_route(raw, t, source):
            return
        if (self.bg_search_on() and self.looks_like_question(raw, t, source)
                and not difflib.get_close_matches(t, CANON, n=1, cutoff=0.8)):     # not a mistyped command
            if not self.answer_offline(t):
                self.start_search(t)
            return
        self.unknown(t)

    FILE_HANDLERS = {"c_file_info", "c_file_list", "c_file_move", "c_file_undo", "c_file_new_folder",
                     "c_file_new_file", "c_file_any"}

    def try_files(self, t):
        """Only the file commands, and only when they understand the sentence (so the AI never has to refuse it)."""
        for pat, fn in self.commands:
            if fn.__name__ in self.FILE_HANDLERS:
                m = pat.search(t)
                if m:
                    if not self.guard(fn):
                        return True
                    if fn(m, t) is not False:
                        self._observe(fn, t)
                        return True
        return False

    def dispatch(self, t):
        """Run the first command that understands the sentence. True if one did."""
        for pat, fn in self.commands:
            m = pat.search(t)
            if m:
                if fn.__name__ in self.KEYWORD_ONLY and not reads_as_command(t):
                    continue                            # "why does my pc restart" is a question, not a restart
                if not self.guard(fn):                  # face security: this face isn't allowed to do that
                    return True
                if fn(m, t) is not False:
                    self._observe(fn, t)
                    return True
        return False

    def unknown(self, t):
        words = t.split()
        if 1 <= len(words) <= 6:
            # mis-heard or mistyped? find the closest thing PAC knows how to do
            best = difflib.get_close_matches(t, CANON, n=1, cutoff=0.6)
            if best:
                score = difflib.SequenceMatcher(None, t, best[0]).ratio()
                if score >= 0.86:
                    self.emit("sys", f'(understood as "{best[0]}")')
                    if self.dispatch(best[0]):
                        return
                elif self.source == "text" or words[0] in COMMAND_VERBS:
                    cand = best[0]
                    self.ask(f'Did you mean "{cand}"?', lambda: self.dispatch(cand))
                    return
        first = t.split()[0] if t.split() else ""
        if self.source == "text" or first in COMMAND_VERBS:
            self.say("Sorry, I didn't understand that. Say help to see what I can do.")
        else:
            self.emit("sys", f"(not a command: {t})")

    # ---------- Claude (online, only on your say-so)
    def claude_set(self, on, announce=True):
        if on and not claude_key_get(self.cfg):
            self.say("I need your Claude API key first. I've opened the box for it. I'm staying offline until then.")
            self.notify("claude_setup", None)
            return
        changed = on != self.claude_on
        self.claude_on = on
        self.claude_history = []
        self.notify("claude", on)
        if not announce:
            return
        if on:
            self.emit("sys", "Claude mode is ON. Anything I can't do myself is sent to Anthropic's servers, "
                             "and so is the conversation so far. Say 'claude mode off' to go back offline.")
            self.say("Claude mode on. Ask me anything.")
        elif changed:
            self.say("Claude mode off. I'm back to working offline.")
        else:
            self.say("I'm already offline.")

    def c_claude_on(self, m, t):
        self.claude_set(True)

    def c_claude_off(self, m, t):
        self.claude_set(False)

    def c_claude_forget(self, m, t):
        self.claude_history = []
        self.say("Okay, I've forgotten this conversation.")

    def c_claude_ask(self, m, t):
        q = (m.group("q") or "").strip()
        if not q or re.fullmatch(r"(?:api )?mode(?: on| off)?", q):
            return False
        self.claude_answer(q, oneshot=not self.claude_on)      # a one-off leaves the mode exactly as it was

    def claude_answer(self, question, oneshot=False):
        key = claude_key_get(self.cfg)
        if not key:
            self.say("I need your Claude API key first. I've opened the box for it.")
            self.notify("claude_setup", None)
            return
        history = ([] if oneshot else list(self.claude_history)) + [{"role": "user", "content": question}]
        while history and history[0]["role"] != "user":
            history.pop(0)
        self.emit("sys", "(asking Claude...)")
        try:
            reply = ask_claude(key, self.cfg.get("claude_model") or CLAUDE_MODELS[0][0], history[-12:],
                               system_extra=self._mem_block(question, cloud=True))
        except ClaudeError as e:
            logger.warning("claude request failed: %s", e)
            if e.kind in ("auth", "no_key"):
                self.say(f"Sorry, {e}. Please check the key in the Claude setup box.")
                self.notify("claude_setup", None)
            elif e.kind == "offline":
                self.say("I couldn't reach Claude. You may be offline." + (
                    " I'm still in Claude mode - say 'claude mode off' to stay fully offline." if self.claude_on else ""))
            else:
                self.say(f"Sorry, {e}.")
            return
        if not oneshot:
            self.claude_history = (history + [{"role": "assistant", "content": reply}])[-12:]
        if len(reply) > 350:                       # long answer: show all of it, speak the first part
            cut = reply[:350].rsplit(". ", 1)[0].rstrip(".") + "."
            self.emit("pac", reply)
            self.last_reply = reply
            self._speak(self._sirify(cut))
        else:
            self.say(reply)

    # ---------- LLM brain: any phrasing -> one of PAC's own commands
    def brain_active(self):
        if self.cfg.get("brain", "hybrid") == "rules":
            return False
        if self.cfg.get("brain_provider", "claude") == "ollama":
            return True
        return bool(claude_key_get(self.cfg))        # Claude brain only works once you've given a key

    def brain_route(self, raw, t, source="voice"):
        """Send the sentence to the model, then run what it chose. Returns True when handled; False means the
        model was unavailable and the caller should carry on with the old pattern-matching chain."""
        if self._in_brain:                            # a command the AI chose must never bounce back to the AI
            return False
        history = list(self.brain_history) + [{"role": "user", "content": raw}]
        while history and history[0]["role"] != "user":
            history.pop(0)
        token = self.brain_token
        block = self._mem_block(raw, cloud=self.cfg.get("brain_provider", "claude") != "ollama")
        self.emit("sys", "(thinking...)")
        try:
            name, args = brain_decide(self.cfg, history[-10:], memory_block=block)
        except ClaudeError as e:
            logger.warning("brain request failed: %s", e)
            self.emit("sys", f"(AI brain unavailable: {e}. Using the built-in commands instead.)")
            return False
        except Exception:
            logger.exception("brain crashed")
            return False
        if token != self.brain_token:                 # you said stop meanwhile
            return True
        if name in ("remember", "forget"):
            return self._brain_memory(name, args or {}, raw)
        phrase = brain_tool_to_phrase(name, args)
        if phrase is None:                            # conversation / answer
            text = str((args or {}).get("text", "")).strip()
            if not text:
                return False
            self.brain_remember(raw, text)
            if len(text) > 350:
                cut = text[:350].rsplit(". ", 1)[0].rstrip(".") + "."
                self.emit("pac", text)
                self.last_reply = text
                self._speak(self._sirify(cut))
            else:
                self.say(text)
            return True
        if phrase:
            self.emit("sys", f'(brain: {name} -> "{phrase}")')
            self.brain_remember(raw, f"[did: {phrase}]")
            self._in_brain = True
            try:
                if name == "whatsapp":                # call the handler directly: a message containing "to" must not be read as a preset
                    done = True
                    if self.guard(self.c_wa_compose):
                        rest = re.sub(r"^whatsapp\s+", "", phrase)
                        done = self.c_wa_compose({"rest": rest}, phrase) is not False
                else:
                    kept_raw, self.raw = self.raw, phrase      # handlers that keep dots and capitals read the phrase
                    try:
                        done = self.dispatch(self.clean(phrase))
                    finally:
                        self.raw = kept_raw
            finally:
                self._in_brain = False
            if done:
                return True
            self.say("Sorry, I understood that but couldn't do it.")
            return True
        return False

    def brain_remember(self, user, outcome):
        self.brain_history = (self.brain_history + [{"role": "user", "content": user},
                                                    {"role": "assistant", "content": outcome}])[-10:]

    def c_brain(self, m, t):
        g = m.groupdict()
        mode, prov = g.get("m"), g.get("p") or g.get("p2")
        if prov:
            self.cfg["brain_provider"] = prov
            save_config(self.cfg)
            self.brain_history = []
            if prov == "ollama":
                self.say("Brain set to your local Ollama model. Nothing leaves this laptop.")
            elif claude_key_get(self.cfg):
                self.say("Brain set to Claude. What you say goes to Anthropic's servers.")
            else:
                self.say("Brain set to Claude, but I need your API key first. I've opened the box for it.")
                self.notify("claude_setup", None)
            return
        mode = {"off": "rules", "on": "hybrid"}.get(mode, mode)
        self.cfg["brain"] = mode
        save_config(self.cfg)
        self.brain_history = []
        names = {"rules": "Brain off. I'm using my built-in commands only.",
                 "hybrid": "Hybrid brain. I try my built-in commands first, then the AI for everything else.",
                 "llm": "Full AI brain. The AI understands every sentence first."}
        self.say(names[mode] + ("" if mode == "rules" or self.brain_active() else
                                " It won't work until you add a Claude key or say 'use ollama brain'."))

    def answer_offline_first(self, t):
        """In full-AI mode your own notes/facts still win, but only for a clear question."""
        return bool(re.match(r"^(?:who|what|when|where|why|how|which)\b", t)) and self.answer_offline(t)

    # ---------- phone <-> laptop file transfer
    def _xfer(self):
        if self.transfer is None:
            self.transfer = PhoneTransfer(self.cfg, self._on_phone_file, self._on_phone_event, self._on_phone_contacts)
        return self.transfer

    def _on_phone_file(self, path):
        self.emit("sys", f"Received from phone: {path}")
        t = getattr(self, "_shelf_timer", None)
        if t is not None:
            t.cancel()
        self._shelf_timer = threading.Timer(1.2, self.show_phone_shelf, kwargs={"announce": True})
        self._shelf_timer.daemon = True
        self._shelf_timer.start()                      # wait a moment so a batch of files makes one shelf

    def show_phone_shelf(self, announce=False):
        x = self._xfer()
        files = [p for p in x.unplaced if p.exists()]
        if not files and x.received and x.received[-1].exists():
            files = [x.received[-1]]
        if not files:
            self.say("Nothing has come from your phone yet.")
            return
        if getattr(self, "shelf", None) is None:
            self.shelf = PhoneShelf()
        many = len(files) != 1
        if self.shelf.show(files):
            if getattr(self, "air_drag_on", False):
                self.say(f"{'Your files are' if many else 'Your file is'} on the shelf. Pinch "
                         f"{'one' if many else 'it'}, move, and let go where you want it.")
            else:
                self.say(f"{'Your files are' if many else 'Your file is'} on the shelf at the right of the screen. "
                         f"Say start air drag to grab {'them' if many else 'it'} with your hand.")
            def _check():
                if not self.shelf.alive():            # the shelf window died at once: fall back to the folder
                    open_path(x.inbox)
                    self.emit("sys", "The shelf couldn't open, so I opened the Received folder instead.")
            t = threading.Timer(2.5, _check)
            t.daemon = True
            t.start()
        else:
            open_path(x.inbox)
            self.say("I opened the folder with your phone's files. Drag them from there.")

    # ---------- files: look at, list, move and create (the work is done by FileAssistant)
    def _file_cmd(self, name, t):
        try:
            if getattr(self, "fileasst", None) is None:
                self.fileasst = FileAssistant(self)
            return getattr(self.fileasst, name)(t)
        except Exception:
            logger.exception("file command failed")
            self.say("Sorry, something went wrong with that file request.")
            return True

    def c_file_info(self, m, t):
        return self._file_cmd("info", t)

    def c_file_list(self, m, t):
        return self._file_cmd("listing", t)

    def c_file_move(self, m, t):
        return self._file_cmd("move", t)

    def c_file_any(self, m, t):
        return self._file_cmd("overview", t)

    def c_file_undo(self, m, t):
        return self._file_cmd("undo", t)

    def c_file_new_folder(self, m, t):
        return self._file_cmd("create_folder", t)

    def c_file_new_file(self, m, t):
        return self._file_cmd("create_file", t)

    def c_show_shelf(self, m, t):
        self.show_phone_shelf()

    def c_hide_shelf(self, m, t):
        sh = getattr(self, "shelf", None)
        if sh is not None:
            sh.close()
        self.say("Shelf closed.")

    def transfer_stop(self):
        if self.transfer is not None:
            self.transfer.stop()

    def transfer_start(self, announce=True):
        x = self._xfer()
        try:
            url = x.start()
        except OSError as e:
            logger.warning("transfer server failed: %s", e)
            self.say("I couldn't open the transfer port. Something else may be using it.")
            return None
        if announce:
            self.emit("sys", "File transfer is ON. On your phone (same Wi-Fi) open this address:\n" + url +
                      "\nIt only works with this exact link. To link your phone without typing, say: pair my phone."
                      "\nFiles from your phone are saved in " + str(x.inbox))
            if OS == "Windows":
                try:
                    subprocess.run(["clip"], input=url.encode("ascii"), creationflags=NO_WINDOW, timeout=5)
                except Exception:
                    pass
            self.say("File transfer is on. Open the address in the chat on your phone. I copied it to the clipboard.")
        return url


    # ---------- phone link: QR pairing, events from the phone, calling through the phone
    def _on_phone_event(self, ev):
        kind = str(ev.get("type", ""))
        who = clean_phone_text(ev.get("who"), 80)
        text = clean_phone_text(ev.get("text"))
        if kind == "hello":
            p, self._qr_proc = self._qr_proc, None
            if p is not None:
                try:
                    p.terminate()
                except Exception:
                    pass
            self.say(f"Your phone is linked{(' (' + who + ')') if who else ''}.")
        elif kind == "missed_call":
            self.say(f"You missed a call from {who or 'an unknown number'}.")
        elif kind == "sms":
            self.say(f"Text from {who or 'an unknown sender'}.")
            self.emit("sys", f"Text from {who}: {text}")
        else:
            self.emit("sys", f"Phone: {who} {text}".strip())

    def _on_phone_contacts(self, data):
        rows = []
        for c in (data.get("contacts") or [])[:20000]:
            if isinstance(c, dict) and c.get("name") and c.get("number"):
                rows.append([clean_phone_text(c["name"], 80), clean_phone_text(c["number"], 30)])
        if not rows:
            return
        try:
            save_phonebook(rows)
        except OSError:
            logger.exception("could not save the phone's contacts")
            return
        self.emit("sys", f"Got {len(rows)} contacts from your phone. Try: call <name>")

    def _show_qr(self, url):
        script = DATA_DIR / "qr_window.py"
        try:
            import segno                                   # noqa: F401
        except ImportError:
            if not pip_install(["segno"], lambda m: self.emit("sys", m), "the QR code maker", "QR code maker installed."):
                self.say("I couldn't install the QR code maker. In the phone's Settings, paste this address instead: " + url)
                return
        try:
            script.write_text(QR_WINDOW_SCRIPT, encoding="utf-8")
            if self._qr_proc is not None and self._qr_proc.poll() is None:
                self._qr_proc.terminate()
            self._qr_proc = subprocess.Popen([str(_pip_python()), str(script), url], creationflags=NO_WINDOW)
            self.say("Scan the code on the screen with PAC on your phone. Type pair on the phone to open its scanner.")
        except Exception:
            logger.exception("QR window failed")
            self.say("I couldn't open the QR window. In the phone's Settings, paste this address instead: " + url)

    def c_pair_qr(self, m, t):
        url = self.transfer_start(announce=False)
        if url:
            threading.Thread(target=self._show_qr, args=(url,), daemon=True).start()

    def c_unpair_phone(self, m, t):
        self.cfg.pop("phone_token", None)
        try:
            save_config(self.cfg)
        except Exception:
            logger.exception("could not save config")
        if self.transfer is not None:
            self.transfer.stop()
        self.say("Your phone is unlinked. Say pair my phone to link it again.")

    def c_phone_call(self, m, t):
        name = (m.groupdict().get("n") or "").strip()
        book = load_phonebook()
        if not book:
            self.say("I don't have your phone's contacts yet. On the phone, say: import contacts.")
            return
        hits = find_contacts(book, name)
        if not hits:
            self.say(f"I couldn't find {name} in your phone's contacts.")
            return
        if len({h[0].lower() for h in hits}) > 1:
            self.say("More than one match: " + ", ".join(h[0] for h in hits[:5]) + ". Say the full name.")
            return
        x = self._xfer()
        if not x.connected():
            if not x.running():
                self.transfer_start(announce=False)
            self.say("Your phone isn't connected right now. Is PAC open on it, on the same Wi-Fi?")
            return
        x.send_command({"cmd": "call", "name": hits[0][0], "number": hits[0][1]})
        self.say(f"Calling {hits[0][0]} on your phone.")


    # handlers that fire on one keyword anywhere in the sentence: they must not take over a long or explanatory sentence
    KEYWORD_ONLY = {"c_shutdown", "c_restart", "c_laptop_sleep", "c_joke", "c_coin", "c_dice", "c_random", "c_mute",
                    "c_minimize", "c_screenshot", "c_battery", "c_system", "c_timer", "c_vol_up", "c_vol_down",
                    "c_voice", "c_speak_ctl"}

    def understands(self, t):
        """True if one of PAC's own commands (not the maths catch-all) recognises this sentence."""
        return any(pat.search(t) for pat, fn in self.commands if fn.__name__ not in ("c_math", "c_brain"))

    def _prewarm(self):
        """While you read the first screen: load what the first answers need (maths library, AI connection)."""
        try:
            _sympy()
        except Exception:
            pass
        try:
            if self.brain_active() or claude_key_get(self.cfg):
                warm_ai_connection()
        except Exception:
            pass

    def compose_request(self, raw, t, source):
        """The sentence wants new text written (a poem, an email, code, a document about something). Hand it to the
        AI that is switched on, and never type it or make a file out of the words after the verb. True = handled."""
        if self.claude_on:
            self.claude_answer(raw)
            return True
        if self.brain_active() and self.brain_route(raw, t, source):
            return True
        self.say("That is a request to write something new, and I can only do that with the AI brain or Claude mode on. "
                 "To have me type exact words, say: type, then the words.")
        return True

    def c_transfer_on(self, m, t):
        self.transfer_start()

    def c_transfer_off(self, m, t):
        if self.transfer is not None and self.transfer.running():
            self.transfer.stop()
            self.say("File transfer is off.")
        else:
            self.say("File transfer wasn't on.")

    def _selected_files(self):
        """Paths of whatever is selected in File Explorer (Windows): copy it, then read the clipboard's file list."""
        if OS != "Windows":
            return None

        def ps(cmd):
            return subprocess.run(["powershell", "-NoProfile", "-Command",
                                   "[Console]::OutputEncoding=[Text.Encoding]::UTF8; " + cmd],
                                  capture_output=True, text=True, encoding="utf-8", errors="replace",
                                  timeout=10, creationflags=NO_WINDOW).stdout
        try:
            ps("Set-Clipboard -Value ''")                 # so an old copied file can't be mistaken for the selection
            pyautogui.hotkey("ctrl", "c")
            for _ in range(5):
                time.sleep(0.3)
                out = ps("Get-Clipboard -Format FileDropList | ForEach-Object { $_.FullName }")
                paths = [Path(l.strip()) for l in out.splitlines() if l.strip()]
                if paths:
                    return paths
        except Exception:
            logger.exception("could not read the selected files")
        return []

    def _hold(self, paths):
        x = self._xfer()
        if self.transfer_start(announce=False) is None:
            return
        paths = [p for p in paths if p.exists()]
        if not paths:
            self.say("I couldn't find that file.")
            return
        if len(paths) == 1 and paths[0].is_file():
            target = paths[0]
        else:
            self.say("Packing that into a zip file first.")
            name = (paths[0].name if len(paths) == 1 else "PAC_selection") + ".zip"
            try:
                target = zip_paths(paths, x.root / name)
            except OSError:
                logger.exception("zip failed")
                self.say("I couldn't pack that. Is it still open somewhere?")
                return
        x.held = target
        url = x.url()
        self.emit("sys", f"Holding: {target}\nOn your phone: {url}")
        self.say(f"Holding {target.name}. On your phone, tap Download.")

    def c_grab_file(self, m, t):
        paths = self._selected_files()
        if paths is None:
            self.say("Selecting from Explorer works on Windows. Say: send, then the file name, to phone.")
        elif not paths:
            self.say("I don't see a selected file. Click a file in File Explorer first, then try again.")
        else:
            self._hold(paths)

    def c_send_phone(self, m, t):
        name = (m.groupdict().get("n") or "").strip()
        if not name:
            return self.c_grab_file(m, t)
        f = find_file(name)
        if not f:
            self.say(f"I couldn't find a file called {name}.")
            return
        self._hold([f])

    def c_drop_file(self, m, t):
        x = self._xfer()
        files = [p for p in x.unplaced if p.exists()]
        if not files and x.received and x.received[-1].exists():
            files = [x.received[-1]]
        if not files:
            self.say("Nothing has come from your phone yet.")
            return
        if OS == "Windows":
            arr = ",".join("'" + str(p).replace("'", "''") + "'" for p in files)
            try:
                subprocess.run(["powershell", "-NoProfile", "-Command", f"Set-Clipboard -LiteralPath {arr}"],
                               capture_output=True, timeout=10, creationflags=NO_WINDOW)
                time.sleep(0.2)
                pyautogui.hotkey("ctrl", "v")
            except Exception:
                logger.exception("drop failed")
                self.say("I couldn't paste that here. I'll open the folder instead.")
                open_path(x.inbox)
                return
            x.unplaced = []
            self.say(f"Dropped {len(files)} file{'s' if len(files) != 1 else ''} here.")
        else:
            x.unplaced = []
            open_path(x.inbox)
            self.say("I opened the folder with your phone's files.")

    def c_transfer_folder(self, m, t):
        x = self._xfer()
        x.inbox.mkdir(parents=True, exist_ok=True)
        open_path(x.inbox)
        self.say("Here are the files from your phone.")

    def c_transfer_gestures(self, m, t):
        gmap = dict(self.cfg.get("gesture_map") or {})
        gmap["fist"] = {"type": "cmd", "arg": "grab file"}
        gmap["open_palm"] = {"type": "cmd", "arg": "drop file"}
        self.cfg["gesture_map"] = gmap
        save_config(self.cfg)
        self.say("Done. A fist grabs the selected file, an open palm drops files from your phone. "
                 "A fist no longer plays or pauses music. Make sure gestures are on.")

    def c_transfer_gestures_reset(self, m, t):
        gmap = dict(self.cfg.get("gesture_map") or {})
        gmap.pop("fist", None)
        gmap.pop("open_palm", None)
        self.cfg["gesture_map"] = gmap
        save_config(self.cfg)
        self.say("Fist and open palm are back to their normal jobs.")

    # ---------- stop talking, and the "daddy is home" news briefing
    def _stop_applies(self):
        """A bare 'stop' / 'mute' means 'be quiet' - unless PAC is asleep or you are dictating and she isn't talking,
        when it is just another word."""
        busy = self.speaker is not None and self.speaker.busy()
        return busy or not (self.asleep or self.dictating)

    def stop_speaking(self):
        """Silence PAC at once: cut the voice, empty its queue, and cancel a news reading still on its way."""
        self.news_token += 1
        self.search_token += 1
        self.math_token += 1
        self.brain_token += 1
        if self.speaker is not None:
            self.speaker.stop_now()

    def c_stop(self, m, t):
        self.pending = None
        self.awaiting = None
        self.stop_speaking()
        self.emit("sys", "(stopped)")

    def wake_home(self):
        if self.asleep:
            self.asleep = False
            self.notify("asleep", False)
        self.stop_speaking()                      # drop anything she was in the middle of saying
        self.say(f"Hello {self.mem_title()}.")
        self.cfg["auto_home_date"] = datetime.date.today().isoformat()     # done for today, so the 5:30-8:00 AM timer won't repeat it
        try:
            save_config(self.cfg)
        except Exception:
            logger.exception("could not save auto_home_date")
        try:
            if self.timetable.load():             # no timetable yet: skip quietly rather than pop the editor open
                now = datetime.datetime.now()
                self._say_day(now.weekday(), "today", now)
        except Exception:
            logger.exception("could not tell the schedule after wake-up")
        self.start_news(int(self.cfg.get("news_count", 20)))

    def c_home(self, m, t):
        self.wake_home()

    def c_news(self, m, t):
        n = m.groupdict().get("n")
        count = int(n) if n and n.isdigit() else _NEWS_NUMBERS.get(n, int(self.cfg.get("news_count", 20)))
        self.stop_speaking()
        self.say("One moment, I'm getting the world headlines.")
        self.start_news(max(1, min(30, count)))

    def start_news(self, count=20):
        self.news_token += 1
        threading.Thread(target=self._news_job, args=(self.news_token, count), daemon=True).start()

    def _news_job(self, token, count):
        try:
            items = fetch_world_news(count, self.cfg.get("lang", "en-IN"))
        except Exception as e:
            logger.warning("news fetch failed: %s", e)
            if token == self.news_token:
                self.say("I couldn't reach Google News just now. Please check the internet connection.")
            return
        if token != self.news_token:              # you said stop (or asked for something else) meanwhile
            return
        if not items:
            self.say("Google News didn't give me any headlines right now.")
            return
        lines = [f"{i}. {t}" + (f"   [{s}]" if s else "") for i, (t, s, _l) in enumerate(items, 1)]
        self.emit("sys", f"Top {len(items)} international headlines today:\n" + "\n".join(lines))
        self.last_reply = f"Here are today's top {len(items)} international headlines."
        self._speak(self.last_reply)
        for i, (title, _s, _l) in enumerate(items, 1):
            if token != self.news_token:
                return
            self._speak(f"Number {i}. {title.rstrip('. ')}.")

    # ---------- control
    def c_sleep(self, m, t):
        self.asleep = True
        self.notify("asleep", True)
        self.say("Okay, I'll stay quiet. Say wake up when you need me.")

    def c_exit(self, m, t):
        self.say("Goodbye! Have a lovely day.")
        self.request_quit()

    def c_help(self, m, t):
        self.emit("sys", HELP_TEXT)
        self._speak(self._sirify("I can open apps and files, search Google, send WhatsApp messages, type for you, "
                                 "control your laptop and more. The full list is on screen."))

    def c_mode(self, m, t):
        if m["m"] == "offline" and self.claude_on:
            self.claude_set(False, announce=False)
        self.notify("mode", "voice" if m["m"] == "voice" else "text")

    def c_voice(self, m, t):
        if not self.speaker:
            self.say("Voice changing isn't available.")
            return
        named = re.search(r"voice\s+(?:to|into)\s+(?:the\s+)?(.+)$", t)      # "change voice to british"
        if named and self.speaker.pick_voice(named.group(1)):
            return
        self.speaker.cycle_voice()

    def c_voice_list(self, m, t):
        sp = self.speaker
        if not sp:
            return False
        labels, natural = sp.list_labels()
        if not labels:
            self.say("I couldn't find any voices on this laptop.")
            return
        self.emit("sys", ("Natural voices" if natural else "Voices installed on this laptop") + ":\n"
                  + "\n".join(f"  {i}. {n}" for i, n in enumerate(labels, 1))
                  + "\nSay:  use Sonia voice   |   use British voice   |   change voice")
        if not natural and edge_tts is None:
            self.emit("sys", "For several human-sounding voices: menu Assistant > Install natural voices.")
        names = ", ".join(voice_first_name(n) for n in labels[:8])
        self._speak(self._sirify(f"I have {len(labels)} voices: {names}. Say, use, and a name, to switch."))

    def c_voice_pick(self, m, t):
        sp = self.speaker
        q = m.group("v") or m.group("v2") or ""
        if not sp:
            return False
        words = voice_query_words(q)
        if not words:
            return False
        if set(words) <= _VOICE_CYCLE_WORDS:
            sp.cycle_voice()
            return
        if sp.pick_voice(q) is None:
            self.say(f"I couldn't find a voice called {q}. Say list voices to hear the options.")

    def c_speak_ctl(self, m, t):
        sp = self.speaker
        if not sp:
            return False
        if re.search(r"faster|quicker", t):
            sp.change_rate(+25)
            self.say("Speaking faster.")
        elif re.search(r"slower|slowly", t):
            sp.change_rate(-25)
            self.say("Speaking slower.")
        elif re.search(r"louder|up", t):
            sp.volume = 1.0
            for _ in range(5):
                pyautogui.press("volumeup")
            self.say("Is this better?")
        else:
            sp.volume = max(0.3, sp.volume - 0.3)
            self.say("Speaking more softly.")

    # ---------- power
    def c_shutdown(self, m, t):
        def go():
            self.say("Shutting down in five seconds. Goodbye!")
            run_power("shutdown")
        self.ask("Are you sure you want to shut down? Say yes or no.", go)

    def c_restart(self, m, t):
        def go():
            self.say("Restarting in five seconds.")
            run_power("restart")
        self.ask("Are you sure you want to restart? Say yes or no.", go)

    def c_cancel_shutdown(self, m, t):
        if OS == "Windows":
            sh("shutdown /a")
        self.say("Shutdown cancelled.")

    def c_lock(self, m, t):
        self.say("Locking the laptop.")
        run_power("lock")

    def c_laptop_sleep(self, m, t):
        self.say("Putting the laptop to sleep.")
        run_power("sleep")

    # ---------- typing
    def punctuate(self, s):
        s = re.sub(r"\s*\b(?:full stop|period)\b", ".", s)
        s = re.sub(r"\s*\bcomma\b", ",", s)
        s = re.sub(r"\s*\bquestion mark\b", "?", s)
        s = re.sub(r"\s*\bexclamation (?:mark|point)\b", "!", s)
        s = s.strip()
        return (s[0].upper() + s[1:] + " ") if s else ""

    def type_text(self, text):
        if self.source == "text":
            self.say("Click where you want me to type. I'll start in 4 seconds.")
            time.sleep(4)
        parts = re.split(r"\bnew line\b", text, flags=re.I)
        for i, part in enumerate(parts):
            part = self.punctuate(part)
            if part:
                pyautogui.write(part, interval=0.01)
            if i < len(parts) - 1:
                pyautogui.press("enter")

    def c_type(self, m, t):
        txt = m["txt"]
        if re.fullmatch(r"(?:that|it|the (?:reply|answer|text)|your (?:reply|answer)|what you (?:said|wrote))", txt.strip()) and self.last_reply:
            txt = self.last_reply                      # "type that" types what PAC just wrote
        self.type_text(txt)

    def c_dictate_on(self, m, t):
        self.dictating = True
        self.notify("dictating", True)
        self.say("Dictation on. Click where you want the text, then start speaking. "
                 "Say stop typing when you're done.")

    def c_dictate_off(self, m, t):
        self.dictating = False
        self.notify("dictating", False)
        self.say("Dictation off.")

    def c_key(self, m, t):
        kind, val = KEYS[m["key"]]
        if kind == "press":
            pyautogui.press(val)
        else:
            pyautogui.hotkey(*val)

    # ---------- web
    # ---------- web: a quiet search first; a browser tab only when you ask for one
    def bg_search_on(self):
        return bool(self.cfg.get("background_search", True))

    @staticmethod
    def looks_like_question(raw, t, source):
        words = t.split()
        if not words or (source != "text" and len(words) < 3):      # one or two words heard from the room: not a question
            return False
        return raw.rstrip().endswith("?") or words[0] in QUESTION_WORDS

    @staticmethod
    def _shorten(text, n=300):
        text = " ".join(text.split())
        if len(text) <= n:
            return text
        cut = text[:n]
        i = max(cut.rfind(". "), cut.rfind("; "))
        return cut[:i + 1] if i > 80 else cut.rsplit(" ", 1)[0] + "..."

    def open_google_tab(self, query=None):
        """The only place PAC opens Google in a browser: a NEW TAB, and only when you asked for it."""
        url = "https://www.google.com/search?q=" + quote_plus(query) if query else "https://www.google.com"
        webbrowser.open_new_tab(url)

    def start_search(self, query):
        """Look the question up on the web on another thread. Nothing is asked first and no browser opens: the
        answer arrives in the chat and is read out, and 'open in a new tab' shows the same search on Google."""
        query = " ".join(query.split()).strip(" ?!.,")
        if not query:
            return
        self.search_token += 1
        self.last_search = {"query": query, "time": time.time()}
        where = "Google" if self.cfg.get("search_engine", "google") == "google" else "DuckDuckGo"
        self.emit("sys", f'(looking up "{query}" on {where} in the background - no browser window)')
        threading.Thread(target=self._search_job, args=(self.search_token, query), daemon=True).start()

    def _search_job(self, token, query):
        try:
            answer, results, engine, notes = web_search(self.cfg, query)
        except Exception:
            logger.exception("background search crashed")
            answer, results, engine, notes = "", [], None, ["the search crashed (see ~/.pac/pac.log)"]
        if token != self.search_token:             # you said stop (or asked something else) meanwhile
            return
        if not (answer or results):
            if notes:
                self.emit("sys", "Search problems:  " + "  |  ".join(notes))
            self.say("I couldn't get an answer in the background just now. Say open in a new tab, "
                     "and I'll show you the Google results.")
            return
        lines = [f'Web results for "{query}" ({engine}):']
        if answer:
            lines.append("  Answer: " + self._shorten(answer))
        for i, r in enumerate(results, 1):
            host = urlparse(r["url"]).netloc.replace("www.", "")
            lines.append(f"  {i}. {r['title']}  [{host}]")
            if r["snippet"]:
                lines.append("       " + self._shorten(r["snippet"], 170))
        if engine != "Google" and self.cfg.get("search_engine", "google") == "google":
            lines.append("  (Google wouldn't answer a hidden request just now, so this came from " + engine + ".)")
        lines.append("  Say 'open in a new tab' to see this search on Google.")
        reading = not answer and bool(self.cfg.get("read_pages", True))
        if reading:
            lines.append("  Reading the top pages for a fuller answer...")
        self.emit("sys", "\n".join(lines))
        if answer:
            self.say(self._shorten(answer))
            return
        if reading:                               # open the top results quietly and answer from what they say
            try:
                passage, src = read_web_answer(query, results)
            except Exception:
                logger.exception("reading the result pages failed")
                passage, src = "", ""
            if token != self.search_token:
                return
            if passage:
                host = urlparse(src).netloc.replace("www.", "")
                self.emit("sys", f"From {host}:\n  {passage}")
                self.say(f"According to {host}: {self._shorten(passage, 350)}")
                return
        top = next((r for r in results if r["snippet"]), results[0])
        host = urlparse(top["url"]).netloc.replace("www.", "")
        self.say(f"According to {host}: {self._shorten(top['snippet'])}" if top["snippet"]
                 else f"The top result is {top['title']}, from {host}.")

    def c_open_search(self, m, t):
        ls = self.last_search
        if ls:
            self.say(f"Opening Google in a new tab for {ls['query']}.")
            self.open_google_tab(ls["query"])
        elif "google" in t:
            self.say("Opening Google in a new tab.")
            self.open_google_tab()
        elif re.search(r"\b(?:tab|browser|window|chrome)\b", t):
            self.say("I haven't looked anything up yet, so there's nothing to open.")
        else:
            return False                   # "open it" with nothing to open: let the other commands try

    def c_google(self, m, t):
        q = m["q"].strip()
        tab = re.search(r"\s+(?:in|on|with)\s+(?:a |the )?(?:new )?(?:tab|browser|google chrome|chrome)$", q)
        if tab:                            # "search for cats in a new tab": you asked for the browser, so open it
            q = q[:tab.start()].strip()
        if not q:
            return False
        if tab or not self.bg_search_on():
            self.last_search = {"query": q, "time": time.time()}
            self.say(f"Searching Google for {q} in a new tab.")
            self.open_google_tab(q)
            return
        self.start_search(q)

    def c_fact_count(self, m, t):
        total, mine = self.kb.count()
        if not total:
            self.say("I don't have any facts yet. Say, learn, followed by a fact, to teach me one.")
            return
        self.say(f"I know {total} things offline: {total - mine} built in and {mine} that you taught me.")

    def answer_offline(self, t):
        """Answer from your own notes/facts. Returns True if it did."""
        ans = self.kb.ask(t) or self.memory_answer(t)
        if not ans:
            return False
        if len(ans) > 300:
            self.emit("sys", ans)
            ans = ans[:300].rsplit(" ", 1)[0] + "..."
        self.say(ans)
        return True

    def c_question(self, m, t):
        if self.answer_offline(t):
            return
        if not getattr(self, "_in_fuzzy", False):            # "what tim is it" -> "what time is it"
            best = difflib.get_close_matches(t, CANON, n=1, cutoff=0.8)
            if best and difflib.SequenceMatcher(None, t, best[0]).ratio() >= 0.86:
                self._in_fuzzy = True
                try:
                    self.emit("sys", f'(understood as "{best[0]}")')
                    if self.dispatch(best[0]):
                        return
                finally:
                    self._in_fuzzy = False

        if self.claude_on:
            self.claude_answer(self.raw or t)
            return

        if self.brain_active() and self.brain_route(self.raw or t, t, self.source):
            return

        if self.bg_search_on():
            self.start_search(t)           # no question asked, no browser opened
            return

        def google():
            self.say("Let me look that up on Google.")
            webbrowser.open("https://www.google.com/search?q=" + quote_plus(t))
        mode = self.cfg.get("online_fallback", "ask")
        if mode == "no":
            self.say("I don't have that in my notes.")
        elif mode == "yes":
            google()
        else:
            self.ask("I don't have that in my notes. Shall I search Google for it?", google)

    def c_youtube(self, m, t):
        q = (m.group("q") or m.group("p") or "").strip()
        if not q:
            return False
        self.say(f"Looking up {q} on YouTube.")
        vid, title = find_top_youtube_result(q)
        if not vid:
            self.say("I couldn't find that. Opening the search results instead.")
            webbrowser.open("https://www.youtube.com/results?search_query=" + quote_plus(q))
            return

        def play():
            self.say(f"Playing {title}." if title else "Playing it now.")
            webbrowser.open(f"https://www.youtube.com/watch?v={vid}")
        prompt = f'The top result is "{title}". Shall I play it?' if title else "Shall I play the top result?"
        self.ask(prompt, play)

    def c_website(self, m, t):
        site = m["site"].strip()
        site = re.sub(r"\s+dot\s+", ".", site)
        site = site.replace(" ", "")
        if "." not in site:
            return self.c_google(re.match(r"(?P<q>.+)", m["site"]), t)
        self.say(f"Opening {site}.")
        webbrowser.open(site if site.startswith("http") else "https://" + site)

    def c_open_google(self, m, t):
        self.say("Opening Google.")
        webbrowser.open("https://www.google.com")

    # ---------- files and apps
    def c_open_file(self, m, t):
        path = find_file(m["name"])
        if path:
            self.say(f"Opening {path.name}.")
            open_path(path)
        else:
            self.say(f"Sorry, I couldn't find a file called {m['name']}.")

    def c_open_folder(self, m, t):
        name = m["name"].strip()
        target = next((d for d in SEARCH_DIRS if d.name.lower() == name), None)
        if target and target.exists():
            self.say(f"Opening {target.name}.")
            open_path(target)
        else:
            self.say("I couldn't find that folder.")

    def build_app_index(self):
        """List installed apps (Start menu on Windows) so 'open <anything>' works."""
        idx = {}
        try:
            if OS == "Windows":
                r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command",
                                    "Get-StartApps | ConvertTo-Json"],
                                   capture_output=True, text=True, timeout=90, creationflags=NO_WINDOW)
                data = json.loads(r.stdout or "[]")
                if isinstance(data, dict):
                    data = [data]
                for a in data:
                    if "uninstall" not in a["Name"].lower():
                        idx[norm(a["Name"])] = (a["Name"], "uwp", a["AppID"])
                for base in (Path(os.environ.get("ProgramData", "")) / "Microsoft/Windows/Start Menu/Programs",
                             Path(os.environ.get("APPDATA", "")) / "Microsoft/Windows/Start Menu/Programs"):
                    if base.exists():
                        for p in base.rglob("*.lnk"):
                            if "uninstall" not in p.stem.lower():
                                idx.setdefault(norm(p.stem), (p.stem, "lnk", str(p)))
            elif OS == "Darwin":
                for base in (Path("/Applications"), Path("/System/Applications"), HOME / "Applications"):
                    for p in base.glob("*.app"):
                        idx[norm(p.stem)] = (p.stem, "mac", p.stem)
            else:
                for base in (Path("/usr/share/applications"), HOME / ".local/share/applications"):
                    for p in base.glob("*.desktop"):
                        name = next((l[5:].strip() for l in p.read_text(errors="ignore").splitlines()
                                     if l.startswith("Name=")), p.stem)
                        idx[norm(name)] = (name, "linux", p.stem)
        except Exception:
            logger.exception("app index failed")
        self.app_index = idx
        logger.info("indexed %d apps", len(idx))

    def best_app(self, key):
        best = None
        for n, (disp, kind, target) in self.app_index.items():
            if key == n:
                s = 1.0
            elif key and len(n) >= 3 and (key in n or n in key):
                s = 0.8 + 0.2 * (min(len(key), len(n)) / max(len(key), len(n)))
            else:
                s = difflib.SequenceMatcher(None, key, n).ratio()
            if best is None or s > best[0]:
                best = (s, disp, kind, target)
        return best

    def launch(self, best):
        _, disp, kind, target = best
        self.say(f"Opening {disp}.")
        if kind == "uwp":
            subprocess.Popen(["explorer.exe", f"shell:AppsFolder\\{target}"], creationflags=NO_WINDOW)
        elif kind == "lnk":
            os.startfile(target)  # type: ignore[attr-defined]
        elif kind == "mac":
            subprocess.Popen(["open", "-a", target])
        else:
            subprocess.Popen(["gtk-launch", target])

    def c_open_app(self, m, t):
        name = re.sub(r"^(?:the|my)\s+", "", m["name"].strip())
        key = norm(name)
        if not key:
            return False
        web = difflib.get_close_matches(key, list(WEB_ALIASES), n=1, cutoff=0.85)
        if web:
            self.say(f"Opening {web[0]}.")
            webbrowser.open(WEB_ALIASES[web[0]])
            return
        best = self.best_app(key)
        if best and best[0] >= 0.85:
            return self.launch(best)
        if OS == "Windows":
            al = difflib.get_close_matches(key, list(WIN_ALIASES), n=1, cutoff=0.75)
            if al:
                self.say(f"Opening {al[0]}.")
                sh(WIN_ALIASES[al[0]])
                return
        if best and best[0] >= 0.6:
            return self.launch(best)
        fb = difflib.get_close_matches(key, list(WEB_FALLBACK), n=1, cutoff=0.85)
        if fb:
            self.say(f"I couldn't find the {fb[0]} app, so I'm opening it in your browser.")
            webbrowser.open(WEB_FALLBACK[fb[0]])
            return
        exe = shutil.which(key.replace(" ", ""))
        if exe:
            self.say(f"Opening {name}.")
            subprocess.Popen([exe])
            return
        path = find_file(key)
        if path:
            self.say(f"Opening {path.name}.")
            open_path(path)
            return
        self.say(f"Sorry, I couldn't find an app called {name}.")

    # ---------- WhatsApp
    def normalize_number(self, s):
        digits = re.sub(r"\D", "", s)
        if not digits:
            return None
        if digits.startswith("0") and len(digits) == 11:
            digits = digits[1:]
        if len(digits) == 10:
            digits = self.cfg.get("country_code", "91") + digits
        return digits

    def resolve_contact(self, who):
        who = re.sub(r"^(?:my|the)\s+", "", who.strip())
        if re.fullmatch(r"[\d\s+()-]{8,}", who):
            n = self.normalize_number(who)
            return (who, n) if n else None
        contacts = self._contact_book()
        hit = difflib.get_close_matches(who, list(contacts), n=1, cutoff=0.7)
        if hit:
            n = self.normalize_number(contacts[hit[0]])
            return (hit[0], n) if n else None
        return None

    def find_contact_prefix(self, text):
        words = text.split()
        contacts = self._contact_book()
        for n in range(min(3, len(words)), 0, -1):
            cand = re.sub(r"^(?:my|the)\s+", "", " ".join(words[:n]))      # "message my wife saying hi"
            hit = difflib.get_close_matches(cand, list(contacts), n=1, cutoff=0.75) if cand else []
            if hit:
                num = self.normalize_number(contacts[hit[0]])
                if num:
                    return hit[0], num, " ".join(words[n:])
        if words and re.fullmatch(r"\d{8,}", words[0]):
            return words[0], self.normalize_number(words[0]), " ".join(words[1:])
        return None

    def c_wa_preset(self, m, t):
        n = extract_number(m["num"])
        if n is None:
            return False
        msgs = self.cfg.get("messages", [])
        if not 1 <= n <= len(msgs):
            self.say(f"I only have {len(msgs)} preloaded messages. Say list messages to hear them.")
            return
        who = self.resolve_contact(m["who"])
        if not who:
            self.say(f"I couldn't find {m['who']} in your contacts. Add them with the Contacts button.")
            return
        self.confirm_whatsapp(who[0], who[1], msgs[n - 1])

    def c_wa_compose(self, m, t):
        rest = m["rest"].strip()
        found = self.find_contact_prefix(rest)
        if not found:
            self.say("I couldn't find that contact. Add them with the Contacts button first.")
            return
        name, number, body = found
        body = re.sub(r"^(?:saying|say|that|to say|says)\s+", "", body).strip()
        if body:
            self.confirm_whatsapp(name, number, polish(body))
        else:
            self.say(f"What should I say to {name}?")
            self.awaiting = lambda text: self.confirm_whatsapp(name, number, text)

    def confirm_whatsapp(self, name, number, message):
        def go():
            self.send_whatsapp(name, number, message)
        if self.cfg.get("confirm_send", True):
            self.ask(f'Send to {name}: "{message}". Shall I send it?', go)
        else:
            go()

    def send_whatsapp(self, name, number, message):
        text = quote(message)
        if OS == "Windows" and not protocol_registered("whatsapp"):
            webbrowser.open(f"https://web.whatsapp.com/send?phone={number}&text={text}")
            self.say(f"WhatsApp isn't installed, so I opened WhatsApp Web with your message to {name}. "
                     "Press Enter to send it.")
            return
        url = f"whatsapp://send?phone={number}&text={text}"
        try:
            open_path(url) if OS != "Windows" else os.startfile(url)  # type: ignore[attr-defined]
        except Exception:
            webbrowser.open(f"https://wa.me/{number}?text={text}")
            self.say("I opened WhatsApp in your browser. Press the send button to finish.")
            return
        self.say(f"Opening WhatsApp for {name}. Please don't touch the keyboard for a few seconds.")
        time.sleep(float(self.cfg.get("wa_delay", 7)))
        pyautogui.press("enter")
        self.say(f"Message sent to {name}.")

    def c_list_messages(self, m, t):
        msgs = self.cfg.get("messages", [])
        self.emit("sys", "Preloaded messages:\n" + "\n".join(f"  {i}. {x}" for i, x in enumerate(msgs, 1)))
        self._speak(f"You have {len(msgs)} preloaded messages. They are on screen. "
                    "Say, send message 2 to mom, for example.")

    def c_list_contacts(self, m, t):
        names = list(self.cfg.get("contacts", {}))
        if names:
            self.emit("sys", "Contacts: " + ", ".join(names))
            self._speak(f"You have {len(names)} contacts: " + ", ".join(names[:8]))
        else:
            self.say("You have no contacts yet. Use the Contacts button to add some.")

    # ---------- notes, timers, small stuff
    def c_note(self, m, t):
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M}] {m['txt']}\n")
        self.say("Noted.")

    def c_read_notes(self, m, t):
        if NOTES_FILE.exists():
            lines = NOTES_FILE.read_text(encoding="utf-8").strip().splitlines()[-5:]
            self.say("Your latest notes: " + ". ".join(l.split("] ", 1)[-1] for l in lines))
        else:
            self.say("You have no notes yet.")

    def c_open_notes(self, m, t):
        self.say("Opening your notes in Notepad.")
        open_in_notepad(NOTES_FILE)

    def c_open_knowledge(self, m, t):
        ensure_knowledge_file()
        self.say("Opening your facts file in Notepad. Save it and I'll know the new facts straight away.")
        open_in_notepad(KNOWLEDGE_FILE)

    def c_learn(self, m, t):
        fact = m["txt"]
        i = self.raw.lower().find(fact)          # keep the capital letters / punctuation you typed
        if i >= 0:
            fact = self.raw[i:].strip()
        Knowledge.add(fact)
        self.say("Got it. I'll remember that.")

    # ---------- long-term memory
    # Handlers whose repeated use (same words, same part of the day, several days) becomes a remembered routine.
    OBSERVE_HANDLERS = frozenset({"c_open_app", "c_website", "c_open_notes", "c_open_file", "c_open_folder", "c_youtube",
                                  "c_news", "c_mail_check", "c_schedule", "c_timer", "c_gesture", "c_vol_up",
                                  "c_vol_down", "c_screenshot", "c_open_google", "c_file_list", "c_file_move", "c_file_any"})
    MEMORY_CONTROLS = frozenset({"c_mem_remember", "c_mem_show", "c_mem_forget", "c_mem_forget_last", "c_mem_clear",
                                 "c_mem_toggle", "c_mem_open"})

    def _install_memory_hooks(self):
        global MEMORY_PATH_LOOKUP
        MEMORY_PATH_LOOKUP = self._memory_path

    def _memory_path(self, key):
        """A folder you nicknamed -> that folder, if it still exists."""
        if not self.mem_on():
            return None
        try:
            key = " ".join(norm(key).split())
            book = self.memory.folder_aliases()
            if key not in book:
                close = difflib.get_close_matches(key, list(book), n=1, cutoff=0.88)    # forgives a mis-heard word
                key = close[0] if close else key
            p = Path(book[key]) if key in book else None
            return p if p is not None and p.is_dir() else None
        except Exception:
            logger.exception("folder nickname lookup failed")
            return None

    def mem_on(self):
        return bool(self.cfg.get("memory_enabled", True))

    def mem_title(self):
        """What PAC calls you: 'sir' unless you asked to be called something else."""
        if self.mem_on():
            try:
                return self.memory.address() or "sir"
            except Exception:
                logger.exception("memory address lookup failed")
        return "sir"

    def _mem_block(self, query, cloud):
        """The few memories relevant to this request, formatted for an AI's system prompt ('' = none / not allowed)."""
        if not self.mem_on() or (cloud and not self.cfg.get("memory_share_ai", True)):
            return ""
        try:
            items = self.memory.recall(query)
            block = self.memory.format_block(items)
        except Exception:
            logger.exception("memory recall failed")
            return ""
        if not block:
            return ""
        self.memory.touch(items)
        if cloud and not self._mem_shared_note:
            self._mem_shared_note = True
            self.emit("sys", "(The few memories that fit a request are shared with the AI to personalise its answer. "
                             "Menu > Memory switches that off.)")
        return block

    @staticmethod
    def _pretty_number(n):
        d = re.sub(r"\D", "", n)
        return f"{d[:-5]} {d[-5:]}" if len(d) == 10 else n

    def _contact_book(self):
        """Your contacts, plus the people in your life by relationship ('wife', 'mother') when the name is a contact."""
        book = {k.lower(): v for k, v in self.cfg.get("contacts", {}).items()}
        if self.mem_on():
            try:
                for alias, target in self.memory.alias_map().items():
                    if alias not in book and target in book:
                        book[alias] = book[target]
            except Exception:
                logger.exception("alias lookup failed")
        return book

    def _mem_save_contact(self, name, number):
        contacts = self.cfg.setdefault("contacts", {})
        how = "updated" if name in contacts and contacts[name] != number else "known" if contacts.get(name) == number else "new"
        contacts[name] = number
        save_config(self.cfg)
        return name, number, how

    def _mem_say_saved(self, results, announce_hint=True):
        parts = []
        for r in results:
            if r[0] == "contact":
                _, name, number, how = r
                parts.append(f"{'Updated' if how == 'updated' else 'Saved'} {name} as {self._pretty_number(number)}")
                continue
            item, how = r
            if item.get("key") == "address":
                parts.append(f"Okay, from now on I'll call you {item['value']}")
            elif how == "known":
                parts.append("I already knew that")
            else:
                said = lower_first(you_form(item["text"]))
                parts.append(f"Okay, I've updated that: {said}" if how == "updated" else f"Noted, {said}")
        self.say(". ".join(parts) + ".")
        if announce_hint and not self._mem_hint_shown:
            self._mem_hint_shown = True
            self.emit("sys", "(Say 'forget that' to undo, or 'what do you remember about me' to see everything. "
                             "Menu > Memory has the settings.)")

    def _mem_save(self, found, source="auto"):
        """Keep what extract_memories() found. True if anything was saved or the sentence was clearly a memory request."""
        results, ids, refused = [], [], False
        for f in found:
            if f.get("kind") == "contact":
                if not self.guard(self.c_wa_compose):        # contacts belong to the 'messages' face group
                    return True
                results.append(("contact",) + self._mem_save_contact(*f["contact"]))
                continue
            if f.get("kind") == "folder":
                alias, ptext = f["folder"]
                path = resolve_folder(ptext, [], strict=True)         # must be a real folder, or it's no use to the file manager
                if path is None:
                    self.say(f"I couldn't find a folder called {ptext}, so I haven't saved {alias} as a nickname.")
                    return True
                item, how = self.memory.add(f["text"], "fact", f["key"], source, str(path))
                if item:
                    results.append((item, how))
                    ids.append(item["id"])
                continue
            item, how = self.memory.add(f["text"], f["kind"], f.get("key"), source, f.get("value"))
            if item is None:
                refused = refused or looks_secret(f["text"])
                continue
            results.append((item, how))
            ids.append(item["id"])
        if refused and f.get("explicit"):
            self.say("I don't keep passwords, PINs or card numbers in memory, because memory can be shared with the AI. "
                     "To store one privately on this laptop, say learn that, and the fact: that goes in your facts file, "
                     "which is never sent anywhere.", plain=True)
            return True
        if not results:
            return False
        if ids:
            self._mem_last = (ids, time.time())
        self._mem_say_saved(results)
        return True

    def memory_learn(self, raw, t, source):
        """Notice a statement about yourself ('my name is...', 'I prefer...', 'every morning I...') and keep it.
        True if the sentence was one (then it is not treated as a command)."""
        if not self.mem_on() or self._in_brain:
            return False
        found = extract_memories(raw)
        if not found:
            return False
        mode = self.cfg.get("memory_learn", "all")
        if mode == "explicit" or (mode == "typed" and source != "text"):
            found = [f for f in found if f.get("explicit")]
            if not found:
                return False
        if not self.guard(self.c_note):                      # face security: 'notes' group
            return True
        return self._mem_save(found, "auto")

    def memory_answer(self, t):
        """An answer to a question about you, from what you've told PAC. None unless it fits well."""
        if not self.mem_on():
            return None
        hits = self.memory.search(t, k=3)
        if not hits or hits[0][1] < 0.6:
            return None
        self.memory.touch([hits[0][2]])
        return you_form(hits[0][2]["text"]) + "."

    def memory_question(self, t):
        """'where do I live', 'who is my wife', 'what time do I wake up': answered from memory before any other
        command can misread them. Your own facts file still comes first."""
        if not self.mem_on() or not re.match(r"^(?:what|when|where|who|which|how|do i|did i|am i)\b", t) \
                or not re.search(r"\b(?:my|i|i'm|me|mine)\b", t):
            return False
        if self.kb.ask(t):
            return False
        ans = self.memory_answer(t)
        if not ans:
            return False
        self.say(ans)
        return True

    def _observe(self, fn, t):
        if getattr(fn, "__name__", "") == "c_file_move" and not re.search(r"\b(?:all|every|everything)\b", t):
            return                                           # a one-off move names a file; only bulk moves are routines
        if (getattr(fn, "__name__", "") in self.OBSERVE_HANDLERS and self.mem_on()
                and self.cfg.get("memory_habits", True)):
            try:
                self.memory.prune()
                item = self.memory.observe(t)
            except Exception:
                logger.exception("habit tracking failed")
                return
            if item:
                self._mem_last = ([item["id"]], time.time())        # so "forget that" removes exactly this
                self.emit("sys", f"(I've noticed a routine and noted it: {lower_first(item['text'])}. "
                                 "Say 'forget that' to remove it.)")

    # --- the AI brain's 'remember' / 'forget' tools
    @staticmethod
    def _first_person(text):
        """'The user loves jazz' -> 'I love jazz' (models sometimes ignore 'write it in the first person')."""
        m = re.match(r"^(?:the )?user(?:'s)?\s+(.*)$", text.strip(), re.I)
        if not m:
            return text
        rest = m.group(1)
        if re.match(r"^(?:name|birthday|wife|husband|mom|mother|dad|father|favou?rite)\b", rest, re.I):
            return "My " + rest                                  # "The user's name is Ankush"
        first, _, tail = rest.partition(" ")
        fix = {"is": "am", "has": "have", "does": "do", "goes": "go", "was": "was", "were": "was"}
        v = fix.get(first.lower(), first[:-1] if first.endswith("s") and not first.endswith("ss") and len(first) > 3 else first)
        return f"I {v} {tail}".strip()

    def _brain_memory(self, name, args, raw):
        text = self._first_person(str(args.get("text", "") or "").strip())
        if not text or not self.mem_on():
            return False
        if name == "forget":
            self._mem_forget_query(text)
            self.brain_remember(raw, f"[forgot: {text}]")
            return True
        found = extract_memories(text, explicit=True)
        if not found:
            clean = _tidy(text)
            kind = args.get("kind") if args.get("kind") in MEMORY_KINDS else infer_kind(clean)
            found = [_item(kind, clean, None, None, True)]
        if not self.guard(self.c_note):
            return True
        ok = self._mem_save(found, "brain")
        self.brain_remember(raw, f"[remembered: {text}]")
        return ok

    # --- commands
    def c_mem_remember(self, m, t):
        g = m.groupdict()
        stmt = g["txt"].strip()
        prefix = re.sub(FILLER_START, "", self.raw.strip(), flags=re.I)
        mm = re.match(r"^(?:remember|memori[sz]e|keep in mind|don'?t forget|do not forget)(?:\s+that)?\s+(.+)$", prefix, re.I | re.S)
        if mm:
            stmt = mm.group(1).strip()                       # keep the capital letters you typed
        found = extract_memories(stmt, explicit=True)
        if not found:
            if not _PERSONAL_START.match(stmt) or _TRANSIENT_RE.search(stmt):
                return False                                 # a note or reminder, not a lasting fact: c_note takes it
            clean = _tidy(stmt)
            if looks_secret(clean):
                self.say("I don't keep passwords, PINs or card numbers in memory, because memory can be shared with the "
                         "AI. To store one privately on this laptop, say learn that, and the fact.", plain=True)
                return
            found = [_item(infer_kind(clean), clean, None, None, True)]
        if not self.mem_on():
            self.say("My long-term memory is switched off. Say turn on memory first.")
            return
        self._mem_save(found, "said")

    def c_mem_show(self, m, t):
        topic = (m.groupdict().get("topic") or "").strip()
        kinds = None
        if re.search(r"routine|habit|schedule|day", topic):
            kinds = ("routine",)
        elif re.search(r"prefer|like|favou?rite|taste", topic):
            kinds = ("preference",)
        elif re.search(r"people|family|friend|contact|relat", topic):
            kinds = ("person",)
        groups = self.memory.grouped(kinds)
        total = sum(len(v) for v in groups.values())
        if not total:
            self.say("I haven't learned anything about you yet. Tell me things like my name is, or I prefer, "
                     "or every morning I, and I'll remember them.")
            return
        lines = []
        for kind in MEMORY_KINDS:
            if kind in groups:
                lines.append(MEMORY_KIND_LABEL[kind] + ":")
                lines += [f"  - {you_form(it['text'])}" for it in groups[kind]]
        book = len(self.cfg.get("contacts", {}))
        share = "off" if not self.cfg.get("memory_share_ai", True) else "on"
        lines.append(f"({'Memory is ON' if self.mem_on() else 'Memory is OFF'}; sharing relevant items with the AI is {share}. "
                     f"Contacts ({book}) are kept separately. Menu > Memory to edit.)")
        self.emit("sys", "What I remember about you:\n" + "\n".join(lines))
        top = [lower_first(you_form(it["text"])) for g in groups.values() for it in g][:3]
        self.say(f"I remember {total} thing{'s' if total != 1 else ''} about you. For example, {join_and(top)}. "
                 "The full list is on screen.")

    def _mem_forget_query(self, q):
        q = re.sub(r"^(?:that|about|what i (?:said|told you) about|the fact that)\s+", "", q.strip(), flags=re.I)
        hits = [(c, it) for _, c, it in self.memory.search(q, k=5) if c >= 0.5]
        if not hits:
            extra = (" Contacts are edited under Menu, Contacts and messages." if re.search(r"number|contact", q, re.I) else "")
            self.say(f"I couldn't find anything about {q} in my memory.{extra}")
            return
        gone = self.memory.remove([it["id"] for _, it in hits])
        self._mem_last = None                                # "forget that" now means the next thing learned, not this
        if len(gone) == 1:
            self.say(f"Okay, I've forgotten that {lower_first(you_form(gone[0]['text']))}.")
        else:
            self.emit("sys", "Forgotten:\n" + "\n".join(f"  - {you_form(i['text'])}" for i in gone))
            self.say(f"Okay, I've forgotten {len(gone)} things about {q}. They're listed on screen.")

    def c_mem_forget(self, m, t):
        q = (m.group("q") or "").strip()
        if not q or q in ("it", "this", "that"):
            return self.c_mem_forget_last(m, t)
        self._mem_forget_query(q)

    def c_mem_forget_last(self, m, t):
        ids, when = self._mem_last or ([], 0)
        if ids and time.time() - when < 900:
            gone = self.memory.remove(ids)
            self._mem_last = None
            if gone:
                self.say("Okay, forgotten: " + "; ".join(lower_first(you_form(i["text"])) for i in gone) + ".")
                return
        if re.search(r"wrong|right|incorrect|true|mistake", t):
            return False                                     # \"that's wrong\" about something else
        self.say("There's nothing recent to forget. Say forget about, and what to forget, "
                 "or say what do you remember about me to see everything.")

    def c_mem_clear(self, m, t):
        n = self.memory.count()
        if not n:
            self.say("My memory of you is already empty.")
            return

        def go():
            self.memory.clear()
            self._mem_last = None
            self.say("Done. I've forgotten everything I learned about you.")
        self.ask(f"Shall I forget all {n} things I've learned about you? Say yes or no.", go)

    def c_mem_toggle(self, m, t):
        g = m.groupdict()
        on = bool(g.get("on") or g.get("on2"))
        self.cfg["memory_enabled"] = on
        save_config(self.cfg)
        self.notify("memory_state", on)
        self.say("Long-term memory is on. I'll remember what you tell me about yourself." if on else
                 "Long-term memory is off. I won't learn or use anything about you until you turn it back on. "
                 "What I already know is kept.")

    def c_mem_open(self, m, t):
        self.notify("memory_edit", None)
        self.say("Opening your memories so you can read and edit them.")

    # ---------- e-mail
    def _mail_ready(self):
        if self.mailbox.configured():
            return True
        self.say("Your mail isn't set up yet. Click the Email setup button on the right and sign in with Google.")
        return False

    def _mail_error(self, e):
        logger.exception("mail problem")
        detail = f"{type(e).__name__}: {e}"
        if isinstance(e, MailAuthError):
            if e.code in ("invalid_grant",):
                return "Your Google sign-in has expired or was removed. Click Email setup and sign in again."
            if e.code in ("invalid_client", "unauthorized_client"):
                self.emit("sys", f"Google says: {e}. Check the Client ID and Client secret in Email setup.")
                return "Google didn't accept the Client ID or secret. Check them in Email setup."
            if e.code == "api_disabled":
                self.emit("sys", "The Gmail API is switched off for your Google Cloud project. Open "
                                 "console.cloud.google.com > APIs & Services > Library, search 'Gmail API', "
                                 "click Enable, wait a minute, then try again.")
                return "The Gmail API isn't switched on in your Google Cloud project. The steps are on screen."
            if e.code == "insufficient_scope":
                return "PAC needs a new permission. Click Email setup and sign in with Google again."
            self.emit("sys", f"Gmail problem: {detail}")
            return "Gmail refused that. The details are on screen."
        if isinstance(e, (OSError, TimeoutError)) or type(e).__module__.startswith("ssl"):
            self.emit("sys", f"Network problem: {detail}")
            return "I couldn't connect. The details are on screen."
        if isinstance(e, RuntimeError):
            return str(e)
        self.emit("sys", f"Unexpected mail error: {detail}  (full trace in ~/.pac/pac.log)")
        return "Something went wrong with the mail. The details are on screen."

    def _fetch_mail(self, unread_only):
        try:
            total, items = self.mailbox.recent(unread_only, int(self.cfg.get("mail_count", 10)))
        except Exception as e:
            self.say(self._mail_error(e))
            return None
        self.mail_list = items
        return total, items

    def _show_mail_list(self, speak=True):
        lines = [f"{i}. {it['name']} - {it['subject']}" for i, it in enumerate(self.mail_list, 1)]
        self.emit("sys", "\n".join(lines) or "(no mails)")
        if speak and self.mail_list:
            self._speak(". ".join(f"Mail {i}, from {it['name']}: {it['subject']}"
                                  for i, it in enumerate(self.mail_list[:5], 1)))

    def c_mail_check(self, m, t):
        if not self._mail_ready():
            return
        unread_only = not re.search(r"\b(?:inbox|all|latest|recent)\b", t)
        self.say("Checking your mail.")
        got = self._fetch_mail(unread_only)
        if got is None:
            return
        total, items = got
        if not items:
            self.say("You have no unread mail." if unread_only else "Your inbox is empty.")
            return
        if unread_only:
            self.say(f"You have {total} unread mail{'s' if total != 1 else ''}. Here are the latest {len(items)}.")
        else:
            self.say(f"Here are your latest {len(items)} mails.")
        self._show_mail_list()
        self.emit("sys", "Say 'delete mail 2', 'delete mails 1 and 3', 'delete mails from amazon' or "
                         "'review my mail' to go through them one by one. Nothing is removed without your yes.")

    def _confirm_trash(self, items):
        n = len(items)
        self.emit("sys", "Ready to move to Trash:\n" + "\n".join(f"  {it['name']} - {it['subject']}" for it in items))
        detail = "; ".join(f"{it['name']}: {it['subject']}" for it in items[:3]) + (" and more" if n > 3 else "")
        self.ask(f"Move {n} mail{'s' if n != 1 else ''} to Trash? {detail}. Say yes to confirm.",
                 lambda: self._do_trash(items))

    def _do_trash(self, items):
        err = None
        try:
            self.mailbox.trash([it["uid"] for it in items])
            done = {it["uid"] for it in items}
        except Exception as e:
            err, done = e, set(getattr(e, "done", []))
        self.mail_list = [x for x in self.mail_list if x["uid"] not in done]
        n = len(done)
        if err:
            msg = self._mail_error(err)
            self.say((f"I moved {n} to Trash, but then hit a problem. " if n else "") + msg)
            return
        self.say(f"Done. Moved {n} mail{'s' if n != 1 else ''} to Trash. You can still restore them from there.")
        if self.mail_list:
            self._show_mail_list(speak=False)

    def c_mail_delete(self, m, t):
        if not self._mail_ready():
            return
        what = f"{m['a']} {m['b']}".strip()
        if not self.mail_list:
            self.say("Say check my mail first, so I know which mails you mean.")
            return
        sender = re.search(r"\bfrom\s+(.+)$", what)
        if sender:
            want = norm(sender.group(1))
            picked = [it for it in self.mail_list if want and want in norm(f"{it['name']} {it['addr']}")]
            if not picked:
                self.say(f"None of the mails I listed are from {sender.group(1)}.")
                return
        elif re.search(r"\b(?:all|every|everything|these|them)\b", what):
            picked = list(self.mail_list)
        else:
            idx = parse_indices(what)
            bad = [i for i in idx if not 1 <= i <= len(self.mail_list)]
            if not idx or bad:
                self.say(f"There's no mail number {bad[0]}." if bad else
                         "Which mail? For example, say delete mail 2, or delete mails from amazon.")
                return
            picked = [self.mail_list[i - 1] for i in idx]
        self._confirm_trash(picked)

    def c_mail_review(self, m, t):
        """Read the mails out one by one; you say delete or keep for each; one final yes moves the chosen ones."""
        if not self._mail_ready():
            return
        self.say("Okay, let's go through your unread mail.")
        got = self._fetch_mail(True)
        if got is None:
            return
        if not got[1]:
            self.say("You have no unread mail.")
            return
        self.emit("sys", "For each mail say: delete, keep, or done to finish. Say stop to cancel - nothing is deleted then.")
        self._review_next({"items": got[1], "i": 0, "marked": []})

    def _review_next(self, st):
        items, i = st["items"], st["i"]
        if i >= len(items):
            return self._review_finish(st)
        it = items[i]
        self.emit("sys", f"{i + 1}/{len(items)}  {it['name']} - {it['subject']}")
        self.awaiting = lambda ans, st=st: self._review_answer(st, ans)
        self._speak(self._sirify(f"Mail {i + 1} of {len(items)}. From {it['name']}. {it['subject']}. Delete it?"))

    def _review_answer(self, st, ans):
        words = set(re.findall(r"[a-z']+", ans.lower()))
        if words & {"yes", "yeah", "yep", "yup", "delete", "remove", "trash", "bin"}:
            st["marked"].append(st["items"][st["i"]])
        elif words & {"no", "nope", "keep", "skip", "next", "leave"}:
            pass
        elif words & {"done", "finish", "finished", "enough", "end"}:
            return self._review_finish(st)
        elif words & {"repeat", "again"}:
            return self._review_next(st)
        else:
            self.say("Say delete, keep, or done.")
            self.awaiting = lambda a, st=st: self._review_answer(st, a)
            return
        st["i"] += 1
        self._review_next(st)

    def _review_finish(self, st):
        if not st["marked"]:
            self.say("Okay, I haven't deleted anything.")
            return
        self._confirm_trash(st["marked"])

    def start_timer(self, secs, message):
        tm = threading.Timer(secs, lambda: self.say(message))
        tm.daemon = True
        tm.start()

    @staticmethod
    def _amount(text):
        n = extract_number(text)
        if n is None and re.search(r"\b(?:a|an)\s+(?:second|minute|hour)", text):
            n = 1
        unit = "hour" if "hour" in text else "second" if "second" in text else "minute"
        return n, unit

    def c_timer(self, m, t):
        n, unit = self._amount(t)
        if not n:
            self.say("For how long?")
            return
        self.start_timer(n * {"hour": 3600, "minute": 60, "second": 1}[unit], "Your timer is done.")
        self.say(f"Timer set for {n} {unit}{'s' if n != 1 else ''}.")

    def c_remind(self, m, t):
        n, unit = self._amount(m["amt"])
        if not n:
            return False
        self.start_timer(n * {"hour": 3600, "minute": 60, "second": 1}[unit], f"Reminder: {m['what']}")
        self.say(f"Okay, I'll remind you in {n} {unit}{'s' if n != 1 else ''}.")

    def c_joke(self, m, t):
        self.say(random.choice(JOKES))

    def c_greet(self, m, t):
        if "night" in t:
            self.say("Good night! Sleep well.")
            return
        h = datetime.datetime.now().hour
        hello = "Good morning!" if h < 12 else "Good afternoon!" if h < 18 else "Good evening!"
        self.say((hello + " " + self._next_class_hint()).strip())

    def c_how_are_you(self, m, t):
        self.say("I'm doing great, thank you for asking! How can I help?")

    def c_who(self, m, t):
        self.say("I'm PAC, your personal assistant. I can open apps, search the web, "
                 "send messages and lots more.")

    def c_thanks(self, m, t):
        self.say("You're welcome!")

    def c_calc(self, m, t):
        expr = spoken_to_expr(m["expr"])
        if re.fullmatch(r"[\d\s+\-*/().%]+", expr) and re.search(r"\d", expr):
            try:
                val = safe_eval(expr)
                val = int(val) if float(val).is_integer() else round(val, 4)
                self.say(f"The answer is {val}.")
                return
            except Exception:
                pass
        if re.match(r"^(?:what|who|how|whats|what's)", t):
            return self.c_question(m, t)
        return False

    # ---------- maths: complex arithmetic, logarithms, algebra (offline first; the internet only as a fallback)
    def c_math(self, m, t):
        text = self.raw if self.raw and self.clean(self.raw) == t else t      # the raw text keeps 2.5, (1, 2) ...
        req = parse_math_request(text)
        if not req:
            return False                                                       # not maths: let the others try
        self.math_token += 1
        threading.Thread(target=self._math_job, args=(self.math_token, req), daemon=True).start()

    def _math_job(self, token, req):
        """Works the problem out on its own thread so a hard integral never holds up the next command."""
        slow = threading.Timer(2.5, lambda: token == self.math_token and self.emit("sys", "(still working it out...)"))
        slow.daemon = True
        slow.start()
        try:
            res, fail = solve_math(req), None
        except MathFail as e:
            res, fail = None, e
        except Exception:
            logger.exception("maths failed on %r", req.get("text"))
            res, fail = None, MathFail("something went wrong while working it out")
        finally:
            slow.cancel()
        if token != self.math_token:              # you said stop (or asked another sum) meanwhile
            return
        if res:
            self.emit("sys", "\n".join(res["lines"]))
            self.say(res["say"])
            if res.get("hint"):
                self.emit("sys", res["hint"])
            return
        if fail.need_sympy:
            self.ask("That needs SymPy, a free maths library that isn't installed yet. Shall I install it?",
                     lambda: self.install_sympy(req))
            return
        if fail.final:                            # "that divides by zero" IS the answer
            self.say(_sentence(str(fail)))
            return
        self.math_online(req, str(fail))

    def install_sympy(self, req=None):
        """pip-install SymPy into the Python running PAC, then (if there was one) solve the problem that needed it."""
        def work():
            if _sympy() is None:
                self.say("Installing the maths engine. It takes a minute or two.")
                ok = pip_install(["sympy"], lambda s: self.emit("sys", s), "the maths engine (SymPy)",
                                 "Installed - exact algebra now works offline.")
                reset_sympy()
                if not ok or _sympy() is None:
                    self.say("I couldn't install the maths engine. The details are in the chat.")
                    return
            elif not req:
                self.say("The maths engine is already installed.")
                return
            if req:
                self.math_token += 1
                self._math_job(self.math_token, req)
            else:
                self.say("The maths engine is ready.")
        threading.Thread(target=work, daemon=True).start()

    def math_online(self, req, why=""):
        """PAC couldn't do it offline (usually a word problem): Wolfram|Alpha if you've added a free AppID, then Claude
        if Claude mode is on, then a quiet web search that reads the top pages. Nothing goes online if you switched
        that off (Menu > Maths)."""
        q = req["text"]
        if not self.cfg.get("math_online", True):
            self.say(_sentence(f"I couldn't work that out offline - {why}" if why else "I couldn't work that out offline"))
            return
        self.emit("sys", f"(Couldn't do this one offline{': ' + why if why else ''}. Looking it up online...)")
        appid = (self.cfg.get("wolfram_appid") or "").strip()
        if appid:
            try:
                ans = wolfram_short_answer(appid, q)
            except Exception as e:
                logger.warning("Wolfram|Alpha failed: %s", e)
                self.emit("sys", f"Wolfram|Alpha: {e}")
                ans = ""
            if ans:
                self.emit("sys", f"Wolfram|Alpha: {ans}")
                self.say(ans)
                return
        if self.claude_on:
            self.claude_answer(q)
            return
        if self.bg_search_on():
            self.start_search(q)
            return
        self.say("I couldn't work that out offline, and quiet web lookups are switched off under Menu, Assistant.")

    # ---------- system controls
    def c_vol_up(self, m, t):
        for _ in range(5):
            pyautogui.press("volumeup")

    def c_vol_down(self, m, t):
        for _ in range(5):
            pyautogui.press("volumedown")

    def c_mute(self, m, t):
        pyautogui.press("volumemute")

    def c_screenshot(self, m, t):
        try:
            path = HOME / "Pictures" / f"pac_{datetime.datetime.now():%Y%m%d_%H%M%S}.png"
            path.parent.mkdir(exist_ok=True)
            pyautogui.screenshot(str(path))
            self.say("Screenshot saved in your Pictures folder.")
        except Exception as e:
            logger.exception("screenshot")
            self.say("Sorry, I couldn't take a screenshot. Try: pip install pillow")

    def c_minimize(self, m, t):
        pyautogui.hotkey("win", "d") if OS == "Windows" else pyautogui.hotkey("command", "m")

    def c_close_window(self, m, t):
        pyautogui.hotkey("alt", "f4") if OS != "Darwin" else pyautogui.hotkey("command", "w")

    def c_battery(self, m, t):
        b = psutil.sensors_battery()
        if b is None:
            self.say("I can't see a battery on this computer.")
        else:
            self.say(f"Battery is at {int(b.percent)} percent" + (" and charging." if b.power_plugged else "."))

    def c_system(self, m, t):
        self.say(f"CPU is at {psutil.cpu_percent(interval=0.5)} percent and memory is at "
                 f"{psutil.virtual_memory().percent} percent.")

    def c_time(self, m, t):
        self.say("It's " + datetime.datetime.now().strftime("%I:%M %p").lstrip("0"))

    def c_date(self, m, t):
        self.say("Today is " + datetime.datetime.now().strftime("%A, %d %B %Y"))

    # ---------- schedule (reads ~/.pac/timetable.txt)
    def startup_greeting(self):
        h = datetime.datetime.now().hour
        hello = "Good morning!" if h < 12 else "Good afternoon!" if h < 18 else "Good evening!"
        return f"{hello} I'm PAC. How can I help you today? {self._next_class_hint()}".strip()

    def _next_class_hint(self):
        if not self.timetable.load():
            return ""
        now = datetime.datetime.now()
        cur, nxt = self.timetable.now_and_next(now)
        if cur:
            return f"You're in {cur['subject']} until {fmt_time(cur['end'])}."
        if nxt and nxt["start"] - (now.hour * 60 + now.minute) <= 180:
            return f"Your next class is {nxt['subject']} at {fmt_time(nxt['start'])}."
        return ""

    def c_timetable_import(self, m, t):
        self.say("Choose your timetable file.")
        self.notify("timetable_import", True)

    def c_timetable_edit(self, m, t):
        self.say("Opening your timetable.")
        self.notify("timetable_edit", True)

    def _tt_missing(self, clear):
        """True if there is no timetable yet (and, if the request was clearly about one, tells the user how)."""
        if self.timetable.load():
            return False
        if clear:
            ensure_timetable_file()
            self.say("I don't have your timetable yet. I've opened the editor - paste your classes there and save.")
            self.emit("sys", "Format, one class per line:\n  Monday 09:00-10:00 Mathematics, Room 204\n"
                             "  Tue/Thu 2 pm - 3 pm Chemistry\n(or paste a CSV grid with the days across the top)")
            self.notify("timetable_edit", True)
        return True

    @staticmethod
    def _room(e):
        return f" in {e['room']}" if e.get("room") else ""

    @staticmethod
    def _line(e):
        return f"{fmt_range(e['start'], e['end'])}   {e['subject']}" + (f"   ({e['room']})" if e.get("room") else "")

    def c_schedule(self, m, t):
        if re.match(r"^(?:open|type|write|send|search|google|play|note|learn|remember|delete|message|text|whatsapp|"
                    r"go|visit|schedule (?:a|an))\b", t):
            return False
        about_classes = re.search(r"\b(?:schedule|timetable|time table|classes|lectures)\b|\b(?:next|current) (?:class|lecture|period)\b", t)
        if self._tt_missing(bool(about_classes)):
            return False if not about_classes else None
        now = datetime.datetime.now()
        if re.search(r"\bnow\b", self.raw.lower()):         # clean() trims a trailing "now"; it matters here
            t += " now"
        if re.search(r"\bnext (?:class|lecture|period)\b|\bwhat(?:'s| is) next\b", t):
            return self._say_next(now)
        if re.search(r"\b(?:current|right now|ongoing|now)\b", t) and re.search(r"\b(?:class|lecture|period)\b|\bfree\b", t):
            return self._say_current(now)
        if re.search(r"\bam i free\b", t):
            return self._say_current(now)
        if re.search(r"\b(?:week|weekly|whole|full|entire)\b", t):
            return self._say_week()
        day, label = self._pick_day(t, now)
        self._say_day(day, label, now)

    @staticmethod
    def _pick_day(t, now):
        if "day after tomorrow" in t:
            off = 2
        elif "tomorrow" in t:
            off = 1
        elif "yesterday" in t:
            off = -1
        else:
            off = None
            for w in re.findall(r"[a-z]+", t):
                d = day_index(w)
                if d is not None and w not in ("sun", "sat") or (d is not None and re.search(r"\b(?:on|for)\s+" + w, t)):
                    off = (d - now.weekday()) % 7
                    break
            if off is None:
                off = 0
        day = (now.weekday() + off) % 7
        label = {0: "today", 1: "tomorrow", -1: "yesterday", 2: "the day after tomorrow"}.get(
            off, f"on {DAYS[day].capitalize()}")
        if off == 0 and re.search(r"\b(?:on|for)\s+" + DAYS[now.weekday()], t):
            label = f"on {DAYS[now.weekday()].capitalize()}"
        return day, label

    def _say_day(self, day, label, now):
        items = self.timetable.on(day)
        is_today = label == "today"
        if not items:
            self.say(f"You have no classes {label}." + (" Enjoy the free time!" if is_today else ""))
            return
        full_list = f"Schedule {label}:\n" + "\n".join("  " + self._line(e) for e in items)
        mins = now.hour * 60 + now.minute
        show, done = items, 0
        if is_today:
            show = [e for e in items if e["end"] > mins]
            done = len(items) - len(show)
            if not show:
                self.say(f"You've finished all {len(items)} classes for today.")
                self.emit("list", full_list)
                return
        head = (f"Today you have {len(items)} class{'es' if len(items) != 1 else ''}"
                + (f", {done} already done" if done else "") + ". " if is_today
                else f"{label[0].upper() + label[1:]} you have {len(items)} class{'es' if len(items) != 1 else ''}. ")
        spoken = [f"{e['subject']} at {fmt_time(e['start'])}{self._room(e)}" for e in show[:5]]
        more = f", and {len(show) - 5} more. The full list is on screen" if len(show) > 5 else ""
        self.say(head.rstrip(". ") + ": " + join_and(spoken) + more + ".")
        self.emit("list", full_list)          # after the spoken line, so it stays at the bottom of the chat, bright and readable

    def _say_next(self, now):
        cur, nxt = self.timetable.now_and_next(now)
        mins = now.hour * 60 + now.minute
        prefix = f"You're in {cur['subject']} until {fmt_time(cur['end'])}. " if cur else ""
        if nxt:
            gap = nxt["start"] - mins
            when = f", in {gap} minutes" if 0 < gap <= 90 else ""
            self.say(f"{prefix}Your next class is {nxt['subject']} at {fmt_time(nxt['start'])}{self._room(nxt)}{when}.")
            return
        e, ahead = self.timetable.next_class(now)
        if not e:
            self.say(f"{prefix}I don't see any upcoming classes.")
        else:
            day = "tomorrow" if ahead == 1 else f"on {DAYS[e['day']].capitalize()}"
            self.say(f"{prefix}You're done for today. Your next class is {e['subject']} {day} at "
                     f"{fmt_time(e['start'])}{self._room(e)}.")

    def _say_current(self, now):
        cur, nxt = self.timetable.now_and_next(now)
        if cur:
            self.say(f"Right now you have {cur['subject']} until {fmt_time(cur['end'])}{self._room(cur)}.")
        else:
            self.say("You're free right now. " + (f"Your next class is {nxt['subject']} at {fmt_time(nxt['start'])}."
                                                  if nxt else "No more classes today."))

    def _say_week(self):
        lines, total, busiest = [], 0, (0, None)
        for d in range(7):
            items = self.timetable.on(d)
            if items:
                lines.append(DAYS[d].capitalize())
                lines += ["  " + self._line(e) for e in items]
                total += len(items)
                if len(items) > busiest[0]:
                    busiest = (len(items), d)
        self.say(f"Your whole week is on screen. That's {total} classes, and {DAYS[busiest[1]].capitalize()} "
                 f"is the busiest with {busiest[0]}.")
        self.emit("list", "Your week:\n" + "\n".join(lines))

    def c_when_class(self, m, t):
        if not self.timetable.load():
            return False
        hits = self.timetable.find(m["subj"])
        if not hits:
            return False                  # not one of my classes - let the other commands try
        parts = [f"{DAYS[e['day']].capitalize()} at {fmt_time(e['start'])}" for e in hits[:7]]
        self.say(f"{hits[0]['subject']} is on {join_and(parts)}.")

    # ---------- smarter little helpers
    # ---------- faces: who is at the laptop, and what they may do
    def face_denied(self, status, name="", role="", need=""):
        if status == "nocam":
            err = (self.faces.error or "").split("\n")[0]
            self.say("I can't see through the camera, so I can't check your face. " + err +
                     " If this keeps locking you out, use Menu, Faces, Camera trouble.", plain=True)
        elif status == "noface":
            self.say("I can't see a face. Look at the camera and ask again.", plain=True)
        elif status == "unknown":
            self.say("I don't recognise you, so I won't do that.", plain=True)
        else:
            self.say(f"Sorry {name}, that needs {need} permission and you're {role}.", plain=True)

    def face_check(self, need):
        """Looks at the camera. True if the face in front of it is enrolled with at least the `need` role."""
        key, score, status = self.faces.verify()
        if status != "ok":
            self.face_denied(status)
            return False
        p = self.faces.db.get(key) or {}
        role = p.get("role", "guest")
        if FACE_LEVELS.get(role, 0) < FACE_LEVELS[need]:
            self.face_denied("role", p.get("name", ""), role, need)
            return False
        self.emit("sys", f"(face check passed: {p.get('name', '')})")
        return True

    def require_owner(self):
        """Managing faces needs an owner's face - unless nobody is enrolled yet, or face security is off."""
        if self.faces is None or not self.faces.db.owners() or not self.cfg.get("face_security"):
            return True
        return self.face_check("owner")

    def guard(self, fn):
        group = FACE_GROUPS.get(getattr(fn, "__name__", ""))
        if not group or not self.cfg.get("face_security") or self.faces is None or not self.faces.db.owners():
            return True
        need = face_rule(self.cfg, group)
        return need == "anyone" or self.face_check(need)

    def on_face_event(self, kind, key):
        """Called from the camera thread when someone arrives, leaves, or a stranger sits down."""
        p = self.faces.db.get(key) if key else None
        name = p["name"] if p else ""
        if kind != "unknown" and not p:                  # forgotten a moment ago
            return
        if kind == "arrive":
            self.emit("sys", f"(I can see {name})")
            if self.asleep:
                return
            now = time.time()
            if self.cfg.get("face_greet", True) and now - self._last_greet.get(key, 0) > 1800:
                self._last_greet[key] = now
                self.say(f"Welcome back, {name}.", plain=True)
            if p.get("on_arrival"):
                self.notify("submit", p["on_arrival"])
        elif kind == "leave":
            self.emit("sys", f"({name} has gone out of sight)")
            if (self.cfg.get("face_lock_on_leave") and self.cfg.get("face_security") and p.get("role") == "owner"
                    and not any((self.faces.db.get(k) or {}).get("role") == "owner" for k in self.faces.present
                                if self.faces.present[k])):
                self.emit("sys", "(the owner left, locking the laptop)")
                run_power("lock")
        elif kind == "unknown":
            self.emit("sys", "(someone I don't recognise is at the laptop)")
            if not self.asleep:
                self.say("I don't recognise the person at the laptop.", plain=True)

    def _face_name(self, text):
        return self.faces.db.key(text) if self.faces else ""

    def c_face_enroll(self, m, t):
        name, role = (m["n"] or "").strip(), (m["r"] or "").strip()
        if name in FACE_ROLES or name == "family":
            role, name = name, ""
        role = "trusted" if role == "family" else role
        if not name:
            self.awaiting = lambda txt: self.face_enroll(txt, role)
            self.say("What name should I save this face under?", plain=True)
            return
        self.face_enroll(name, role)

    def face_enroll(self, name, role=""):
        name = self.faces.db.key(name)
        if not name or len(name) > 30:
            self.say("I couldn't use that as a name. Say enroll my face again.", plain=True)
            return
        first = not self.faces.db.owners()
        if not first and not self.require_owner():
            return
        existing = self.faces.db.get(name)                           # more pictures of someone already known
        role = "owner" if first else (role or (existing["role"] if existing else "guest"))
        shown = name.title()
        self.say(f"Okay {shown}. Look at the camera and slowly turn your head a little. This takes about ten seconds.",
                 plain=True)

        def work():
            embs, problem = self.faces.enroll(name)
            if problem:
                self.say(problem, plain=True)
                return
            self.faces.db.add(name, role, embs)
            self.say(f"Done. I'll recognise you now, {shown}. You're saved as {role}."
                     + (" Say turn on face security when you want commands locked to faces." if first else ""),
                     plain=True)
        threading.Thread(target=work, daemon=True).start()

    def c_face_forget(self, m, t):
        db = self.faces.db
        name = (m["n"] or "").strip()
        if not self.require_owner():
            return
        if name in ("", "all", "everyone", "everybody", "all faces", "everything"):
            if not db.people:
                self.say("I don't have any faces saved.", plain=True)
                return

            def go():
                db.remove_all()
                self.cfg["face_security"] = False
                save_config(self.cfg)
                self.notify("face_security", False)
                self.say("Done. I've forgotten every face, and face security is off.", plain=True)
            self.ask("Forget every saved face? Say yes or no.", go)
            return
        if not db.has(name):
            self.say(f"I don't know a face called {name}.", plain=True)
            return
        db.remove(name)
        self._after_face_removed(f"Okay, I've forgotten {name.title()}'s face.")

    def _after_face_removed(self, said):
        if self.cfg.get("face_security") and not self.faces.db.owners():
            self.cfg["face_security"] = False
            save_config(self.cfg)
            self.notify("face_security", False)
            said += " There's no owner left, so face security is off."
        self.say(said, plain=True)

    def c_face_who(self, m, t):
        ppl = self.faces.look()
        if ppl is None:
            self.face_denied("nocam")
            return
        if not ppl:
            self.say("I can't see anyone.", plain=True)
            return
        known = [self.faces.db.get(k)["name"] for k, _ in ppl if k]
        strangers = sum(1 for k, _ in ppl if not k)
        bits = []
        if known:
            bits.append(join_and(known))
        if strangers:
            bits.append("one person I don't recognise" if strangers == 1 else f"{strangers} people I don't recognise")
        self.say("I can see " + " and ".join(bits) + ".", plain=True)

    def c_face_list(self, m, t):
        db = self.faces.db
        if not db.people:
            self.say("I don't know any faces yet. Say enroll my face.", plain=True)
            return
        lines = [f"  {p['name']}  -  {p['role']}" + (f"  -  on arrival: {p['on_arrival']}" if p.get("on_arrival") else "")
                 for p in db.people.values()]
        self.emit("list", "Faces I know:\n" + "\n".join(lines))
        self.say(f"I know {len(lines)} {'face' if len(lines) == 1 else 'faces'}: " + join_and(db.names()) + ".", plain=True)

    def c_face_watch(self, m, t):
        if not m["on"] and self.cfg.get("face_security") and not self.require_owner():
            return
        self.notify("face", "on" if m["on"] else "off")

    def c_face_security(self, m, t):
        if m["on"]:
            if not self.faces.db.owners():
                self.say("I need to know your face first. Say enroll my face.", plain=True)
                return
            self.cfg["face_security"] = True
            save_config(self.cfg)
            self.notify("face_security", True)
            self.say("Face security is on. I'll check your face before the commands you've locked.", plain=True)
            return
        if not self.require_owner():
            return
        self.cfg["face_security"] = False
        save_config(self.cfg)
        self.notify("face_security", False)
        self.say("Face security is off.", plain=True)

    def c_face_role(self, m, t):
        name, role = (m["n"] or "").strip(), m["r"]
        if not self.faces.db.has(name):
            return False
        role = "trusted" if role == "family" else role
        if not self.require_owner():
            return
        k = self.faces.db.key(name)
        if self.faces.db.get(k)["role"] == "owner" and role != "owner" and len(self.faces.db.owners()) == 1:
            self.say("That's the only owner. Make someone else the owner first.", plain=True)
            return
        self.faces.db.set_role(name, role)
        self.say(f"{name.title()} is now {role}.", plain=True)

    def c_face_arrival(self, m, t):
        name, cmd = (m["n"] or "").strip(), (m["cmd"] or "").strip()
        if not self.faces.db.has(name) or not cmd:
            return False
        if not self.require_owner():
            return
        self.faces.db.set_arrival(name, cmd)
        self.say(f"Okay. When {name.title()} arrives I'll run: {cmd}.", plain=True)

    def c_face_arrival_clear(self, m, t):
        name = (m["n"] or "").strip()
        if not self.faces.db.has(name):
            return False
        if not self.require_owner():
            return
        self.faces.db.set_arrival(name, "")
        self.say(f"Okay, nothing will run when {name.title()} arrives.", plain=True)

    def c_face_rule(self, m, t):
        group, level = m["g"], m["lvl"]
        if group not in FACE_GROUP_LABEL:
            self.say("The groups are: " + ", ".join(FACE_GROUP_LABEL) + ".", plain=True)
            return
        if not self.require_owner():
            return
        self.cfg.setdefault("face_rules", {})[group] = level
        save_config(self.cfg)
        self.say(f"Okay. {FACE_GROUP_LABEL[group].capitalize()} now needs {level}." if level != "anyone"
                 else f"Okay. Anyone can use {FACE_GROUP_LABEL[group]}.", plain=True)

    def c_face_rules_list(self, m, t):
        lines = [f"  {g:<9} {face_rule(self.cfg, g):<8} {label}" for g, label in FACE_GROUP_LABEL.items()]
        self.emit("list", "Who may do what (when face security is on):\n" + "\n".join(lines))
        self.say("The rules are on screen. Say face rule, a group, then anyone, guest, trusted or owner, to change one.",
                 plain=True)

    # ---------- augmented reality
    @staticmethod
    def _ar_display(raw):
        s = " ".join(re.sub(r"[^a-z0-9' -]", " ", raw.lower()).split())
        return re.sub(r"^my ", "your ", s)

    def _ar_ready(self):
        if self.ar is None:
            self.say("Augmented reality isn't available in this window.")
            return False
        return True

    def c_ar_toggle(self, m, t):
        self.notify("ar", "on" if m["on"] else "off")

    def c_ar_learn(self, m, t):
        if t.startswith("this is") and not (self.ar is not None and self.ar.running):
            return False                                   # just a sentence, not a lesson
        display = self._ar_display(m["n"])
        key = ARVision.key_of(display)
        if not key or len(key) > 40:
            return False
        if not self._ar_ready():
            return
        if key in AR_SHAPES:
            self.say(f"A {key} is one of the shapes I already know. Say when you see a {key}, then what to do.")
            return
        self.say(f"Okay. Hold {display} inside the box and turn it slowly. This takes a few seconds.", plain=True)

        def work():
            ok, msg = self.ar.learn(display, key)
            self.say(msg, plain=True)
        threading.Thread(target=work, daemon=True).start()

    def c_ar_what(self, m, t):
        if self.ar is None or not self.ar.running:
            self.say("Augmented reality is off. Say start AR, then show me something.")
            return
        names, shape = self.ar.what_now()
        if names:
            self.say("I can see " + join_and(names) + (f", and a {shape} shape in the box" if shape else "") + ".")
        elif shape:
            self.say(f"I can see a {shape} shape in the box. I don't know it as an object yet. "
                     "Say learn this as, and a name, to teach me.")
        else:
            self.say("I can't see anything I know. Hold it inside the box, or say learn this as, and a name.")

    def c_ar_list(self, m, t):
        if not self._ar_ready():
            return
        rows = self.ar.entries()
        if not rows:
            self.say("I haven't learned any objects yet. Say start AR, hold something in the box, and say learn this as, and a name.")
            return
        lines = [f"  {name}   ({'shape' if kind == 'shape' else str(n) + ' views'})" + (f"  ->  {act}" if act else "")
                 for _k, name, kind, act, n in rows]
        self.emit("list", "What I recognise:\n" + "\n".join(lines))
        objs = [r[1] for r in rows if r[2] == "object"]
        self.say(f"I know {len(objs)} object{'s' if len(objs) != 1 else ''}" + (": " + join_and(objs[:6]) if objs else "") + ". The full list is on screen.")

    def c_ar_forget(self, m, t):
        if not self._ar_ready():
            return
        name = m["n"].strip()
        if name in ("all", "everything", "all objects", "all of them"):
            n = self.ar.remove_all()
            self.say(f"Done. I've forgotten {n} object{'s' if n != 1 else ''}." if n else "I hadn't learned any objects.")
            return
        key = self.ar.find_key(name)
        if key is None or key.startswith("shape:"):
            self.say(f"I don't know an object called {name}.")
            return
        label = self.ar.objs[key]["name"]
        self.ar.remove(key)
        self.say(f"Okay, I've forgotten {label}.")

    def c_ar_bind(self, m, t):
        if not self._ar_ready():
            return
        display = self._ar_display(m["n"])
        key = self.ar.find_key(display)
        cmd = m["cmd"].strip()
        if cmd.startswith("say "):                          # keep the capital letters you typed
            mm = re.search(r"\bsay\s+(.+)$", self.raw.strip().rstrip(".!?"), re.I)
            cmd = "say " + (mm.group(1) if mm else cmd[4:])
        if key is None:
            self.say(f"I haven't learned {display} yet. Say learn this as {display} first.")
            return
        if key.startswith("shape:"):
            self.ar.set_action(key, cmd, name=key[6:], kind="shape")
        else:
            self.ar.set_action(key, cmd)
        shown = self.ar.objs.get(key, {}).get("name", display)
        self.say(f"Okay. When I see {shown} I'll {'say that' if cmd.startswith('say ') else cmd}."
                 + ("" if self.ar.running else " Say start AR for me to watch."))

    def c_ar_unbind(self, m, t):
        if not self._ar_ready():
            return
        name = (m.groupdict().get("n") or "").strip()
        if not name:
            self.say("Which one? Say clear AR action for, and its name.")
            return
        key = self.ar.find_key(name)
        if key is None:
            self.say(f"I don't know {name}.")
            return
        if key.startswith("shape:"):
            self.ar.set_action(key, "", name=key[6:], kind="shape")
        else:
            self.ar.set_action(key, "")
        self.say(f"Okay, nothing will happen when I see {name}.")

    def c_ar_presets(self, m, t):
        lines = [f"  {n}  -  {d}" for n, d in AR_PRESETS.items()]
        self.emit("list", "Things PAC already guesses by outline (hold one in the guide box):\n" + "\n".join(lines))
        self.say("I already know a " + ", ".join(list(AR_PRESETS)[:-1]) + " and a " + list(AR_PRESETS)[-1] +
                 " by their shape. They're guesses, so teach me yours for a sure match.")

    def c_ar_starter(self, m, t):
        if not self._ar_ready():
            return
        n = self.ar.starter_pack()
        lines = [f"  {s}  ->  {c}" for s, c in AR_STARTER.items()]
        self.emit("list", "AR starter commands (hold the shape in the box):\n" + "\n".join(lines))
        self.say(f"Added {n} starter shape command{'s' if n != 1 else ''}. They're on screen. Change them under Menu, "
                 "Augmented reality, Objects and actions." if n else "The starter shape commands are already set up.")

    def c_gesture(self, m, t):
        self.notify("gesture", "on" if m["on"] else "off")

    def c_air_drag(self, m, t):
        on = bool(m.groupdict().get("on"))
        self.notify("airdrag", "on" if on else "off")
        self.say("Air drag and drop is on. Pinch your thumb and finger together to select and drag a file, and let go to drop it."
                 if on else "Air drag and drop is off.")

    def c_gesture_teach(self, m, t):
        self.say("Okay, opening the gesture teacher.")
        self.notify("gesture", "teach")

    def c_gesture_list(self, m, t):
        self.notify("gesture", "list")

    def c_gesture_delete_dialog(self, m, t):
        self.say("Opening the gesture list. Tick the ones you want to delete.")
        self.notify("gesture", "delete")

    @staticmethod
    def _gcore(s):
        """A gesture name boiled down for matching: 'Peace sign' / 'the peace sign gesture' -> 'peace'."""
        return " ".join(norm(re.sub(r"\b(?:hand|gestures?|signs?|the|my|an?)\b", " ", s.lower())).split())

    def _find_gestures(self, text):
        """Ids of the gestures whose name fits what was said ('thumbs up', 'the fist', 'peace sign')."""
        core = self._gcore
        q = core(text)
        if not q:
            return []
        pool = {core(label): gid for gid, label in GESTURES.items() if not gesture_is_deleted(self.cfg, gid)}
        pool.update({core(g["name"]): g["id"] for g in self.cfg.get("custom_gestures", [])})
        if q in pool:
            return [pool[q]]
        hits = [gid for name, gid in pool.items() if name and (q in name or name in q)]
        if hits:
            return hits
        close = difflib.get_close_matches(q, list(pool), n=1, cutoff=0.7)
        return [pool[close[0]]] if close else []

    def c_gesture_delete(self, m, t):
        name = (m.groupdict().get("a") or m.groupdict().get("b") or "").strip()
        q = self._gcore(name)
        gone = [GESTURES[g] for g in (self.cfg.get("deleted_gestures") or []) if g in GESTURES and self._gcore(GESTURES[g]) == q]
        if gone:                           # not "Both fists" just because plain "Fist" is already gone
            self.say(f"The {gone[0]} gesture is already deleted. Say restore gestures to bring it back.")
            return
        hits = self._find_gestures(name)
        if not hits:
            self.say(f"I couldn't find a gesture called {name}. Say delete gestures to pick from the list.")
            return
        if len(hits) > 1:
            names = join_and([gesture_title(self.cfg, g) for g in hits[:4]])
            self.say(f"That could be {names}. Say delete, then the full name, or say delete gestures to pick from the list.")
            return
        gid = hits[0]
        label = gesture_title(self.cfg, gid)
        taught = gid.startswith("custom:")

        def go():
            delete_gestures(self.cfg, [gid])
            self.say(f"Done. The {label} gesture is deleted." + ("" if taught else " Say restore gestures to bring it back."))
        self.ask(f"Delete the {label} gesture? " + ("It will be erased for good. " if taught else "") + "Say yes to confirm.", go)

    def c_gesture_restore(self, m, t):
        back = restore_gestures(self.cfg)
        if back:
            self.say(f"Restored {join_and(back)}.")
        else:
            self.say("No built-in gestures are deleted. A gesture you taught and deleted has to be taught again.")

    def c_repeat(self, m, t):
        if self.last_reply:
            self.say(self.last_reply)
        else:
            self.say("I haven't said anything yet.")

    def _when_clock(self, text):
        got = parse_clock(text)
        if not got:
            return None
        mins, explicit = got
        now = datetime.datetime.now()
        base = now.replace(hour=0, minute=0, second=0, microsecond=0)
        options = [base + datetime.timedelta(minutes=mins), base + datetime.timedelta(days=1, minutes=mins)]
        if not explicit and mins < 12 * 60:
            options.insert(1, base + datetime.timedelta(minutes=mins + 720))
        target = next(o for o in sorted(options) if o > now)
        return target, mins

    def c_remind_at(self, m, t):
        got = self._when_clock(m["when"])
        if not got:
            return False
        target, mins = got
        self.start_timer((target - datetime.datetime.now()).total_seconds(), f"Reminder: {m['what']}")
        day = "" if target.date() == datetime.datetime.now().date() else " tomorrow"
        self.say(f"Okay, I'll remind you{day} at {fmt_time(target.hour * 60 + target.minute)}.")

    def c_alarm(self, m, t):
        got = self._when_clock(m["when"])
        if not got:
            return False
        target, mins = got
        self.start_timer((target - datetime.datetime.now()).total_seconds(), "Time's up! Your alarm is going off.")
        day = "" if target.date() == datetime.datetime.now().date() else " tomorrow"
        self.say(f"Alarm set for {fmt_time(target.hour * 60 + target.minute)}{day}. Keep PAC running.")

    def c_convert(self, m, t):
        n = float(m["n"])
        res = convert_units(n, m["a"], m["b"])
        if res is None:
            return False                  # not two units that go together, e.g. "5 apples to pears"
        def f(x):
            return f"{x:,.2f}".rstrip("0").rstrip(".")
        self.say(f"{f(n)} {m['a']} is {f(res)} {m['b']}.")

    def c_coin(self, m, t):
        self.say(random.choice(["Heads.", "Tails."]))

    def c_dice(self, m, t):
        self.say(f"You rolled a {random.randint(1, 6)}.")

    def c_random(self, m, t):
        a, b = int(m["a"] or 1), int(m["b"] or 100)
        self.say(f"Your number is {random.randint(min(a, b), max(a, b))}.")

    def c_date_offset(self, m, t):
        off = 1 if m["w"] == "tomorrow" else -1
        d = datetime.datetime.now() + datetime.timedelta(days=off)
        self.say(f"{m['w'].capitalize()} {'is' if off == 1 else 'was'} " + d.strftime("%A, %d %B %Y"))


# --------------------------------------------------------------- listening (Google Web Speech)
def internet_ok(timeout=3.0):
    """Quick check that Google is reachable. Only ever called in Voice mode;
    Text mode never touches the network."""
    import socket
    for addr in (("www.google.com", 443), ("8.8.8.8", 53)):
        try:
            with socket.create_connection(addr, timeout=timeout):
                return True
        except OSError:
            continue
    return False


class SoundTriggers:
    """Spots a double clap and a whistle in the raw microphone blocks. Plain python, runs on your
    PC only - no recognition, no internet."""

    SENS = {"low": 9000, "medium": 5000, "high": 2500}     # smallest raw peak that can count as a clap

    def __init__(self, block_sec):
        self.bs = block_sec
        self.n = 0
        self.ema = 60.0                # how loud the room normally is
        self.prev = 0.0
        self.cand = None               # a possible clap, waiting to see whether it dies away at once
        self.claps = []
        self.clap_cool = -1.0
        self.whistle_blocks = 0
        self.whistle_miss = 0
        self.whistle_freq = 0.0
        self.whistle_cool = -1.0

    @staticmethod
    def tone(raw, rate):
        """Pitch in Hz if the block is one steady whistle-like tone, else None. A whistle is nearly a pure
        sine, so the gaps between its upward zero-crossings are all almost the same; speech and noise aren't."""
        n = len(raw)
        mean = sum(raw) / n
        cross, prev = [], raw[0] - mean
        for i in range(1, n):
            cur = raw[i] - mean
            if prev < 0 <= cur:
                cross.append(i - 1 + (-prev) / (cur - prev))
            prev = cur
        if len(cross) < 6:
            return None
        gaps = [b - a for a, b in zip(cross, cross[1:])]
        mean_gap = sum(gaps) / len(gaps)
        spread = math.sqrt(sum((g - mean_gap) ** 2 for g in gaps) / len(gaps))
        return rate / mean_gap if spread / mean_gap < 0.06 else None

    def feed(self, raw, rate, peak, rms, sens="medium"):
        """One 50 ms block in. Returns 'clap' (a double clap), 'whistle' or None."""
        self.n += 1
        t = self.n * self.bs
        out = None
        floor = max(self.ema, 30.0)
        sudden = (peak >= self.SENS.get(sens, 5000) and rms > floor * 4 and rms > self.prev * 3)
        if self.cand is not None:
            # a clap is over almost at once; speech or music is still going in the next block
            if rms < self.cand * 0.5:
                self.claps = [c for c in self.claps if t - c < 1.2] + [t - self.bs]
                if (len(self.claps) >= 2 and 0.15 <= self.claps[-1] - self.claps[-2] <= 1.0
                        and t >= self.clap_cool):
                    self.claps = []
                    self.clap_cool = t + 2.0
                    out = "clap"
            self.cand = None
        elif sudden:
            self.cand = rms
        else:
            self.ema = 0.97 * self.ema + 0.03 * rms        # learn the background from ordinary blocks only

        f = self.tone(raw, rate) if rms > max(250.0, floor * 3) else None
        if f and 800 <= f <= 4500:
            if self.whistle_blocks and abs(f - self.whistle_freq) <= 0.2 * self.whistle_freq:
                self.whistle_blocks += 1
            else:
                self.whistle_blocks = 1
            self.whistle_freq, self.whistle_miss = f, 0
        elif self.whistle_blocks:
            self.whistle_miss += 1
            if self.whistle_miss >= 2:                      # one dropped block is forgiven
                self.whistle_blocks = 0
        if self.whistle_blocks >= 6 and t >= self.whistle_cool:      # about 0.3 s of steady tone
            self.whistle_blocks = 0
            self.whistle_cool = t + 4.0
            out = out or "whistle"
        self.prev = rms
        return out


class Listener:
    """Owns the microphone. It does two jobs:
      1. Voice mode: cuts speech into phrases and sends each to the SpeechRecognition library's
         Google Web Speech API (recognize_google). Needs internet.
      2. Sound triggers (clap / whistle): analysed locally. Works in Text mode too, offline.
    The microphone is only open while one of those is switched on.

    While PAC is talking she normally can't hear you (her own voice would confuse her). To still let you say
    "stop", the listener watches for you speaking clearly louder than her voice, holds her voice for a moment,
    listens, and either stops her (you said stop / mute) or lets her carry on."""

    BLOCK_SEC = 0.05          # microphone is read in 50 ms pieces (also drives the orb)
    PREROLL_SEC = 0.3         # audio kept from just before you start talking, so first words aren't cut
    # How much quiet after speech means "finished", as (for a short phrase like a command, for a longer sentence).
    # A command is usually one breath, so it can be cut off sooner; a long sentence gets more room for pauses.
    SPEED = {"fast": (0.40, 0.60), "balanced": (0.55, 0.75), "careful": (0.80, 0.95)}
    SHORT_PHRASE_SEC = 1.6    # speech shorter than this counts as a short phrase
    TAIL_KEEP_BLOCKS = 2      # of the trailing quiet, send only this much - a shorter clip uploads and decodes faster
    MIN_SPEECH_SEC = 0.2      # shorter blips (coughs, clicks) are ignored
    MAX_PHRASE_SEC = 14.0     # Google's free endpoint likes short clips
    MIN_THRESHOLD = 120.0     # never treat anything quieter than this (after boost) as speech
    INTERRUPT_RATIO = {"low": 2.8, "medium": 2.1, "high": 1.7}   # how much louder than PAC you must be

    def __init__(self, app):
        self.app = app
        self.stop = threading.Event()
        self.restart = threading.Event()   # set to reopen the microphone (e.g. new input device)
        self.wake = threading.Event()      # set when the mode / mic switch changes
        self.jobs = queue.Queue()          # phrases waiting to be sent to Google
        self.triggers = SoundTriggers(self.BLOCK_SEC)
        self.in_speech = False
        self.rec_started = 0.0
        self.inflight = 0
        self.peak_seen = 0                 # loudest raw sample since the voice check began
        self.blocks = 0                    # microphone blocks received since then
        self.barge = False                 # PAC's voice is on hold while we check whether you said "stop"
        self.bi_base, self.bi_env, self.bi_run, self.bi_last, self.bi_cool = 0.0, 0.0, 0, 0.0, 0.0
        self.bi_learn = 0.0
        self._lock = threading.Lock()

    def start(self):
        threading.Thread(target=self.run, daemon=True).start()
        if sr is not None:
            threading.Thread(target=self._recognizer_worker, daemon=True).start()

    def state(self):
        if not self.app.capture_wanted():
            return "idle"
        if not self.app.recognition_wanted():
            return "triggers"
        if self.in_speech:
            return "hearing"
        if self.inflight:
            return "recognizing"
        return "listening"

    def run(self):
        while not self.stop.is_set():
            if not self.app.capture_wanted():
                self.wake.wait(0.5)
                self.wake.clear()
                continue
            try:
                self.listen()
            except Exception as e:
                logger.exception("microphone error")
                if self.app.recognition_wanted():
                    self.app.ui("log", "sys", f"Microphone problem: {e}. Pick another one under "
                                              "Menu > Voice input > Input device.")
                else:                      # only the clap / whistle triggers wanted it: say so once, then stop trying
                    self.app.trigger_mic_failed = True
                    self.app.ui("log", "sys", f"Couldn't open the microphone for clap / whistle detection ({e}).")
                time.sleep(3)

    def _carry_on(self):
        """Nothing to stop after all: let PAC continue, and don't pause her again for a moment."""
        self.barge = False
        self.app.speaker.resume()
        self.bi_cool = time.time() + 1.2

    def _interrupt_seen(self, rms, sp, threshold, sens):
        """While PAC is talking: True once something much louder than her own voice (as the microphone hears it)
        has gone on for about a fifth of a second - that's you speaking over her."""
        now = time.time()
        since = sp.audible_since
        if not since or now < since:
            return False                                   # no sound from her yet, so nothing to compare with
        if now - self.bi_last > 1.5:                       # a fresh stretch of her talking, or she was on hold:
            self.bi_base, self.bi_env, self.bi_run = 0.0, 0.0, 0     # forget the old level and learn it again
            self.bi_learn = now + 0.9
        self.bi_last = now
        self.bi_env = max(rms, self.bi_env * 0.88)         # the loudest recent moment, fading quickly
        if now - since < 0.9 or now < self.bi_learn or now < self.bi_cool:
            self.bi_base = max(self.bi_base * 0.995, self.bi_env)    # just learn how loud she is; don't judge yet
            self.bi_run = 0
            return False
        ratio = self.INTERRUPT_RATIO.get(sens, 2.1)
        ref = max(self.bi_base, threshold)                 # with headphones her level is ~0, so the room's is used
        if self.bi_env > ratio * ref and rms > 0.6 * ratio * ref:
            self.bi_run += 1
            if self.bi_run >= 4:
                self.bi_run = 0
                return True
        else:
            self.bi_run = 0
            if self.bi_env > 0.5 * ref:
                self.bi_base = 0.98 * self.bi_base + 0.02 * self.bi_env     # follow her loudness changes slowly
        return False

    def listen(self):
        app = self.app
        self.restart.clear()
        self.triggers = SoundTriggers(self.BLOCK_SEC)
        device = app.cfg.get("mic")
        rate = 16000
        try:
            sd.check_input_settings(device=device, samplerate=rate, channels=1, dtype="int16")
        except Exception:
            rate = int(sd.query_devices(device, "input")["default_samplerate"])
        block = int(rate * self.BLOCK_SEC)
        q = queue.Queue()

        def cb(indata, frames, t, status):
            q.put(bytes(indata))

        end_short, end_long = (max(2, round(x / self.BLOCK_SEC)) for x in
                               self.SPEED.get(app.cfg.get("voice_speed", "fast"), self.SPEED["fast"]))
        preroll = collections.deque(maxlen=int(self.PREROLL_SEC / self.BLOCK_SEC))
        phrase, speech_blocks, quiet_blocks = [], 0, 0
        noise = 60.0                       # running estimate of the room's background loudness
        self.in_speech = False
        self.barge = False
        with sd.RawInputStream(samplerate=rate, blocksize=block, dtype="int16", channels=1,
                               device=device, callback=cb):
            while not self.stop.is_set() and not self.restart.is_set() and app.capture_wanted():
                try:
                    data = q.get(timeout=0.3)
                except queue.Empty:
                    continue
                raw0 = array("h", data)
                if not raw0:
                    continue
                raw_peak = max(map(abs, raw0))
                rms_raw = math.sqrt(sum(x * x for x in raw0) / len(raw0))
                self.blocks += 1
                self.peak_seen = max(self.peak_seen, raw_peak)
                gain = float(app.cfg.get("gain", 2.0))
                rms = min(32768.0, rms_raw * gain)
                # what the orb on screen shows
                app.level_target = min(1.0, math.sqrt(rms / 4000.0))
                app.level_time = time.time()
                sp = app.speaker
                busy = sp.busy()
                speaking = busy and not sp.paused          # a voice we have put on hold is silent: listen normally

                if app.cfg.get("sound_triggers", True) and not busy:
                    ev = self.triggers.feed(raw0, rate, raw_peak, rms_raw, app.cfg.get("trigger_sens", "medium"))
                    if ev:
                        app.ui("trigger", ev)

                if not app.recognition_wanted():       # Text mode: triggers only, nothing is recognised
                    if self.barge:
                        self._carry_on()
                    preroll.clear()
                    phrase, speech_blocks, quiet_blocks = [], 0, 0
                    self.in_speech = False
                    continue
                if gain != 1.0:
                    data = array("h", [max(-32768, min(32767, int(x * gain))) for x in raw0]).tobytes()
                threshold = max(self.MIN_THRESHOLD, noise * 2.5)
                if speaking:                           # PAC is talking: only listen for you speaking over her
                    self.in_speech = False
                    phrase, speech_blocks, quiet_blocks = [], 0, 0
                    preroll.append(data)
                    if (app.cfg.get("voice_interrupt", True)
                            and self._interrupt_seen(rms, sp, threshold, app.cfg.get("voice_interrupt_sens", "medium"))
                            and sp.pause()):
                        self.barge = True
                        self.in_speech, self.rec_started = True, time.time()
                        phrase, speech_blocks, quiet_blocks = list(preroll), 4, 0
                    continue

                if not self.in_speech:
                    preroll.append(data)
                    noise = min(1500.0, noise * 0.95 + rms * 0.05)
                    if rms > threshold:
                        self.in_speech = True
                        self.rec_started = time.time()
                        phrase = list(preroll)
                        speech_blocks, quiet_blocks = 1, 0
                    elif self.barge:                   # we paused her but nothing followed: let her carry on
                        self._carry_on()
                    continue

                phrase.append(data)
                if rms > threshold * 0.6:
                    speech_blocks += 1
                    quiet_blocks = 0
                    if app.cfg.get("auto_gain", True) and raw_peak > 200 and not self.barge:
                        # keep your voice at a good level: nudge the boost up if too quiet, down if clipping
                        boosted = raw_peak * gain
                        if boosted < 5400:
                            app.cfg["gain"] = round(min(8.0, gain * 1.05), 2)
                        elif boosted > 30000:
                            app.cfg["gain"] = round(max(1.0, gain * 0.85), 2)
                else:
                    quiet_blocks += 1
                too_long = len(phrase) * self.BLOCK_SEC >= self.MAX_PHRASE_SEC
                end_blocks = end_short if speech_blocks * self.BLOCK_SEC < self.SHORT_PHRASE_SEC else end_long
                if quiet_blocks >= end_blocks or too_long:
                    self.in_speech = False
                    if speech_blocks * self.BLOCK_SEC >= self.MIN_SPEECH_SEC:
                        trim = max(0, quiet_blocks - self.TAIL_KEEP_BLOCKS)
                        if trim:
                            phrase = phrase[:-trim]
                        with self._lock:
                            self.inflight += 1
                        self.jobs.put((b"".join(phrase), rate, self.barge))
                    elif self.barge:
                        self._carry_on()
                    self.barge = False
                    preroll.clear()
                    phrase, speech_blocks, quiet_blocks = [], 0, 0
        self.in_speech = False
        if self.barge:
            self._carry_on()

    def _recognizer_worker(self):
        rec = None
        while not self.stop.is_set():
            try:
                pcm, rate, barge = self.jobs.get(timeout=0.5)
            except queue.Empty:
                continue
            try:
                if not (self.app.mode == "voice" and self.app.voice_ok):
                    continue               # switched to Text mode while this was waiting
                if rec is None:
                    rec = sr.Recognizer()
                    rec.operation_timeout = 12
                text = rec.recognize_google(sr.AudioData(pcm, rate, 2),
                                            language=self.app.cfg.get("lang", "en-US"))
                text = (text or "").strip()
                if text and barge:
                    # said over PAC's voice: only "stop" / "mute" count. Anything else is most likely her own
                    # voice coming back through the microphone, so it is ignored and she carries on.
                    if STOP_SPEAKING.match(re.sub(r"[^a-z' ]+", " ", text.lower()).strip()):
                        self.app.ui("heard", text)
                        self.app.ui("log", "you", text)
                        self.app.assistant.stop_speaking()
                elif text:
                    self.app.ui("heard", text)
                    self.app.cmd_q.put(("voice", text))
            except sr.UnknownValueError:
                if not barge:
                    self.app.ui("heard", "(Google couldn't make out any words)")
            except (sr.RequestError, OSError) as e:
                logger.warning("Google speech request failed: %s", e)
                if barge:
                    pass
                elif internet_ok():        # online, so it's something else - show the real reason
                    self.app.ui("log", "sys", f"Voice recognition error: {e}")
                else:
                    self.app.ui("voice_offline", str(e))
            except Exception:
                logger.exception("speech recognition failed")
            finally:
                if barge:
                    self._carry_on()                   # no-op if she was just stopped
                with self._lock:
                    self.inflight = max(0, self.inflight - 1)


# --------------------------------------------------------------- the window
def list_mics():
    items = [("System default", None)]
    if sd is None:
        return items
    try:
        api = sd.default.hostapi
        for i, d in enumerate(sd.query_devices()):
            if d["max_input_channels"] > 0 and d["hostapi"] == api:
                items.append((f"{i}: {d['name']}", i))
    except Exception:
        pass
    return items


def mix(c1, c2, t):
    """Blend two '#rrggbb' colours; t=0 gives c1, t=1 gives c2."""
    t = max(0.0, min(1.0, t))
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(int(a[k] + (b[k] - a[k]) * t) for k in range(3))


# --------------------------------------------------------------- hand gestures (laptop camera)
HAND_MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/"
                  "float16/latest/hand_landmarker.task")
HAND_MODEL_FILE = DATA_DIR / "hand_landmarker.task"

GESTURES = {
    "open_palm": "Open palm", "fist": "Fist", "thumbs_up": "Thumbs up", "thumbs_down": "Thumbs down",
    "point": "Pointing finger", "peace": "Peace sign", "three": "Three fingers", "four": "Four fingers",
    "rock": "Rock on", "call": "Call me", "love": "I love you", "ok": "OK sign",
    "swipe_left": "Swipe left", "swipe_right": "Swipe right", "swipe_up": "Swipe up", "swipe_down": "Swipe down",
    # two hands at once
    "two_palms": "Both palms open", "two_fists": "Both fists", "two_thumbs_up": "Both thumbs up",
    "two_thumbs_down": "Both thumbs down", "two_peace": "Both peace signs",
    "spread": "Hands apart (both open)", "together": "Hands together (both open)",
}
# the same pose held in both hands -> this two-hand gesture
TWO_HAND_POSES = {"open_palm": "two_palms", "fist": "two_fists", "thumbs_up": "two_thumbs_up",
                  "thumbs_down": "two_thumbs_down", "peace": "two_peace"}
STABLE_WINDOW, STABLE_NEED = 4, 3     # a pose counts once it shows in 3 of the last 4 pictures (about 0.1 s)
# What each built-in gesture does until you change it (Menu > Gestures > Gesture actions)
GESTURE_DEFAULTS = {
    "thumbs_up": {"type": "vol_up"}, "thumbs_down": {"type": "vol_down"}, "fist": {"type": "play_pause"},
    "peace": {"type": "screenshot"}, "ok": {"type": "mute"},
    "swipe_right": {"type": "next_track"}, "swipe_left": {"type": "prev_track"},
    "spread": {"type": "zoom_in"}, "together": {"type": "zoom_out"},
}
# (id, label, hint for the extra box, repeats while you keep holding the gesture)
ACTIONS = [
    ("none", "Do nothing", "", False),
    ("stop_speaking", "Stop PAC talking", "", False),
    ("play_pause", "Play / pause media", "", False),
    ("next_track", "Next track", "", False),
    ("prev_track", "Previous track", "", False),
    ("vol_up", "Volume up", "", True),
    ("vol_down", "Volume down", "", True),
    ("mute", "Mute / unmute", "", False),
    ("screenshot", "Take a screenshot", "", False),
    ("show_desktop", "Show desktop", "", False),
    ("switch_window", "Switch window (Alt+Tab)", "", False),
    ("scroll_up", "Scroll up", "", True),
    ("scroll_down", "Scroll down", "", True),
    ("zoom_in", "Zoom in (Ctrl +)", "", False),
    ("zoom_out", "Zoom out (Ctrl -)", "", False),
    ("next_slide", "Next slide (Right arrow)", "", False),
    ("prev_slide", "Previous slide (Left arrow)", "", False),
    ("cmd", "Run a PAC command...", "e.g. open chrome   or   what's my schedule", False),
    ("keys", "Press keys...", "e.g. ctrl+shift+t", False),
    ("url", "Open website...", "e.g. youtube.com", False),
]
ACTION_LABEL = {a[0]: a[1] for a in ACTIONS}
ACTION_ID = {a[1]: a[0] for a in ACTIONS}
ACTION_HINT = {a[0]: a[2] for a in ACTIONS}
ACTION_REPEATS = {a[0] for a in ACTIONS if a[3]}
HAND_LINES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
              (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (17, 18), (18, 19), (19, 20), (0, 17)]


def gesture_is_deleted(cfg, gid):
    """True for a built-in gesture you deleted: the camera may still see the pose, but PAC ignores it."""
    return gid in (cfg.get("deleted_gestures") or [])


def delete_gestures(cfg, gids):
    """Delete gestures. One you taught is erased for good; a built-in one is switched off (it can be restored).
    Returns (names erased, names switched off)."""
    gids = list(dict.fromkeys(gids))
    erased = [g["name"] for g in cfg.get("custom_gestures", []) if g.get("id") in gids]
    newly_off = [g for g in gids if g in GESTURES and not gesture_is_deleted(cfg, g)]
    cfg["custom_gestures"] = [g for g in cfg.get("custom_gestures", []) if g.get("id") not in gids]
    cfg["deleted_gestures"] = list(cfg.get("deleted_gestures") or []) + newly_off
    save_config(cfg)
    return erased, [GESTURES[g] for g in newly_off]


def restore_gestures(cfg, gids=None):
    """Bring back deleted built-in gestures (all of them when gids is None). Returns their names."""
    gone = [g for g in (cfg.get("deleted_gestures") or []) if g in GESTURES]
    back = gone if gids is None else [g for g in gone if g in gids]
    cfg["deleted_gestures"] = [g for g in (cfg.get("deleted_gestures") or []) if g not in back]
    save_config(cfg)
    return [GESTURES[g] for g in back]


def gesture_action(cfg, gid):
    """The action tied to a gesture id ('thumbs_up' or 'custom:my gesture'). A deleted gesture does nothing."""
    if gesture_is_deleted(cfg, gid):
        return {"type": "none"}
    if gid.startswith("custom:"):
        for g in cfg.get("custom_gestures", []):
            if g.get("id") == gid:
                return g.get("action") or {"type": "none"}
        return {"type": "none"}
    return (cfg.get("gesture_map") or {}).get(gid) or GESTURE_DEFAULTS.get(gid) or {"type": "none"}


def gesture_title(cfg, gid):
    if gid.startswith("custom:"):
        for g in cfg.get("custom_gestures", []):
            if g.get("id") == gid:
                return g["name"]
    return GESTURES.get(gid, gid)


def _dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def hand_size(lm):
    """Wrist to the knuckle of the middle finger - the yardstick every other distance is measured in."""
    return max(_dist(lm[0], lm[9]), 0.9 * _dist(lm[0], lm[5]), 1e-6)


def finger_states(lm):
    """(thumb, index, middle, ring, pinky): True when that finger is stretched out."""
    size = hand_size(lm)
    thumb = _dist(lm[4], lm[5]) > _dist(lm[3], lm[5]) * 1.2 and _dist(lm[4], lm[9]) > 0.5 * size
    out = [thumb]
    for pip, tip in ((6, 8), (10, 12), (14, 16), (18, 20)):
        out.append(_dist(lm[0], lm[tip]) > _dist(lm[0], lm[pip]) * 1.08)   # tip reaches farther than the middle joint
    return out


def classify_builtin(lm):
    """Name of the pose in 21 hand landmarks, or None. Works whichever way the hand is turned, except that
    thumbs up / down need the hand to be upright."""
    size = hand_size(lm)
    th, ix, md, rg, pk = finger_states(lm)
    if _dist(lm[4], lm[8]) < 0.32 * size and md and rg and pk:
        return "ok"
    four = (ix, md, rg, pk)
    if four == (False, False, False, False):
        if not th:
            return "fist"
        vx, vy = lm[4][0] - lm[2][0], lm[4][1] - lm[2][1]
        if abs(vy) > 0.7 * abs(vx) and abs(vy) > 0.4 * size:
            return "thumbs_up" if vy < 0 else "thumbs_down"
        return None
    if four == (True, False, False, False):
        return "point"
    if four == (True, True, False, False):
        return "peace"
    if four == (True, True, True, False):
        return "three"
    if four == (True, True, True, True):
        return "open_palm" if th else "four"
    if four == (True, False, False, True):
        return "love" if th else "rock"
    if four == (False, False, False, True) and th:
        return "call"
    return None


def pose_vector(lm, label):
    """The hand's shape as numbers, independent of where it is in the picture and how far from the camera.
    A left hand is mirrored so the same pose made with either hand matches."""
    ox, oy, s = lm[0][0], lm[0][1], hand_size(lm)
    sign = -1.0 if label == "Left" else 1.0
    return [round(c, 4) for p in lm for c in (sign * (p[0] - ox) / s, (p[1] - oy) / s)]


def pose_distance(a, b):
    """(average, worst) distance between two poses, over the 21 landmarks, in hand sizes."""
    ds = [math.hypot(a[2 * i] - b[2 * i], a[2 * i + 1] - b[2 * i + 1]) for i in range(len(a) // 2)]
    return sum(ds) / len(ds), max(ds)


def _mean_pose(vecs):
    return [sum(v[i] for v in vecs) / len(vecs) for i in range(len(vecs[0]))]


def build_custom_gesture(name, vecs, action):
    """Turn the recorded poses into a gesture PAC can recognise. The tolerance is worked out from how much
    your hand wobbled while you recorded it, so a steady hand gives a stricter (more accurate) gesture."""
    mean = _mean_pose(vecs)
    dev = [pose_distance(v, mean) for v in vecs]
    thr = min(0.36, max(0.16, 1.6 * max(d[0] for d in dev) + 0.04))
    thr_max = min(0.6, max(0.30, 2.2 * max(d[1] for d in dev) + 0.05))
    step = max(1, len(vecs) // 20)
    return {"id": "custom:" + name.strip().lower(), "name": name.strip(), "enabled": True, "action": action,
            "samples": [[round(c, 4) for c in mean]] + [v for v in vecs[::step]][:20],
            "thr": round(thr, 3), "thr_max": round(thr_max, 3), "hold": None}


def match_custom(vec, customs):
    """Id of the taught gesture this pose matches best, or None. Both the average and the worst-landmark
    difference must be small, so a pose that differs by a single finger is not mistaken for it."""
    best, best_score = None, 1.0
    for g in customs:
        if not g.get("enabled", True) or not g.get("samples"):
            continue
        thr, thr_max = g.get("thr", 0.3), g.get("thr_max", 0.5)
        score = 9.9
        for s in g["samples"]:
            mean, worst = pose_distance(vec, s)
            score = min(score, max(mean / thr, worst / thr_max))
        if score <= best_score:
            best, best_score = g["id"], score
    return best


class SwipeTracker:
    """Spots a quick sweep of an open hand across the picture."""

    def __init__(self):
        self.pts = collections.deque()

    def clear(self):
        self.pts.clear()

    def feed(self, now, lm, open_hand):
        self.pts.append((now, lm[0][0], lm[0][1], hand_size(lm)))
        while self.pts and now - self.pts[0][0] > 0.7:
            self.pts.popleft()
        if not open_hand or len(self.pts) < 4:
            return None
        t0, x0, y0, s0 = self.pts[0]
        size = (s0 + self.pts[-1][3]) / 2
        dx, dy = (lm[0][0] - x0) / size, (lm[0][1] - y0) / size
        if now - t0 < 0.12:
            return None
        if abs(dx) >= 2.2 and abs(dy) < 0.55 * abs(dx):
            return "swipe_right" if dx > 0 else "swipe_left"
        if abs(dy) >= 2.2 and abs(dx) < 0.55 * abs(dy):
            return "swipe_down" if dy > 0 else "swipe_up"
        return None


class HandTrack:
    """Everything remembered about ONE hand (or the pair, for two-hand gestures): its last few poses, its swipe
    path, and where it is in 'hold the pose, fire once, then wait until the pose changes'."""

    def __init__(self):
        self.recent = collections.deque(maxlen=STABLE_WINDOW)
        self.swipes = SwipeTracker()
        self.missing_since = None
        self.reset()

    def reset(self):
        self.recent.clear()
        self.swipes.clear()
        self.cand, self.cand_since, self.armed, self.last_repeat = None, 0.0, True, 0.0

    def stable(self):
        if not self.recent:
            return None
        top, n = collections.Counter(self.recent).most_common(1)[0]
        return top if (top and n >= STABLE_NEED) else None


def assign_hands(hands):
    """[(landmarks, model_label, points)] -> {'Left': hand, 'Right': hand}. One hand keeps the model's left/right
    label. With two, the labels are used if they differ; if the model calls both the same, the hand on the left of
    the (mirrored) picture is Left."""
    if not hands:
        return {}
    if len(hands) == 1:
        lm, label, pts = hands[0]
        return {label if label in ("Left", "Right") else "Right": hands[0]}
    hands = sorted(hands[:2], key=lambda h: h[0][0][0])           # by wrist x, left side of the picture first
    labels = [h[1] for h in hands]
    if labels[0] == labels[1] or labels[0] == "Right":            # duplicate or crossed over: trust position
        return {"Left": (hands[0][0], "Left", hands[0][2]), "Right": (hands[1][0], "Right", hands[1][2])}
    return {"Left": hands[0], "Right": hands[1]}


def dedupe_hands(hands):
    """The tracker sometimes reports ONE real hand twice (a "ghost" with the other label). Two hands whose
    outlines overlap that much can only be the same hand, so keep the first."""
    if len(hands) < 2:
        return hands
    (_l0, _n0, p0), (_l1, _n1, p1) = hands[0], hands[1]

    def box(pts):
        xs, ys = [q[0] for q in pts], [q[1] for q in pts]
        return min(xs), min(ys), max(xs), max(ys)
    a, b = box(p0), box(p1)
    iw, ih = min(a[2], b[2]) - max(a[0], b[0]), min(a[3], b[3]) - max(a[1], b[1])
    inter = max(iw, 0.0) * max(ih, 0.0)
    union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    if (union > 0 and inter / union > 0.55) or math.hypot(p0[0][0] - p1[0][0], p0[0][1] - p1[0][1]) < 0.05:
        return [hands[0]]
    return hands


class HandAssigner:
    """Gives each hand in view a steady slot, 'Left' or 'Right', frame after frame.
    The tracker's own left/right label flips from picture to picture (especially for a single hand, a fist or the
    back of a hand), and sorting by position swaps the hands the moment they cross. So a hand keeps the slot of
    the hand that was nearest to it a moment ago; the label and position only decide when a hand first appears."""
    FRESH = 0.8        # seconds a slot's last position still counts
    NEAR = 0.35        # picture widths a hand may travel between two pictures and still be the same hand

    def __init__(self):
        self.last = {}                                 # slot -> (x, y, time) of its wrist

    def reset(self):
        self.last.clear()

    def _gap(self, slot, pts, now):
        l = self.last.get(slot)
        if l is None or now - l[2] > self.FRESH:
            return None
        return math.hypot(pts[0][0] - l[0], pts[0][1] - l[1])

    def assign(self, hands, now):
        hands = dedupe_hands(hands)[:2]
        if not hands:
            return {}
        if len(hands) == 1:
            lm, label, pts = hands[0]
            best, bd = None, self.NEAR
            for slot in ("Left", "Right"):
                d = self._gap(slot, pts, now)
                if d is not None and d < bd:
                    best, bd = slot, d
            slot = best or (label if label in ("Left", "Right") else "Right")
            out = {slot: (lm, slot, pts)}
        else:
            a, b = sorted(hands, key=lambda h: h[2][0][0])       # picture-left hand first

            def cost(left, right):
                c = 0.0
                for slot, h in (("Left", left), ("Right", right)):
                    d = self._gap(slot, h[2], now)
                    c += d if d is not None else 0.0
                return c
            if cost(b, a) + 0.05 < cost(a, b):                    # clearly the same hands, crossed over
                a, b = b, a
            out = {"Left": (a[0], "Left", a[2]), "Right": (b[0], "Right", b[2])}
        for slot, h in out.items():
            self.last[slot] = (h[2][0][0], h[2][0][1], now)
        return out


class AirMouse:
    """Moves the real mouse pointer and holds / releases its left button. On Windows it sends genuine mouse events
    (so File Explorer and websites treat it as a real drag-and-drop); elsewhere it falls back to pyautogui.
    Positions are 0..1 across the screen, so display scaling never matters."""

    def __init__(self):
        self.down = False
        self._u = None
        if OS == "Windows":
            try:
                import ctypes
                self._u = ctypes.windll.user32
            except Exception:
                self._u = None

    def move(self, nx, ny):
        nx, ny = min(max(nx, 0.0), 1.0), min(max(ny, 0.0), 1.0)
        if self._u:
            self._u.mouse_event(0x8001, int(nx * 65535), int(ny * 65535), 0, 0)      # MOVE | ABSOLUTE
        else:
            w, h = pyautogui.size()
            pyautogui.moveTo(int(nx * (w - 1)), int(ny * (h - 1)), _pause=False)

    def press(self):
        if self.down:
            return
        self.down = True
        if self._u:
            self._u.mouse_event(0x0002, 0, 0, 0, 0)                                  # LEFT DOWN
        else:
            pyautogui.mouseDown(_pause=False)

    def release(self):
        if not self.down:
            return
        self.down = False
        if self._u:
            self._u.mouse_event(0x0004, 0, 0, 0, 0)                                  # LEFT UP
        else:
            pyautogui.mouseUp(_pause=False)


class OneEuro:
    """Smooths a moving point (the "1-euro" filter): rock steady when your hand is still, so you can aim at a small
    target, and nearly lag-free when you move quickly, so a fast carry doesn't trail behind your hand."""

    def __init__(self, min_cutoff=1.3, beta=12.0, d_cutoff=1.0):
        self.min_cutoff, self.beta, self.d_cutoff = min_cutoff, beta, d_cutoff
        self.x, self.dx, self.t = None, (0.0, 0.0), 0.0

    @staticmethod
    def _alpha(cutoff, dt):
        return 1.0 / (1.0 + (1.0 / (2.0 * math.pi * cutoff)) / dt)

    def hold(self, pos, t):
        """Carry on smoothly from `pos` (used after the pointer was frozen or moved by hand)."""
        self.x, self.dx, self.t = pos, (0.0, 0.0), t

    def __call__(self, p, t):
        if self.x is None:
            self.hold(p, t)
            return p
        dt = max(t - self.t, 1e-3)
        self.t = t
        ad = self._alpha(self.d_cutoff, dt)
        raw = ((p[0] - self.x[0]) / dt, (p[1] - self.x[1]) / dt)
        self.dx = (self.dx[0] + ad * (raw[0] - self.dx[0]), self.dx[1] + ad * (raw[1] - self.dx[1]))
        a = self._alpha(self.min_cutoff + self.beta * math.hypot(*self.dx), dt)
        self.x = (self.x[0] + a * (p[0] - self.x[0]), self.x[1] + a * (p[1] - self.x[1]))
        return self.x


class AirDrag:
    """Hand-driven drag and drop. While it is on, one hand (the right, by default) is the mouse:

      PINCH     touch your thumb and index finger together: that PRESSES the mouse button, so it selects the file
                under the pointer. Keep pinching and move your hand to drag it; let go to drop it. A quick pinch
                is a click (two quick pinches open a file, like a double click).
      POINT     point with just your index finger: the pointer sits on your fingertip.  Double air-tap (bend the
                finger twice, like pressing a button) on a file: it is selected.
      FIST      close your hand and the selected file (or whatever is under the pointer) is grabbed.
                Move your hand to carry it. OPEN PALM drops it.
    Dropping works on File Explorer, the desktop and website upload boxes - no "Choose file" needed.

    Made to feel solid:
      * the pointer is smoothed by a 1-euro filter: steady when you hold still, quick when you move;
      * the pointer freezes as your thumb and finger come together, and a grab lands where the pointer was when
        your hand was last steady, not where it drifted while you closed it;
      * the pointer never jumps when you switch between pointing, open hand, pinch and fist (it moves by how far
        your hand moves, not by where a different part of it happens to be);
      * a pinch needs the thumb and index TIP together with the index finger out, so a fist is never a pinch, and
        a pinch with the other fingers open never counts as an open palm; a pinch only starts after your fingers
        have been apart for a moment, so switching air drag on with a pinched hand doesn't click;
      * a drop needs a clear release (2-3 pictures), so a wobble can't let go by accident;
      * the mouse hand is remembered by where it is, not by the tracker's flip-flopping left/right label, so it
        can't be swapped for your other hand; a hand that leaves the picture drops what it holds after 0.7 s.
    The other hand still does the normal gestures."""
    CLOSE_FRAMES, OPEN_FRAMES = 2, 3             # pictures a fist / open palm must show (about 0.07 / 0.1 s)
    X_RANGE, Y_RANGE = (0.12, 0.88), (0.10, 0.80)  # the part of the camera picture that covers the whole screen
    LOST_DROP_SECS = 0.7
    POINT_SETTLE = 0.3                           # pointing this long makes it "pointing mode" (taps count there)
    TAP_DIP, TAP_BACK = 0.72, 0.86               # finger length vs its recent best: a tap dips below, returns above
    TAP_MIN, TAP_MAX = 0.04, 0.5                 # seconds a tap may last
    DOUBLE_TAP_GAP = 0.8                         # two taps within this = double tap
    SELECT_SECS = 8.0                            # after a double tap, a fist grabs the selected file for this long
    PINCH_ON, PINCH_OFF, PINCH_IDX = 0.25, 0.42, 1.2   # thumb-tip to index-tip gap (in hand sizes): pinched / let go; index must be out

    def __init__(self, app):
        self.app = app
        self.mouse = AirMouse()
        self.filt = OneEuro()
        self.enable()
        self.enabled = False

    @property
    def holding(self):
        return self.mouse.down

    def enable(self):
        self.pos, self.pts, self.slot, self.last_wrist = None, None, None, None
        self.off, self.mode = (0.0, 0.0), "knuckle"
        self.hist = collections.deque(maxlen=40)      # (time, pointer) while it was free to move
        self.closed_run = self.open_run = 0
        self.armed, self.lost_since = False, None     # must show an open hand first, so a fist can't grab at once
        self.open_t = self.point_last = -9.0          # last time the hand was open / pointing
        self.point_since, self.point_until = None, -9.0
        self.rbuf = collections.deque()               # (time, index length / hand size) while pointing
        self.dip_t0, self.dip_base, self.taps, self.dip_wait = None, 0.0, [], False
        self.sel_until = -9.0                         # a file was selected by double tap until this time
        self.pinch_run = self.unpinch_run = self.far_run = 0
        self.pinch_armed, self.far_t, self.hold_by = False, -9.0, None   # a pinch only counts after fingers were apart
        self.filt.x = None
        self.enabled = True

    def disable(self):
        self.enabled = False
        self.release()
        self.pos, self.pts, self.slot = None, None, None

    def release(self):
        if self.mouse.down:
            self.mouse.release()
            self._beep(1400)
        self.hold_by, self.pinch_run = None, 0

    def _beep(self, hz, times=1):
        if self.app.cfg.get("gesture_beep", True) and OS == "Windows":
            def play():
                try:
                    import winsound
                    for _ in range(times):
                        winsound.Beep(hz, 35)
                except Exception:
                    pass
            threading.Thread(target=play, daemon=True).start()     # a beep blocks: never in the camera loop

    def _pick(self, slots):
        """Which of the visible hands is the mouse hand? The same one as a moment ago, whatever label it carries."""
        if self.slot in slots:
            return self.slot
        if self.mouse.down:                           # holding: only the very same hand may carry on
            if len(slots) == 1 and self.last_wrist is not None:
                n = next(iter(slots))
                w = slots[n][2][0]
                if math.hypot(w[0] - self.last_wrist[0], w[1] - self.last_wrist[1]) < 0.3:
                    return n
            return None
        want = self.app.cfg.get("air_drag_hand", "Right")
        if want in slots:
            return want
        return next(iter(slots)) if len(slots) == 1 else None

    def _tap(self, lm, pointing_ctx, now):
        """True when the index finger has just finished its second quick bend-and-return."""
        if not pointing_ctx or self.mouse.down:
            self.rbuf.clear()
            self.dip_t0, self.taps, self.dip_wait = None, [], False
            return False
        size = hand_size(lm) or 1e-6
        r = _dist(lm[8], lm[5]) / size
        self.rbuf.append((now, r))
        while self.rbuf and now - self.rbuf[0][0] > 0.9:
            self.rbuf.popleft()
        base = max(v for _t, v in self.rbuf)
        if self.dip_wait:
            if r > self.TAP_BACK * self.dip_base:     # a long curl ended: only now can a new tap begin
                self.dip_wait = False
                self.rbuf.clear()
        elif self.dip_t0 is None:
            if base > 0.4 and r < float(self.app.cfg.get("air_tap_dip", self.TAP_DIP)) * base:
                self.dip_t0, self.dip_base = now, base
        elif r > self.TAP_BACK * self.dip_base:
            dur = now - self.dip_t0
            self.dip_t0 = None
            if self.TAP_MIN <= dur <= self.TAP_MAX:
                self.taps = [t for t in self.taps if now - t <= self.DOUBLE_TAP_GAP] + [now]
                if len(self.taps) >= 2:
                    self.taps = []
                    return True
        elif now - self.dip_t0 > self.TAP_MAX:
            self.dip_t0, self.dip_wait = None, True   # finger stayed curled: not a tap
        return False

    def _grab(self, now, ref=None, by="fist"):
        """Press the button - at the spot the pointer was when the hand was last steady, not where it drifted."""
        ref = max(self.open_t, self.point_last) if ref is None else ref
        if now - ref < 1.0:
            for t, q in reversed(self.hist):
                if t <= ref + 0.02:
                    if math.hypot(q[0] - self.pos[0], q[1] - self.pos[1]) < 0.1:
                        self.pos = q
                        self.filt.hold(q, now)
                        self.mouse.move(*q)
                    break
        self.mouse.press()
        self.hold_by = by
        self.sel_until = -9.0
        self._beep(900)

    def step(self, slots, now):
        """Take the mouse hand out of `slots` (so it can't also fire normal gestures) and drive the pointer."""
        if not self.enabled:
            return slots
        name = self._pick(slots)
        if name is None:
            self.pts = None
            self.closed_run = self.open_run = 0
            self.pinch_run = self.unpinch_run = self.far_run = 0
            self.point_since, self.dip_t0, self.taps = None, None, []
            if self.lost_since is None:
                self.lost_since = now
            if self.mouse.down:
                if now - self.lost_since > self.LOST_DROP_SECS:
                    self.release()                    # hand left the picture: let go rather than hold the button
            else:
                self.armed = self.pinch_armed = False
                if now - self.lost_since > 1.0:
                    self.slot = None                  # gone for a while: any hand may take over
            return slots
        lm, _label, pts = slots.pop(name)
        self.slot, self.lost_since, self.pts, self.last_wrist = name, None, pts, pts[0]

        st = finger_states(lm)
        ext = sum(st[1:])                             # fingers stretched out, not counting the thumb
        pointing = bool(st[1]) and not any(st[2:])    # only the index finger is out
        if pointing:
            self.point_last = now
            if self.point_since is None:
                self.point_since = now
            if now - self.point_since >= self.POINT_SETTLE:
                self.point_until = now + 0.5          # a bending (tapping) finger still counts as pointing
                self.armed = True                     # pointing steadily is as good as an open hand for arming
        else:
            self.point_since = None
        pointing_ctx = now < self.point_until and not any(st[2:])

        # pinch: thumb tip and index tip together, index finger held out (so a fist is not a pinch)
        on = float(self.app.cfg.get("air_pinch_on", self.PINCH_ON))
        off = float(self.app.cfg.get("air_pinch_off", self.PINCH_OFF))
        gap = _dist(lm[4], lm[8]) / (hand_size(lm) or 1e-6)
        reach = _dist(lm[0], lm[8]) / (_dist(lm[0], lm[5]) or 1e-6)
        near = gap < max(on, off) and reach >= 1.1    # index tip held out in front of its knuckle (a fist curls it in)
        if gap < on and reach >= self.PINCH_IDX:
            self.pinch_run, self.unpinch_run = self.pinch_run + 1, 0
        elif gap > off or reach < 1.1:
            self.unpinch_run, self.pinch_run = self.unpinch_run + 1, 0
        else:
            self.pinch_run = 0                        # in between: neither pinched nor let go
        if near:
            self.far_run = 0
        else:
            self.far_t = now
            self.far_run += 1
            if self.far_run >= 3:
                self.pinch_armed = True

        if near:                                      # fingers together: a pinch, never a fist or an open palm
            self.closed_run = self.open_run = 0
        elif ext == 0:
            self.closed_run, self.open_run = self.closed_run + 1, 0
        elif ext >= 3:
            self.open_run, self.closed_run = self.open_run + 1, 0
            self.open_t = now
            self.point_until = -9.0                   # a fully open hand ends pointing mode at once
            if self.open_run >= self.OPEN_FRAMES:
                self.armed = True
        else:
            self.open_run = 0                         # in-between pose: neither a drop nor a grab

        holding = self.mouse.down
        selected = now < self.sel_until and not holding
        tapped = self._tap(lm, pointing_ctx and not selected and not near, now)
        tapping = self.dip_t0 is not None

        # where the hand points: the fingertip while pointing, otherwise the knuckles (steadiest when a hand closes)
        mode = "tip" if (pointing_ctx and not holding) else "knuckle"
        if mode == "tip":
            kx, ky = pts[8]
        else:
            kx = sum(pts[i][0] for i in (5, 9, 13, 17)) / 4
            ky = sum(pts[i][1] for i in (5, 9, 13, 17)) / 4
        (x0, x1), (y0, y1) = self.X_RANGE, self.Y_RANGE
        tx = min(max((kx - x0) / (x1 - x0), 0.0), 1.0)
        ty = min(max((ky - y0) / (y1 - y0), 0.0), 1.0)
        fist_closing = self.closed_run > 0 and not holding and (not pointing_ctx or selected)
        pinch_closing = near and not holding and self.pinch_armed
        freezing = fist_closing or pinch_closing or tapping or (self.open_run > 0 and holding)
        if self.pos is None:
            self.pos, self.mode, self.off = (tx, ty), mode, (0.0, 0.0)
            self.filt.hold(self.pos, now)
            self.mouse.move(tx, ty)
        else:
            if mode != self.mode:                     # pointing <-> open hand <-> fist: keep the pointer where it is
                self.off = (self.pos[0] - tx, self.pos[1] - ty)
                self.mode = mode
                self.filt.hold(self.pos, now)
            elif not holding:
                self.off = (self.off[0] * 0.92, self.off[1] * 0.92)    # free again: drift back to the hand
            if freezing:
                self.filt.hold(self.pos, now)
            else:
                gx = min(max(tx + self.off[0], 0.0), 1.0)
                gy = min(max(ty + self.off[1], 0.0), 1.0)
                self.pos = self.filt((gx, gy), now)
                self.mouse.move(*self.pos)
                self.hist.append((now, self.pos))

        if tapped and not holding:                    # double air-tap: select the file under the pointer
            self.closed_run = self.open_run = 0
            self.mouse.move(*self.pos)
            self.mouse.press()
            self.mouse.release()                      # one plain click selects it (nothing is held yet)
            self.sel_until = now + self.SELECT_SECS
            self.armed = True
            self._beep(900, 2)
        elif not holding and self.pinch_armed and self.pinch_run >= 2:
            self._grab(now, ref=self.far_t, by="pinch")   # pinch: press the button (select it / pick it up)
        elif (not holding and self.armed and self.closed_run >= (3 if selected else self.CLOSE_FRAMES)
              and (selected or (not pointing_ctx and now - self.open_t < 0.8))):
            self._grab(now)                           # fist: grab (the selected file, or what's under the pointer)
        elif holding and (self.open_run >= self.OPEN_FRAMES or (self.hold_by == "pinch" and self.unpinch_run >= 2)):
            self.release()                            # open palm, or the pinch let go
        return slots


class GestureSetupError(Exception):
    pass


GESTURE_PACKAGES = ["opencv-python", "mediapipe"]


def _pip_python():
    """The python.exe that is running PAC (never pythonw.exe, which has no console for pip)."""
    exe = Path(sys.executable)
    if exe.name.lower() == "pythonw.exe" and exe.with_name("python.exe").exists():
        return exe.with_name("python.exe")
    return exe


def gesture_install_command():
    return f'"{_pip_python()}" -m pip install ' + " ".join(GESTURE_PACKAGES)


def pip_install(packages, log, what, then, version_hint=""):
    """pip-install into the SAME Python that is running PAC. 'No module named ...' right after a successful
    pip install almost always means pip belonged to a different Python than the one PAC uses."""
    log(f"Installing {what} into the Python PAC is running on:\n  {_pip_python()}\n"
        "This can take a few minutes - keep PAC open.")
    try:
        r = subprocess.run([str(_pip_python()), "-m", "pip", "install", "--upgrade", *packages],
                           capture_output=True, text=True, timeout=1200, creationflags=NO_WINDOW)
    except Exception as e:
        log(f"Couldn't run pip: {e}")
        return False
    if r.returncode == 0:
        import importlib
        importlib.invalidate_caches()
        log(then)
        return True
    tail = " ".join((r.stderr or r.stdout or "").strip().splitlines()[-4:])
    hint = version_hint if ("No matching distribution" in (r.stderr or "") or "from versions: none" in (r.stderr or "")) else ""
    log(f"pip couldn't install {what}: {tail}{hint}")
    return False


def install_gesture_packages(log):
    return pip_install(
        GESTURE_PACKAGES, log, "the camera packages",
        "Installed. Now tick Gestures > Gesture control again. (If it still says the package is missing, "
        "close PAC and open it again.)",
        f"\nYour Python is {sys.version_info.major}.{sys.version_info.minor}; mediapipe only publishes packages "
        "for some Python versions (3.9 to 3.12 at the time of writing). Installing Python 3.12 from python.org "
        "and running PAC with it will fix this.")


def ensure_hand_model():
    """The hand-landmark model for MediaPipe's Tasks API: downloaded once (about 8 MB), then used offline."""
    if HAND_MODEL_FILE.exists():
        return
    import urllib.request
    tmp = HAND_MODEL_FILE.with_suffix(".part")
    try:
        with urllib.request.urlopen(HAND_MODEL_URL, timeout=30) as r, open(tmp, "wb") as f:
            shutil.copyfileobj(r, f)
        tmp.replace(HAND_MODEL_FILE)
    except Exception as e:
        raise GestureSetupError(
            f"Couldn't download the hand model ({e}). It's a one-time download and needs internet. "
            f"Or save this file by hand to {HAND_MODEL_FILE} :  {HAND_MODEL_URL}")


class HandSource:
    """The laptop camera plus MediaPipe's hand tracker. read() gives a list with one (landmarks, 'Left'/'Right',
    points) per hand in view (up to two; empty when none). Pictures are mirrored, so moving your hand to your
    right moves it right on screen."""

    def __init__(self, cfg):
        missing = []
        for mod, pkg in (("cv2", "opencv-python"), ("mediapipe", "mediapipe")):
            try:
                __import__(mod)
            except Exception as e:
                missing.append(f"{pkg} ({e})")
        if missing:
            raise GestureSetupError(
                f"Gesture control can't find: {', '.join(missing)}.\n"
                f"PAC is running on this Python: {_pip_python()}  (version {sys.version_info.major}."
                f"{sys.version_info.minor}).\n"
                "Easiest fix: menu Gestures > Install gesture packages  (installs into exactly this Python).\n"
                f"Or in Command Prompt:  {gesture_install_command()}")
        import cv2
        import mediapipe as mp
        self.cv2, self.mp = cv2, mp
        cam = int(cfg.get("gesture_cam", 0))
        self.cap, first, info = open_camera_any(cv2, cam)
        if self.cap is None:
            raise GestureSetupError(f"Couldn't open camera {cam}" + (f" ({info})" if info else "") + ". Another app (or PAC's face "
                                    "recognition) may be using it, or Windows is blocking it: Settings > Privacy & security > "
                                    "Camera > let desktop apps use the camera. Menu > Faces > Find cameras shows what PAC can see.")
        self.last_frame, self.last_frame_time = first, time.time()      # faces borrow these when there is only one camera
        for prop, val in ((cv2.CAP_PROP_FPS, 30), (cv2.CAP_PROP_BUFFERSIZE, 1)):    # newest picture, never a stale one
            try:
                self.cap.set(prop, val)
            except Exception:
                pass
        self.t0, self.last_ts, self.fails, self._close = time.time(), 0, 0, lambda: None
        try:
            self._make_detector(mp)
        except Exception:
            self.cap.release()
            raise

    def _make_detector(self, mp):
        legacy = getattr(getattr(mp, "solutions", None), "hands", None)
        if legacy is not None and not HAND_MODEL_FILE.exists():
            hands = legacy.Hands(static_image_mode=False, max_num_hands=2, model_complexity=0,
                                 min_detection_confidence=0.6, min_tracking_confidence=0.5)

            def detect(rgb, ts):
                res = hands.process(rgb)
                if not res.multi_hand_landmarks:
                    return []
                out = []
                for i, h in enumerate(res.multi_hand_landmarks):
                    label = "Right"
                    if res.multi_handedness and i < len(res.multi_handedness):
                        label = res.multi_handedness[i].classification[0].label
                    out.append(([(p.x, p.y, p.z) for p in h.landmark], label))
                return out
            self.detect, self._close = detect, hands.close
            return
        ensure_hand_model()
        from mediapipe.tasks.python import BaseOptions
        from mediapipe.tasks.python import vision
        opts = vision.HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(HAND_MODEL_FILE)),
            running_mode=vision.RunningMode.VIDEO, num_hands=2,
            min_hand_detection_confidence=0.6, min_hand_presence_confidence=0.5, min_tracking_confidence=0.5)
        landmarker = vision.HandLandmarker.create_from_options(opts)

        def detect(rgb, ts):
            res = landmarker.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb), ts)
            out = []
            for i, h in enumerate(res.hand_landmarks or []):
                label = res.handedness[i][0].category_name if res.handedness and i < len(res.handedness) else "Right"
                out.append(([(p.x, p.y, p.z) for p in h], label))
            return out
        self.detect, self._close = detect, landmarker.close

    def read(self):
        cv2 = self.cv2
        ok, frame = self.cap.read()
        if not ok:
            self.fails += 1
            if self.fails > 25:
                raise GestureSetupError("The camera stopped sending pictures (unplugged, or taken by another app).")
            time.sleep(0.05)
            return None
        self.fails = 0
        self.last_frame, self.last_frame_time = frame, time.time()
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        ts = max(int((time.time() - self.t0) * 1000), self.last_ts + 1)
        self.last_ts = ts
        aspect = w / h
        return [([(x * aspect, y, z * aspect) for x, y, z in pts], label, [(x, y) for x, y, _ in pts])
                for pts, label in (self.detect(rgb, ts) or [])]            # every hand in view (up to two)

    def close(self):
        try:
            self._close()
        finally:
            self.cap.release()


class GestureEngine:
    """Watches the camera on its own thread, so it keeps working while PAC is minimised and you are in
    other apps. A pose has to be held for a moment before it counts, and a one-off gesture fires once until
    you change pose, so passing hand movements do nothing."""

    def __init__(self, app, source_factory=None):
        self.app = app
        self.source_factory = source_factory
        self.stop = threading.Event()
        self.thread = None
        self.running = False
        self.error = None
        self.frames = 0
        self.latest = {}                        # what the hand-view window draws
        self.rec = None                         # set while a new gesture is being recorded
        self.tracks = {"Left": HandTrack(), "Right": HandTrack(), "Both": HandTrack()}
        self.pair_pts = collections.deque()     # (time, distance between the wrists) while both hands are open
        self.airdrag = AirDrag(app)             # palm-as-mouse drag and drop (off until you switch it on)
        self.assigner = HandAssigner()          # keeps each hand in the same Left / Right slot
        self.pair_moving = False
        self.last_fire = 0.0
        self.suppress_until, self.swipe_cool, self.pair_cool = 0.0, 0.0, 0.0

    # ----- lifecycle
    def start(self):
        if self.thread and self.thread.is_alive():
            if not self.stop.is_set():
                return
            self.thread.join(3)
        self.stop.clear()
        self.error, self.frames = None, 0
        self.thread = threading.Thread(target=self.run, daemon=True, name="pac-gestures")
        self.thread.start()

    def stop_engine(self):
        self.stop.set()

    def _fail(self, msg):
        self.error = msg
        self.app.ui("gesture_error", msg)

    def run(self):
        try:
            src = (self.source_factory or (lambda: HandSource(self.app.cfg)))()
        except GestureSetupError as e:
            self._fail(str(e))
            return
        except Exception as e:
            logger.exception("gesture setup failed")
            self._fail(f"Couldn't start gesture control: {e}")
            return
        self.running = True
        self.hand_source = src                         # faces can borrow its pictures when there is only one camera
        self.app.ui("gesture_state", True)
        last_hand = time.time()
        try:
            while not self.stop.is_set():
                t0 = time.time()
                hand = src.read()
                self.frames += 1
                if hand:
                    last_hand = t0
                self.process(hand, t0)
                period = 1 / 30 if (t0 - last_hand < 3 or self.rec or self.airdrag.enabled) else 1 / 10    # idle: look less often
                spare = period - (time.time() - t0)
                if spare > 0:
                    self.stop.wait(spare)
        except GestureSetupError as e:
            self._fail(str(e))
        except Exception as e:
            logger.exception("gesture engine crashed")
            self._fail(f"Gesture control stopped: {e}")
        finally:
            try:
                src.close()
            except Exception:
                pass
            self.airdrag.release()                     # never leave the mouse button held down
            self.hand_source = None
            self.running = False
            self.latest = {}
            self.app.ui("gesture_state", False)

    # ----- recording a new gesture
    def start_recording(self, need=30):
        self.rec = {"vecs": [], "need": need, "t0": time.time(), "last": 0.0, "done": False}

    def cancel_recording(self):
        self.rec = None

    # ----- one camera picture
    def _hold(self, gid):
        cfg = self.app.cfg
        if gid.startswith("custom:"):
            for g in cfg.get("custom_gestures", []):
                if g.get("id") == gid and g.get("hold"):
                    return float(g["hold"])
        return max(0.1, float(cfg.get("gesture_hold", 0.35)))

    def _hold_step(self, tr, stable, now):
        """Hold a pose to fire it once; keep holding to repeat the actions that repeat (volume, scroll).
        Returns how far through the hold it is, 0..1."""
        if stable != tr.cand:
            tr.cand, tr.cand_since, tr.armed = stable, now, True
        if not stable or now < self.suppress_until:
            return 0.0
        spec = gesture_action(self.app.cfg, stable)
        if spec.get("type", "none") == "none":
            return 0.0
        hold = self._hold(stable)
        if now - tr.cand_since >= hold:
            if tr.armed:
                tr.armed, tr.last_repeat = False, now
                self._fire(stable, True)
            elif spec["type"] in ACTION_REPEATS and now - tr.last_repeat >= 0.4:
                tr.last_repeat = now
                self._fire(stable, False)
        return min(1.0, (now - tr.cand_since) / hold)

    def _pair_motion(self, now, lm_l, lm_r, open_l, open_r):
        """'Hands apart' / 'hands together': both hands open and moving away from / towards each other."""
        if not (open_l and open_r):
            self.pair_pts.clear()
            return None
        size = (hand_size(lm_l) + hand_size(lm_r)) / 2
        self.pair_pts.append((now, _dist(lm_l[0], lm_r[0]) / size))
        while self.pair_pts and now - self.pair_pts[0][0] > 0.8:
            self.pair_pts.popleft()
        self.pair_moving = False
        if len(self.pair_pts) < 4 or now - self.pair_pts[0][0] < 0.15 or now < self.pair_cool:
            return None
        change = self.pair_pts[-1][1] - self.pair_pts[0][1]
        self.pair_moving = abs(change) >= 0.9          # hands clearly travelling: not a still pose
        if change >= 1.8:
            return "spread"
        if change <= -1.8:
            return "together"
        return None

    def process(self, hands, now):
        """One camera picture. `hands` is the list from HandSource.read() (a single hand tuple or None is also
        accepted). Each hand is followed on its own, so both can make a gesture at the same time; the same pose
        in both hands, or moving them apart / together, counts as a two-hand gesture."""
        cfg = self.app.cfg
        if hands is None:
            hands = []
        elif isinstance(hands, tuple):
            hands = [hands]
        slots = self.assigner.assign(hands, now)
        if self.rec is None:
            slots = self.airdrag.step(slots, now)      # in air-drag mode one hand is the mouse; the rest carries on

        # a hand that has left the picture for a moment lets go of whatever it was doing
        for name in ("Left", "Right"):
            tr = self.tracks[name]
            if name in slots:
                tr.missing_since = None
            else:
                if tr.missing_since is None:
                    tr.missing_since = now
                if now - tr.missing_since > 0.3:
                    tr.reset()
        if len(slots) < 2:
            self.tracks["Both"].reset()
            self.pair_pts.clear()
        if not slots:
            ad = self.airdrag
            if ad.enabled and ad.pts:
                prog = 1.0 if ad.holding else 0.0
                self.latest = {"pts": ad.pts, "gid": None, "progress": prog, "t": now,
                               "hands": [{"slot": ad.slot or "Right", "pts": ad.pts, "gid": None, "progress": prog}]}
            else:
                self.latest = {"pts": None, "gid": None, "progress": 0.0, "t": now, "hands": []}
            return

        if self.rec is not None:                       # teaching: collect samples from one hand, never trigger anything
            name = "Right" if "Right" in slots else next(iter(slots))
            lm, label, pts = slots[name]
            r = self.rec
            if now - r["last"] >= 0.08 and not r["done"]:
                r["vecs"].append(pose_vector(lm, label))
                r["last"] = now
                r["done"] = len(r["vecs"]) >= r["need"]
            self.latest = {"pts": pts, "gid": None, "progress": len(r["vecs"]) / r["need"], "t": now,
                           "hands": [{"slot": name, "pts": pts, "gid": None, "progress": 0.0}]}
            return

        customs = cfg.get("custom_gestures", [])
        raw, stable = {}, {}
        for name, (lm, label, pts) in slots.items():
            tr = self.tracks[name]
            gid = match_custom(pose_vector(lm, label), customs) or classify_builtin(lm)
            raw[name] = gid
            tr.recent.append(gid)
            stable[name] = tr.stable()

        # swipes: a quick sweep of an open hand, from either hand (one swipe at a time)
        for name, (lm, label, pts) in slots.items():
            tr = self.tracks[name]
            open_now = stable[name] in ("open_palm", "four") or raw[name] in ("open_palm", "four")
            swipe = tr.swipes.feed(now, lm, open_now)
            if swipe and gesture_is_deleted(cfg, swipe):
                swipe = None
            if swipe and now >= self.swipe_cool:
                self.swipe_cool = self.suppress_until = now + 1.0
                for t2 in self.tracks.values():
                    t2.swipes.clear()
                self._fire(swipe, True)
                self.latest = {"pts": pts, "gid": swipe, "progress": 1.0, "t": now,
                               "hands": [{"slot": n, "pts": h[2], "gid": swipe if n == name else raw[n],
                                          "progress": 1.0 if n == name else 0.0} for n, h in slots.items()]}
                return

        # two hands: the same pose in both, or both open and moving apart / together
        combo = None
        if "Left" in slots and "Right" in slots:
            sl, sr = stable["Left"], stable["Right"]
            both = self.tracks["Both"]
            both.recent.append(TWO_HAND_POSES.get(sl) if (sl and sl == sr) else None)
            pair = both.stable()
            if pair and gesture_action(cfg, pair).get("type", "none") != "none":
                combo = pair
            elif sl and sl == sr:
                stable["Left"] = None                  # same pose in both hands, no two-hand action: act once, not twice
            move = self._pair_motion(now, slots["Left"][0], slots["Right"][0],
                                     sl in ("open_palm", "four"), sr in ("open_palm", "four"))
            if self.pair_moving:
                combo = None                           # moving apart / together: don't also count it as a held pose
            if move and gesture_action(cfg, move).get("type", "none") != "none":
                self.pair_cool = self.suppress_until = now + 1.2
                self.pair_pts.clear()
                self._fire(move, True)
                combo = None
                self.latest = {"pts": slots["Right"][2], "gid": move, "progress": 1.0, "t": now,
                               "hands": [{"slot": n, "pts": h[2], "gid": raw[n], "progress": 0.0}
                                         for n, h in slots.items()], "combo": move}
                return

        progress = {}
        if combo:                                      # the pair acts as one; neither hand fires on its own
            progress["Both"] = self._hold_step(self.tracks["Both"], combo, now)
            self.tracks["Left"].cand = self.tracks["Right"].cand = None
            stable["Left"] = stable["Right"] = None
        else:
            self.tracks["Both"].cand = None
        for name in slots:
            progress[name] = self._hold_step(self.tracks[name], stable[name], now)

        primary = "Both" if combo else max(slots, key=lambda n: (progress.get(n, 0.0), n == "Right"))
        shown = combo or stable.get(primary) or raw.get(primary)
        self.latest = {
            "pts": slots[primary if primary in slots else next(iter(slots))][2],
            "gid": shown, "progress": progress.get(primary, 0.0), "t": now, "combo": combo,
            "hands": [{"slot": n, "pts": h[2], "gid": stable[n] or raw[n], "progress": progress.get(n, 0.0)}
                      for n, h in slots.items()]}
        ad = self.airdrag
        if ad.enabled and ad.pts:                      # the mouse hand was taken out of `slots`: still show it
            self.latest["hands"].append({"slot": ad.slot or "Right", "pts": ad.pts, "gid": None,
                                         "progress": 1.0 if ad.holding else 0.0})

    def _fire(self, gid, first):
        spec = gesture_action(self.app.cfg, gid)
        if spec.get("type", "none") == "none":
            return
        try:
            self.app.run_gesture_action(spec)
        except Exception:
            logger.exception("gesture action failed")
            self.app.ui("log", "sys", f"The action for {gesture_title(self.app.cfg, gid)} failed (see ~/.pac/pac.log).")
            return
        self.last_fire = time.time()
        self.app.ui("gesture_fired", gid, ACTION_LABEL.get(spec["type"], spec["type"]), first)


# --------------------------------------------------------------- opening a camera (shared by faces, gestures, Find cameras)
def camera_backends():
    """The ways to open a camera, best first. Windows: DirectShow is quick, but plenty of drivers (and many Windows
    Hello cameras) only work through Media Foundation, so both are tried. Elsewhere OpenCV's default."""
    try:
        import cv2
    except Exception:
        return [("default", 0)]
    if OS == "Windows":
        return [("DirectShow", getattr(cv2, "CAP_DSHOW", 700)), ("Media Foundation", getattr(cv2, "CAP_MSMF", 1400))]
    return [("default", 0)]


def open_camera_any(cv2, idx, size=(640, 480), deadline=None, warm=2.5):
    """Open camera number `idx` any way that works: each backend, with the picture size forced and then left alone,
    waiting for real pictures. -> (capture, first picture, backend name) or (None, None, what went wrong)."""
    reasons = []
    for name, api in camera_backends():
        for force in ((True, False) if size else (False,)):
            if deadline is not None and time.time() > deadline:
                break
            cap = None
            try:
                cap = cv2.VideoCapture(idx, api)
                if not cap.isOpened():
                    reasons.append(f"{name}: won't open")
                    cap.release()
                    break                                   # no point trying another picture size
                if force:
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])
                end = time.time() + warm
                if deadline is not None:
                    end = min(end, deadline)
                frame, good = None, 0
                while time.time() < end:                    # a camera needs a moment before its pictures are real
                    ok, f = cap.read()
                    if ok and f is not None and getattr(f, "size", 1):
                        frame, good = f, good + 1
                        if good >= 3:
                            break
                    else:
                        time.sleep(0.08)
                if frame is not None:
                    return cap, frame, name
                reasons.append(f"{name}: opens but sends no pictures")
                cap.release()
            except Exception as e:
                reasons.append(f"{name}: {e}")
                try:
                    if cap is not None:
                        cap.release()
                except Exception:
                    pass
    return None, None, "; ".join(dict.fromkeys(reasons))


class SharedCamera:
    """One camera, and gesture control already holds it: faces borrow gesture control's pictures instead of failing."""

    def __init__(self, get_source):
        self.get = get_source

    def isOpened(self):
        return True

    def read(self):
        src = self.get()
        f = getattr(src, "last_frame", None) if src is not None else None
        if f is None or time.time() - getattr(src, "last_frame_time", 0.0) > 2.0:
            time.sleep(0.1)
            return False, None
        return True, f.copy()

    def set(self, *a):
        return False

    def release(self):
        pass


# --------------------------------------------------------------- faces (laptop camera, infrared first)
# Who is in front of the laptop? PAC learns faces you enrol (only a 128-number "fingerprint" per picture is
# kept, in ~/.pac/faces.json - never the pictures), notices when someone arrives, leaves or is a stranger, and
# can lock chosen commands to chosen faces.  It uses OpenCV's own YuNet (find the face) and SFace (tell faces
# apart) models, so there is nothing to install beyond opencv-python, which the hand gestures already need.
FACE_DB_FILE = DATA_DIR / "faces.json"
FACE_DIR = DATA_DIR / "faces"
FACE_DETECT_FILE = DATA_DIR / "face_detection_yunet_2023mar.onnx"
FACE_RECOG_FILE = DATA_DIR / "face_recognition_sface_2021dec.onnx"
FACE_DETECT_URL = ("https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/"
                   "face_detection_yunet_2023mar.onnx")
FACE_RECOG_URL = ("https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/"
                  "face_recognition_sface_2021dec.onnx")

FACE_ROLES = {"guest": 1, "trusted": 2, "owner": 3}                  # what a recognised face may do
FACE_LEVELS = {"anyone": 0, **FACE_ROLES}                            # what a command asks for
FACE_GROUPS = {                                                      # handler name -> permission group
    "c_shutdown": "power", "c_restart": "power", "c_laptop_sleep": "power",
    "c_mail_review": "mail", "c_mail_delete": "mail", "c_mail_check": "mail",
    "c_wa_preset": "messages", "c_wa_compose": "messages", "c_list_messages": "messages", "c_list_contacts": "messages",
    "c_key": "typing", "c_type": "typing", "c_dictate_on": "typing",
    "c_open_file": "files", "c_open_folder": "files", "c_open_notes": "files", "c_open_knowledge": "files",
    "c_read_notes": "files",
    "c_note": "notes", "c_learn": "notes", "c_timetable_import": "notes", "c_timetable_edit": "notes",
    "c_claude_on": "claude", "c_claude_ask": "claude",
    "c_transfer_on": "files", "c_grab_file": "files", "c_send_phone": "files", "c_drop_file": "files",
    "c_file_info": "files", "c_file_list": "files", "c_file_move": "files", "c_file_undo": "files",
    "c_file_new_folder": "files", "c_file_new_file": "files", "c_file_any": "files",
    "c_mem_remember": "notes", "c_mem_forget": "notes", "c_mem_forget_last": "notes", "c_mem_clear": "notes",
    "c_mem_show": "files", "c_mem_open": "files",
    "c_ar_learn": "notes", "c_ar_forget": "notes", "c_ar_bind": "notes", "c_ar_unbind": "notes",
}
FACE_GROUP_LABEL = {
    "power": "shut down, restart or sleep the laptop", "mail": "e-mail", "messages": "WhatsApp messages and contacts",
    "typing": "typing and key presses", "files": "opening files, folders and notes",
    "notes": "saving notes and facts, editing the timetable", "claude": "Claude mode (online)",
}
DEFAULT_FACE_RULES = {"power": "owner", "mail": "owner", "messages": "owner", "typing": "trusted",
                      "files": "trusted", "notes": "trusted", "claude": "trusted"}


def face_rule(cfg, group):
    """The lowest role allowed to use a group of commands (anyone / guest / trusted / owner)."""
    level = (cfg.get("face_rules") or {}).get(group) or DEFAULT_FACE_RULES.get(group, "owner")
    return level if level in FACE_LEVELS else "owner"


class FaceSetupError(Exception):
    pass


def face_install_command():
    return f'"{_pip_python()}" -m pip install --upgrade opencv-python'


def ensure_face_models(log=None):
    """The two small face models (about 40 MB together): downloaded once, then used offline."""
    import urllib.request
    for path, url in ((FACE_DETECT_FILE, FACE_DETECT_URL), (FACE_RECOG_FILE, FACE_RECOG_URL)):
        if path.exists() and path.stat().st_size > 100_000:
            continue
        if log:
            log(f"Downloading the face model {path.name} (one time, needs internet)...")
        tmp = path.with_suffix(".part")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 PAC"})
            with urllib.request.urlopen(req, timeout=60) as r, open(tmp, "wb") as f:
                shutil.copyfileobj(r, f)
            if tmp.stat().st_size < 100_000:
                raise OSError("the download was too small - probably an error page")
            tmp.replace(path)
        except Exception as e:
            try:
                tmp.unlink()
            except OSError:
                pass
            raise FaceSetupError(
                f"Couldn't download {path.name} ({e}). It's a one-time download and needs internet. "
                f"Or save this file by hand to {path} :  {url}")


class FaceDB:
    """Who PAC knows: name, role, arrival command and the face fingerprints. Kept on this PC only."""

    def __init__(self, path=FACE_DB_FILE):
        self.path = path
        self.lock = threading.RLock()
        self.people = {}
        self.load()

    @staticmethod
    def key(name):
        return " ".join(re.sub(r"[^a-z' -]", " ", str(name).lower()).split())

    def load(self):
        try:
            self.people = json.loads(self.path.read_text(encoding="utf-8")).get("people", {})
        except Exception:
            self.people = {}

    def save(self):
        with self.lock:
            try:
                tmp = self.path.with_suffix(".tmp")
                tmp.write_text(json.dumps({"people": self.people}), encoding="utf-8")
                tmp.replace(self.path)
                try:
                    os.chmod(self.path, 0o600)
                except OSError:
                    pass
            except Exception:
                logger.exception("could not save faces")

    def has(self, name):
        return self.key(name) in self.people

    def get(self, key):
        return self.people.get(key)

    def names(self):
        return [p["name"] for p in self.people.values()]

    def owners(self):
        return [k for k, p in self.people.items() if p.get("role") == "owner"]

    def add(self, name, role, embeds):
        """New person, or more pictures of someone already known (their role is kept unless one is given)."""
        k = self.key(name)
        with self.lock:
            p = self.people.setdefault(k, {"name": name.strip().title(), "role": role or "guest", "embeds": [],
                                           "on_arrival": "", "added": datetime.date.today().isoformat()})
            if role:
                p["role"] = role
            p["embeds"] = (p["embeds"] + [[round(float(x), 5) for x in e] for e in embeds])[-60:]
            self.save()
        return k

    def remove(self, name):
        with self.lock:
            gone = self.people.pop(self.key(name), None)
            self.save()
        return gone is not None

    def remove_all(self):
        with self.lock:
            self.people = {}
            self.save()

    def set_role(self, name, role):
        with self.lock:
            if self.key(name) in self.people:
                self.people[self.key(name)]["role"] = role
                self.save()

    def set_arrival(self, name, command):
        with self.lock:
            if self.key(name) in self.people:
                self.people[self.key(name)]["on_arrival"] = command.strip()
                self.save()

    def identify(self, vec, threshold, margin=0.03):
        """(key, score) for the person this fingerprint is, or (None, best score) for a stranger. A person's
        score is the average of their three closest pictures; a near-tie between two people counts as unknown."""
        import numpy as np
        scores = []
        for k, p in list(self.people.items()):
            if not p.get("embeds"):
                continue
            sims = np.sort(np.asarray(p["embeds"], dtype=np.float32) @ vec)
            scores.append((float(sims[-3:].mean()), k))
        if not scores:
            return None, 0.0
        scores.sort(reverse=True)
        best, key = scores[0]
        if best < threshold or (len(scores) > 1 and best - scores[1][0] < margin):
            return None, best
        return key, best


class FaceEngine:
    """Watches the camera on its own thread: finds faces, says who they are, notices arrivals, departures and
    strangers, records new faces, and answers "who is at the laptop right now?" for the permission checks.
    It prefers the laptop's infrared camera (the Windows Hello one) and falls back to the normal webcam."""

    def __init__(self, app):
        self.app = app
        self.db = FaceDB()
        self.stop = threading.Event()
        self.ready = threading.Event()
        self.thread = None
        self.running = False
        self.temp = False                   # started just for one check or enrolment: switches itself off again
        self.temp_until = 0.0
        self.error = None
        self.cam_label = ""
        self.is_ir = False
        self.cap = None
        self.diag = []                      # why each camera failed, for the error message
        self.tick_time = 0.0
        self.people = []                    # newest picture: [(key or None, score, face width)], biggest face first
        self.present = {}                   # key -> last seen, for the people PAC counts as "here"
        self.streak = collections.defaultdict(int)
        self.unk_streak = 0
        self.last_unknown = 0.0
        self.enroll_job = None

    # ----- start / stop
    def start(self, temp=False):
        if self.running:
            if not temp:
                self.temp = False
            elif self.temp:
                self.temp_until = time.time() + 25
            return
        self.stop.clear()
        self.ready.clear()
        self.error = None
        self.temp = temp
        self.temp_until = time.time() + 25 if temp else 0.0
        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True, name="faces")
        self.thread.start()

    def stop_engine(self):
        self.stop.set()
        t = self.thread
        if t and t.is_alive() and t is not threading.current_thread():
            t.join(2.5)
        self.running = False

    # ----- camera
    def _classify_ir(self, frame):
        """Infrared cameras give grey pictures: a single channel, or three nearly equal ones."""
        if frame.ndim == 2:
            return True
        small = frame[::8, ::8].astype(self.np.int16)
        return float(self.np.abs(small[..., 0] - small[..., 2]).mean()) < 3.0

    def _camera_error(self):
        lines = list(dict.fromkeys(self.diag))               # each camera once, and the empty numbers folded into one line
        dead = [l.split(":")[0].replace("camera ", "") for l in lines
                if all(x.strip().endswith("won't open") for x in l.split(": ", 1)[1].split("; "))]
        lines = [l for l in lines if l.split(":")[0].replace("camera ", "") not in dead]
        if dead:
            lines.append("camera " + ", ".join(dead) + ": nothing there (won't open)")
        text = "\n".join(lines)
        if "sends no pictures" in text:
            head = ("Couldn't open a camera for face recognition: the camera opens but sends no pictures, so another app is "
                    "using it or the system is blocking it.")
        else:
            head = "Couldn't open a camera for face recognition: no camera would open (none found, or another app has it)."
        if OS == "Windows":
            fix = ("  - Windows: Settings > Privacy & security > Camera: turn on Camera access, 'Let apps access your camera' "
                   "and 'Let desktop apps access your camera'.\n")
        elif OS == "Darwin":
            fix = "  - Mac: System Settings > Privacy & Security > Camera: allow the app that runs PAC (Terminal, IDLE, Python).\n"
        else:
            fix = "  - Linux: your user needs access to /dev/video0 (the 'video' group).\n"
        return (head + "\n" + (text + "\n" if text else "") + "What to try:\n"
                "  - Close anything else using the camera: Teams, Zoom, Skype, the Camera app, a browser tab on a video call.\n"
                + fix +
                "  - Menu > Faces > Find cameras shows what PAC can see. Pick a working one in Menu > Faces > Camera.\n"
                "  - The Windows Hello infrared camera is often reserved by Windows; PAC then needs the normal webcam.\n"
                "  - Locked out? Menu > Faces > Camera trouble tests the camera and lets you switch face security off.")

    def _open_camera(self):
        cv2 = self.cv2
        cfg = self.app.cfg
        want = cfg.get("face_cam", "auto")
        gest_cam = int(cfg.get("gesture_cam", 0)) if self.app.gesture.running else None
        self.diag = []
        deadline = time.time() + 18
        cands = [int(want)] if want != "auto" else list(range(6))
        fallback = None                                      # (capture, index, backend) of the first normal webcam
        for _attempt in range(2):                            # a camera another part of PAC just let go of needs a moment
            for i in cands:
                if i == gest_cam or time.time() > deadline:
                    continue
                cap, frame, info = open_camera_any(cv2, i, deadline=deadline)
                if cap is None:
                    if info:
                        self.diag.append(f"camera {i}: {info}")
                    continue
                if self._classify_ir(frame):
                    if fallback is not None:
                        fallback[0].release()
                    self.cap, self.is_ir, self.cam_label = cap, True, f"camera {i} (infrared, {info})"
                    return
                if fallback is None:
                    fallback = (cap, i, info)
                else:
                    cap.release()
            if fallback is not None or time.time() > deadline:
                break
            time.sleep(0.8)
        if fallback is not None:
            self.cap, self.is_ir = fallback[0], False
            self.cam_label = f"camera {fallback[1]} (normal webcam, {fallback[2]})"
            return
        if gest_cam is not None:                             # one camera, and gesture control has it: share its pictures
            shared = SharedCamera(lambda: getattr(self.app.gesture, "hand_source", None))
            end, frame = time.time() + 3, None
            while time.time() < end and frame is None:
                ok, f = shared.read()
                frame = f if ok else None
            if frame is not None:
                self.cap, self.is_ir = shared, self._classify_ir(frame)
                self.cam_label = f"camera {gest_cam} (shared with gesture control)"
                return
            self.diag.append(f"camera {gest_cam}: gesture control has it, and its pictures weren't available")
        logger.warning("face camera could not be opened: %s", "; ".join(self.diag))
        raise FaceSetupError(self._camera_error())

    def _open(self):
        try:
            import cv2
            import numpy as np
        except Exception as e:
            raise FaceSetupError(f"Face recognition needs opencv-python ({e}).\nInstall it with:  {face_install_command()}")
        if not (hasattr(cv2, "FaceDetectorYN") and hasattr(cv2, "FaceRecognizerSF")):
            raise FaceSetupError(f"Your opencv-python ({cv2.__version__}) is too old for face recognition (needs 4.5.4 "
                                 f"or newer).  Upgrade it with:  {face_install_command()}")
        self.cv2, self.np = cv2, np
        ensure_face_models(lambda m: self.app.ui("log", "sys", m))
        self.det = cv2.FaceDetectorYN.create(str(FACE_DETECT_FILE), "", (320, 240), 0.85, 0.3, 20)
        self.rec = cv2.FaceRecognizerSF.create(str(FACE_RECOG_FILE), "")
        self.clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        self.fails = 0
        self._open_camera()

    def _grab(self):
        cv2 = self.cv2
        ok, frame = self.cap.read()
        if not ok or frame is None:
            self.fails += 1
            if self.fails > 40:
                raise FaceSetupError("The camera stopped sending pictures (unplugged, or taken by another app).")
            time.sleep(0.1)
            return None
        self.fails = 0
        if frame.ndim == 2:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        if self.is_ir:                                # dark, flat infrared pictures: stretch the contrast
            frame = cv2.cvtColor(self.clahe.apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)), cv2.COLOR_GRAY2BGR)
        return frame

    def _faces(self, frame):
        h, w = frame.shape[:2]
        self.det.setInputSize((w, h))
        _, rows = self.det.detect(frame)
        if rows is None:
            return []
        smallest = float(self.app.cfg.get("face_min_px", 70))
        return sorted((r for r in rows if r[2] >= smallest), key=lambda r: -r[2] * r[3])

    def _feature(self, frame, row):
        f = self.np.asarray(self.rec.feature(self.rec.alignCrop(frame, row)), dtype=self.np.float32).flatten()
        n = float(self.np.linalg.norm(f))
        return f / n if n else f

    # ----- the loop
    def _run(self):
        try:
            self._open()
        except FaceSetupError as e:
            self._fail(str(e))
            return
        except Exception as e:
            logger.exception("face engine could not start")
            self._fail(f"Face recognition couldn't start: {e}")
            return
        self.app.ui("log", "sys", f"Face recognition is on, using {self.cam_label}.")
        self.ready.set()
        try:
            while not self.stop.is_set():
                t0 = time.time()
                if self.temp and not self.enroll_job and t0 > self.temp_until:
                    break
                frame = self._grab()
                if frame is not None:
                    try:
                        self._update(frame, self._faces(frame), t0)
                    except FaceSetupError:
                        raise
                    except Exception:
                        logger.exception("face tick failed")
                period = 1.0 / max(1.0, float(self.app.cfg.get("face_fps", 4)))
                self.stop.wait(max(0.02, period - (time.time() - t0)))
        except FaceSetupError as e:
            self._fail(str(e))
        finally:
            try:
                if self.cap is not None:
                    self.cap.release()
            except Exception:
                pass
            self.cap = None
            self.running = False
            self.ready.clear()

    def _fail(self, message):
        self.error = message
        self.running = False
        self.ready.set()                       # whoever is waiting finds out right away that it failed
        self.app.ui("face_error", message)

    def _update(self, frame, rows, now):
        thr = float(self.app.cfg.get("face_threshold", 0.40))
        people = []
        for r in rows:
            key, score = self.db.identify(self._feature(frame, r), thr) if self.db.people else (None, 0.0)
            people.append((key, score, float(r[2])))
        self.people = people
        self.tick_time = now
        job = self.enroll_job
        if job is not None:                                          # recording a new face
            if len(rows) == 1 and float(rows[0][-1]) >= 0.9 and now - job["last"] >= 0.45:
                job["embs"].append(self._feature(frame, rows[0]))
                job["last"] = now
                if len(job["embs"]) >= job["need"]:
                    job["done"].set()
            elif len(rows) > 1:
                job["multi"] += 1
            return
        # ----- arrivals, departures, strangers
        seen = {k for k, _, _ in people if k}
        for k in seen:
            self.present.setdefault(k, 0.0)
            self.streak[k] += 1
            if self.streak[k] == 2 and now - self.present[k] > float(self.app.cfg.get("face_absent_secs", 45)):
                self._event("arrive", k)
            self.present[k] = now
        for k in list(self.streak):
            if k not in seen:
                self.streak[k] = 0
        for k, last in list(self.present.items()):
            if k not in seen and last and now - last > float(self.app.cfg.get("face_absent_secs", 45)):
                self.present[k] = 0.0
                self._event("leave", k)
        if any(k is None for k, _, _ in people):
            self.unk_streak += 1
            if self.unk_streak == 4 and now - self.last_unknown > 120:
                self.last_unknown = now
                if self.app.cfg.get("face_save_unknown"):
                    self._snapshot(frame)
                self._event("unknown", None)
        else:
            self.unk_streak = 0

    def _event(self, kind, key):
        try:
            self.app.assistant.on_face_event(kind, key)
        except Exception:
            logger.exception("face event failed")

    def _snapshot(self, frame):
        try:
            FACE_DIR.mkdir(exist_ok=True)
            self.cv2.imwrite(str(FACE_DIR / time.strftime("unknown_%Y%m%d_%H%M%S.jpg")), frame)
            for old in sorted(FACE_DIR.glob("unknown_*.jpg"))[:-20]:           # keep only the newest 20
                old.unlink()
        except Exception:
            logger.exception("could not save the snapshot")

    # ----- questions other parts of PAC ask
    def verify(self, wait=5.0):
        """Who is in front of the camera right now? -> (key, score, status); status is ok / unknown / noface / nocam."""
        t0 = time.time()
        self.start(temp=True)
        if not self.ready.wait(25) or self.error:
            return None, 0.0, "nocam"
        deadline = time.time() + wait
        while time.time() < deadline:
            if self.error:
                return None, 0.0, "nocam"
            if self.temp:
                self.temp_until = time.time() + 25
            if self.tick_time >= t0 - 0.8 and self.people:
                key, score, _ = self.people[0]
                return key, score, "ok" if key else "unknown"
            time.sleep(0.12)
        return None, 0.0, "noface"

    def look(self, wait=5.0):
        """Everyone the camera sees right now: a list of (key or None, score); empty when nobody is there."""
        t0 = time.time()
        self.start(temp=True)
        if not self.ready.wait(25) or self.error:
            return None
        deadline = time.time() + wait
        while time.time() < deadline:
            if self.error:
                return None
            if self.temp:
                self.temp_until = time.time() + 25
            if self.tick_time >= t0 + 0.3 and self.people:
                break
            time.sleep(0.12)
        if self.tick_time >= t0 + 0.3:
            return [(k, s) for k, s, _ in self.people]
        return []

    def enroll(self, name, count=14, timeout=45):
        """Record `count` pictures of the one face in view. -> (fingerprints, problem or '')."""
        self.start(temp=True)
        if not self.ready.wait(25) or self.error:
            return [], self.error or "The camera didn't start."
        job = {"embs": [], "need": count, "last": 0.0, "multi": 0, "done": threading.Event()}
        self.enroll_job = job
        try:
            job["done"].wait(timeout)
        finally:
            self.enroll_job = None
            if self.temp:
                self.temp_until = time.time() + 3
        embs = job["embs"]
        if len(embs) < max(6, count // 2):
            more = " I could see more than one face - only one person should be in front of the camera." if job["multi"] else ""
            return [], "I couldn't get enough good pictures of one face. Face the camera, in good light, and keep still-ish." + more
        sims = [float(a @ b) for i, a in enumerate(embs) for b in embs[i + 1:]]
        if sims and sum(sims) / len(sims) < 0.40:
            return [], "Those pictures didn't look like one person. Let's try again with just you in front of the camera."
        return embs, ""


def face_camera_report(cfg, log):
    """Menu > Faces > Find cameras: which cameras open, how big, and which look like infrared."""
    try:
        import cv2
        import numpy as np
    except Exception as e:
        log(f"Face recognition needs opencv-python ({e}).  Install it with:  {face_install_command()}")
        return
    log("Looking at camera numbers 0 to 5, each way Windows offers (this can take up to a minute)...")
    found = 0
    for i in range(6):
        cap, frame, info = open_camera_any(cv2, i, warm=3.0)
        if cap is None:
            log(f"  Camera {i}: " + (info or "not available"))
            continue
        cap.release()
        found += 1
        h, w = frame.shape[:2]
        grey = frame.ndim == 2 or float(np.abs(frame[::8, ::8, 0].astype(np.int16) - frame[::8, ::8, 2]).mean()) < 3.0
        log(f"  Camera {i}: {w}x{h}, {'looks like an INFRARED camera' if grey else 'normal colour webcam'} (works via {info})")
    if not found:
        log("  None worked. 'Opens but sends no pictures' means another app has the camera or the system is blocking it; "
            "close Teams/Zoom/the Camera app, and check Settings > Privacy & security > Camera. If gesture control "
            "is on, it is using a camera: switch it off and run this again.")
    log("Pick the one you want in Menu > Faces > Camera. 'Automatic' prefers an infrared one.")


# --------------------------------------------------------------- augmented reality (laptop camera)
# A live camera window ("PAC AR") with overlays. PAC learns the objects you show it - hold one inside the guide box
# and say "learn this as my keys" - and recognises it again later, drawing an outline and a label on it and running
# whatever command you tied to it ("when you see my keys say don't forget your wallet"). It matches the object's
# visual features (OpenCV ORB, from several angles); a plain object with too few details is matched by its outline
# instead. Clean geometric shapes shown in the box (circle, triangle, square...) are predefined and can also be tied
# to commands. Everything stays on this laptop (~/.pac/ar_objects.json holds numbers, never pictures).
AR_FILE = DATA_DIR / "ar_objects.json"
AR_WIN = "PAC AR"
AR_SHAPES = ["circle", "triangle", "square", "rectangle", "pentagon", "hexagon"]
AR_BOX = (0.28, 0.18, 0.72, 0.82)          # the guide box, as fractions of the picture (left, top, right, bottom)
AR_STARTER = {"triangle": "what time is it", "circle": "open chrome", "square": "take a screenshot",
              "rectangle": "what's my schedule today", "pentagon": "battery", "hexagon": "tell me a joke"}
# Everyday things PAC already "knows" by their outline - no teaching needed. These are shape guesses (long thin = pen,
# flat slab = phone...), so they are announced as "looks like"; teach PAC the real thing for a sure match.
AR_PRESETS = {"pen": "a long thin object", "phone": "a flat rectangular slab", "remote": "a long bar",
              "bottle": "a tall shape with a narrower neck", "card": "a small flat rectangle",
              "book": "a large, nearly square rectangle", "watch": "a small round face"}
AR_BLUE = (255, 140, 26)                    # OpenCV colours are blue-green-red
AR_PALE = (255, 190, 110)


class ARError(Exception):
    pass


def ar_shape_of(cnt):
    """Name of a clean geometric shape for an OpenCV contour, or None."""
    import cv2
    area = cv2.contourArea(cnt)
    peri = cv2.arcLength(cnt, True)
    if area < 400 or peri <= 0:
        return None
    hull = cv2.convexHull(cnt)
    if area / max(cv2.contourArea(hull), 1.0) < 0.9:
        return None
    approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)
    n = len(approx)
    circ = 4 * math.pi * area / (peri * peri)
    if n == 3:
        return "triangle"
    if n == 4:
        _x, _y, w, h = cv2.boundingRect(approx)
        return "square" if 0.9 <= w / max(h, 1) <= 1.1 else "rectangle"
    if n == 5:
        return "pentagon"
    if n == 6 and circ < 0.93:
        return "hexagon"
    if n > 5 and circ > 0.8:
        return "circle"
    return None


def ar_main_contour(gray, min_frac=0.06):
    """The outline of the one thing held in the middle of a grey picture, or None."""
    import cv2
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 40, 120)
    edges = cv2.dilate(edges, None, iterations=2)
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    h, w = gray.shape[:2]
    best, best_area = None, 0.0
    for c in cnts:
        a = cv2.contourArea(c)
        x, y, cw, ch = cv2.boundingRect(c)
        if a < min_frac * w * h or a > 0.95 * w * h:
            continue
        if x <= 1 or y <= 1 or x + cw >= w - 1 or y + ch >= h - 1:      # touches the edge: that is the background
            continue
        if a > best_area:
            best, best_area = c, a
    return best


def ar_preset_of(cnt, box_area):
    """Guess an everyday thing (pen, phone, watch...) from an outline's proportions, or None."""
    import cv2
    area = cv2.contourArea(cnt)
    peri = cv2.arcLength(cnt, True)
    if area <= 0 or peri <= 0 or box_area <= 0:
        return None
    (_cx, _cy), (rw, rh), _ang = cv2.minAreaRect(cnt)
    long_, short = max(rw, rh), min(rw, rh)
    if short < 6:
        return None
    aspect = long_ / short
    fill = area / (long_ * short)                 # 1.0 = a perfect rectangle
    frac = area / box_area
    circ = 4 * math.pi * area / (peri * peri)
    if aspect >= 6 and fill >= 0.6:
        return "pen"
    if 2.2 <= aspect < 5 and 0.55 <= fill < 0.8 and frac >= 0.05:
        return "bottle"
    if 3.2 <= aspect < 6 and fill >= 0.8:
        return "remote"
    if 1.7 <= aspect < 3.2 and fill >= 0.85 and frac >= 0.2:
        return "phone"
    if 1.4 <= aspect < 1.75 and fill >= 0.85 and frac < 0.2:
        return "card"
    if 1.1 <= aspect < 1.6 and fill >= 0.85 and frac >= 0.3:
        return "book"
    if aspect < 1.25 and circ > 0.8 and frac < 0.18:
        return "watch"
    return None


def ar_hu(cnt):
    """Seven shape numbers (log Hu moments) for an outline: the same outline gives the same numbers at any size."""
    import cv2
    hu = cv2.HuMoments(cv2.moments(cnt)).flatten()
    return [float(-math.copysign(1.0, h) * math.log10(abs(h))) if h else 0.0 for h in hu]


class ARVision:
    """The camera thread. Shows the PAC AR window, learns objects on request, recognises them again, and runs the
    actions you tied to them. Objects are kept as JSON in ~/.pac/ar_objects.json."""
    FONT = 0

    def __init__(self, app):
        self.app = app
        self.stop = threading.Event()
        self.ready = threading.Event()
        self.lock = threading.RLock()
        self.thread = None
        self.running = False
        self.error = None
        self.cv2 = self.np = None
        self.cap = None
        self.rt = {}                      # key -> {"views": [numpy views], "plain": bool}  (built when the engine runs)
        self.objs = {}                    # key -> {"name","kind","action","views","added"}  (JSON-friendly)
        self.visible = {}                 # key -> when last seen
        self.quads = {}                   # key -> (outline, when, score)
        self.streak = collections.defaultdict(int)
        self.announced = {}
        self.learn_job = None
        self.shape_name, self.shape_last, self.shape_streak = "", "", 0
        self.small_shape = (360, 640)
        self.hud_at, self.hud = 0.0, []
        self.frames = 0
        self.load()

    # ----- storage
    def load(self):
        try:
            self.objs = json.loads(AR_FILE.read_text(encoding="utf-8")).get("objects", {})
        except Exception:
            self.objs = {}

    def save(self):
        with self.lock:
            try:
                tmp = AR_FILE.with_suffix(".tmp")
                tmp.write_text(json.dumps({"objects": self.objs}), encoding="utf-8")
                tmp.replace(AR_FILE)
            except Exception:
                logger.exception("could not save AR objects")

    def _rebuild(self):
        np = self.np
        if np is None:
            return
        rt = {}
        with self.lock:
            for key, o in self.objs.items():
                if o.get("kind") != "object":
                    continue
                views = []
                for v in o.get("views", []):
                    try:
                        d = np.frombuffer(base64.b64decode(v["desc"]), dtype=np.uint8).reshape(-1, 32)
                        views.append({"desc": d, "pts": np.float32(v["pts"]), "size": v["size"], "hu": v.get("hu"),
                                      "n": len(d)})
                    except Exception:
                        continue
                if views:
                    rt[key] = {"views": views, "plain": max(v["n"] for v in views) < 30}
        self.rt = rt

    @staticmethod
    def key_of(display):
        return norm(re.sub(r"^(?:your|my|the|a|an)\s+", "", display.lower())).strip()

    def find_key(self, text):
        """The learned object (or predefined shape) a spoken name refers to, or None."""
        key = self.key_of(text)
        if key in AR_SHAPES or key in AR_PRESETS:
            return "shape:" + key
        with self.lock:
            if key in self.objs:
                return key
            close = difflib.get_close_matches(key, [k for k in self.objs if not k.startswith("shape:")], n=1, cutoff=0.75)
        return close[0] if close else None

    def set_action(self, key, action, name=None, kind="object"):
        with self.lock:
            o = self.objs.get(key)
            if o is None:
                if kind != "shape":
                    return False
                o = self.objs[key] = {"name": name or key.split(":")[-1], "kind": "shape", "action": "", "views": [],
                                      "added": datetime.date.today().isoformat()}
            o["action"] = (action or "").strip()
            if o["kind"] == "shape" and not o["action"]:
                del self.objs[key]
            self.save()
        return True

    def remove(self, key):
        with self.lock:
            gone = self.objs.pop(key, None)
            self.visible.pop(key, None)
            self.save()
        self._rebuild()
        return gone is not None

    def remove_all(self):
        with self.lock:
            n = len(self.objs)
            self.objs, self.visible = {}, {}
            self.save()
        self._rebuild()
        return n

    def starter_pack(self):
        n = 0
        for shape, cmd in AR_STARTER.items():
            if "shape:" + shape not in self.objs:
                self.set_action("shape:" + shape, cmd, name=shape, kind="shape")
                n += 1
        return n

    def entries(self):
        with self.lock:
            return [(k, o["name"], o.get("kind", "object"), o.get("action", ""), len(o.get("views", [])))
                    for k, o in self.objs.items()]

    def what_now(self):
        with self.lock:
            names = [self.objs[k]["name"] for k in self.visible if k in self.objs and not k.startswith("shape:")]
        return names, self.shape_name

    # ----- start / stop
    def start(self):
        if self.running or (self.thread and self.thread.is_alive() and not self.stop.is_set()):
            return
        if self.thread and self.thread.is_alive():
            self.thread.join(3)
        self.stop.clear()
        self.ready.clear()
        self.error = None
        self.frames = 0
        self.thread = threading.Thread(target=self._run, daemon=True, name="pac-ar")
        self.thread.start()

    def stop_engine(self):
        self.stop.set()

    def _fail(self, msg):
        self.error = msg
        self.running = False
        self.ready.set()
        self.app.ui("ar_error", msg)

    # ----- camera
    def _open_camera(self):
        cv2, np = self.cv2, self.np
        if self.app.gesture.running:                         # gesture control already holds the camera: share its pictures
            shared = SharedCamera(lambda: getattr(self.app.gesture, "hand_source", None))
            end = time.time() + 3
            while time.time() < end:
                ok, _f = shared.read()
                if ok:
                    self.cap = shared
                    return
            raise ARError("Gesture control has the camera and isn't sending pictures yet. Try again in a moment.")
        want = self.app.cfg.get("ar_cam", "auto")
        cands = [int(want)] if want != "auto" else list(range(4))
        grey, tried = None, []
        for i in cands:
            cap, frame, info = open_camera_any(cv2, i, size=(1280, 720))
            if cap is None:
                if info:
                    tried.append(f"camera {i}: {info}")
                continue
            ir = frame.ndim == 2 or float(np.abs(frame[::8, ::8, 0].astype(np.int16)
                                                 - frame[::8, ::8, 2].astype(np.int16)).mean()) < 3.0
            if ir:                                            # an infrared camera shows no colour: prefer a normal webcam
                if grey is None:
                    grey = cap
                else:
                    cap.release()
                continue
            if grey is not None:
                grey.release()
            self.cap = cap
            return
        if grey is not None:
            self.cap = grey
            return
        raise ARError("Couldn't open a camera for AR." + ("\n" + "\n".join(tried) if tried else "") +
                      "\nClose other apps using the camera, and check Settings > Privacy & security > Camera. "
                      "Menu > Faces > Find cameras shows what PAC can see.")

    def _grab(self):
        ok, frame = self.cap.read()
        if not ok or frame is None:
            self.fails += 1
            if self.fails > 40:
                raise ARError("The camera stopped sending pictures (unplugged, or taken by another app).")
            time.sleep(0.05)
            return None
        self.fails = 0
        if frame.ndim == 2:
            frame = self.cv2.cvtColor(frame, self.cv2.COLOR_GRAY2BGR)
        return frame

    # ----- the loop
    def _run(self):
        try:
            import cv2
            import numpy as np
        except Exception as e:
            self._fail(f"Augmented reality needs opencv-python ({e}).\nInstall it with:  {face_install_command()}")
            return
        self.cv2, self.np = cv2, np
        self.fails = 0
        try:
            self.orb = cv2.ORB_create(nfeatures=900, fastThreshold=12)
            self.orb_learn = cv2.ORB_create(nfeatures=500, fastThreshold=10)
            self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
            self._rebuild()
            self._open_camera()
        except ARError as e:
            self._fail(str(e))
            return
        except Exception as e:
            logger.exception("AR could not start")
            self._fail(f"AR couldn't start: {e}")
            return
        self.running = True
        self.ready.set()
        self.app.ui("ar_state", True)
        self.app.ui("log", "sys", "AR is on. In the PAC AR window: press L to teach it an object, Esc to close.")
        last_scan, shown = 0.0, 0
        try:
            cv2.namedWindow(AR_WIN, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(AR_WIN, 960, 540)
            try:
                cv2.setWindowProperty(AR_WIN, cv2.WND_PROP_TOPMOST, 1)
            except Exception:
                pass
            while not self.stop.is_set():
                frame = self._grab()
                if frame is None:
                    continue
                self.frames += 1
                now = time.time()
                if now - last_scan >= 0.18:
                    last_scan = now
                    try:
                        self._scan(frame, now)
                    except Exception:
                        logger.exception("AR scan failed")
                cv2.imshow(AR_WIN, self._draw(frame.copy(), now))
                key = cv2.waitKey(1) & 0xFF
                shown += 1
                if key in (27, ord("q")):
                    break
                if key in (ord("l"), ord("L")):
                    self.app.ui("ar_learn_prompt")
                if shown > 10:
                    try:
                        if cv2.getWindowProperty(AR_WIN, cv2.WND_PROP_VISIBLE) < 1:
                            break                              # the window's close button
                    except Exception:
                        break
        except ARError as e:
            self.app.ui("ar_error", str(e))
        except Exception as e:
            logger.exception("AR crashed")
            self.app.ui("ar_error", f"AR stopped: {e}")
        finally:
            try:
                cv2.destroyWindow(AR_WIN)
                cv2.waitKey(1)
            except Exception:
                pass
            try:
                if self.cap is not None:
                    self.cap.release()
            except Exception:
                pass
            self.cap = None
            self.running = False
            self.ready.clear()
            self.visible = {}
            self.app.ui("ar_state", False)

    # ----- learning
    def _box(self, shape):
        h, w = shape[:2]
        return int(w * AR_BOX[0]), int(h * AR_BOX[1]), int(w * AR_BOX[2]), int(h * AR_BOX[3])

    def learn(self, display, key, timeout=30):
        """Look at what is inside the guide box from a few moments and remember it. -> (ok, message to say)."""
        self.start()
        if not self.ready.wait(25) or self.error or not self.running:
            return False, self.error or "The camera didn't start."
        job = {"name": display, "views": [], "need": 5, "last": 0.0, "done": threading.Event(), "t0": time.time()}
        self.learn_job = job
        try:
            job["done"].wait(timeout)
        finally:
            self.learn_job = None
        views = job["views"]
        if len(views) < 3:
            return False, ("I couldn't get a clear look at it. Hold it inside the box, fairly close, in good light, "
                           "and turn it slowly while I look.")
        with self.lock:
            o = self.objs.setdefault(key, {"name": display, "kind": "object", "action": "", "views": [],
                                           "added": datetime.date.today().isoformat()})
            o["views"] = (o.get("views", []) + views)[-8:]
            self.save()
        self._rebuild()
        plain = self.rt.get(key, {}).get("plain")
        msg = f"I've learned {display} from {len(views)} angles."
        if plain:
            msg += " It has few details, so I'll recognise it by its outline: hold it inside the box when you show it."
        else:
            msg += " I'll know it when I see it again, anywhere in view."
        return True, msg

    def _learn_step(self, gray, now):
        job = self.learn_job
        if job is None or now - job["last"] < 0.55:
            return
        job["last"] = now
        cv2, np = self.cv2, self.np
        x1, y1, x2, y2 = self._box(gray.shape)
        roi = gray[y1:y2, x1:x2]
        kps, des = self.orb_learn.detectAndCompute(roi, None)
        cnt = ar_main_contour(roi)
        hu = ar_hu(cnt) if cnt is not None else None
        if (des is None or len(kps) < 12) and hu is None:
            return
        n = len(kps) if des is not None else 0
        if des is None:
            des, kps = np.zeros((0, 32), np.uint8), []
        job["views"].append({"desc": base64.b64encode(des.tobytes()).decode("ascii"),
                             "pts": [[round(float(k.pt[0]), 1), round(float(k.pt[1]), 1)] for k in kps],
                             "size": [roi.shape[1], roi.shape[0]], "hu": hu, "n": n})
        if len(job["views"]) >= job["need"]:
            job["done"].set()

    # ----- recognising
    def _match(self, v, des, pts_all):
        cv2, np = self.cv2, self.np
        if len(des) < 2 or len(v["desc"]) < 8:
            return None
        pairs = self.bf.knnMatch(v["desc"], des, k=2)
        good = [p[0] for p in pairs if len(p) == 2 and p[0].distance < 0.75 * p[1].distance]
        need = int(self.app.cfg.get("ar_min_matches", 12))
        if len(good) < need:
            return None
        src = v["pts"][[m.queryIdx for m in good]].reshape(-1, 1, 2)
        dst = pts_all[[m.trainIdx for m in good]].reshape(-1, 1, 2)
        H, mask = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
        if H is None or mask is None:
            return None
        inl = int(mask.sum())
        if inl < max(9, need - 2):
            return None
        w, h = v["size"]
        quad = cv2.perspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2), H)
        quad = quad.reshape(-1, 2).astype(np.float32)
        if not cv2.isContourConvex(quad.reshape(-1, 1, 2)):
            return None
        area = cv2.contourArea(quad)
        fh, fw = self.small_shape
        if area < 0.003 * fw * fh or area > 0.9 * fw * fh:
            return None
        return inl, quad

    def _scan(self, frame, now):
        cv2, np = self.cv2, self.np
        h, w = frame.shape[:2]
        scale = min(1.0, 640.0 / w)
        small = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA) if scale < 1 else frame
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        self.small_shape = gray.shape
        if self.learn_job is not None:
            self._learn_step(gray, now)
            return
        inv = 1.0 / scale
        found = {}
        # 1. learned objects, anywhere in the picture
        if any(not o["plain"] for o in self.rt.values()):
            kps, des = self.orb.detectAndCompute(gray, None)
            if des is not None and len(kps) >= 15:
                pts_all = np.float32([k.pt for k in kps])
                for key, o in list(self.rt.items()):
                    if o["plain"]:
                        continue
                    best = None
                    for v in o["views"]:
                        r = self._match(v, des, pts_all)
                        if r and (best is None or r[0] > best[0]):
                            best = r
                    if best:
                        found[key] = (best[0], best[1] * inv)
        # 2. the guide box: predefined shapes, and plain objects known by their outline
        x1, y1, x2, y2 = self._box(gray.shape)
        box_quad = np.float32([[x1, y1], [x2, y1], [x2, y2], [x1, y2]]) * inv
        cnt = ar_main_contour(gray[y1:y2, x1:x2])
        name = ar_shape_of(cnt) if cnt is not None else None
        hu = ar_hu(cnt) if cnt is not None else None
        # everyday things known by their proportions (a learned object found by looks always wins over a guess)
        loose = ar_main_contour(gray[y1:y2, x1:x2], 0.015)
        guess = ar_preset_of(loose, (x2 - x1) * (y2 - y1)) if loose is not None else None
        if guess and not any(k in found for k in self.rt) and "shape:" + guess not in self.objs:
            name = guess
        elif guess and "shape:" + guess in self.objs and not any(k in found for k in self.rt):
            name = guess
        self.shape_name = name or ""
        if name and name == self.shape_last:
            self.shape_streak += 1
        else:
            self.shape_streak = 1 if name else 0
        self.shape_last = name or ""
        skey = "shape:" + (name or "")
        if self.shape_streak >= 4 and (skey in self.objs or name in AR_PRESETS):
            found[skey] = (1, box_quad)
        if hu:
            for key, o in list(self.rt.items()):
                if not o["plain"]:
                    continue
                dists = [sum(abs(a - b) for a, b in zip(hu[:5], v["hu"][:5])) / 5 for v in o["views"] if v.get("hu")]
                if dists and min(dists) < 0.3:
                    found[key] = (0, box_quad)
        with self.lock:
            for key, (score, quad) in found.items():
                self.streak[key] += 1
                self.quads[key] = (quad, now, score)
                if self.streak[key] >= 3:
                    new = key not in self.visible
                    self.visible[key] = now
                    if new:
                        self._seen(key, now)
            for key in list(self.streak):
                if key not in found:
                    self.streak[key] = 0
            for key, t in list(self.visible.items()):
                if now - t > 1.5:
                    del self.visible[key]

    def _seen(self, key, now):
        o = self.objs.get(key)
        if o is None and key.startswith("shape:") and key[6:] in AR_PRESETS:
            o = {"name": key[6:], "kind": "preset", "action": ""}
        if not o or now - self.announced.get(key, 0.0) < 20:
            return
        self.announced[key] = now
        a, action = self.app.assistant, (o.get("action") or "").strip()
        self.app.ui("log", "sys", f"(AR: I can see {o['name']})" if o["kind"] != "preset"
                    else f"(AR: that looks like a {o['name']})")
        if action.lower().startswith("say "):
            a.say(action[4:].strip(), plain=True)
            return
        if o.get("kind") == "object" and self.app.cfg.get("ar_announce", True):
            a.say(f"I can see {o['name']}.")
        elif o.get("kind") == "preset" and self.app.cfg.get("ar_announce", True):
            a.say(f"That looks like a {o['name']}.")
        if action:
            self.app.submit(action)

    # ----- drawing
    def _label(self, img, text, org, color=AR_PALE, scale=0.55):
        cv2 = self.cv2
        (tw, th), _ = cv2.getTextSize(text, self.FONT, scale, 1)
        x = max(4, min(org[0], img.shape[1] - tw - 8))
        y = max(th + 8, min(org[1], img.shape[0] - 6))
        cv2.rectangle(img, (x - 4, y - th - 6), (x + tw + 4, y + 4), (0, 0, 0), -1)
        cv2.putText(img, text, (x, y), self.FONT, scale, color, 1, cv2.LINE_AA)

    def _hud_lines(self, now):
        if now - self.hud_at < 5:
            return self.hud
        self.hud_at = now
        lines = [time.strftime("%I:%M %p").lstrip("0") + "   " + time.strftime("%a %d %b")]
        try:
            b = psutil.sensors_battery()
            if b is not None:
                lines.append(f"Battery {int(b.percent)}%" + (" (charging)" if b.power_plugged else ""))
        except Exception:
            pass
        try:
            hint = self.app.assistant._next_class_hint()
            if hint:
                lines.append(hint)
        except Exception:
            pass
        self.hud = lines
        return lines

    def _draw(self, img, now):
        cv2, np = self.cv2, self.np
        h, w = img.shape[:2]
        # the guide box: four corner brackets
        x1, y1, x2, y2 = int(w * AR_BOX[0]), int(h * AR_BOX[1]), int(w * AR_BOX[2]), int(h * AR_BOX[3])
        arm = int(min(x2 - x1, y2 - y1) * 0.12)
        for (cx, cy, dx, dy) in ((x1, y1, 1, 1), (x2, y1, -1, 1), (x1, y2, 1, -1), (x2, y2, -1, -1)):
            cv2.line(img, (cx, cy), (cx + dx * arm, cy), AR_BLUE, 2, cv2.LINE_AA)
            cv2.line(img, (cx, cy), (cx, cy + dy * arm), AR_BLUE, 2, cv2.LINE_AA)
        if self.shape_name:
            self._label(img, ("looks like: " if self.shape_name in AR_PRESETS else "shape: ") + self.shape_name,
                        (x1, y2 + 22), AR_BLUE)
        # recognised objects
        with self.lock:
            for key in list(self.visible):
                o, q = self.objs.get(key), self.quads.get(key)
                if not o or not q or now - q[1] > 1.0:
                    continue
                poly = q[0].astype(np.int32).reshape(-1, 1, 2)
                cv2.polylines(img, [poly], True, AR_BLUE, 3, cv2.LINE_AA)
                top = poly.reshape(-1, 2)[:, 1].argmin()
                px, py = poly.reshape(-1, 2)[top]
                self._label(img, o["name"], (int(px), int(py) - 10), (255, 255, 255), 0.7)
                if o.get("action"):
                    self._label(img, "-> " + o["action"], (int(px), int(py) + 18), AR_PALE, 0.5)
        # your hands, when gesture control is running too
        lat = self.app.gesture.latest if self.app.gesture.running else {}
        if lat and now - lat.get("t", 0) < 0.5:
            for hand in lat.get("hands") or []:
                pts = hand.get("pts")
                if pts:
                    P = [(int((1 - x) * w), int(y * h)) for x, y in pts]
                    for a, b in HAND_LINES:
                        cv2.line(img, P[a], P[b], AR_PALE, 1, cv2.LINE_AA)
                    if hand.get("gid"):
                        self._label(img, gesture_title(self.app.cfg, hand["gid"]), (P[0][0], P[0][1] + 24), AR_PALE, 0.5)
        # learning progress
        job = self.learn_job
        if job is not None:
            frac = len(job["views"]) / job["need"]
            cv2.rectangle(img, (x1, y1 - 18), (x2, y1 - 8), (40, 40, 40), -1)
            cv2.rectangle(img, (x1, y1 - 18), (x1 + int((x2 - x1) * frac), y1 - 8), AR_BLUE, -1)
            self._label(img, f"Learning {job['name']} - turn it slowly", (x1, y1 - 26), (255, 255, 255), 0.6)
        else:
            self._label(img, "Hold an object here.  L = learn it   Esc = close", (x1, y1 - 12), AR_PALE, 0.5)
        # info panel
        if self.app.cfg.get("ar_hud", True):
            for i, line in enumerate(self._hud_lines(now)):
                self._label(img, line, (12, 28 + 26 * i), AR_PALE, 0.6)
        return img


class Orb:
    """The voice display: a blue wireframe sphere whose surface ripples and swells with the sound,
    ringed by drifting specks. Pure tkinter canvas drawing - no extra packages."""

    NL, NP = 13, 36      # latitude rings, points per ring
    NM, NQ = 20, 28      # meridians, points per meridian

    def __init__(self, bg, deep, bright):
        self.t = 0.0
        self.rot = 0.0
        self.bg, self.deep = bg, deep
        self.shades = [mix(deep, bright, i / 7.0) for i in range(8)]
        two_pi = 2 * math.pi
        self.rings = []
        for i in range(1, self.NL + 1):
            th = math.pi * i / (self.NL + 1)
            s, c = math.sin(th), math.cos(th)
            self.rings.append([(s * math.cos(two_pi * j / self.NP), c, s * math.sin(two_pi * j / self.NP))
                               for j in range(self.NP + 1)])
        self.meridians = []
        for k in range(self.NM):
            ph = two_pi * k / self.NM
            cp, sp = math.cos(ph), math.sin(ph)
            self.meridians.append([(math.sin(math.pi * j / self.NQ) * cp, math.cos(math.pi * j / self.NQ),
                                    math.sin(math.pi * j / self.NQ) * sp) for j in range(self.NQ + 1)])
        rnd = random.Random(11)
        self.dust = []
        for _ in range(120):
            z, a = rnd.uniform(-1, 1), rnd.uniform(0, two_pi)
            r = math.sqrt(1 - z * z)
            self.dust.append((r * math.cos(a), z, r * math.sin(a), rnd.uniform(1.1, 1.6), rnd.random()))

    def draw(self, cv, cx, cy, R, level, dt):
        self.t += dt * (0.7 + 2.4 * level)
        self.rot += dt * 0.32
        t, sin, cos = self.t, math.sin, math.cos
        amp = 0.05 + 0.36 * level              # how much the surface ripples
        grow = 1.0 + 0.12 * level              # how much the whole orb swells
        cr, sr = cos(self.rot), sin(self.rot)
        ct, st = cos(0.5), sin(0.5)            # tilted a little toward the viewer
        f = 4.2                                # perspective
        shades = self.shades
        buckets = [[] for _ in shades]

        for scale, a in ((1.38, 0.05), (1.24, 0.09), (1.12, 0.14)):          # soft halo
            g = R * scale * (1 + 0.05 * level)
            cv.create_oval(cx - g, cy - g, cx + g, cy + g, outline="",
                           fill=mix(self.bg, self.deep, min(1.0, a + 0.3 * level)))

        def emit(line):
            run, cur, first = [], 0, True
            for ux, uy, uz in line:
                x1 = ux * cr + uz * sr                      # spin, then tilt
                z1 = uz * cr - ux * sr
                y2 = uy * ct - z1 * st
                z2 = uy * st + z1 * ct
                k = grow * (1.0 + amp * (0.55 * sin(2.1 * ux + 1.3 * t + 1.7 * uy)
                                         + 0.30 * sin(3.3 * uy - 1.1 * t + 2.3 * uz)
                                         + 0.15 * sin(5.1 * uz + 1.9 * t + 3.1 * ux)))
                s = f / (f - z2 * k)
                # brighter where the surface faces us, plus a glow on the lower right rim
                b = (0.12 + 0.55 * (z2 if z2 > 0 else 0.0) ** 1.3
                     + 0.55 * max(0.0, 0.6 * x1 - 0.8 * y2) * (1 - abs(z2)) ** 1.5 + 0.18 * level)
                i = min(7, int(max(0.0, b) * 7.99))
                x, y = cx + x1 * k * R * s, cy - y2 * k * R * s
                if first:
                    run, cur, first = [x, y], i, False
                    continue
                run += (x, y)
                if i != cur:                                 # brightness changed: close this stretch of line
                    if len(run) >= 4:
                        buckets[cur].append(run)
                    run, cur = [x, y], i
            if len(run) >= 4:
                buckets[cur].append(run)

        for ring in self.rings:
            emit(ring)
        for mer in self.meridians:
            emit(mer)
        for i, runs in enumerate(buckets):                   # dim lines first so bright ones sit on top
            for run in runs:
                cv.create_line(*run, fill=shades[i], width=2 if i >= 6 else 1)

        spin = self.rot * 0.6
        c2, s2 = cos(spin), sin(spin)
        for ux, uy, uz, rad, ph in self.dust:               # the drifting specks around it
            x = ux * c2 + uz * s2
            z = uz * c2 - ux * s2
            y, z = uy * ct - z * st, uy * st + z * ct
            r = rad * (1 + 0.28 * level * (0.4 + ph))
            s = f / (f - z * r)
            tw = 0.35 + 0.65 * abs(sin(t * 0.9 + ph * 6.28))
            idx = int(min(7, max(0.0, (0.25 + 0.25 * (z + 1)) * tw * 9)))
            px, py = cx + x * r * R * s, cy - y * r * R * s
            sz = 1.8 if z > 0 else 1.0
            cv.create_rectangle(px, py, px + sz, py + sz, fill=shades[idx], outline="")


LANGS = [("en-IN", "English (India)"), ("en-US", "English (US)"),
         ("en-GB", "English (UK)"), ("en-AU", "English (Australia)")]


class PacApp:
    # Strictly black and blue: pure black is the canvas, every other tone is a blue. (The RED_* names are kept from the old red theme.)
    BG = "#000000"
    RED = "#1a8cff"          # accents, active menu rows, the recorder at full volume
    RED_TEXT = "#45a5ff"     # text you read
    RED_MID = "#1670c8"
    RED_DIM = "#14518c"      # secondary text
    RED_DEEP = "#07264a"     # hairlines and the quietest bars

    def __init__(self, root):
        import tkinter as tk
        import tkinter.font as tkfont
        self.tk = tk
        self.root = root
        fams = set(tkfont.families(root))
        pick = lambda *names: next((n for n in names if n in fams), names[-1])
        self.F = pick("Bahnschrift", "Segoe UI", "Helvetica Neue", "DejaVu Sans", "Helvetica")
        self.FM = pick("Consolas", "Menlo", "DejaVu Sans Mono", "Courier")
        self.cfg = load_config()
        install_knowledge_pack(self.cfg)
        self.ui_q = queue.Queue()
        self.cmd_q = queue.Queue()
        self.mic_on = True
        self.voice_ok = VOICE_LIBS_OK
        self.mode = "voice" if (self.cfg.get("mode") == "voice" and self.voice_ok) else "text"
        self.level_target = 0.0     # written by the Listener thread
        self.level_time = 0.0
        self.level_shown = 0.0
        self.orb = Orb(self.BG, self.RED_DEEP, self.RED_TEXT)
        self.last_frame = time.time()
        self.pulse = 0.0                     # brief flash of the orb when a clap / whistle is heard
        self.trigger_mic_failed = False
        self.heard_text, self.heard_until = "", 0.0
        self.speaker = Speaker(self.cfg, on_info=lambda s: self.ui("log", "sys", s))
        self.speaker.on_voice = lambda code: self.ui("voice_changed", code)
        self.assistant = Assistant(self.cfg, self.speaker.say, lambda w, t: self.ui("log", w, t),
                                   notify=self.on_assistant_notify, request_quit=lambda: self.ui("quit"),
                                   speaker=self.speaker)
        self.listener = Listener(self)
        self.gesture = GestureEngine(self)
        self.faces = FaceEngine(self)
        self.assistant.faces = self.faces
        self.ar = ARVision(self)
        self.assistant.ar = self.ar
        self.build_ui()
        threading.Thread(target=self._cmd_worker, daemon=True).start()
        threading.Thread(target=self.assistant.build_app_index, daemon=True).start()
        threading.Thread(target=lambda: self.ui("autostart_state", autostart_enabled()), daemon=True).start()
        self.listener.start()
        if self.cfg.get("gesture_enabled"):
            self.root.after(1500, self.gesture.start)
        if self.cfg.get("face_enabled"):
            self.root.after(3000, self.faces.start)
        if self.cfg.get("ar_enabled"):
            self.root.after(3500, self.ar.start)           # after the gesture camera has had its turn
        if self.cfg.get("start_minimized"):
            self.root.after(400, self.root.iconify)
        if self.mode == "voice":
            self.ui("log", "sys", "Voice mode: just speak. Checking the connection to Google's speech service...")
            threading.Thread(target=self._verify_online, daemon=True).start()
        else:
            if self.cfg.get("mode") == "voice" and not self.voice_ok:
                self.ui("log", "sys", "Voice mode needs: pip install SpeechRecognition sounddevice. "
                                      "Starting in Text mode, which needs neither.")
            self.ui("log", "sys", "Text mode: type a command below. Speech recognition is off, so PAC runs offline" + (
                " - except that a question I can't answer from your facts is looked up quietly on the web "
                "(switch that off under Menu > Assistant)." if self.cfg.get("background_search", True) else "."))
        if not self.cfg.get("autostart_setup_done"):
            self.cfg["autostart_setup_done"] = True
            save_config(self.cfg)

            def setup():
                self.ui("log", "sys", make_autostart(True))
                self.ui("autostart_state", autostart_enabled())
            threading.Thread(target=setup, daemon=True).start()
        self.root.after(100, self.poll)
        self.root.after(40, self.animate)
        self.root.after(800, self.first_words)
        self.root.after(30000, self.morning_check)

    def ui(self, *event):
        self.ui_q.put(event)

    def first_words(self):
        """At launch: inside 5:30-8:00 AM run the wake-up routine, otherwise the normal greeting."""
        if self.morning_due():
            self.append("sys", "Good-morning routine (5:30 - 8:00 AM): wake up, schedule, headlines.")
            self.assistant.wake_home()
        else:
            self.assistant.say(self.assistant.startup_greeting())

    # ---------- automatic "wake up daddy is home" between 5:30 and 8:00 AM
    @staticmethod
    def _hhmm(text, default):
        try:
            h, m = str(text).split(":")
            return int(h) * 60 + int(m)
        except Exception:
            return default

    def morning_due(self):
        """True when the auto routine is on, it is inside the window, and it hasn't run yet today."""
        if not self.cfg.get("auto_home", True):
            return False
        now = datetime.datetime.now()
        mins = now.hour * 60 + now.minute
        lo = self._hhmm(self.cfg.get("auto_home_start", "05:30"), 330)
        hi = self._hhmm(self.cfg.get("auto_home_end", "08:00"), 480)
        return lo <= mins < hi and self.cfg.get("auto_home_date") != datetime.date.today().isoformat()

    def morning_check(self):
        try:
            if self.morning_due():
                self.append("sys", "Good-morning routine (5:30 - 8:00 AM): wake up, schedule, headlines.")
                self.assistant.wake_home()
        except Exception:
            logger.exception("morning routine failed")
        self.root.after(30000, self.morning_check)       # look again every 30 seconds

    def on_assistant_notify(self, kind, value):
        if kind == "mode":                       # "voice mode" / "text mode" said or typed to PAC
            self.ui("set_mode", value)
        elif kind == "timetable_edit":
            self.ui("timetable_edit")
        elif kind == "timetable_import":
            self.ui("timetable_import")
        elif kind == "gesture":
            self.ui("gesture_cmd", value)
        elif kind == "airdrag":
            self.ui("airdrag_cmd", value)
        elif kind == "face":
            self.ui("face_cmd", value)
        elif kind == "ar":
            self.ui("ar_cmd", value)
        elif kind == "face_security":
            self.ui("face_security", value)
        elif kind == "submit":
            self.ui("submit", value)
        elif kind == "claude":
            self.ui("claude_state", value)
        elif kind == "claude_setup":
            self.ui("claude_setup")
        elif kind == "memory_edit":
            self.ui("memory_edit")
        elif kind == "memory_state":
            self.ui("memory_state", value)

    def recognition_wanted(self):
        """Voice mode with a working microphone switch: speech goes to Google."""
        return self.mode == "voice" and self.voice_ok and self.mic_on

    def capture_wanted(self):
        """The microphone is open - for voice recognition and/or the clap / whistle triggers."""
        return (sd is not None and self.mic_on
                and (self.recognition_wanted()
                     or (bool(self.cfg.get("sound_triggers", True)) and not self.trigger_mic_failed)))

    def _verify_online(self):
        if not internet_ok():
            self.ui("voice_offline", "no internet connection")

    # ----- layout
    def build_ui(self):
        tk, r = self.tk, self.root
        r.title("PAC")
        sw, sh = r.winfo_screenwidth(), r.winfo_screenheight()
        r.geometry(f"{min(780, sw - 60)}x{min(740, sh - 90)}")
        r.minsize(520, 440)
        r.configure(bg=self.BG)
        make_icon(ICON_FILE)
        try:
            r.iconbitmap(default=str(ICON_FILE))
        except Exception:
            pass

        # top bar: the name on the left, the one menu that holds every feature on the right
        top = tk.Frame(r, bg=self.BG)
        top.pack(fill="x", padx=20, pady=(16, 0))
        tk.Label(top, text="PAC", font=(self.F, 24, "bold"), fg=self.RED, bg=self.BG).pack(side="left")
        self.menu_btn = tk.Menubutton(top, text="Menu  \u25be", font=(self.F, 11, "bold"), bg=self.RED,
                                      fg=self.BG, activebackground=self.RED_TEXT, activeforeground=self.BG,
                                      relief="flat", bd=0, padx=18, pady=7, cursor="hand2", direction="below")
        self.menu_btn.pack(side="right")
        self.build_menu()

        strip = tk.Frame(r, bg=self.BG)
        strip.pack(fill="x", padx=20, pady=(10, 0))
        self.badge = tk.Label(strip, font=(self.F, 9, "bold"), padx=9, pady=2, bd=0, highlightthickness=1)
        self.badge.pack(side="left")
        self.status = tk.Label(strip, font=(self.F, 10), fg=self.RED_DIM, bg=self.BG, anchor="w")
        self.status.pack(side="left", padx=12)

        # the voice orb: a blue wireframe sphere that ripples and swells with your voice
        self.cv = tk.Canvas(r, height=max(200, min(290, int(sh * 0.30))), bg=self.BG, highlightthickness=0, bd=0)
        self.cv.pack(fill="x", padx=20, pady=(6, 0))
        self.live = tk.Label(r, text="", font=(self.F, 10, "italic"), fg=self.RED_DIM, bg=self.BG,
                             anchor="w", justify="left")
        self.live.pack(fill="x", padx=22, pady=(6, 0))

        # footer, then the entry row: both packed before the chat so they can never be squeezed off a small screen
        self.footer = tk.Label(r, text=FOOTER_TEXT, font=(self.F, 9), fg=self.RED_DIM, bg=self.BG)
        self.footer.pack(side="bottom", pady=(0, 10))
        row = tk.Frame(r, bg=self.BG)
        row.pack(side="bottom", fill="x", padx=20, pady=(0, 6))
        tk.Label(row, text=">", font=(self.FM, 14, "bold"), fg=self.RED, bg=self.BG).pack(side="left", padx=(0, 8))
        self.entry = tk.Entry(row, font=(self.F, 12), bg=self.BG, fg=self.RED_TEXT, insertbackground=self.RED,
                              relief="flat", bd=0, highlightthickness=1, highlightbackground=self.RED_DEEP,
                              highlightcolor=self.RED, selectbackground=self.RED, selectforeground=self.BG)
        self.entry.pack(side="left", fill="x", expand=True, ipady=9, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.send_entry())
        self.entry.focus_set()
        self.mkbtn(row, "Send", self.send_entry).pack(side="right", ipady=3)

        box = tk.Frame(r, bg=self.RED_DEEP, padx=1, pady=1)
        box.pack(fill="both", expand=True, padx=20, pady=(8, 12))
        inner = tk.Frame(box, bg=self.BG)
        inner.pack(fill="both", expand=True)
        self.chat = tk.Text(inner, wrap="word", bg=self.BG, fg=self.RED_TEXT, font=(self.F, 11), relief="flat",
                            padx=12, pady=10, state="disabled", cursor="arrow", spacing3=6, bd=0,
                            highlightthickness=0, selectbackground=self.RED, selectforeground=self.BG)
        sb = tk.Scrollbar(inner, command=self.chat.yview, bg=self.RED_DEEP, troughcolor=self.BG,
                          activebackground=self.RED, relief="flat", bd=0, width=10)
        self.chat.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.chat.pack(side="left", fill="both", expand=True)
        self.chat.tag_config("you_label", foreground=self.RED, font=(self.F, 10, "bold"))
        self.chat.tag_config("pac_label", foreground=self.RED_MID, font=(self.F, 10, "bold"))
        self.chat.tag_config("you", foreground=self.RED_TEXT)
        self.chat.tag_config("pac", foreground=self.RED)
        self.chat.tag_config("sys", foreground=self.RED_DIM, font=(self.F, 10, "italic"))
        self.chat.tag_config("list", foreground=self.RED_TEXT, font=(self.FM, 11), lmargin1=12, lmargin2=12)

        r.protocol("WM_DELETE_WINDOW", self.on_close)
        r.bind("<Escape>", lambda e: self.assistant.stop_speaking())
        self.refresh_badge()

    def build_menu(self):
        """One dropdown holds every feature. Its sub-menus overlay the window, so nothing ever
        takes up space or gets pushed off a small screen."""
        tk = self.tk

        def mk(parent):
            return tk.Menu(parent, tearoff=False, bg=self.BG, fg=self.RED_TEXT, activebackground=self.RED,
                           activeforeground=self.BG, disabledforeground=self.RED_DEEP, selectcolor=self.RED_TEXT,
                           bd=1, relief="flat", font=(self.F, 10))

        def sub(parent, label):
            m = mk(parent)
            parent.add_cascade(label=label, menu=m)
            return m

        menu = mk(self.menu_btn)
        self.menu_btn.configure(menu=menu)

        # --- Mode
        self.mode_var = tk.StringVar(value=self.mode)
        m = sub(menu, "Mode")
        m.add_radiobutton(label="Voice  (Google speech, needs internet)", variable=self.mode_var, value="voice",
                          command=lambda: self.set_mode("voice"))
        m.add_radiobutton(label="Text  (type only, works offline)", variable=self.mode_var, value="text",
                          command=lambda: self.set_mode("text"))

        # --- Voice input
        v = sub(menu, "Voice input")
        self.mic_var = tk.BooleanVar(value=True)
        v.add_checkbutton(label="Microphone on", variable=self.mic_var, command=self.toggle_mic)
        dev = sub(v, "Input device")
        self.mic_items = list_mics()
        cur = self.cfg.get("mic")
        self.dev_var = tk.StringVar(value="default" if cur is None else str(cur))
        for label, idx in self.mic_items:
            dev.add_radiobutton(label=label, variable=self.dev_var, value="default" if idx is None else str(idx),
                                command=lambda i=idx, l=label: self.pick_mic(i, l))
        self.auto_var = tk.BooleanVar(value=bool(self.cfg.get("auto_gain", True)))
        v.add_checkbutton(label="Auto boost", variable=self.auto_var, command=self.toggle_autogain)
        boost = sub(v, "Boost level")
        self.gain_var = tk.StringVar(value="")
        for g in (1, 1.5, 2, 3, 4, 6, 8):
            boost.add_radiobutton(label=f"{g}x", variable=self.gain_var, value=str(g),
                                  command=lambda g=g: self.set_gain(g))
        spd = sub(v, "Reaction speed")
        self.vspeed_var = tk.StringVar(value=self.cfg.get("voice_speed", "fast"))
        for key, label in (("fast", "Fast (sends as soon as you stop) - default"),
                           ("balanced", "Balanced (allows short pauses)"),
                           ("careful", "Careful (waits for long pauses)")):
            spd.add_radiobutton(label=label, variable=self.vspeed_var, value=key,
                                command=lambda k=key: self.set_voice_speed(k))
        self.vint_var = tk.BooleanVar(value=bool(self.cfg.get("voice_interrupt", True)))
        v.add_checkbutton(label="Say \"stop\" while PAC is talking", variable=self.vint_var,
                          command=self.toggle_vint)
        isens = sub(v, "Stop-word sensitivity")
        self.visens_var = tk.StringVar(value=self.cfg.get("voice_interrupt_sens", "medium"))
        for key, label in (("low", "Low (shout over her - fewest false stops)"), ("medium", "Medium"),
                           ("high", "High (quiet voice, headphones)")):
            isens.add_radiobutton(label=label, variable=self.visens_var, value=key,
                                  command=lambda k=key: self.set_vint_sens(k))
        lang = sub(v, "Recognition language")
        self.lang_var = tk.StringVar(value=self.cfg.get("lang", "en-IN"))
        for code, name in LANGS:
            lang.add_radiobutton(label=name, variable=self.lang_var, value=code,
                                 command=lambda c=code: self.set_lang(c))

        # --- Sound triggers
        tg = sub(menu, "Sound triggers")
        self.trig_var = tk.BooleanVar(value=bool(self.cfg.get("sound_triggers", True)))
        tg.add_checkbutton(label="Clap twice to wake PAC, whistle for YouTube", variable=self.trig_var,
                           command=self.toggle_triggers)
        sens = sub(tg, "Sensitivity")
        self.sens_var = tk.StringVar(value=self.cfg.get("trigger_sens", "medium"))
        for key, label in (("low", "Low  (loud claps only)"), ("medium", "Medium"), ("high", "High  (quiet claps)")):
            sens.add_radiobutton(label=label, variable=self.sens_var, value=key, command=lambda k=key: self.set_sens(k))

        # --- Schedule
        sc = sub(menu, "Schedule")
        sc.add_command(label="Today", command=lambda: self.submit("what's my schedule today"))
        sc.add_command(label="Tomorrow", command=lambda: self.submit("what's my schedule tomorrow"))
        sc.add_command(label="Next class", command=lambda: self.submit("next class"))
        sc.add_command(label="Whole week", command=lambda: self.submit("show my whole timetable week"))
        sc.add_separator()
        sc.add_command(label="Edit timetable...", command=self.edit_timetable)
        sc.add_command(label="Import timetable (.csv / .txt)...", command=self.import_timetable)

        # --- Gestures
        gm = sub(menu, "Gestures")
        self.gest_var = tk.BooleanVar(value=bool(self.cfg.get("gesture_enabled")))
        gm.add_checkbutton(label="Gesture control (uses the camera)", variable=self.gest_var,
                           command=self.toggle_gestures)
        self.airdrag_var = tk.BooleanVar(value=False)
        gm.add_checkbutton(label="Air drag & drop (palm moves the mouse)", variable=self.airdrag_var,
                           command=lambda: self.set_air_drag(self.airdrag_var.get()))
        gm.add_command(label="Gesture actions...", command=self.gesture_actions_dialog)
        gm.add_command(label="Teach a new gesture...", command=self.teach_gesture_dialog)
        gm.add_command(label="Delete gestures...", command=self.delete_gestures_dialog)
        gm.add_command(label="Hand view...", command=self.hand_view_window)
        gm.add_command(label="Install gesture packages (camera)...", command=self.install_gesture_packages_ui)
        gm.add_separator()
        hold = sub(gm, "Hold time")
        self.hold_var = tk.StringVar(value=str(self.cfg.get("gesture_hold", 0.35)))
        for secs in (0.2, 0.35, 0.5, 0.7, 1.0):
            hold.add_radiobutton(label=f"{secs} seconds", variable=self.hold_var, value=str(secs),
                                 command=lambda s=secs: self.set_gesture_hold(s))
        cam = sub(gm, "Camera")
        self.cam_var = tk.StringVar(value=str(self.cfg.get("gesture_cam", 0)))
        for i in range(4):
            cam.add_radiobutton(label=f"Camera {i}", variable=self.cam_var, value=str(i),
                                command=lambda i=i: self.set_gesture_cam(i))
        self.gbeep_var = tk.BooleanVar(value=bool(self.cfg.get("gesture_beep", True)))
        gm.add_checkbutton(label="Beep when a gesture fires", variable=self.gbeep_var, command=self.toggle_gbeep)

        # --- Faces
        fm = sub(menu, "Faces")
        self.face_var = tk.BooleanVar(value=bool(self.cfg.get("face_enabled")))
        fm.add_checkbutton(label="Face recognition (uses the camera)", variable=self.face_var, command=self.toggle_faces)
        self.facesec_var = tk.BooleanVar(value=bool(self.cfg.get("face_security")))
        fm.add_checkbutton(label="Face security (lock commands to faces)", variable=self.facesec_var,
                           command=self.toggle_face_security)
        fm.add_separator()
        fm.add_command(label="Enrol a face...", command=self.face_enroll_dialog)
        fm.add_command(label="People & permissions...", command=self.face_people_dialog)
        fm.add_command(label="Who's there?", command=lambda: self.submit("who is there"))
        fm.add_separator()
        fcam = sub(fm, "Camera")
        self.fcam_var = tk.StringVar(value=str(self.cfg.get("face_cam", "auto")))
        fcam.add_radiobutton(label="Automatic (prefers infrared)", variable=self.fcam_var, value="auto",
                             command=lambda: self.set_face_cam("auto"))
        for i in range(4):
            fcam.add_radiobutton(label=f"Camera {i}", variable=self.fcam_var, value=str(i),
                                 command=lambda i=i: self.set_face_cam(i))
        fm.add_command(label="Find cameras (which is infrared?)", command=self.face_find_cameras)
        fm.add_command(label="Camera trouble: switch face security off...", command=self.face_security_rescue)
        fm.add_command(label="Download face models (one time)", command=self.face_download_models)

        # --- Augmented reality
        arm = sub(menu, "Augmented reality")
        self.ar_var = tk.BooleanVar(value=bool(self.cfg.get("ar_enabled")))
        arm.add_checkbutton(label="AR vision (uses the camera)", variable=self.ar_var, command=self.toggle_ar)
        arm.add_command(label="Learn an object now...", command=self.ar_learn_dialog)
        arm.add_command(label="Objects and actions...", command=self.ar_manage_dialog)
        arm.add_command(label="What do you see?", command=lambda: self.submit("what do you see"))
        arm.add_command(label="Add starter shape commands", command=lambda: self.submit("set up ar starter commands"))
        arm.add_separator()
        self.arann_var = tk.BooleanVar(value=bool(self.cfg.get("ar_announce", True)))
        arm.add_checkbutton(label="Say what I see when a learned object appears", variable=self.arann_var,
                            command=self.toggle_ar_announce)
        self.arhud_var = tk.BooleanVar(value=bool(self.cfg.get("ar_hud", True)))
        arm.add_checkbutton(label="Info panel (time, battery, next class)", variable=self.arhud_var,
                            command=self.toggle_ar_hud)
        acam = sub(arm, "Camera")
        self.arcam_var = tk.StringVar(value=str(self.cfg.get("ar_cam", "auto")))
        acam.add_radiobutton(label="Automatic (normal webcam first)", variable=self.arcam_var, value="auto",
                             command=lambda: self.set_ar_cam("auto"))
        for i in range(4):
            acam.add_radiobutton(label=f"Camera {i}", variable=self.arcam_var, value=str(i),
                                 command=lambda i=i: self.set_ar_cam(i))
        strict = sub(arm, "Recognition strictness")
        self.armatch_var = tk.StringVar(value=str(self.cfg.get("ar_min_matches", 12)))
        for n, label in ((9, "Forgiving (finds more, may mix up similar things)"), (12, "Balanced"),
                         (18, "Strict (fewest false matches)")):
            strict.add_radiobutton(label=label, variable=self.armatch_var, value=str(n),
                                   command=lambda n=n: self.set_ar_strict(n))
        arm.add_command(label="Install camera packages...", command=self.install_gesture_packages_ui)

        # --- Quick actions
        q = sub(menu, "Quick actions")
        for label, cmd in [("Open Chrome", "open chrome"), ("Open WhatsApp", "open whatsapp"),
                           ("Open Notes (Notepad)", "open notes"), ("Open Calculator", "open calculator"),
                           ("What time is it", "what time is it"), ("Battery", "battery"),
                           ("Take a screenshot", "screenshot"), ("Tell me a joke", "tell me a joke"),
                           ("Top 20 world news", "world news")]:
            q.add_command(label=label, command=lambda c=cmd: self.submit(c))

        # --- Contacts and messages
        c = sub(menu, "Contacts and messages")
        c.add_command(label="Edit contacts...", command=self.edit_contacts)
        c.add_command(label="Import contacts from .vcf...", command=self.import_vcard)
        c.add_command(label="Edit preloaded messages...", command=self.edit_messages)

        # --- Knowledge and mail
        k = sub(menu, "Knowledge and mail")
        k.add_command(label="Open my facts (Notepad)", command=lambda: self.submit("open my facts"))
        k.add_command(label="Add a text file to my facts...", command=self.add_knowledge_file)
        self.pack_var = tk.BooleanVar(value=bool(self.cfg.get("builtin_knowledge", True)))
        k.add_checkbutton(label="Built-in facts pack (offline answers)", variable=self.pack_var,
                          command=self.toggle_knowledge_pack)
        k.add_command(label="How many facts do I know?", command=lambda: self.submit("how many facts do you know"))
        k.add_separator()
        k.add_command(label="Check my mail", command=lambda: self.submit("check my mail"))
        k.add_command(label="Review my mail", command=lambda: self.submit("review my mail"))
        k.add_command(label="Email setup...", command=self.mail_setup)

        # --- Memory
        mm = sub(menu, "Memory")
        self.mem_var = tk.BooleanVar(value=bool(self.cfg.get("memory_enabled", True)))
        mm.add_checkbutton(label="Long-term memory (remember what I tell it about me)", variable=self.mem_var,
                           command=self.toggle_memory)
        lm = sub(mm, "Learn from what I say")
        self.memlearn_var = tk.StringVar(value=self.cfg.get("memory_learn", "all"))
        for key, label in (("all", "Typed and spoken sentences"), ("typed", "Typed sentences only"),
                           ("explicit", "Only when I say \"remember\"")):
            lm.add_radiobutton(label=label, variable=self.memlearn_var, value=key,
                               command=lambda k=key: self.set_memory_learn(k))
        self.memhabit_var = tk.BooleanVar(value=bool(self.cfg.get("memory_habits", True)))
        mm.add_checkbutton(label="Notice habits (commands I repeat at the same time of day)", variable=self.memhabit_var,
                           command=self.toggle_memory_habits)
        self.memshare_var = tk.BooleanVar(value=bool(self.cfg.get("memory_share_ai", True)))
        mm.add_checkbutton(label="Let the AI brain / Claude see the memories that fit a request", variable=self.memshare_var,
                           command=self.toggle_memory_share)
        mm.add_separator()
        mm.add_command(label="What do you remember about me?", command=lambda: self.submit("what do you remember about me"))
        mm.add_command(label="View and edit memories...", command=self.memory_dialog)
        mm.add_command(label="Forget everything...", command=self.memory_clear_ui)

        # --- Maths
        mt = sub(menu, "Maths")
        for label, cmd in [("Solve  x\u00b2 + 5x + 6 = 0", "solve x^2 + 5x + 6 = 0"),
                           ("Solve  log x + log(x - 3) = 1", "solve log x + log(x - 3) = 1"),
                           ("Solve  x + y = 10 and x - y = 2", "solve x + y = 10 and x - y = 2"),
                           ("Calculate  (3 + 4i)(2 - i)", "calculate (3 + 4i)(2 - i)"),
                           ("Factorise  x\u00b3 - 6x\u00b2 + 11x - 6", "factorise x^3 - 6x^2 + 11x - 6"),
                           ("Differentiate  x\u00b3 sin x", "differentiate x^3 sin x"),
                           ("Integrate  x\u00b2 from 0 to 3", "integrate x^2 from 0 to 3")]:
            mt.add_command(label=label, command=lambda c=cmd: self.submit(c))
        mt.add_separator()
        mt.add_command(label="Install the algebra engine (SymPy)...", command=self.assistant.install_sympy)
        self.math_online_var = tk.BooleanVar(value=bool(self.cfg.get("math_online", True)))
        mt.add_checkbutton(label="Use the internet when I can't solve it offline", variable=self.math_online_var,
                           command=self.toggle_math_online)
        mt.add_command(label="Wolfram|Alpha AppID (optional, for word problems)...", command=self.wolfram_setup)

        # --- Assistant
        a = sub(menu, "Assistant")
        a.add_command(label="Stop speaking  (Esc)", command=self.assistant.stop_speaking)
        a.add_command(label="Change voice", command=self.speaker.cycle_voice)
        a.add_command(label="List voices", command=lambda: self.submit("list voices"))
        a.add_command(label="Install natural voices (edge-tts)...", command=self.install_voices_ui)
        a.add_separator()
        self.claude_var = tk.BooleanVar(value=False)       # never remembered: PAC always starts offline
        a.add_checkbutton(label="Claude mode (online - off until you switch it on)", variable=self.claude_var,
                          command=self.toggle_claude)
        a.add_command(label="Claude setup (API key, model)...", command=self.claude_setup)
        self.bgs_var = tk.BooleanVar(value=bool(self.cfg.get("background_search", True)))
        a.add_checkbutton(label="Look questions up on the web quietly (no prompt, no browser)", variable=self.bgs_var,
                          command=self.toggle_bg_search)
        se = sub(a, "Quiet search engine")
        self.engine_var = tk.StringVar(value=self.cfg.get("search_engine", "google"))
        for key, label in (("google", "Google in a hidden browser (DuckDuckGo if it refuses)"),
                           ("duckduckgo", "DuckDuckGo only (faster)")):
            se.add_radiobutton(label=label, variable=self.engine_var, value=key,
                               command=lambda k=key: self.set_search_engine(k))
        self.read_var = tk.BooleanVar(value=bool(self.cfg.get("read_pages", True)))
        a.add_checkbutton(label="Read the top web pages for fuller answers", variable=self.read_var,
                          command=self.toggle_read_pages)
        self.neural_var = tk.BooleanVar(value=bool(self.cfg.get("neural", True)))
        a.add_checkbutton(label="Natural voice (online, needs edge-tts)", variable=self.neural_var,
                          command=self.toggle_neural)
        nv = sub(a, "Natural voice style")
        self.nvoice_var = tk.StringVar(value=self.cfg.get("neural_voice", NEURAL_VOICES[0][0]))
        for code, name in NEURAL_VOICES:
            nv.add_radiobutton(label=name, variable=self.nvoice_var, value=code,
                               command=lambda c=code: self.set_neural_voice(c))
        a.add_command(label="Speak faster", command=lambda: self.submit("speak faster"))
        a.add_command(label="Speak slower", command=lambda: self.submit("speak slower"))
        self.speak_var = tk.BooleanVar(value=bool(self.cfg.get("speak_replies", True)))
        a.add_checkbutton(label="Speak replies aloud", variable=self.speak_var, command=self.toggle_speak)
        a.add_separator()
        a.add_command(label="Stop listening (sleep)", command=lambda: self.submit("stop listening"))
        a.add_command(label="Wake up", command=lambda: self.submit("wake up"))

        # --- System
        s = sub(menu, "System")
        s.add_command(label="Create desktop shortcut", command=self.do_shortcut)
        self.autostart_var = tk.BooleanVar(value=False)
        s.add_checkbutton(label="Start PAC when Windows starts", variable=self.autostart_var,
                          command=self.toggle_autostart)
        self.min_var = tk.BooleanVar(value=bool(self.cfg.get("start_minimized", False)))
        s.add_checkbutton(label="Start minimized (run in the background)", variable=self.min_var,
                          command=self.toggle_start_min)
        s.add_command(label="Minimize to background now", command=self.root.iconify)
        s.add_command(label="Clear chat", command=self.clear_chat)

        # --- Help
        h = sub(menu, "Help")
        h.add_command(label="Test voice input", command=self.diagnose_voice)
        h.add_command(label="All features...", command=self.show_all_features)
        h.add_command(label="Say \"help\" aloud", command=lambda: self.submit("help"))

        menu.add_separator()
        menu.add_command(label="Exit", command=self.on_close)

    def mkbtn(self, parent, text, cmd):
        return self.tk.Button(parent, text=text, command=cmd, font=(self.F, 10, "bold"), bg=self.RED, fg=self.BG,
                              relief="flat", bd=0, padx=16, pady=6, cursor="hand2",
                              activebackground=self.RED_TEXT, activeforeground=self.BG)

    def dialog(self, title, size):
        tk = self.tk
        win = tk.Toplevel(self.root)
        win.title(title)
        win.configure(bg=self.BG)
        win.geometry(size)
        return win

    def diagnose_voice(self):
        """Checks every link in the voice chain and says in the chat which one is broken."""
        def work():
            say = lambda s: self.ui("log", "sys", s)
            say("Voice check:")
            say(f"  Mode: {self.mode}.  SpeechRecognition: {'ok' if sr else 'MISSING'}.  "
                f"sounddevice: {'ok' if sd else 'MISSING'}.")
            if not self.voice_ok:
                say("  Install them with: pip install SpeechRecognition sounddevice  (then restart PAC).")
                return
            try:
                say("  Input device: " + sd.query_devices(self.cfg.get("mic"), "input")["name"])
            except Exception as e:
                say(f"  No input device found ({e}). Plug in or enable a microphone.")
                return
            say("  Internet: " + ("reachable." if internet_ok() else "NOT reachable - Voice mode needs it."))
            if self.mode != "voice" or not self.mic_on:
                say("  Turn on Menu > Mode > Voice and Menu > Voice input > Microphone on, then test again.")
                return
            say("  Speak normally for 4 seconds...")
            self.listener.peak_seen, self.listener.blocks = 0, 0
            time.sleep(4)
            p, n = self.listener.peak_seen, self.listener.blocks
            if n == 0:
                say("  No audio arrived at all. Try another entry under Menu > Voice input > Input device.")
            elif p < 20:
                say("  The microphone is sending silence. On Windows: Settings > Privacy & security > "
                    "Microphone > allow desktop apps, and make sure it isn't muted. Or pick another input device.")
            elif p < 1500:
                say(f"  Heard you, but very quietly (peak {p} of 32768). Raise the mic volume in Windows "
                    "Sound settings, or set Menu > Voice input > Boost level higher.")
            else:
                say(f"  Microphone level is good (peak {p} of 32768). If nothing is recognised, look for the "
                    "'Heard:' line under the recorder or an error message in this chat.")
        threading.Thread(target=work, daemon=True).start()

    def show_all_features(self):
        tk = self.tk
        win = self.dialog("All features", "540x580")
        tk.Label(win, text="Everything PAC can do", font=(self.F, 14, "bold"), fg=self.RED,
                 bg=self.BG).pack(anchor="w", padx=16, pady=(14, 6))
        body = tk.Frame(win, bg=self.RED_DEEP, padx=1, pady=1)
        body.pack(fill="both", expand=True, padx=16, pady=(0, 14))
        txt = tk.Text(body, wrap="word", bg=self.BG, fg=self.RED_TEXT, font=(self.F, 11), relief="flat",
                      padx=12, pady=10, bd=0, highlightthickness=0)
        txt.pack(fill="both", expand=True)
        txt.insert("1.0", HELP_TEXT)
        txt.configure(state="disabled")

    # ----- actions
    def send_entry(self):
        txt = self.entry.get().strip()
        if txt:
            self.entry.delete(0, "end")
            self.submit(txt)

    def submit(self, text):
        self.cmd_q.put(("text", text))

    def _cmd_worker(self):
        while True:
            src, text = self.cmd_q.get()
            try:
                self.assistant.process(text, src)
            except Exception:
                logger.exception("command failed: %s", text)
                self.ui("log", "sys", "Something went wrong with that command (see ~/.pac/pac.log).")
                self.speaker.say("Sorry, something went wrong with that.")

    def set_mode(self, mode, persist=True, announce=True):
        """Voice = Google Web Speech (internet). Text = no microphone, no recognition, no network."""
        if mode == "voice" and not self.voice_ok:
            self.append("sys", "Voice mode needs two packages: pip install SpeechRecognition sounddevice")
            mode = "text"
        changed = mode != self.mode
        self.mode = mode
        self.mode_var.set(mode)
        self.level_target = 0.0
        if persist:
            self.cfg["mode"] = mode
            save_config(self.cfg)
        self.listener.wake.set()
        self.refresh_badge()
        if announce and changed:
            if mode == "voice":
                threading.Thread(target=self._verify_online, daemon=True).start()
                self.assistant.say("Voice mode on. I'm listening.")
            else:
                self.assistant.say("Text mode on. Type your commands.")

    def toggle_mic(self):
        self.mic_on = self.mic_var.get()
        self.level_target = 0.0
        self.listener.wake.set()

    def pick_mic(self, idx, label):
        self.cfg["mic"] = idx
        save_config(self.cfg)
        self.listener.restart.set()
        self.append("sys", f"Microphone: {label}")

    def set_gain(self, g):
        self.cfg["gain"] = float(g)
        self.auto_var.set(False)
        self.cfg["auto_gain"] = False
        save_config(self.cfg)

    def toggle_autogain(self):
        self.cfg["auto_gain"] = self.auto_var.get()
        save_config(self.cfg)

    def toggle_knowledge_pack(self):
        self.cfg["builtin_knowledge"] = self.pack_var.get()
        save_config(self.cfg)
        n = install_knowledge_pack(self.cfg)
        self.append("sys", f"Built-in facts pack on: {n} ready-made answers, all offline." if n
                    else "Built-in facts pack off. Your own facts are untouched.")

    def set_voice_speed(self, key):
        self.cfg["voice_speed"] = key
        save_config(self.cfg)
        self.listener.restart.set()                     # reopen the microphone so the new timing applies
        self.append("sys", f"Voice reaction speed: {key}.")

    def set_lang(self, code):
        self.cfg["lang"] = code
        save_config(self.cfg)
        self.append("sys", f"Recognition language: {code}")

    def toggle_speak(self):
        self.cfg["speak_replies"] = self.speak_var.get()
        save_config(self.cfg)

    def toggle_vint(self):
        self.cfg["voice_interrupt"] = self.vint_var.get()
        save_config(self.cfg)

    def set_vint_sens(self, key):
        self.cfg["voice_interrupt_sens"] = key
        save_config(self.cfg)

    # ----- hand gestures
    def run_gesture_action(self, spec):
        """Carries out an action. Called from the camera thread, so it works with PAC minimised."""
        t, arg = spec.get("type", "none"), (spec.get("arg") or "").strip()
        keys = {"play_pause": "playpause", "next_track": "nexttrack", "prev_track": "prevtrack",
                "mute": "volumemute", "next_slide": "right", "prev_slide": "left"}
        if t in keys:
            pyautogui.press(keys[t])
        elif t in ("vol_up", "vol_down"):
            for _ in range(2):
                pyautogui.press("volumeup" if t == "vol_up" else "volumedown")
        elif t == "stop_speaking":
            self.assistant.stop_speaking()
        elif t == "zoom_in":
            pyautogui.hotkey("ctrl", "=")
        elif t == "zoom_out":
            pyautogui.hotkey("ctrl", "-")
        elif t == "scroll_up":
            pyautogui.scroll(400)
        elif t == "scroll_down":
            pyautogui.scroll(-400)
        elif t == "switch_window":
            pyautogui.hotkey("alt", "tab")
        elif t == "show_desktop":
            if OS == "Windows":
                pyautogui.hotkey("win", "d")
            else:
                self.submit("show desktop")
        elif t == "screenshot":
            self.submit("screenshot")
        elif t == "cmd" and arg:
            self.submit(arg)
        elif t == "keys" and arg:
            pyautogui.hotkey(*[k for k in arg.lower().replace(" ", "").split("+") if k])
        elif t == "url" and arg:
            webbrowser.open(arg if "://" in arg else "https://" + arg)
        if self.cfg.get("gesture_beep", True) and OS == "Windows":
            try:
                import winsound
                winsound.Beep(1250, 55)
            except Exception:
                pass

    def install_gesture_packages_ui(self):
        self.gest_var.set(False)
        threading.Thread(target=lambda: install_gesture_packages(lambda m: self.ui("log", "sys", m)),
                         daemon=True).start()

    def toggle_gestures(self):
        want = self.gest_var.get()
        self.cfg["gesture_enabled"] = want
        save_config(self.cfg)
        if want:
            self.append("sys", "Starting gesture control (camera on)...")
            self.gesture.start()
        else:
            self.set_air_drag(False, announce=False)
            self.gesture.stop_engine()
            self.append("sys", "Gesture control off. The camera is released.")

    def set_air_drag(self, on, announce=True):
        """Palm-as-mouse mode. Always starts OFF at launch, so PAC never grabs your pointer by surprise."""
        on = bool(on)
        self.airdrag_var.set(on)
        self.assistant.air_drag_on = on
        if on:
            self.gesture.airdrag.enable()
            if not self.gest_var.get():
                self.set_gestures(True)                 # the camera has to be running
            if announce:
                self.append("sys", "Air drag & drop is ON. Hold your open hand up: the pointer follows it. "
                                   "Pinch your thumb and index finger together to select a file, keep pinching and move to drag it, "
                                   "and let go to drop it. Works on File Explorer, the desktop and website upload boxes. "
                                   "Say 'stop air drag' to get your mouse back.")
        else:
            was = self.gesture.airdrag.enabled
            self.gesture.airdrag.disable()
            if announce and was:
                self.append("sys", "Air drag & drop is off. The mouse is yours again.")

    def set_gestures(self, on):
        self.gest_var.set(bool(on))
        self.toggle_gestures()

    def set_gesture_cam(self, idx):
        self.cfg["gesture_cam"] = idx
        save_config(self.cfg)
        if self.gesture.running:
            self.gesture.stop_engine()
            self.root.after(1200, self.gesture.start)

    def set_gesture_hold(self, secs):
        self.cfg["gesture_hold"] = float(secs)
        save_config(self.cfg)

    def toggle_gbeep(self):
        self.cfg["gesture_beep"] = self.gbeep_var.get()
        save_config(self.cfg)

    def toggle_start_min(self):
        self.cfg["start_minimized"] = self.min_var.get()
        save_config(self.cfg)

    def say_gesture_list(self):
        rows = [(gesture_title(self.cfg, gid), gesture_action(self.cfg, gid))
                for gid in list(GESTURES) + [g["id"] for g in self.cfg.get("custom_gestures", [])]]
        rows = [(n, s) for n, s in rows if s.get("type", "none") != "none"]
        self.append("sys", "Gestures:\n" + "\n".join(
            f"  {n}  ->  {ACTION_LABEL.get(s['type'])}" + (f" ({s['arg']})" if s.get("arg") else "") for n, s in rows))
        if rows:
            spoken = [f"{n}, {ACTION_LABEL.get(s['type']).lower()}" for n, s in rows[:5]]
            self.assistant.say("Your gestures are: " + "; ".join(spoken) + ("; and more on screen." if len(rows) > 5 else "."))
        else:
            self.assistant.say("No gestures are set up yet. Open Menu, Gestures, Gesture actions.")

    def styled_option(self, parent, var, values):
        om = self.tk.OptionMenu(parent, var, *values)
        om.config(bg=self.BG, fg=self.RED_TEXT, activebackground=self.RED, activeforeground=self.BG,
                  highlightthickness=1, highlightbackground=self.RED_DEEP, relief="flat", bd=0,
                  font=(self.F, 10), width=24, anchor="w")
        om["menu"].config(bg=self.BG, fg=self.RED_TEXT, activebackground=self.RED, activeforeground=self.BG,
                          font=(self.F, 10), bd=0)
        return om

    def _entry(self, parent, **kw):
        return self.tk.Entry(parent, bg=self.BG, fg=self.RED_TEXT, insertbackground=self.RED, relief="flat",
                             font=(self.F, 10), highlightthickness=1, highlightbackground=self.RED_DEEP,
                             highlightcolor=self.RED, selectbackground=self.RED, selectforeground=self.BG, **kw)

    def gesture_actions_dialog(self):
        tk = self.tk
        win = self.dialog("Gesture actions", "880x600")
        tk.Label(win, text="What each gesture does", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=740, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9),
                 text=("Hold a gesture for a moment to trigger it. For 'Run a PAC command', 'Press keys' and 'Open "
                       "website', type the command, keys (ctrl+shift+t) or site in the box beside it. "
                       "Swipes are a quick sweep of an open hand.")).pack(anchor="w", padx=16, pady=(0, 8))
        outer = tk.Frame(win, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=16)
        cv = tk.Canvas(outer, bg=self.BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)
        body = tk.Frame(cv, bg=self.BG)
        cv.create_window((0, 0), window=body, anchor="nw")
        body.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))

        rows = []
        customs = self.cfg.get("custom_gestures", [])
        for gid in [g for g in GESTURES if not gesture_is_deleted(self.cfg, g)] + [g["id"] for g in customs]:
            spec = gesture_action(self.cfg, gid)
            row = tk.Frame(body, bg=self.BG)
            row.pack(fill="x", pady=3)
            tk.Label(row, text=gesture_title(self.cfg, gid), width=17, anchor="w", fg=self.RED_TEXT, bg=self.BG,
                     font=(self.F, 10, "bold" if gid.startswith("custom:") else "normal")).pack(side="left")
            var = tk.StringVar(value=ACTION_LABEL.get(spec.get("type"), "Do nothing"))
            arg = tk.StringVar(value=spec.get("arg", ""))
            self.styled_option(row, var, [a[1] for a in ACTIONS]).pack(side="left", padx=6)
            self._entry(row, textvariable=arg, width=24).pack(side="left", padx=6, ipady=3)
            self.mkbtn(row, "Test", lambda v=var, a=arg: self.test_gesture_action(v, a)).pack(side="left", padx=4)
            self.mkbtn(row, "Delete", lambda g=gid, w=win: self.delete_gesture_prompt(g, w)).pack(side="left", padx=4)
            rows.append((gid, var, arg))

        def save():
            gmap = dict(self.cfg.get("gesture_map") or {})
            for gid, var, arg in rows:
                spec = {"type": ACTION_ID.get(var.get(), "none")}
                if arg.get().strip() and ACTION_HINT.get(spec["type"]):
                    spec["arg"] = arg.get().strip()
                if gid.startswith("custom:"):
                    for g in self.cfg["custom_gestures"]:
                        if g["id"] == gid:
                            g["action"] = spec
                else:
                    gmap[gid] = spec
            self.cfg["gesture_map"] = gmap
            save_config(self.cfg)
            self.append("sys", "Gesture actions saved.")
            win.destroy()
        self.mkbtn(win, "Save", save).pack(pady=12)

    def test_gesture_action(self, var, arg):
        spec = {"type": ACTION_ID.get(var.get(), "none"), "arg": arg.get().strip()}
        threading.Thread(target=self.run_gesture_action, args=(spec,), daemon=True).start()

    def delete_gesture_prompt(self, gid, win):
        """The Delete button beside a gesture in 'Gesture actions'."""
        from tkinter import messagebox
        name = gesture_title(self.cfg, gid)
        taught = gid.startswith("custom:")
        msg = (f"Delete the gesture '{name}'?\n\nYou taught this one, so it is erased for good." if taught else
               f"Delete the built-in gesture '{name}'?\n\nPAC will stop reacting to it. You can bring it back from "
               "Menu > Gestures > Delete gestures.")
        if messagebox.askyesno("Delete gesture", msg, parent=win):
            delete_gestures(self.cfg, [gid])
            win.destroy()
            self.append("sys", f"Deleted gesture '{name}'." + ("" if taught else " (Menu > Gestures > Delete gestures brings it back.)"))
            self.gesture_actions_dialog()

    def delete_gestures_dialog(self):
        """Tick the gestures you don't want and press Delete. Gestures you taught are erased for good; built-in ones
        are switched off (PAC stops reacting to them) and can be brought back from the Restore list."""
        from tkinter import messagebox
        tk = self.tk
        win = self.dialog("Delete gestures", "600x660")
        tk.Label(win, text="Delete gestures", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=560, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "Tick the gestures you don't want, then press Delete selected. Gestures you taught are erased for good. "
            "Built-in ones are switched off - PAC stops reacting to them - and you can bring them back from the "
            "Restore list at the bottom.")).pack(anchor="w", padx=16, pady=(0, 8))
        bar = tk.Frame(win, bg=self.BG)                 # packed first, so a small screen can never push it away
        bar.pack(side="bottom", fill="x", padx=16, pady=12)
        outer = tk.Frame(win, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=16)
        cv = tk.Canvas(outer, bg=self.BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)
        body = tk.Frame(cv, bg=self.BG)
        cv.create_window((0, 0), window=body, anchor="nw")
        body.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))

        picks, restore = {}, {}

        def heading(text):
            tk.Label(body, text=text, font=(self.F, 10, "bold"), fg=self.RED, bg=self.BG).pack(anchor="w", pady=(10, 2))

        def tick(store, gid, text):
            var = tk.BooleanVar(value=False)
            tk.Checkbutton(body, text=text, variable=var, anchor="w", justify="left", bg=self.BG, fg=self.RED_TEXT,
                           selectcolor=self.BG, activebackground=self.BG, activeforeground=self.RED,
                           font=(self.F, 10), highlightthickness=0, bd=0).pack(fill="x", anchor="w", pady=1)
            store[gid] = var

        def what(gid):
            spec = gesture_action(self.cfg, gid)
            return ACTION_LABEL.get(spec.get("type"), "") if spec.get("type", "none") != "none" else "no action set"

        heading("Your gestures")
        live = [g for g in GESTURES if not gesture_is_deleted(self.cfg, g)] + [g["id"] for g in self.cfg.get("custom_gestures", [])]
        for gid in live:
            kind = "taught by you" if gid.startswith("custom:") else "built in"
            tick(picks, gid, f"{gesture_title(self.cfg, gid)}    ({kind}; {what(gid)})")
        gone = [g for g in (self.cfg.get("deleted_gestures") or []) if g in GESTURES]
        if gone:
            heading("Deleted built-in gestures (tick to restore)")
            for gid in gone:
                tick(restore, gid, GESTURES[gid])

        def chosen(store):
            return [g for g, v in store.items() if v.get()]

        def delete_selected():
            gids = chosen(picks)
            if not gids:
                messagebox.showinfo("Delete gestures", "Tick at least one gesture first.", parent=win)
                return
            names = ", ".join(gesture_title(self.cfg, g) for g in gids)
            if not messagebox.askyesno("Delete gestures", f"Delete {len(gids)} gesture(s)?\n\n{names}", parent=win):
                return
            erased, off = delete_gestures(self.cfg, gids)
            if erased:
                self.append("sys", "Erased for good: " + ", ".join(erased) + ".")
            if off:
                self.append("sys", "Switched off: " + ", ".join(off) + ".  (Menu > Gestures > Delete gestures brings them back.)")
            win.destroy()
            self.delete_gestures_dialog()

        def restore_selected():
            gids = chosen(restore)
            if not gids:
                messagebox.showinfo("Delete gestures", "Tick at least one deleted gesture first.", parent=win)
                return
            self.append("sys", "Restored: " + ", ".join(restore_gestures(self.cfg, gids)) + ".")
            win.destroy()
            self.delete_gestures_dialog()

        def select_all():
            for v in picks.values():
                v.set(True)

        self.mkbtn(bar, "Delete selected", delete_selected).pack(side="left")
        self.mkbtn(bar, "Select all", select_all).pack(side="left", padx=8)
        if gone:
            self.mkbtn(bar, "Restore selected", restore_selected).pack(side="left")
        self.mkbtn(bar, "Close", win.destroy).pack(side="right")

    # ---------- faces (Menu > Faces)
    def toggle_faces(self):
        self.set_faces(self.face_var.get())

    def set_faces(self, on):
        on = bool(on)
        self.face_var.set(on)
        self.cfg["face_enabled"] = on
        save_config(self.cfg)
        if on:
            self.append("sys", "Starting face recognition (camera on)...")
            self.faces.start()
        else:
            self.faces.stop_engine()
            self.append("sys", "Face recognition off. The camera is released.")

    def toggle_face_security(self):
        want = self.facesec_var.get()
        if want and not self.faces.db.owners():
            self.facesec_var.set(False)
            self.append("sys", "Enrol your face first (Menu > Faces > Enrol a face...). The first face becomes the owner.")
            return
        if not want and self.cfg.get("face_security"):
            self.facesec_var.set(True)                       # stays on until an owner's face says otherwise
            self.submit("turn off face security")
            return
        self.cfg["face_security"] = want
        save_config(self.cfg)
        self.append("sys", "Face security is ON: the commands you locked now need a face that's allowed to use them. "
                           "(Menu > Faces > People & permissions)" if want else "Face security is off.")

    def set_face_cam(self, value):
        self.cfg["face_cam"] = value
        save_config(self.cfg)
        if self.faces.running:
            self.faces.stop_engine()
            self.root.after(1200, self.faces.start)

    def face_security_rescue(self):
        """Face security needs the camera, and 'turn off face security' needs your face - so a broken camera would lock
        you out. This menu item (deliberately not a spoken command) tests the camera and, only if it really can't
        see, lets you switch the lock off."""
        if not self.cfg.get("face_security"):
            self.append("sys", "Face security is already off.")
            return
        self.append("sys", "Testing the camera (up to about 30 seconds)...")

        def work():
            try:
                self.faces.start(temp=True)
                self.faces.ready.wait(30)
                if self.faces.error:
                    self.ui("face_rescue", self.faces.error)
                else:
                    self.ui("log", "sys", f"The camera is working ({self.faces.cam_label}), so face security can be "
                                          "managed normally: untick Menu > Faces > Face security, with your face in view.")
            except Exception:
                logger.exception("camera test failed")
                self.ui("face_rescue", "The camera test itself failed.")
        threading.Thread(target=work, daemon=True).start()

    def _face_rescue_dialog(self, why):
        from tkinter import messagebox
        first = (why or "").split("\n")[0]
        if messagebox.askyesno("Camera trouble", f"PAC can't use the camera right now:\n\n{first}\n\nWithout the camera it "
                               "can't check faces, so the commands you locked stay locked.\n\nSwitch face security OFF until "
                               "the camera works? (Switch it back on in Menu > Faces.)"):
            self.cfg["face_security"] = False
            save_config(self.cfg)
            self.facesec_var.set(False)
            self.append("sys", "Face security is off. Fix the camera (Menu > Faces > Find cameras), then switch it back on.")

    def face_find_cameras(self):
        was_gesture = self.gesture.running
        if was_gesture:
            self.append("sys", "Tip: switch gesture control off while checking, or its camera will show as busy.")
        threading.Thread(target=lambda: face_camera_report(self.cfg, lambda m: self.ui("log", "sys", m)),
                         daemon=True).start()

    def face_download_models(self):
        def work():
            try:
                ensure_face_models(lambda m: self.ui("log", "sys", m))
                self.ui("log", "sys", "The face models are ready.")
            except FaceSetupError as e:
                self.ui("log", "sys", str(e))
        threading.Thread(target=work, daemon=True).start()

    def face_enroll_dialog(self):
        tk = self.tk
        first = not self.faces.db.owners()
        win = self.dialog("Enrol a face", "460x300")
        tk.Label(win, text="Enrol a face", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=420, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "The first face you enrol becomes the owner. Press Start, then look at the camera and slowly turn your head "
            "a little for about ten seconds. Only one person should be in front of the camera. PAC keeps a set of "
            "numbers, not the pictures.")).pack(anchor="w", padx=16, pady=(0, 10))
        row = tk.Frame(win, bg=self.BG)
        row.pack(fill="x", padx=16, pady=4)
        tk.Label(row, text="Name", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10), width=8, anchor="w").pack(side="left")
        name = tk.StringVar()
        tk.Entry(row, textvariable=name, bg="#040a14", fg=self.RED_TEXT, insertbackground=self.RED, relief="flat",
                 font=(self.F, 11)).pack(side="left", fill="x", expand=True)
        row2 = tk.Frame(win, bg=self.BG)
        row2.pack(fill="x", padx=16, pady=4)
        tk.Label(row2, text="Role", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10), width=8, anchor="w").pack(side="left")
        role = tk.StringVar(value="owner" if first else "guest")
        self._styled_menu(row2, role, ["owner", "trusted", "guest"]).pack(side="left")
        if first:
            role.set("owner")

        def start():
            n = name.get().strip()
            if not n:
                return
            win.destroy()
            self.append("sys", f"Enrolling {n}: look at the camera and slowly turn your head a little...")
            threading.Thread(target=lambda: self.assistant.face_enroll(n, role.get()), daemon=True).start()
        bar = tk.Frame(win, bg=self.BG)
        bar.pack(side="bottom", fill="x", padx=16, pady=14)
        self.mkbtn(bar, "Start", start).pack(side="left")
        self.mkbtn(bar, "Cancel", win.destroy).pack(side="right")

    def _styled_menu(self, parent, var, values):
        om = self.tk.OptionMenu(parent, var, *values)
        om.config(bg=self.BG, fg=self.RED_TEXT, activebackground=self.BG, activeforeground=self.RED,
                  highlightthickness=1, highlightbackground=self.RED_DIM, bd=0, font=(self.F, 10), width=8)
        om["menu"].config(bg=self.BG, fg=self.RED_TEXT, activebackground=self.RED_DIM, activeforeground=self.BG,
                          font=(self.F, 10))
        return om

    def face_people_dialog(self):
        """Roles, arrival commands and who may run which commands - the face-security settings in one place."""
        from tkinter import messagebox
        tk, db = self.tk, self.faces.db
        win = self.dialog("People & permissions", "700x720")
        tk.Label(win, text="People & permissions", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=660, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "Owner can do everything and manage faces. Trusted and guest can only use the commands whose rule allows "
            "them (below). An unknown face can only use commands set to 'anyone'. The rules apply when Face security "
            "is ticked. 'On arrival' is a command PAC runs when that face shows up, e.g. what's my schedule today."
        )).pack(anchor="w", padx=16, pady=(0, 8))
        bar = tk.Frame(win, bg=self.BG)
        bar.pack(side="bottom", fill="x", padx=16, pady=12)
        outer = tk.Frame(win, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=16)
        cv = tk.Canvas(outer, bg=self.BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)
        body = tk.Frame(cv, bg=self.BG)
        cv.create_window((0, 0), window=body, anchor="nw")
        body.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))

        def heading(text):
            tk.Label(body, text=text, font=(self.F, 10, "bold"), fg=self.RED, bg=self.BG).pack(anchor="w", pady=(10, 2))

        heading("People")
        rows = {}
        if not db.people:
            tk.Label(body, text="Nobody yet. Menu > Faces > Enrol a face...", fg=self.RED_DIM, bg=self.BG,
                     font=(self.F, 10)).pack(anchor="w")
        for k, p in db.people.items():
            r = tk.Frame(body, bg=self.BG)
            r.pack(fill="x", pady=2)
            tk.Label(r, text=p["name"], fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10, "bold"), width=12,
                     anchor="w").pack(side="left")
            role = tk.StringVar(value=p["role"])
            self._styled_menu(r, role, ["owner", "trusted", "guest"]).pack(side="left", padx=4)
            arrive = tk.StringVar(value=p.get("on_arrival", ""))
            tk.Entry(r, textvariable=arrive, width=26, bg="#040a14", fg=self.RED_TEXT, insertbackground=self.RED,
                     relief="flat", font=(self.F, 10)).pack(side="left", padx=4)
            gone = tk.BooleanVar(value=False)
            tk.Checkbutton(r, text="delete", variable=gone, bg=self.BG, fg=self.RED_TEXT, selectcolor=self.BG,
                           activebackground=self.BG, activeforeground=self.RED, font=(self.F, 9),
                           highlightthickness=0, bd=0).pack(side="left")
            rows[k] = (role, arrive, gone)
        tk.Label(body, text="(column 2: role   column 3: command to run on arrival)", fg=self.RED_DIM, bg=self.BG,
                 font=(self.F, 8)).pack(anchor="w")

        heading("Who may do what (needs at least this role)")
        rules = {}
        for g, label in FACE_GROUP_LABEL.items():
            r = tk.Frame(body, bg=self.BG)
            r.pack(fill="x", pady=2)
            lv = tk.StringVar(value=face_rule(self.cfg, g))
            self._styled_menu(r, lv, ["anyone", "guest", "trusted", "owner"]).pack(side="left", padx=(0, 8))
            tk.Label(r, text=label, fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10), anchor="w").pack(side="left")
            rules[g] = lv

        heading("Behaviour")
        opts = {}
        for key, label in (("face_greet", "Say welcome back when a known face arrives"),
                           ("face_lock_on_leave", "Lock the laptop when the owner walks away (needs Face security)"),
                           ("face_save_unknown", "Keep a snapshot of a stranger in ~/.pac/faces (off = no pictures kept)")):
            v = tk.BooleanVar(value=bool(self.cfg.get(key)))
            tk.Checkbutton(body, text=label, variable=v, anchor="w", bg=self.BG, fg=self.RED_TEXT, selectcolor=self.BG,
                           activebackground=self.BG, activeforeground=self.RED, font=(self.F, 10),
                           highlightthickness=0, bd=0).pack(fill="x", anchor="w", pady=1)
            opts[key] = v

        def save():
            keep = {k: v for k, v in rows.items() if not v[2].get()}
            if db.people and not any(v[0].get() == "owner" for v in keep.values()):
                if self.cfg.get("face_security") or not keep:
                    messagebox.showinfo("People & permissions", "There must be at least one owner.", parent=win)
                    return
            for k, (role, arrive, gone) in rows.items():
                if gone.get():
                    db.remove(k)
                else:
                    db.set_role(k, role.get())
                    db.set_arrival(k, arrive.get())
            self.cfg["face_rules"] = {g: v.get() for g, v in rules.items()}
            for key, v in opts.items():
                self.cfg[key] = bool(v.get())
            if self.cfg.get("face_security") and not db.owners():
                self.cfg["face_security"] = False
                self.facesec_var.set(False)
            save_config(self.cfg)
            self.append("sys", "Saved the people and permissions.")
            win.destroy()
        self.mkbtn(bar, "Save", save).pack(side="left")
        self.mkbtn(bar, "Cancel", win.destroy).pack(side="right")

    # ---------- augmented reality (Menu > Augmented reality)
    def toggle_ar(self):
        self.set_ar(self.ar_var.get())

    def set_ar(self, on):
        on = bool(on)
        self.ar_var.set(on)
        self.cfg["ar_enabled"] = on
        save_config(self.cfg)
        if on:
            self.append("sys", "Starting AR (camera on). A window called PAC AR opens. Hold an object in its box and say "
                               "'learn this as ...' (or press L in that window).")
            self.ar.start()
        else:
            self.ar.stop_engine()
            self.append("sys", "AR off. The camera is released.")

    def toggle_ar_announce(self):
        self.cfg["ar_announce"] = self.arann_var.get()
        save_config(self.cfg)

    def toggle_ar_hud(self):
        self.cfg["ar_hud"] = self.arhud_var.get()
        save_config(self.cfg)

    def set_ar_cam(self, value):
        self.cfg["ar_cam"] = value
        save_config(self.cfg)
        if self.ar.running:
            self.ar.stop_engine()
            self.root.after(1500, self.ar.start)

    def set_ar_strict(self, n):
        self.cfg["ar_min_matches"] = int(n)
        save_config(self.cfg)

    def ar_learn_dialog(self):
        tk = self.tk
        win = self.dialog("Learn an object", "460x250")
        tk.Label(win, text="Learn an object", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=420, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "Name it, press Start, then hold the object inside the box in the PAC AR window and turn it slowly for "
            "about three seconds. Teach it again later from other angles to make it recognise better.")
                 ).pack(anchor="w", padx=16, pady=(0, 10))
        name = tk.StringVar()
        e = self._entry(win, textvariable=name)
        e.pack(fill="x", padx=16, pady=4, ipady=5)
        e.focus_set()

        def start(_e=None):
            n = name.get().strip()
            if not n:
                return
            win.destroy()
            self.submit(f"learn this as {n}")
            if not self.ar.running:
                self.append("sys", "Starting AR first...")
        e.bind("<Return>", start)
        self.mkbtn(win, "Start", start).pack(pady=14)

    def ar_manage_dialog(self):
        from tkinter import messagebox
        tk = self.tk
        win = self.dialog("Objects and actions", "720x680")
        tk.Label(win, text="Objects and actions", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=680, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "When PAC sees one of these in the AR window it runs the action: any PAC command (open chrome, what's my "
            "schedule today, remind me to call mom in 10 minutes) or 'say' followed by words to speak. Leave it empty "
            "to just announce the object. Shapes: draw one on paper and hold it inside the box.")
                 ).pack(anchor="w", padx=16, pady=(0, 8))
        bar = tk.Frame(win, bg=self.BG)
        bar.pack(side="bottom", fill="x", padx=16, pady=12)
        outer = tk.Frame(win, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=16)
        cv = tk.Canvas(outer, bg=self.BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)
        body = tk.Frame(cv, bg=self.BG)
        cv.create_window((0, 0), window=body, anchor="nw")
        body.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))

        def heading(text):
            tk.Label(body, text=text, font=(self.F, 10, "bold"), fg=self.RED, bg=self.BG).pack(anchor="w", pady=(10, 2))

        entries = {e[0]: e for e in self.ar.entries()}
        heading("Learned objects")
        rows = {}
        objs = [e for e in entries.values() if e[2] == "object"]
        if not objs:
            tk.Label(body, text="None yet. Say: learn this as my keys", fg=self.RED_DIM, bg=self.BG,
                     font=(self.F, 10)).pack(anchor="w")
        for key, name, _kind, action, nviews in objs:
            r = tk.Frame(body, bg=self.BG)
            r.pack(fill="x", pady=2)
            tk.Label(r, text=f"{name} ({nviews})", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10, "bold"), width=22,
                     anchor="w").pack(side="left")
            act = tk.StringVar(value=action)
            self._entry(r, textvariable=act, width=30).pack(side="left", padx=4, ipady=3)
            gone = tk.BooleanVar(value=False)
            tk.Checkbutton(r, text="forget", variable=gone, bg=self.BG, fg=self.RED_TEXT, selectcolor=self.BG,
                           activebackground=self.BG, activeforeground=self.RED, font=(self.F, 9),
                           highlightthickness=0, bd=0).pack(side="left")
            rows[key] = (act, gone)
        heading("Predefined shapes")
        srows = {}
        for s in AR_SHAPES:
            cur = entries.get("shape:" + s)
            r = tk.Frame(body, bg=self.BG)
            r.pack(fill="x", pady=2)
            tk.Label(r, text=s, fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10, "bold"), width=22, anchor="w").pack(side="left")
            act = tk.StringVar(value=cur[3] if cur else "")
            self._entry(r, textvariable=act, width=30).pack(side="left", padx=4, ipady=3)
            srows[s] = act

        def save():
            for key, (act, gone) in rows.items():
                if gone.get():
                    self.ar.remove(key)
                else:
                    self.ar.set_action(key, act.get())
            for s, act in srows.items():
                self.ar.set_action("shape:" + s, act.get(), name=s, kind="shape")
            self.append("sys", "AR objects and actions saved.")
            win.destroy()

        def starter():
            n = self.ar.starter_pack()
            win.destroy()
            self.append("sys", f"Added {n} starter shape command(s).")
            self.ar_manage_dialog()
        self.mkbtn(bar, "Save", save).pack(side="left")
        self.mkbtn(bar, "Add starter shape commands", starter).pack(side="left", padx=8)
        self.mkbtn(bar, "Cancel", win.destroy).pack(side="right")

    def toggle_bg_search(self):
        self.cfg["background_search"] = self.bgs_var.get()
        save_config(self.cfg)
        self.refresh_badge()
        self.append("sys", "Questions I can't answer from your facts are now looked up quietly on the web - no prompt, "
                           "no browser window." if self.cfg["background_search"] else
                           "Quiet web lookups are off. For a question I can't answer I'll ask before opening Google.")

    def set_search_engine(self, key):
        self.cfg["search_engine"] = key
        save_config(self.cfg)
        self.append("sys", "Quiet search: Google through a hidden browser, with DuckDuckGo as the backup."
                    if key == "google" else "Quiet search: DuckDuckGo only.")

    def toggle_read_pages(self):
        self.cfg["read_pages"] = self.read_var.get()
        save_config(self.cfg)
        self.append("sys", "After a quiet search I'll open the top pages myself and answer from what they say."
                    if self.cfg["read_pages"] else "Quiet searches now answer from the search snippets only.")

    def toggle_math_online(self):
        self.cfg["math_online"] = self.math_online_var.get()
        save_config(self.cfg)
        self.append("sys", "A maths problem I can't do offline (a word problem, say) will be looked up online."
                    if self.cfg["math_online"] else "Maths stays fully offline now - nothing is looked up online.")

    def wolfram_setup(self):
        tk = self.tk
        win = self.dialog("Wolfram|Alpha (optional)", "500x340")
        tk.Label(win, justify="left", wraplength=460, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "PAC works maths out offline. A word problem it can't turn into an equation (\"a train covers 120 km in "
            "2 hours...\") can go to Wolfram|Alpha, which is very good at them.\n\n"
            "Get a free AppID (personal, non-commercial use) at developer.wolframalpha.com, choosing the Short "
            "Answers API, and paste it below. Only the text of the problem is sent.\n\n"
            "Leave it empty and PAC asks Claude instead (when Claude mode is on), or does a quiet web search.")
                 ).pack(anchor="w", padx=14, pady=(12, 8))
        tk.Label(win, text="AppID", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 9)).pack(anchor="w", padx=14)
        e = self._entry(win)
        e.pack(fill="x", padx=14, pady=(0, 4), ipady=5)
        e.insert(0, self.cfg.get("wolfram_appid", ""))

        def save():
            self.cfg["wolfram_appid"] = e.get().strip()
            save_config(self.cfg)
            self.append("sys", "Wolfram|Alpha AppID saved - word problems I can't do offline go there first."
                        if self.cfg["wolfram_appid"] else "Wolfram|Alpha AppID cleared.")
            win.destroy()
        self.mkbtn(win, "Save", save).pack(pady=12)

    def teach_gesture_dialog(self):
        """Record a new gesture: pick a name and an action, hold the pose in front of the camera for a couple of
        seconds, and PAC remembers its shape."""
        from tkinter import messagebox
        tk = self.tk
        win = self.dialog("Teach a new gesture", "540x560")
        tk.Label(win, text="Teach a new gesture", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG
                 ).pack(anchor="w", padx=16, pady=(14, 2))
        tk.Label(win, justify="left", wraplength=500, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9),
                 text=("1. Name it and choose what it does.  2. Press Record, then hold your hand in view in the pose "
                       "you want, steady, with your palm or the back of your hand towards the camera.  "
                       "The same pose with your other hand works too.")).pack(anchor="w", padx=16, pady=(0, 10))
        tk.Label(win, text="Gesture name", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10)).pack(anchor="w", padx=16)
        name_e = self._entry(win)
        name_e.pack(fill="x", padx=16, pady=(0, 8), ipady=5)
        tk.Label(win, text="When I make it, PAC should", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 10)
                 ).pack(anchor="w", padx=16)
        act = tk.StringVar(value=ACTION_LABEL["play_pause"])
        self.styled_option(win, act, [a[1] for a in ACTIONS if a[0] != "none"]).pack(anchor="w", padx=16, pady=(0, 6))
        hint = tk.Label(win, text="", fg=self.RED_DIM, bg=self.BG, font=(self.F, 9))
        hint.pack(anchor="w", padx=16)
        arg_e = self._entry(win)
        arg_e.pack(fill="x", padx=16, pady=(0, 10), ipady=4)

        def refresh_hint(*_):
            h = ACTION_HINT.get(ACTION_ID.get(act.get(), "none"), "")
            hint.configure(text=h)
            arg_e.configure(state="normal" if h else "disabled")
        act.trace_add("write", refresh_hint)
        refresh_hint()

        status = tk.Label(win, text="", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 11), wraplength=500, justify="left")
        status.pack(anchor="w", padx=16, pady=(6, 4))
        bar = tk.Canvas(win, height=14, bg=self.BG, highlightthickness=1, highlightbackground=self.RED_DEEP)
        bar.pack(fill="x", padx=16)
        btn = self.mkbtn(win, "Record", lambda: begin())
        btn.pack(pady=16)

        def set_bar(frac):
            bar.delete("all")
            bar.create_rectangle(0, 0, bar.winfo_width() * frac, 14, fill=self.RED, outline="")

        def fail(msg):
            self.gesture.cancel_recording()
            status.configure(text=msg)
            set_bar(0)
            btn.configure(state="normal")

        def begin():
            name = name_e.get().strip()
            atype = ACTION_ID.get(act.get(), "none")
            arg = arg_e.get().strip()
            taken = {g["name"].lower() for g in self.cfg.get("custom_gestures", [])} | {v.lower() for k, v in GESTURES.items() if not gesture_is_deleted(self.cfg, k)}
            if not name:
                messagebox.showinfo("Teach a gesture", "Give the gesture a name first.", parent=win)
                return
            if name.lower() in taken:
                messagebox.showinfo("Teach a gesture", f"There is already a gesture called '{name}'. Pick another name.", parent=win)
                return
            if ACTION_HINT.get(atype) and not arg:
                messagebox.showinfo("Teach a gesture", "Type the command, keys or website in the box.", parent=win)
                return
            btn.configure(state="disabled")
            if not self.gesture.running:
                self.set_gestures(True)
            wait_camera(time.time(), name, atype, arg)

        def wait_camera(t0, name, atype, arg):
            if not win.winfo_exists():
                return
            if self.gesture.running and self.gesture.frames > 2:
                countdown(3, name, atype, arg)
            elif self.gesture.error or time.time() - t0 > 40:
                fail(self.gesture.error or "The camera didn't start.")
            else:
                status.configure(text="Starting the camera...")
                win.after(300, wait_camera, t0, name, atype, arg)

        def countdown(n, name, atype, arg):
            if not win.winfo_exists():
                return
            if n > 0:
                status.configure(text=f"Get your hand in view and make the pose...  {n}")
                win.after(1000, countdown, n - 1, name, atype, arg)
            else:
                status.configure(text="Hold it steady...")
                self.gesture.start_recording(30)
                poll(name, atype, arg)

        def poll(name, atype, arg):
            if not win.winfo_exists():
                return
            r = self.gesture.rec
            if r is None:
                return
            set_bar(len(r["vecs"]) / r["need"])
            if r["done"]:
                self.gesture.cancel_recording()
                finish(r["vecs"], name, atype, arg)
            elif time.time() - r["t0"] > 25:
                fail("I didn't see a hand for long enough. Check the lighting, keep your whole hand in view, and try again.")
            else:
                win.after(100, poll, name, atype, arg)

        def finish(vecs, name, atype, arg):
            spec = {"type": atype}
            if arg:
                spec["arg"] = arg
            g = build_custom_gesture(name, vecs, spec)
            warn = ""
            for other in self.cfg.get("custom_gestures", []):
                mean, worst = pose_distance(g["samples"][0], other["samples"][0])
                if mean / g["thr"] < 1.2 and worst / g["thr_max"] < 1.2:
                    warn = f"  Careful: it looks a lot like '{other['name']}', so the two may get mixed up."
            self.cfg.setdefault("custom_gestures", []).append(g)
            save_config(self.cfg)
            self.append("sys", f"Gesture '{name}' saved. Hold it for a moment to {ACTION_LABEL[atype].lower()}.{warn}")
            win.destroy()
        win.bind("<Destroy>", lambda e: e.widget is win and self.gesture.cancel_recording())

    def hand_view_window(self):
        """A live skeleton of your hand and the gesture PAC thinks it sees - handy for teaching and testing."""
        tk = self.tk
        if not self.gesture.running:
            self.set_gestures(True)
        win = self.dialog("Hand view", "440x420")
        cv = tk.Canvas(win, bg=self.BG, highlightthickness=1, highlightbackground=self.RED_DEEP, width=400, height=300)
        cv.pack(padx=18, pady=(18, 8))
        name = tk.Label(win, text="", font=(self.F, 14, "bold"), fg=self.RED, bg=self.BG)
        name.pack()
        info = tk.Label(win, text="", font=(self.F, 9), fg=self.RED_DIM, bg=self.BG)
        info.pack(pady=(2, 0))

        def tick():
            if not win.winfo_exists():
                return
            cv.delete("all")
            lat = self.gesture.latest or {}
            hands = lat.get("hands") or ([{"slot": "Right", "pts": lat["pts"], "gid": lat.get("gid"),
                                           "progress": lat.get("progress", 0.0)}] if lat.get("pts") else [])
            pts = hands[0]["pts"] if hands else None
            if not self.gesture.running:
                msg = self.gesture.error or "Camera starting..."
                cv.create_text(200, 150, text=msg, fill=self.RED_DIM, width=360, font=(self.F, 10))
                name.configure(text="")
            elif not pts:
                cv.create_text(200, 150, text="Show your hand to the camera", fill=self.RED_DIM, font=(self.F, 11))
                name.configure(text="")
            else:
                for h in hands:                                  # every hand in view, each in its own shade
                    P = [(x * 400, y * 300) for x, y in h["pts"]]
                    line, dot = (self.RED_MID, self.RED) if h["slot"] == "Right" else (self.RED_DEEP, self.RED_MID)
                    for a, b in HAND_LINES:
                        cv.create_line(*P[a], *P[b], fill=line, width=2)
                    for x, y in P:
                        cv.create_oval(x - 3, y - 3, x + 3, y + 3, fill=dot, outline="")
                    cv.create_text(P[0][0], min(290, P[0][1] + 14), text=h["slot"], fill=self.RED_DIM, font=(self.F, 8))
                gid = lat.get("gid")
                if gid and gesture_is_deleted(self.cfg, gid):
                    gid = None
                if len(hands) == 2 and not lat.get("combo"):
                    name.configure(text="   |   ".join(
                        f"{h['slot']}: {gesture_title(self.cfg, h['gid']) if h['gid'] and not gesture_is_deleted(self.cfg, h['gid']) else '...'}"
                        for h in hands))
                else:
                    name.configure(text=gesture_title(self.cfg, gid) if gid else "...")
                prog = lat.get("progress", 0.0)
                if prog:
                    cv.create_rectangle(0, 290, 400 * prog, 300, fill=self.RED, outline="")
                spec = gesture_action(self.cfg, gid) if gid else {"type": "none"}
                info.configure(text=("Will: " + ACTION_LABEL.get(spec["type"], "")) if spec["type"] != "none" else
                               ("No action set" if len(hands) == 1 or lat.get("combo") else "Two hands in view"))
            win.after(70, tick)
        tick()

    def toggle_triggers(self):
        self.cfg["sound_triggers"] = self.trig_var.get()
        self.trigger_mic_failed = False
        save_config(self.cfg)
        self.listener.wake.set()

    def set_sens(self, key):
        self.cfg["trigger_sens"] = key
        save_config(self.cfg)

    def toggle_neural(self):
        self.cfg["neural"] = self.neural_var.get()
        self.speaker.neural_retry_at = 0.0
        save_config(self.cfg)
        if self.cfg["neural"] and edge_tts is None:
            self.append("sys", "Install the natural voice with:  pip install edge-tts  (then restart PAC)")

    def set_neural_voice(self, code):
        self.speaker.set_voice_code(code)

    def toggle_claude(self):
        self.assistant.claude_set(self.claude_var.get())
        self.claude_var.set(self.assistant.claude_on)      # stays unticked if it couldn't start (no key)
        self.refresh_badge()

    def claude_setup(self):
        tk = self.tk
        win = self.dialog("Claude setup", "500x470")
        tk.Label(win, justify="left", wraplength=460, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9), text=(
            "Claude mode lets PAC answer open questions and chat using Anthropic's Claude. It is OFF every time "
            "PAC starts, and nothing is sent to Anthropic unless you switch it on (say 'claude mode on') or say "
            "'ask Claude ...'.\n\nWhen it is used, the text of what you said (and the conversation so far) goes to "
            "Anthropic's servers. Your files, mail, contacts and timetable are never sent.\n\n"
            "You need your own API key from console.anthropic.com (API usage is billed to that account).")
                 ).pack(anchor="w", padx=14, pady=(12, 8))
        tk.Label(win, text="API key", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 9)).pack(anchor="w", padx=14)
        e = tk.Entry(win, show="*", bg=self.BG, fg=self.RED_TEXT, insertbackground=self.RED, relief="flat",
                     font=(self.F, 11), highlightthickness=1, highlightbackground=self.RED_DEEP,
                     highlightcolor=self.RED)
        e.pack(fill="x", padx=14, pady=(0, 4), ipady=5)
        if claude_key_get(self.cfg):
            e.insert(0, claude_key_get(self.cfg))
        tk.Label(win, text="Model", fg=self.RED_TEXT, bg=self.BG, font=(self.F, 9)).pack(anchor="w", padx=14, pady=(8, 0))
        model = tk.StringVar(value=self.cfg.get("claude_model") or CLAUDE_MODELS[0][0])
        for code, label in CLAUDE_MODELS:
            tk.Radiobutton(win, text=label, variable=model, value=code, bg=self.BG, fg=self.RED_TEXT,
                           selectcolor=self.BG, activebackground=self.BG, activeforeground=self.RED,
                           font=(self.F, 10), highlightthickness=0, bd=0, anchor="w").pack(fill="x", padx=14)

        def save(test=False):
            key = e.get().strip()
            if not key:
                self.ui("log", "sys", "Paste your API key first.")
                return
            where = claude_key_set(self.cfg, key)
            self.cfg["claude_model"] = model.get()
            save_config(self.cfg)
            self.ui("log", "sys", f"Claude key saved {where}. Claude mode is still off - say 'claude mode on' to use it.")
            if test:
                def work():
                    try:
                        ask_claude(key, model.get(), [{"role": "user", "content": "Reply with just: ready"}], timeout=25)
                        self.ui("log", "sys", "Claude test: the key works.")
                    except ClaudeError as err:
                        self.ui("log", "sys", f"Claude test failed: {err}")
                self.ui("log", "sys", "Testing the key with one tiny request...")
                threading.Thread(target=work, daemon=True).start()
            win.destroy()
        row = tk.Frame(win, bg=self.BG)
        row.pack(pady=14)
        self.mkbtn(row, "Save", save).pack(side="left", padx=6)
        self.mkbtn(row, "Save and test", lambda: save(True)).pack(side="left", padx=6)

    def install_voices_ui(self):
        def work():
            log = lambda m: self.ui("log", "sys", m)
            if not pip_install(["edge-tts"], log, "the natural voices (edge-tts)",
                               "Installed. Loading the voices..."):
                return
            try:
                import importlib
                globals()["edge_tts"] = importlib.import_module("edge_tts")
            except Exception as e:
                log(f"Installed, but PAC couldn't load it yet ({e}). Close PAC and open it again.")
                return
            self.cfg["neural"] = True
            save_config(self.cfg)
            self.speaker.neural_retry_at = 0.0
            self.speaker.voices_checked = False
            self.speaker.set_voice_code(self.speaker.voices[0][0])
            log("Natural voices are ready. Say  change voice  to hear the others, or  list voices.")
        threading.Thread(target=work, daemon=True).start()

    def edit_timetable(self, initial=None):
        ensure_timetable_file()
        if initial is None:
            try:
                initial = TIMETABLE_FILE.read_text(encoding="utf-8-sig")
            except Exception:
                initial = TIMETABLE_SAMPLE

        def save(text):
            TIMETABLE_FILE.write_text(text.rstrip() + "\n", encoding="utf-8")
            n = len(parse_timetable(text))
            if n:
                self.ui("log", "sys", f"Timetable saved: {n} class period(s) found. Try: what's my schedule.")
            else:
                self.ui("log", "sys", "Timetable saved, but I couldn't find any classes in it. Each line needs a "
                                      "day, a time range and a subject, e.g.  Monday 09:00-10:00 Maths, Room 204")
        self.text_dialog("Timetable",
                         "One class per line: day, start-end, subject, room.\n"
                         "Example:  Monday 09:00-10:00 Mathematics, Room 204\n"
                         "Tue/Thu 2 pm - 3 pm Chemistry   |   or paste a CSV grid (days across the top).\n"
                         "Lines starting with # are ignored.", initial, save, size="560x520")

    def import_timetable(self):
        """Pick a timetable file (.csv / .txt): it is read straight away, saved as clean editable lines, and the
        classes found are listed. If its layout still can't be understood, it opens in the editor instead."""
        from tkinter import filedialog, messagebox
        path = filedialog.askopenfilename(title="Import your timetable (.csv or .txt)",
                                          filetypes=[("Timetable", "*.csv *.txt *.tsv"), ("All files", "*.*")])
        if not path:
            return
        name = Path(path).name
        try:
            text = decode_text_file(Path(path).read_bytes())
            found = parse_timetable(text)
        except Exception as e:
            messagebox.showerror("Import failed", f"Could not read that file: {e}")
            return
        if not found:
            first = next((l.strip() for l in text.splitlines() if l.strip()), "")
            self.ui("log", "sys", f"I opened {name} but its layout isn't one I recognise yet (it starts: "
                                  f"\"{first[:70]}\"). Its contents are in the timetable editor - arrange them as one "
                                  "class per line, like  Monday 09:00-10:00 Maths, Room 204  and press Save.")
            self.edit_timetable(initial=text)
            return
        TIMETABLE_FILE.write_text(timetable_to_text(found, name), encoding="utf-8")
        days = sorted({e["day"] for e in found})
        self.ui("log", "sys", f"Imported {len(found)} class period(s) from {name}, covering "
                              f"{join_and([DAYS[d].capitalize() for d in days])}.")
        for d in days[:7]:
            todays = [e for e in found if e["day"] == d]
            self.ui("log", "sys", f"  {DAYS[d].capitalize()}: " + ",  ".join(
                f"{fmt_time(e['start'])} {e['subject']}" for e in todays[:8]) + (" ..." if len(todays) > 8 else ""))
        self.assistant.say(f"I've read your timetable. I found {len(found)} class periods. "
                           "Ask me, what's my schedule.")

    def on_trigger(self, kind):
        self.pulse = 1.0
        a = self.assistant
        if kind == "clap":
            self.append("sys", "Double clap heard.")
            a.asleep = False
            if self.mode != "voice" and self.voice_ok:
                self.set_mode("voice", persist=False)          # says "Voice mode on" itself
            else:
                a.say("I'm listening." if self.voice_ok else
                      "I'm here. Type your command, or install the voice packages to talk to me.")
        elif kind == "whistle":
            self.append("sys", "Whistle heard - opening YouTube.")
            a.say("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

    def do_shortcut(self):
        self.ui("log", "sys", make_shortcut())

    def toggle_autostart(self):
        want = self.autostart_var.get()

        def work():
            self.ui("log", "sys", make_autostart(want))
            self.ui("autostart_state", autostart_enabled())
        threading.Thread(target=work, daemon=True).start()

    def clear_chat(self):
        self.chat.configure(state="normal")
        self.chat.delete("1.0", "end")
        self.chat.configure(state="disabled")

    def text_dialog(self, title, help_text, initial, on_save, size="480x440"):
        tk = self.tk
        win = self.dialog(title, size)
        tk.Label(win, text=help_text, justify="left", wraplength=440, fg=self.RED_DIM, bg=self.BG,
                 font=(self.F, 9)).pack(anchor="w", padx=14, pady=(12, 6))
        frame = tk.Frame(win, bg=self.RED_DEEP, padx=1, pady=1)
        frame.pack(fill="both", expand=True, padx=14)
        txt = tk.Text(frame, bg=self.BG, fg=self.RED_TEXT, insertbackground=self.RED, relief="flat",
                      font=(self.F, 11), padx=8, pady=8, bd=0, highlightthickness=0,
                      selectbackground=self.RED, selectforeground=self.BG)
        txt.pack(fill="both", expand=True)
        txt.insert("1.0", initial)

        def save():
            on_save(txt.get("1.0", "end"))
            win.destroy()
        self.mkbtn(win, "Save", save).pack(pady=12)

    def add_knowledge_file(self):
        from tkinter import filedialog
        paths = filedialog.askopenfilenames(
            title="Add text files PAC can answer questions from",
            filetypes=[("Text files", "*.txt *.md *.csv"), ("All files", "*.*")])
        added = 0
        for p in paths:
            src = Path(p)
            if src.suffix.lower() not in Knowledge.EXTS:
                self.ui("log", "sys", f"Skipped {src.name}: PAC reads .txt, .md and .csv. "
                                      "Save PDFs / Word files as plain text first.")
                continue
            try:
                shutil.copy(src, KNOWLEDGE_DIR / src.name)
                added += 1
            except Exception as e:
                self.ui("log", "sys", f"Could not add {src.name}: {e}")
        if added:
            self.ui("log", "sys", f"Added {added} file(s). Ask me a question about them - no internet needed.")

    def mail_setup(self):
        tk = self.tk
        win = self.dialog("Email setup - sign in with Google", "520x640")
        tk.Label(win, justify="left", wraplength=480, fg=self.RED_DIM, bg=self.BG, font=(self.F, 9),
                 text=("You sign in on Google's own page - PAC never sees or stores your password. "
                       "One-time setup (about 5 minutes, free):\n"
                       "1. console.cloud.google.com > create a project.\n"
                       "2. APIs & Services > OAuth consent screen: type External, fill in the app name and your "
                       "email, add yourself under Test users, then press 'Publish app' (in Testing mode Google "
                       "signs you out every 7 days).\n"
                       "3. APIs & Services > Library > search 'Gmail API' > Enable.\n"
                       "4. Credentials > Create credentials > OAuth client ID > Application type: Desktop app.\n"
                       "5. Paste the Client ID and Client secret below, then press the button.\n"
                       "On the sign-in page click Advanced > 'Go to PAC (unsafe)' - that warning only appears "
                       "because it's your own unreviewed app.\n"
                       "PAC only moves mails to Trash when you say yes.")
                 ).pack(anchor="w", padx=14, pady=(12, 8))
        fields = {}
        for label, key, show in [("Your Gmail address", "mail_address", ""),
                                 ("Client ID", "mail_client_id", ""),
                                 ("Client secret", "mail_client_secret", "*")]:
            tk.Label(win, text=label, fg=self.RED_TEXT, bg=self.BG, font=(self.F, 9)).pack(anchor="w", padx=14)
            e = tk.Entry(win, show=show, bg=self.BG, fg=self.RED_TEXT, insertbackground=self.RED, relief="flat",
                         font=(self.F, 11), highlightthickness=1, highlightbackground=self.RED_DEEP,
                         highlightcolor=self.RED)
            e.pack(fill="x", padx=14, pady=(0, 8), ipady=5)
            e.insert(0, self.cfg.get(key, ""))
            fields[key] = e

        def sign_in():
            for key, e in fields.items():
                self.cfg[key] = e.get().strip()
            save_config(self.cfg)
            if not all(self.cfg[k] for k in fields):
                self.ui("log", "sys", "Please fill in all three boxes first.")
                return
            win.destroy()
            self.ui("log", "sys", "Your browser will open Google's sign-in page...")

            def work():
                try:
                    token = google_sign_in(self.cfg)
                    where = _secret_set(self.cfg, "mail_refresh_token", token)
                    save_config(self.cfg)
                    self.assistant.mailbox.reset()
                    self.assistant.mailbox.test()
                    self.ui("log", "sys", f"Signed in. Sign-in token kept {where}. Say 'check my mail'.")
                except Exception as e:
                    logger.exception("mail sign-in failed")
                    self.ui("log", "sys", f"Sign-in failed: {e}")
            threading.Thread(target=work, daemon=True).start()
        self.mkbtn(win, "Sign in with Google", sign_in).pack(pady=12)

    def import_vcard(self):
        from tkinter import filedialog, messagebox
        path = filedialog.askopenfilename(title="Import contacts (export this from your phone's Contacts app)",
                                          filetypes=[("vCard contacts", "*.vcf"), ("All files", "*.*")])
        if not path:
            return
        try:
            found = parse_vcf(path)
        except Exception as e:
            messagebox.showerror("Import failed", f"Could not read that file: {e}")
            return
        if not found:
            self.ui("log", "sys", "No contacts with both a name and a phone number were found in that file.")
            return
        self.cfg["contacts"].update(found)
        save_config(self.cfg)
        self.ui("log", "sys", f"Imported {len(found)} contact(s). Say 'list contacts' to hear them.")

    def edit_contacts(self):
        def save(text):
            contacts = {}
            for line in text.splitlines():
                if "=" in line:
                    name, num = line.split("=", 1)
                    name, num = name.strip().lower(), num.strip()
                    if name and re.search(r"\d{8,}", re.sub(r"\D", "", num)):
                        contacts[name] = num
            self.cfg["contacts"] = contacts
            save_config(self.cfg)
            self.ui("log", "sys", f"Saved {len(contacts)} contact(s).")
        self.text_dialog("Contacts",
                         "One per line:  name = phone number\nExample:  mom = 9876543210\n"
                         f"10-digit numbers get +{self.cfg.get('country_code', '91')} added automatically.",
                         "\n".join(f"{k} = {v}" for k, v in self.cfg["contacts"].items()), save)

    def edit_messages(self):
        def save(text):
            msgs = [l.strip() for l in text.splitlines() if l.strip()]
            if msgs:
                self.cfg["messages"] = msgs
                save_config(self.cfg)
                self.ui("log", "sys", f"Saved {len(msgs)} preloaded message(s).")
        self.text_dialog("Preloaded messages",
                         "One message per line. Line 1 is message 1, line 2 is message 2, and so on.\n"
                         "Say:  send message 2 to mom",
                         "\n".join(self.cfg["messages"]), save)

    # ----- memory
    def toggle_memory(self):
        self.cfg["memory_enabled"] = self.mem_var.get()
        save_config(self.cfg)
        self.append("sys", "Long-term memory is on: I'll remember what you tell me about yourself." if self.cfg["memory_enabled"]
                    else "Long-term memory is off: I won't learn or use anything about you. What I know is kept.")

    def set_memory_learn(self, key):
        self.cfg["memory_learn"] = key
        save_config(self.cfg)
        self.append("sys", {"all": "I'll learn from typed and spoken sentences about you.",
                            "typed": "I'll learn only from sentences you type. Spoken ones need the word remember.",
                            "explicit": "I'll only remember what you tell me with the word remember."}[key])

    def toggle_memory_habits(self):
        self.cfg["memory_habits"] = self.memhabit_var.get()
        save_config(self.cfg)
        self.append("sys", "I'll notice commands you repeat at the same time of day." if self.cfg["memory_habits"]
                    else "I've stopped noticing your habits. Routines I already noted are kept.")

    def toggle_memory_share(self):
        self.cfg["memory_share_ai"] = self.memshare_var.get()
        save_config(self.cfg)
        self.append("sys", "The AI brain and Claude may see the few memories relevant to a request (a local Ollama brain "
                           "always may)." if self.cfg["memory_share_ai"] else
                    "Memories are no longer sent to Claude. A local Ollama brain can still use them.")

    def memory_dialog(self):
        def save(text):
            gone, added = self.assistant.memory.replace_all(text)
            self.append("sys", f"Memory saved: {added} added, {gone} removed.")
        self.text_dialog("What PAC remembers about you",
                         "One memory per line, as [kind] text  (kind = preference, routine, person or fact).\n"
                         "Delete a line to forget it, edit a line to correct it, or add a new one.\n"
                         "Passwords, PINs and card numbers are never kept.",
                         "\n".join(self.assistant.memory.export_lines()), save, size="560x520")

    def memory_clear_ui(self):
        from tkinter import messagebox
        n = self.assistant.memory.count()
        if n and messagebox.askyesno("Forget everything", f"Forget all {n} things PAC has learned about you?"):
            self.assistant.memory.clear()
            self.append("sys", "Memory cleared.")
        elif not n:
            self.append("sys", "My memory of you is already empty.")

    # ----- the orb
    def animate(self):
        """Runs 25 times a second: eases the level toward the microphone's loudness (quick up, slow down,
        like a recorder's meter) and redraws the orb."""
        try:
            now = time.time()
            dt = min(0.1, max(0.01, now - self.last_frame))
            self.last_frame = now
            fresh = (now - self.level_time) < 0.4
            target = self.level_target if (self.capture_wanted() and fresh) else 0.0
            if self.speaker.busy():              # PAC is talking: let the orb pulse like a voice
                target = max(target, 0.32 + 0.22 * math.sin(now * 9.0) + 0.12 * math.sin(now * 15.3 + 1.0))
            target = min(1.0, max(target, self.pulse))
            self.pulse = max(0.0, self.pulse - dt * 1.6)
            k = 0.6 if target > self.level_shown else 0.14
            self.level_shown += (target - self.level_shown) * k
            if self.level_shown < 0.01:
                self.level_shown = 0.0
            self.draw_orb(dt)
        finally:
            self.root.after(40, self.animate)

    def draw_orb(self, dt):
        cv = self.cv
        w, h = cv.winfo_width(), cv.winfo_height()
        if w < 60 or h < 60:
            return
        cv.delete("all")
        self.orb.draw(cv, w / 2, h / 2 + 10, min(h * 0.33, w * 0.28), self.level_shown, dt)
        st = self.listener.state()
        hearing = st == "hearing" and not self.assistant.asleep
        dot = False
        if self.mode == "text":
            left = "Text mode"
            right = "Listening for claps and whistles" if self.capture_wanted() else "Microphone closed"
        elif not self.mic_on:
            left, right = "Microphone off", ""
        elif self.assistant.asleep:
            left, right = "Asleep", f"Boost {float(self.cfg.get('gain', 2.0)):.1f}x"
        elif hearing:
            el = max(0, int(time.time() - self.listener.rec_started))
            left, dot = f"REC  {el // 60:02d}:{el % 60:02d}", int(time.time() * 2) % 2 == 0
            right = f"Boost {float(self.cfg.get('gain', 2.0)):.1f}x"
        else:
            left = "Processing" if st == "recognizing" else "Standby"
            right = f"Boost {float(self.cfg.get('gain', 2.0)):.1f}x"
        if self.gesture.running:
            right = ("Gestures on   " + right).strip()
        x0 = 16
        if hearing:
            if dot:
                cv.create_oval(16, 9, 26, 19, fill=self.RED, outline="")
            x0 = 34
        cv.create_text(x0, 14, text=left, anchor="w", fill=self.RED if hearing else self.RED_TEXT,
                       font=(self.FM, 10, "bold"))
        cv.create_text(w - 16, 14, text=right, anchor="e", fill=self.RED_DIM, font=(self.FM, 9))

    # ----- window plumbing
    def append(self, who, text):
        c = self.chat
        c.configure(state="normal")
        if who == "you":
            c.insert("end", "You   ", "you_label")
        elif who == "pac":
            c.insert("end", "PAC   ", "pac_label")
        start = c.index("end-1c")
        c.insert("end", text + "\n", who if who in ("you", "pac", "list") else "sys")
        c.configure(state="disabled")
        c.see("end")
        if who == "list":
            c.see(start)                      # a long list must show from its first line, not just its tail

    def refresh_badge(self):
        claude = getattr(self.assistant, "claude_on", False)
        if self.mode == "voice":
            self.badge.configure(text="Voice mode, Google speech" + (" + Claude" if claude else ""),
                                 bg=self.RED, fg=self.BG, highlightbackground=self.RED)
        elif claude:
            self.badge.configure(text="Text mode + Claude (online)", bg=self.RED, fg=self.BG,
                                 highlightbackground=self.RED)
        else:
            self.badge.configure(text="Text mode, offline" if not self.cfg.get("background_search", True)
                                 else "Text mode, quiet web lookups", bg=self.BG, fg=self.RED,
                                 highlightbackground=self.RED)

    def refresh_status(self):
        a = self.assistant
        st = self.listener.state()
        if self.mode == "text":
            txt, col = ("Type a command below" + ("  |  listening for claps and whistles" if self.capture_wanted() else "")), self.RED_TEXT
        elif not self.mic_on:
            txt, col = "Microphone is off", self.RED_DIM
        elif a.asleep:
            txt, col = "Sleeping - say 'wake up'", self.RED_DIM
        elif self.speaker.busy():
            txt, col = "Speaking...", self.RED
        elif a.dictating:
            txt, col = "Dictation on - say 'stop typing' when done", self.RED_MID
        elif st == "hearing":
            txt, col = "Hearing you...", self.RED
        elif st == "recognizing":
            txt, col = "Recognizing...", self.RED_TEXT
        else:
            txt, col = "Listening...", self.RED_TEXT
        if self.gesture.running:
            txt += "  |  gestures on"
        self.status.configure(text=txt, fg=col)
        if st == "recognizing":
            live = "Recognizing..."
        elif time.time() < self.heard_until:
            live = f'Heard: "{self.heard_text}"'
        else:
            live = ""
        if self.live.cget("text") != live:
            self.live.configure(text=live)

    def poll(self):
        try:
            while True:
                ev = self.ui_q.get_nowait()
                kind = ev[0]
                if kind == "log":
                    self.append(ev[1], ev[2])
                elif kind == "heard":
                    self.heard_text, self.heard_until = ev[1], time.time() + 6
                elif kind == "set_mode":
                    self.set_mode(ev[1])
                elif kind == "trigger":
                    self.on_trigger(ev[1])
                elif kind == "timetable_edit":
                    self.edit_timetable()
                elif kind == "timetable_import":
                    self.import_timetable()
                elif kind == "airdrag_cmd":
                    self.set_air_drag(ev[1] == "on")
                elif kind == "gesture_cmd":
                    if ev[1] in ("on", "off"):
                        self.set_gestures(ev[1] == "on")
                        self.assistant.say("Gesture control is on. Make a gesture in front of the camera."
                                           if ev[1] == "on" else "Gesture control is off.")
                    elif ev[1] == "teach":
                        self.teach_gesture_dialog()
                    elif ev[1] == "delete":
                        self.delete_gestures_dialog()
                    else:
                        self.say_gesture_list()
                elif kind == "gesture_state":
                    self.gest_var.set(bool(ev[1]))
                    if ev[1]:
                        self.append("sys", "Gesture control is on. It keeps watching while you use other apps.")
                elif kind == "claude_state":
                    self.claude_var.set(bool(ev[1]))
                    self.refresh_badge()
                elif kind == "claude_setup":
                    self.claude_var.set(False)
                    self.claude_setup()
                elif kind == "memory_edit":
                    self.memory_dialog()
                elif kind == "memory_state":
                    self.mem_var.set(bool(ev[1]))
                elif kind == "voice_changed":
                    self.nvoice_var.set(ev[1])
                elif kind == "ar_cmd":
                    self.set_ar(ev[1] == "on")
                    self.assistant.say("Augmented reality is on. Hold something in the box to teach it."
                                       if ev[1] == "on" else "Augmented reality is off.")
                elif kind == "ar_state":
                    self.ar_var.set(bool(ev[1]))
                    if not ev[1]:
                        self.cfg["ar_enabled"] = False
                        save_config(self.cfg)
                elif kind == "ar_error":
                    self.ar_var.set(False)
                    self.cfg["ar_enabled"] = False
                    save_config(self.cfg)
                    self.append("sys", ev[1])
                elif kind == "ar_learn_prompt":
                    self.ar_learn_dialog()
                elif kind == "face_cmd":
                    self.set_faces(ev[1] == "on")
                    self.assistant.say("Face recognition is on." if ev[1] == "on" else "Face recognition is off.")
                elif kind == "face_security":
                    self.facesec_var.set(bool(ev[1]))
                elif kind == "submit":
                    self.submit(ev[1])
                elif kind == "face_rescue":
                    self._face_rescue_dialog(ev[1])
                elif kind == "face_error":
                    self.face_var.set(False)
                    self.cfg["face_enabled"] = False
                    save_config(self.cfg)
                    self.append("sys", ev[1])
                elif kind == "gesture_error":
                    self.gest_var.set(False)
                    self.set_air_drag(False, announce=False)
                    self.cfg["gesture_enabled"] = False
                    save_config(self.cfg)
                    self.append("sys", ev[1])
                elif kind == "gesture_fired":
                    if ev[3]:
                        self.append("sys", f"Gesture: {gesture_title(self.cfg, ev[1])}  ->  {ev[2]}")
                        self.pulse = 0.8
                elif kind == "voice_offline":
                    if self.mode == "voice":
                        self.set_mode("text", persist=False, announce=False)
                        self.append("sys", f"Couldn't reach Google's speech service ({ev[1]}). Switched to Text "
                                           "mode, which works offline. Switch back from Menu > Mode when "
                                           "you're online.")
                        self.assistant.say("I can't reach the internet, so I've switched to text mode.")
                elif kind == "autostart_state":
                    self.autostart_var.set(bool(ev[1]))
                elif kind == "quit":
                    self.quit_when_quiet()
        except queue.Empty:
            pass
        self.refresh_status()
        self.root.after(100, self.poll)

    def quit_when_quiet(self):
        if self.speaker.busy():
            self.root.after(300, self.quit_when_quiet)
        else:
            self.on_close()

    def on_close(self):
        self.listener.stop.set()
        self.gesture.stop_engine()
        self.faces.stop_engine()
        self.ar.stop_engine()
        try:
            self.assistant.transfer_stop()
        except Exception:
            pass
        try:
            self.speaker.stop_now()
        except Exception:
            pass
        self.root.destroy()


def main():
    try:
        if OS == "Windows":
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)  # crisp text on high-DPI screens
    except Exception:
        pass
    import tkinter as tk
    root = tk.Tk()
    try:
        PacApp(root)
        root.mainloop()
    except Exception:
        logger.exception("fatal")
        from tkinter import messagebox
        messagebox.showerror("PAC", f"PAC hit a problem. Details are in {LOG_FILE}")


if __name__ == "__main__":
    main()
