import connexion
import six
import os

from swagger_server.models.metrics import Metrics  # noqa: E501
from swagger_server import util


def os_dmesg():  # noqa: E501
    """Returns the operating system boot log

     # noqa: E501


    :rtype: str
    """
    ret = os.popen('dmesg | tail -n 30')
    return ret.read()

def os_metrics():  # noqa: E501
    """Return general metrics from VNF

    Return an array of metrics from the VNF # noqa: E501


    :rtype: Metrics
    """
    return 'do some magic!'


def os_poweroff():  # noqa: E501
    """Power off the system

     # noqa: E501


    :rtype: None
    """
    ret = os.popen('poweroff')
    return ''


def os_reboot():  # noqa: E501
    """Reboots the system

     # noqa: E501


    :rtype: None
    """
    ret = os.popen('reboot')
    return ''

def os_shutdown():  # noqa: E501
    """Shuts down the system

     # noqa: E501


    :rtype: None
    """
    ret = os.popen('poweroff')
    return ''

def read_file():  # noqa: E501
    """Returns File Content

     # noqa: E501


    :rtype: str
    """
    func = open("/test.click",'r')
    return func.read()

def run_app(command):  # noqa: E501
    """Start an application

    Run an application with its command line parameters. The process PID is returned if command was sucessful # noqa: E501

    :param command: command with its parameters
    :type command: str

    :rtype: str
    """
    os.system(command+"&")
    return ''


def running_app(pid):  # noqa: E501
    """Check if application is running

    Check if application specified by PID is still running. # noqa: E501

    :param pid: application main thread ID
    :type pid: str

    :rtype: str
    """
    try:
        os.kill(int(pid),0)
        return True
    except OSError:
        return False

def write_file(path, File):  # noqa: E501
    """Replace File Content or Create File

     # noqa: E501

    :param path: File path string
    :type path: str
    :param File: File to upload
    :type File: werkzeug.datastructures.FileStorage

    :rtype: str
    """
    print(path)
    print(File)
    File.save(path)
    return ''
