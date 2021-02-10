import mock
from requests.exceptions import HTTPError
from unittest import TestCase
from apigee import ApigeeClient


class TestApigeeClient(TestCase):

        @mock.patch('apigee.ApigeeClient.build_authorization_header')
        @mock.patch('apigee.requests.get')
        def test_failure_get_from_url(self, get_mock, header_mock):
            class Organization(object):
                def __init__(self):
                    self.organizationName = "TPE"
                    self.url = "baseUrl"
                    self.username = "user"
                    self.password = "passwd"
                    self.mfa = "mfa"
                    self.seamless = "seamless"
                    self.proxy = None
            get_mock.return_value.raise_for_status.side_effect = HTTPError('An HTTP error occurred.')
            header_mock.return_value = "abc"
            self.assertRaises(Exception, ApigeeClient(Organization()).check_organization_connection)
