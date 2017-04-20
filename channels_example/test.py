import multiprocessing

from channels.test.liveserver import ChannelLiveServerTestCase, WorkerProcess
from django.db import connections
from django.test import override_settings

from aloe import world
from aloe.testclass import TestCase as AloeTestCase


@override_settings(DEBUG=True)
class TestCase(ChannelLiveServerTestCase, AloeTestCase):
    """
    Base test class for Django Gherkin tests in conjunction with Channels.
    """

    def run(self, result=None):
        # Keep a reference to this test case so it can be accessed from the
        # tests in order to restart the workers.
        world.test_case = self

        super().run(result)

    def start_worker(self):
        worker_ready = multiprocessing.Event()
        self._worker_process = self.WorkerProcess(
            worker_ready,
            self.worker_threads,
            self._overridden_settings,
            self._modified_settings,
            connections.databases,
            self.serve_static,
        )
        self._worker_process.start()
        worker_ready.wait()

    def stop_worker(self):
        self._worker_process.terminate()
        self._worker_process.join()

    def restart_worker(self):
        self.stop_worker()
        self.start_worker()

