import requests
import json
import os
import re
import time
import argparse
import pathlib
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

agent_id=''
url = ''
bearer_token=''
base_folder = ''

def save_text_to_responses_file(text, image_filename=None):

    responses_folder = os.path.join(watched_folder, "output")
    # Ensure the folder exists
    os.makedirs(responses_folder, exist_ok=True)

    stem = pathlib.Path(image_filename).stem

    new_filename = f"{stem}.txt"
    full_path = os.path.join(responses_folder, new_filename)

    # Write text to the new file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Saved to {full_path}")

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = os.path.abspath(event.src_path)
            filename = os.path.basename(file_path)
            ext = os.path.splitext(file_path)[1].lower()
            # Only process image files
            if ext not in [".png", ".jpg", ".jpeg"]:
                print(f"Ignored file (unsupported type): {file_path}")
                return

            print(f"New file detected: {file_path}")

            try:
                file_url = f"http://host.docker.internal:8001/{filename}"
                payload = {
                    "stream": False,
                    "messages": [
                        {
                            "role": "user",
                            "content": f"Please look at the image at {file_url}, and give me current market trends based on the products shown in the image. Based on those trends, can you make recommendations for the rearrangement of the products on the shelf?"
                        }
                    ]
                }

                response = requests.post(
                    url,
                    headers={"Content-Type": "application/json", "Authorization": f"Bearer {bearer_token}"},
                    data=json.dumps(payload)
                )
                status = response.status_code
                result = response.json()
                text = result["choices"][0]["message"]["content"]
                print(f"POST response: {status} - {text}")

                answer = f"""
New File Processed: {os.path.basename(file_path)}

Response: {text}
"""
                save_text_to_responses_file(answer, image_filename=filename)

            except Exception as e:
                print(f"Error during POST request: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process an image file with an AI agent.")
    parser.add_argument("--agent_id", required=True, help="The ID of the target agent.")
    parser.add_argument("--target_folder", required=True, help="The base folder for images and responses.")
    parser.add_argument("--token", required=True, help="The bearer token of the local instance.")
    args = parser.parse_args()

    agent_id = args.agent_id
    url = f"http://localhost:4321/api/v1/orchestrate/{agent_id}/chat/completions"
    watched_folder = args.target_folder
    bearer_token = args.token

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=watched_folder, recursive=False)

    print(f"Watching folder: {watched_folder}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping observer...")
        observer.stop()
    observer.join()