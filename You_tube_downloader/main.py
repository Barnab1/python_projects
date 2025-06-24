#Before getting started it is important to install "yt-dlp" by running
# pip install yt-dlp


import subprocess
import os

# Ask user for the YouTube link
link = input("Enter the YouTube video URL: ").strip()
link = link.split('&')[0]  # Remove playlist part, keep only the video

# Ask user for destination folder
destination = input("Enter the destination folder (default is current folder): ").strip()

# If empty, use current directory
if not destination:
    destination = os.getcwd()
else:
    # Create directory if it doesn't exist
    destination = os.path.abspath(destination)
    os.makedirs(destination, exist_ok=True)

# Run yt-dlp
try:
    subprocess.run(["python", "-m", "yt_dlp", "-P", destination, link], check=True)
    print(f"✅ Download completed and saved to: {destination}")
except subprocess.CalledProcessError as e:
    print("❌ Download failed:", e)