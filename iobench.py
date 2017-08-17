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

  def test_iozone_all(self):
    """Test that all of io cases by iozone."""

    target_dir = "/data/local/tmp/"

    self.device.root()
    self.device.wait()
    self.device.push("./iozone-static", target_dir)

    # minfile
    res_file = target_dir + "minfile_res.xls"
    test_file = target_dir + "test_minfile"
    exit_code, stdout, stderr = self.iozone.run("64M", "4k", "128k", res_file, test_file)
    print stdout

if __name__ == '__main__':
  unittest.main(verbosity=3)
