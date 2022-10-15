import subprocess
import datetime

if __name__ == "__main__":
    # Get the current date and time
    now = datetime.datetime.now()
    string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Commit the changes
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', string])
