import shutil
import subprocess
from fman import DirectoryPaneCommand, show_alert


GITHUB_PATH = shutil.which("github")

if GITHUB_PATH is None:
    raise ValueError("Github command-line tool not found in PATH. Please install Github or add it to your PATH.")

class OpenInGithub(DirectoryPaneCommand):
    def __call__(self):
        file_under_cursor_unf = self.pane.get_file_under_cursor() 
        file_under_cursor = file_under_cursor_unf if not file_under_cursor_unf.startswith("file://") else file_under_cursor_unf[7:]
        
        if not file_under_cursor:
            show_alert("No file selected.")
            return
        try:
            subprocess.run([GITHUB_PATH, file_under_cursor], shell=True)
            
        except subprocess.CalledProcessError:
            show_alert("Failed to open file in Github.")
