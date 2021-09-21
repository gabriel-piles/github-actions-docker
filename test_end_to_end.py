import subprocess
import time
from unittest import TestCase

import requests


class TestEndToEnd(TestCase):

    def setUp(self):
        subprocess.run('docker-compose up -d --build', shell=True)
        time.sleep(5)

    def tearDown(self):
        subprocess.run('docker-compose down', shell=True)

    def test_end_to_end(self):
        host = 'http://localhost:5050'

        response = requests.get(f"{host}")

        self.assertEqual('works', response.json())
