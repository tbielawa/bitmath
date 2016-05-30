#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright © 2014-2016 Santoso Wijaya <santoso.wijaya@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sub-license, and/or sell copies of the Software,
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
#
# Originally written by GitHub user @santa4nt (Santoso Wijaya)
#
# Source gist: https://gist.github.com/santa4nt/11068180 (rev 4)
#
# This implements primitives used to query device capacity on windows
# machines.

import ctypes
import ctypes.wintypes as wintypes
from ctypes import windll


LPDWORD = ctypes.POINTER(wintypes.DWORD)
LPOVERLAPPED = wintypes.LPVOID
LPSECURITY_ATTRIBUTES = wintypes.LPVOID

GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
GENERIC_EXECUTE = 0x20000000
GENERIC_ALL = 0x10000000

CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

FILE_ATTRIBUTE_NORMAL = 0x00000080

INVALID_HANDLE_VALUE = -1

NULL = 0
FALSE = wintypes.BOOL(0)
TRUE = wintypes.BOOL(1)


def _CreateFile(filename, access, mode, creation, flags):
    """See: CreateFile function

    http://msdn.microsoft.com/en-us/library/windows/desktop/aa363858(v=vs.85).aspx

    """
    CreateFile_Fn = windll.kernel32.CreateFileW
    CreateFile_Fn.argtypes = [
        wintypes.LPWSTR,                    # _In_          LPCTSTR lpFileName
        wintypes.DWORD,                     # _In_          DWORD dwDesiredAccess
        wintypes.DWORD,                     # _In_          DWORD dwShareMode
        LPSECURITY_ATTRIBUTES,              # _In_opt_      LPSECURITY_ATTRIBUTES lpSecurityAttributes
        wintypes.DWORD,                     # _In_          DWORD dwCreationDisposition
        wintypes.DWORD,                     # _In_          DWORD dwFlagsAndAttributes
        wintypes.HANDLE]                    # _In_opt_      HANDLE hTemplateFile
    CreateFile_Fn.restype = wintypes.HANDLE

    return wintypes.HANDLE(CreateFile_Fn(filename,
                                         access,
                                         mode,
                                         NULL,
                                         creation,
                                         flags,
                                         NULL))


def _DeviceIoControl(devhandle, ioctl, inbuf, inbufsiz, outbuf, outbufsiz):
    """See: DeviceIoControl function

    http://msdn.microsoft.com/en-us/library/aa363216(v=vs.85).aspx

    """
    DeviceIoControl_Fn = windll.kernel32.DeviceIoControl
    DeviceIoControl_Fn.argtypes = [
        wintypes.HANDLE,                    # _In_          HANDLE hDevice
        wintypes.DWORD,                     # _In_          DWORD dwIoControlCode
        wintypes.LPVOID,                    # _In_opt_      LPVOID lpInBuffer
        wintypes.DWORD,                     # _In_          DWORD nInBufferSize
        wintypes.LPVOID,                    # _Out_opt_     LPVOID lpOutBuffer
        wintypes.DWORD,                     # _In_          DWORD nOutBufferSize
        LPDWORD,                            # _Out_opt_     LPDWORD lpBytesReturned
        LPOVERLAPPED]                       # _Inout_opt_   LPOVERLAPPED lpOverlapped
    DeviceIoControl_Fn.restype = wintypes.BOOL

    # allocate a DWORD, and take its reference
    dwBytesReturned = wintypes.DWORD(0)
    lpBytesReturned = ctypes.byref(dwBytesReturned)

    status = DeviceIoControl_Fn(devhandle,
                                ioctl,
                                inbuf,
                                inbufsiz,
                                outbuf,
                                outbufsiz,
                                lpBytesReturned,
                                None)

    return status, dwBytesReturned


class DeviceIoControl(object):

    def __init__(self, path):
        self.path = path
        self._fhandle = None

    def _validate_handle(self):
        if self._fhandle is None:
            raise Exception('No file handle')
        if self._fhandle.value == wintypes.HANDLE(INVALID_HANDLE_VALUE).value:
            raise Exception('Failed to open %s. GetLastError(): %d' %
                            (self.path, windll.kernel32.GetLastError()))

    def ioctl(self, ctl, inbuf, inbufsiz, outbuf, outbufsiz):
        self._validate_handle()
        return _DeviceIoControl(self._fhandle, ctl, inbuf, inbufsiz, outbuf, outbufsiz)

    def __enter__(self):
        self._fhandle = _CreateFile(
            self.path,
            GENERIC_READ | GENERIC_WRITE,
            0,
            OPEN_EXISTING,
            FILE_ATTRIBUTE_NORMAL)
        self._validate_handle()
        return self

    def __exit__(self, typ, val, tb):
        try:
            self._validate_handle()
        except Exception:
            pass
        else:
            windll.kernel32.CloseHandle(self._fhandle)


def query_device_capacity(device=r'\\.\PhysicalDrive0'):
    """Query a device and calculate its capacity on a Windows platform.

    :return: the device capacity in bytes as a number type
    """

    # sample code using \\.\PhysicalDrive0
    # See: http://msdn.microsoft.com/en-us/library/windows/desktop/aa363147(v=vs.85).aspx

    # first, define the Structure in ctypes language
    class DISK_GEOMETRY(ctypes.Structure):
        """See: http://msdn.microsoft.com/en-us/library/aa363972(v=vs.85).aspx"""
        _fields_ = [
            ('Cylinders', wintypes.LARGE_INTEGER),
            ('MediaType', wintypes.BYTE),   # MEDIA_TYPE
            ('TracksPerCylinder', wintypes.DWORD),
            ('SectorsPerTrack', wintypes.DWORD),
            ('BytesPerSector', wintypes.DWORD)
        ]

    IOCTL_DISK_GET_DRIVE_GEOMETRY = 0x70000

    disk_geometry = DISK_GEOMETRY()
    p_disk_geometry = ctypes.pointer(disk_geometry)

    with DeviceIoControl(device) as dctl:
        status, _ = dctl.ioctl(IOCTL_DISK_GET_DRIVE_GEOMETRY,
                               None, 0,                          # no input buffer
                               p_disk_geometry, ctypes.sizeof(DISK_GEOMETRY))

    if status:
        cylinders = getattr(disk_geometry, 'Cylinders')
        trackspercylinder = getattr(disk_geometry, 'TracksPerCylinder')
        sectorspertrack = getattr(disk_geometry, 'SectorsPerTrack')
        bytespersector = getattr(disk_geometry, 'BytesPerSector')
        return cylinders * trackspercylinder * sectorspertrack * bytespersector
    else:
        print 'IOCTL returned failure. GetLastError(): %d' % windll.kernel32.GetLastError()
