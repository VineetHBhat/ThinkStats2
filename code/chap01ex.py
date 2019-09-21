"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def read_2002_fem_resp(stata_file = '2002FemResp.dct', data_file = '2002FemResp.dat.gz'):
    fixed_width_object = thinkstats2.ReadStataDct(stata_file)
    actual_data = fixed_width_object.ReadFixedWidth(data_file, compression='gzip', nrows=None)
    return actual_data

def cross_validate_pregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, item in resp.pregnum.items():
        case_id = resp.caseid[index]
        indices = preg_map[case_id]

        if len(indices) != item:
            print(case_id, len(indices), item)
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = read_2002_fem_resp()
    print(resp.pregnum.value_counts().sort_index())
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[0] == 2610)
    assert(cross_validate_pregnum(resp) == True)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
