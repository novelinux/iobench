# Copyright (C) 2017 The MIUI Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import iozone
import os
import shelltest
import unittest

class IoBench(shelltest.ShellTest):
  def __init__(self, *args, **kwargs):
    super(IoBench, self).__init__(*args, **kwargs)
    self.iozone = iozone.Iozone(self.device)

  def get_total_mem(self):
    self.device.pull("/proc/meminfo", ".")

    with open("./meminfo", "r") as f:
      mem = f.readline()
      while not mem.startswith("MemTotal:"):
        mem = f.readline()

    print mem
    # KiB convert to MiB
    mem = int(mem.split()[1]) / 1024
    os.unlink("./meminfo")

    return mem

  def test_iozone_all(self):
    """Test that all of io cases by iozone"""

    target_dir = "/data/local/tmp/"

    self.device.root()
    self.device.wait()
    self.device.push("./iozone-static", target_dir)

    # minfile
    res_file = target_dir + "res_minfile.xls"
    test_file = target_dir + "test_minfile"
    size = str(self.get_total_mem()) + "M"
    exit_code, stdout, stderr = self.iozone.run(size, "4k", "128k", res_file, test_file)
    print stdout
    self.device.pull(res_file, ".");

if __name__ == '__main__':
  unittest.main(verbosity=3)
