import os
import sys
import shutil
import time

def sync_folders(source_folder, replica_folder, log_file):
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    while True:
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_msg = "{}: Synchronizing {} to {}\n".format(timestamp, source_folder, replica_folder)
            with open(log_file, "a") as f:
                f.write(log_msg)
            print(log_msg)

            for file_name in os.listdir(source_folder):
                source_path = os.path.join(source_folder, file_name)
                replica_path = os.path.join(replica_folder, file_name)

                if os.path.isdir(source_path):
                    sync_folders(source_path, replica_path, log_file)
                else:
                    if os.path.exists(replica_path):
                        os.remove(replica_path)
                    shutil.copy2(source_path, replica_path)

            for file_name in os.listdir(replica_folder):
                replica_path = os.path.join(replica_folder, file_name)
                source_path = os.path.join(source_folder, file_name)
                if not os.path.exists(source_path):
                    os.remove(replica_path)

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_msg = "{}: Synchronization complete.\n".format(timestamp)
            with open(log_file, "a") as f:
                f.write(log_msg)
            print(log_msg)

            time.sleep(sync_interval)
        except Exception as e:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_msg = "{}: Error during synchronization: {}\n".format(timestamp, e)
            with open(log_file, "a") as f:
                f.write(log_msg)
            print(log_msg)

if __name__ == "__main__":
    source_folder = sys.argv[1]
    replica_folder = sys.argv[2]
    sync_interval = int(sys.argv[3])
    log_file = sys.argv[4]

    sync_folders(source_folder, replica_folder, log_file)