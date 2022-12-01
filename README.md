![pylint workflow](https://github.com/mwilliams123/motion-sensor/actions/workflows/pylint.yml/badge.svg)
# Motion Sensor
A motion sensor built on Raspberry Pi hardware using the Camera module.
It works by performing background estimation to detect when objects of interest are in frame, and records video when the motion sensor is activated. 

## Usage
### Installation
Requires Raspberry Pi 4 and Camera V2 module.
If you do not have the latest Rasbian image, you may have to install PiCamera2:
```
sudo apt install -y python3-picamera2
```
To convert video recordings to a watchable format, install ffmpeg:
```
sudo apt install ffmpeg
```
### Running the code
Start the motion sensor with
```
python main.py
```
This will produce video files with the .h264 encoding. Convert these to a watchable format by running:
```
python h264_to_mkv.py
```
This script takes .h264 video files in `videos/` and produces .mkv files in the `processed\` folder.


