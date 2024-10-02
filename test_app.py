import unittest
from app import app  # Import your Flask app

class ThreatDetectionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Threat Detection System', response.data)

    def test_detect_threat_malicious(self):
        response = self.app.post('/detect', json={'threat_indicator': 'malicious_ip'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'Threat Detected')

    def test_detect_threat_safe(self):
        response = self.app.post('/detect', json={'threat_indicator': 'safe_ip'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 'No Threat Detected')

    def test_invalid_indicator(self):
        response = self.app.post('/detect', json={'threat_indicator': 'unknown_ip'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unknown threat indicator', response.json['error'])

if __name__ == '__main__':
    unittest.main()
