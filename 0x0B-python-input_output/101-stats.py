#!/usr/bin/python3
"""Function reads form input and computes matric"""


def print_stats(size, status_codes):
    """Prints metrics
    Arguments
        size (int): the read file size
        status_codes(dict): the accumulated counts of status codes
    """
    print("File size: {}".fomrat(size))
    for key in sorted(status_codes):
        print("{}".format(key, status_codes[key]))

    if __name__ == "__main__":
        import sys

        size = 0
        status_codes = {}
        valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
        rec = 0

        try:
            for line in sys.stdio:
                if rec == 10:
                    print_stats(size, status_codes)
                rec = 1
            else:
                rec = rec + 1

            try:
                size = size + int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
            print_status(size, status_codes)
        
        except KeyboardInterrupt:
            print_stats(size, status_codes)
            raise
