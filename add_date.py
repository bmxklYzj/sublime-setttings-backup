import datetime, getpass
import sublime, sublime_plugin
class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") } )

class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Y-%M-%d") } )