"""Build PAC with Nuitka (compiled to native code, no readable Python in the exe), then write docs/version.json.

Run on Windows, inside your venv, from the PRIVATE source folder:
    python build_release.py 1.0.0 <github-username> [public-releases-repo] [--onefile]
The releases repo is the PUBLIC one that holds only downloads and the website (default: pac-releases).
Needs: pip install nuitka   and a C compiler. Nuitka offers to download MinGW the first time - say yes.
Result: dist/PAC-<version>.zip and an updated docs/version.json."""
import hashlib, json, pathlib, shutil, subprocess, sys, zipfile

if len(sys.argv) < 3:
    sys.exit(__doc__)
version, user = sys.argv[1], sys.argv[2]
repo = sys.argv[3] if len(sys.argv) > 3 else "pac-releases"
root = pathlib.Path(__file__).parent
dist = root / "dist"
dist.mkdir(exist_ok=True)

import importlib.util
# Packages PAC loads dynamically (voice engines, camera models, key stores). Nuitka only sees plain imports, so name them.
EXTRA = ["mediapipe", "cv2", "speech_recognition", "pyttsx3", "edge_tts", "sounddevice", "_sounddevice_data",
         "segno", "keyring", "pyautogui", "PIL", "psutil"]
include = []
for pkg in EXTRA:
    spec = importlib.util.find_spec(pkg)
    if spec and spec.submodule_search_locations:        # a real package (a folder): include it and its data files
        include += [f"--include-package={pkg}", f"--include-package-data={pkg}"]
    elif spec:                                          # a single-file module (e.g. sounddevice): different flag
        include += [f"--include-module={pkg}"]
    else:
        print(f"note: {pkg} is not installed - that feature will be missing from the build")
onefile = "--onefile" in sys.argv          # optional: one single .exe (needs lots of memory; folder build is safer)
sys.argv = [a for a in sys.argv if a != "--onefile"]
cmd = [sys.executable, "-m", "nuitka", "--standalone"] + (["--onefile"] if onefile else []) + [
       "--windows-console-mode=disable", "--enable-plugin=tk-inter",
       "--assume-yes-for-downloads", "--remove-output",
       # The compiler ran out of memory on huge SymPy files. SymPy (exact algebra) is optional in PAC, so leave it out,
       # skip every package's test files, and compile gently.
       "--nofollow-import-to=sympy", "--nofollow-import-to=*.tests", "--nofollow-import-to=*.test",
       "--nofollow-import-to=*.testing", "--low-memory", "--jobs=2",
       f"--output-dir={dist}", "--output-filename=PAC.exe",
       f"--product-version={version}", "--product-name=PAC", "--company-name=PAC",
       "--file-description=PAC voice assistant"] + include + ["pac.py"]
model = root / "hand_landmarker.task"
if model.exists():
    cmd.insert(-1, f"--include-data-files={model}=hand_landmarker.task")
else:
    print("note: hand_landmarker.task not found - gestures will download it on first use (needs internet once)")
subprocess.run(cmd, check=True, cwd=root)

zip_path = dist / f"PAC-{version}.zip"
if onefile:
    exe = dist / "PAC.exe"
    if not exe.exists():
        sys.exit("Build finished but dist/PAC.exe is missing - read the Nuitka messages above.")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(exe, "PAC.exe")
else:
    folder = dist / "pac.dist"                 # standalone build: a folder holding PAC.exe and its files
    if not (folder / "PAC.exe").exists():
        sys.exit("Build finished but dist/pac.dist/PAC.exe is missing - read the Nuitka messages above.")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in folder.rglob("*"):
            if f.is_file():
                z.write(f, pathlib.Path("PAC") / f.relative_to(folder))
sha = hashlib.sha256(zip_path.read_bytes()).hexdigest()
url = f"https://github.com/{user}/{repo}/releases/download/v{version}/{zip_path.name}"
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "version.json").write_text(
    json.dumps({"version": version, "url": url, "sha256": sha, "notes": f"PAC {version}"}, indent=2), encoding="utf-8")
print(f"\nBuilt {zip_path}\nSHA256 {sha}")
print(f"Next: in the PUBLIC repo {user}/{repo} create release v{version}, attach the zip, then push docs/version.json there.")
