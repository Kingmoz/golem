import sys
import unittest
from uuid import uuid1

from golem.clientconfigdescriptor import ClientConfigDescriptor
from golem.monitor.model.nodemetadatamodel import NodeMetadataModel
from golem.monitor.monitor import SystemMonitor
from golem.monitorconfig import MONITOR_CONFIG


def meta_data():
    cliid = str(uuid1())
    sessid = str(uuid1())
    return NodeMetadataModel(cliid, sessid, sys.platform,
                             'app_version', ClientConfigDescriptor())


class MonitorTestBaseClass(unittest.TestCase):
    def setUp(self):
        self.monitor = SystemMonitor(meta_data(), MONITOR_CONFIG)
