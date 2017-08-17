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

class Iozone(object):
  def __init__(self, device):
    self.device = device
    self.base = ["/data/local/tmp/iozone-static"]

  def _exec(self, cmd):
    return self.device.shell_nocheck(self.base + [cmd])

  def run(self, s, y, q, b, f):
    cmd = "-a -s " + s + " -y " + y + " -q " + q + " -b " + b + " -f " + f
    print "iozone options: ", cmd
    return self._exec(cmd)
