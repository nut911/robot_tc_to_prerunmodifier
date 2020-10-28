from robot.api import SuiteVisitor


class SetTimeout(SuiteVisitor):

    def __init__(self, timeout):
        self.timeout = str(timeout)

    def visit_test(self, test):
        """Set identical timeout for each testcase."""
        test.timeout = self.timeout
