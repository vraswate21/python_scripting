import os
import time

now = time.time()

log_dir = "test-logs"

for file in os.listdir(log_dir):
    file_path = os.path.join(log_dir, file)
    if file.endswith(".log") and os.stat(file_path).st_mtime < now - 7 * 86400:
        os.remove(file_path)
        print(f"deleted: {file}")