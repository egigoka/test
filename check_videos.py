import subprocess
import json
import os
import sys
from commands import *


TIMEOUT = 1800


def validate_video(video_path, quick=False):
    
    if not os.path.exists(video_path):
        return False, "File does not exist"
    
    if os.path.getsize(video_path) == 0:
        return False, "File is empty"
    
    try:
        # Get comprehensive video info
        result = subprocess.run([
            'ffprobe', '-v', 'quiet', '-print_format', 'json',
            '-show_format', '-show_streams', '-show_error', video_path
        ], capture_output=True, text=True, timeout=TIMEOUT)
        
        if result.returncode != 0:
            return False, f"ffprobe failed: {result.stderr}"
        
        data = json.loads(result.stdout)
        
        if 'error' in data:
            return False, f"Format error: {data['error'].get('string', 'Unknown error')}"
        
        streams = data.get('streams', [])
        if not streams:
            return False, "No streams found"
        
        video_streams = [s for s in streams if s.get('codec_type') == 'video']
        if not video_streams:
            return False, "No video streams found"
        
        format_info = data.get('format', {})
        duration = float(format_info.get('duration', 0))
        
        if duration <= 0:
            return False, "Invalid or zero duration"
        
        if quick:
            return True, f"Valid video: {duration/3600:.2f}h, {len(video_streams)} video stream(s)"
        
        result = subprocess.run([
            'ffmpeg', '-v', 'error', '-i', video_path, 
            '-t', '1', '-f', 'null', '-'
        ], capture_output=True, text=True, timeout=TIMEOUT)
        
        if result.returncode != 0:
            return False, f"Cannot decode video start: {result.stderr}"
        
        mid_time = duration / 2
        result = subprocess.run([
            'ffmpeg', '-v', 'error', '-ss', str(mid_time),
            '-i', video_path, '-t', '1', '-f', 'null', '-'
        ], capture_output=True, text=True, timeout=TIMEOUT)
        
        if result.returncode != 0:
            return False, f"Cannot decode video middle: {result.stderr}"
        
        end_offset = min(10, duration * 0.01)
        end_time = max(0, duration - end_offset)
        
        result = subprocess.run([
            'ffmpeg', '-v', 'error', '-ss', str(end_time),
            '-i', video_path, '-t', '1', '-f', 'null', '-'
        ], capture_output=True, text=True, timeout=TIMEOUT)
        
        if result.returncode != 0:
            return False, f"Cannot decode video end: {result.stderr}"
        
        return True, f"Video fully valid: {duration/3600:.2f}h, decodable throughout"
        
    except subprocess.TimeoutExpired:
        return False, "Validation timed out"
    except json.JSONDecodeError:
        return False, "Invalid ffprobe output"
    except Exception as e:
        return False, f"Validation error: {str(e)}"

path = sys.argv[1]
for root, dirs, files in OS.walk(path):
    for cnt, file in enumerate(files):
        prog = f"{cnt+1} / {len(files)}"
        Print.rewrite(prog, *Console.fit(file))
        if file.endswith(".py") or file.endswith(".720.tmp.mp4"):
            continue
        
        is_valid, message = validate_video(Path.combine(root, file))
        if not is_valid:
            Print.rewrite()
            print(file)
            Print.colored(f"Result: {message}", "red")
