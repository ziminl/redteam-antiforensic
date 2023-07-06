


import subprocess

def delete_event_logs():
    # Run the command to clear event logs
    subprocess.run(['wevtutil', 'el'], capture_output=True, text=True)
    
delete_event_logs()


