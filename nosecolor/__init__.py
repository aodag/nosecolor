# Copyright (c) 2011 aodag.jp
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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
        self.verbosity = options.verbosity

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

    def addSuccess(self, test):
        self.stream.writeln(colored(test, "green"))

    def addError(self, test, error):
        self.stream.write('[' + colored('ERROR', 'red') + '] ')
        self.stream.writeln(colored(test, "red"))
        self.stream.writeln("".join(traceback.format_exception(*error)))
        self.stream.writeln("=" * 80)
        
    def addFailure(self, test, error):
        self.stream.write('[' + colored('FAILURE', 'red') + '] ')
        self.stream.writeln(colored(test, "red"))
        if self.verbosity:
            self.stream.writeln("".join(traceback.format_exception(*error)))
            self.stream.writeln("=" * 80)

    def finalize(self, result):
        if result.errors or result.failures:
            color = "red"
        else:
            color = "green"

        self.stream.write(colored("Ran %d test " % (result.testsRun,), color))
        self.stream.write(colored("%d errors " % len(result.errors), color))
        self.stream.write(colored("%d failures " % len(result.failures), color))
        self.stream.writeln("")

