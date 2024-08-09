#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None:
      return name
  return "{} {}".format(result[2], result[1])

# if pattern does not match then code return enexpected error so test cases also failed so that way we make some if statement for validation


