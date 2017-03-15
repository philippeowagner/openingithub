from subprocess import Popen
from fman import DirectoryPaneCommand, show_alert, load_json

PLUGIN_SETTINGS = load_json("OpenInGithub Settings.json")[0]
GITHUB_BINARY = PLUGIN_SETTINGS["github_binary"]

class OpenInGithub(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			Popen('%s "%s"' % (GITHUB_BINARY, file_under_cursor), shell=True)
		else:
			show_alert("No file selected.")
