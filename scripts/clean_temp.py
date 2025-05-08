import os
import shutil
import tempfile

def run():
    temp_dir = tempfile.gettempdir()
    print(f"Cleaning the temp folder: {temp_dir}")
    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
        print("Temp files cleaned.")
    except Exception as e:
        print(f"error: {e}")