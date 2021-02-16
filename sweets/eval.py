import os

print(eval("1+1"))
print(eval("os.getcwd()"))
print(eval("os.chmod('%s', 0777)" % 'test.txt'))


# A user-defined method named "eval" should not get flagged.
class Test(object):
    """This class ..."""
    def eval(self):
        print("hi")
    def foo(self):
        self.eval()

Test().eval()
