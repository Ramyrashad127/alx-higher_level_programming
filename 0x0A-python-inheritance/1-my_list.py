#!/usr/bin/python3
""" module """


class MyList(list):
    """ new """
    pass

    def print_sorted(self):
        """ print """

        print(sorted(list(self)))

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/1-my_list.txt')
