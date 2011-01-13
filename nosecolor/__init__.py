from nose.plugins.base import Plugin
from termcolor import colored

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
        return dummy()

    def finalize(self, result):
        self.stream.write("Ran %d test " % (result.testsRun,))
        if result.wasSuccessful():
            self.stream.writeln("[" + colored("SUCCESS", "green") + "]")
        else:
            self.stream.writeln("[" + colored("FAILED", "red") + "]")
            self.stream.writeln('failures=%d errors=%d' % (len(result.failures), len(result.errors)))
        for test, e in result.errors:
            print test

        for test, e in result.failures:
            print test

