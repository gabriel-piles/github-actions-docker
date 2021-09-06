import subprocess
import time
from unittest import TestCase

import requests


class TestEndToEnd(TestCase):

    def test_end_to_end(self):
        subprocess.run('docker-compose up -d --build', shell=True)
        time.sleep(5)

        host = 'http://localhost:5050'

        response = requests.get(f"{host}")

        self.assertEqual(200, response.status_code)

        subprocess.run('docker-compose down', shell=True)
