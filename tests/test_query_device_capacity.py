# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright © 2015 Tim Bielawa <timbielawa@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Test reading block device capacities
"""

from . import TestCase
import bitmath
import mock
import struct

device_file_no = mock.Mock(return_value=4)
device = mock.MagicMock('file')
device.fileno = device_file_no
device.name = "/dev/sda"

non_device_file = mock.MagicMock('file')
non_device_file.name = "/home/"


class TestQueryDeviceCapacity(TestCase):
    def test_query_device_capacity_linux_everything_is_wonderful(self):
        """query device capacity works on a happy Linux host"""
        with mock.patch('os.stat') as os_stat,\
                mock.patch('stat.S_ISBLK') as stat_is_block,\
                mock.patch('platform.system') as plat_system,\
                mock.patch('fcntl.ioctl') as ioctl:
            os_stat.return_value = mock.Mock(st_mode=25008)
            stat_is_block.return_value = True
            plat_system.return_value = 'Linux'
            ioctl.return_value = struct.pack('L', 256060514304)
            # = '\x00`e\x9e;\x00\x00\x00'
            # = 256060514304 ~= 256 GB (in SI)
            buffer_test = ' ' * struct.calcsize('L')

            bytes = bitmath.query_device_capacity(device)
            self.assertEqual(bytes, 256060514304)
            self.assertEqual(ioctl.call_count, 1)
            ioctl.assert_called_once_with(4, 0x80081272, buffer_test)

    def test_query_device_capacity_mac_everything_is_wonderful(self):
        """query device capacity works on a happy Mac OS X host"""
        with mock.patch('os.stat') as os_stat,\
                mock.patch('stat.S_ISBLK') as stat_is_block,\
                mock.patch('platform.system') as plat_system,\
                mock.patch('fcntl.ioctl') as ioctl:
            # These are the struct.pack() equivalents of 244140625
            # (type: u64) and 4096 (type: u32). Multiplied together
            # they equal the number of bytes in 1 TB.
            returns = [
                struct.pack('L', 244140625),  # 'QJ\x8d\x0e\x00\x00\x00\x00'
                struct.pack('I', 4096)  # , '\x00\x10\x00\x00'
            ]

            def side_effect(*args, **kwargs):
                return returns.pop(0)

            os_stat.return_value = mock.Mock(st_mode=25008)
            stat_is_block.return_value = True
            plat_system.return_value = 'Darwin'
            ioctl.side_effect = side_effect

            bytes = bitmath.query_device_capacity(device)
            # The result should be 1 TB
            self.assertEqual(bytes, 1000000000000)
            self.assertEqual(ioctl.call_count, 2)

    def test_query_device_capacity_device_not_block(self):
        """query device capacity aborts if a non-block-device is provided"""
        with mock.patch('os.stat') as os_stat,\
                mock.patch('stat.S_ISBLK') as stat_is_block,\
                mock.patch('fcntl.ioctl') as ioctl:
            os_stat.return_value = mock.Mock(st_mode=33204)
            # Force ISBLK to reject the input 'device'
            stat_is_block.return_value = False

            with self.assertRaises(ValueError):
                bitmath.query_device_capacity(non_device_file)

            self.assertEqual(ioctl.call_count, 0)
