# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def write(output_file, bytes, var_name):
    output_file.write("static const uint8_t {var_name}[] = {{\n  ".format(var_name=var_name))
    for byte, index in zip(bytes, xrange(0, len(bytes))):
        if index != 0 and index % 16 == 0:
            output_file.write("/* bytes {0} - {1} */\n  ".format(index - 16, index))
        output_file.write("0x%02x, " % ord(byte))
    output_file.write("\n};\n")
