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

# test 123
# test 234
# test 345
# test 456
# test 567
# test 678
# test 789
# test 899
