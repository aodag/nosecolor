from nose.plugins.base import Plugin
from termcolor import colored
import traceback

class NoseColorPlugin(Plugin):
    name = "nosecolor"

    def options(self, parser, env):
        parser.add_option(
            "--color", 
            action="store_true", 
            dest="color",
            help="display color report.")

    def configure(self, options, conf):
        if not self.can_configure:
            return
        self.enabled = options.color
        self.conf = conf

    def setOutputStream(self, stream):
        self.stream = stream
        class dummy:
            def write(self, *arg):
                pass
            def writeln(self, *arg):
                pass
            def flush(self):
                pass
        return dummy()


    def addError(self, test, error):
        self.stream.writeln("=" * 80)
        self.stream.writeln(colored(test, "red"))
        self.stream.writeln("".join(traceback.format_exception(*error)))
        self.stream.writeln("=" * 80)
        
    def addFailure(self, test, error):
        self.stream.writeln("=" * 80)
        self.stream.writeln(colored(test, "red"))
        self.stream.writeln("".join(traceback.format_exception(*error)))
        self.stream.writeln("=" * 80)

    def finalize(self, result):
        if result.errors or result.failures:
            color = "red"
        else:
            color = "green"

        self.stream.write(colored("Ran %d test " % (result.testsRun,), color))
        if result.errors:
            self.stream.write(colored("%d errors " % len(result.errors), color))
        if result.failures:
            self.stream.write(colored("%d failures " % len(result.failures), color))
        self.stream.writeln("")

