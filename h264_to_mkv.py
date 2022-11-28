"""
Video Converter.

This script takes all of the .h264 video encodings found in the videos/ subdir
and writes them to .mkv files in the processed/ subdir.

Usage:
    python h264_to_mkv.py
"""
import os
import subprocess

VIDEO_DIR = 'videos/'
OUT_DIR = 'processed/'
for i, file in enumerate(os.listdir(VIDEO_DIR)):
    filename = VIDEO_DIR + file
    outfile = f"{VIDEO_DIR}video{i}.mvk"
    subprocess.run(['ffmpeg', '-y', '-r', '30', '-i', filename, outfile], check=True)
