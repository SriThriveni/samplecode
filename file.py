import time

def monitor_log_file(log_file_path):
    # Open the log file in read mode
    with open(log_file_path, 'r') as log_file:
        # Seek to the end of the file
        log_file.seek(0, 2)
        
        while True:
            # Read new lines continuously
            new_line = log_file.readline()
            
            # If new line is not empty, print it
            if new_line:
                print(new_line.strip())  # Strip to remove newline character
            
            # Wait for a short interval before checking for new lines again
            time.sleep(0.1)

if __name__ == "__main__":
    log_file_path = "path_to_your_log_file.log"  # Replace with the path to your log file
    monitor_log_file(log_file_path)
