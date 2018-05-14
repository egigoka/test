#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
__version__ = "0.0.1"

class List:
    @staticmethod
    def flatterize(input_list):
        import copy
        if not ((isinstance(input_list,list)) or (isinstance(input_list,tuple))):
            raise TypeError("object of type '"+str(type(input_list))+"' can't be flatterized")
        output_list = copy.deepcopy(list(input_list))
        cnt = 0
        for object in output_list:
            if not isinstance(object, (str,int)):
                output_list.pop(cnt)
                for item in reversed(object):
                    output_list.insert(cnt, item)
            cnt+=1
        return output_list

    @staticmethod
    def split_every(list_input, count):
        count = int(count)
        output_lists = [list_input[x:x+count] for x in range(0, len(list_input), count)]  # https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
        return output_lists  # todo отдебажить пограничные моменты
