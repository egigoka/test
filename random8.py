#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
class Random:
    @staticmethod
    def integer(min, max):  # return random integer
        import random
        return random.randrange(min, max+1)

    @staticmethod
    def float(min, max):  # return random floating number
        import random
        return random.uniform(min, max)

    @staticmethod
    def string(length):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
