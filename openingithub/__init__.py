from subprocess import Popen
from fman import DirectoryPaneCommand, show_alert

GITHUB_BINARY = "/usr/local/bin/github"

class OpenInGithub(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			Popen('%s "%s"' % (GITHUB_BINARY, file_under_cursor), shell=True)
		else:
			show_alert("No file selected.")
