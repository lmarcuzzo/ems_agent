# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metrics import Metrics  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_os_dmesg(self):
        """Test case for os_dmesg

        Returns the operating system boot log
        """
        response = self.client.open(
            '//ems/dmesg',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_os_metrics(self):
        """Test case for os_metrics

        Return general metrics from VNF
        """
        response = self.client.open(
            '//ems/metrics',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_os_poweroff(self):
        """Test case for os_poweroff

        Power off the system
        """
        response = self.client.open(
            '//ems/poweroff',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_os_reboot(self):
        """Test case for os_reboot

        Reboots the system
        """
        response = self.client.open(
            '//ems/reboot',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_os_shutdown(self):
        """Test case for os_shutdown

        Shuts down the system
        """
        response = self.client.open(
            '//ems/shutdown',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_file(self):
        """Test case for read_file

        Returns File Content
        """
        response = self.client.open(
            '//ems/read_config',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_app(self):
        """Test case for run_app

        Start an application
        """
        query_string = [('command', 'command_example')]
        response = self.client.open(
            '//ems/run',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_running_app(self):
        """Test case for running_app

        Check if application is running
        """
        query_string = [('pid', 'pid_example')]
        response = self.client.open(
            '//ems/running',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_write_file(self):
        """Test case for write_file

        Replace File Content or Create File
        """
        query_string = [('path', 'path_example')]
        data = dict(File=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '//ems/write_config',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
