import unittest
from unittest.mock import patch
from sharpapi.sharp_api_service import SharpApiService
from sharpapi.dto.job_description_parameters import JobDescriptionParameters
from sharpapi.enums.sharp_api_job_type_enum import SharpApiJobTypeEnum
from sharpapi.dto.sharp_api_job import SharpApiJob
from sharpapi.enums.sharp_api_job_status_enum import SharpApiJobStatusEnum

class TestSharpApiService(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.service = SharpApiService(self.api_key)
    
    @patch('sharpapi.sharp_api_service.requests.post')
    def test_product_categories(self, mock_post):
        mock_response = {'status_url': 'https://sharpapi.com/api/v1/job/status/12345'}
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        product_name = 'Sony Playstation 5'
        status_url = self.service.product_categories(product_name)
        
        self.assertEqual(status_url, mock_response['status_url'])
        mock_post.assert_called_with(
            f'{self.service.api_base_url}{SharpApiJobTypeEnum.ECOMMERCE_PRODUCT_CATEGORIES["url"]}',
            headers=self.service.get_headers(),
            json={'content': product_name}
        )
    
    @patch('sharpapi.sharp_api_service.requests.get')
    def test_fetch_results(self, mock_get):
        mock_job_response = {
            'data': {
                'id': '12345',
                'attributes': {
                    'type': SharpApiJobTypeEnum.ECOMMERCE_PRODUCT_CATEGORIES['value'],
                    'status': SharpApiJobStatusEnum.SUCCESS.value,
                    'result': {'categories': ['Video Games', 'Consoles']}
                }
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_job_response
        
        status_url = 'https://sharpapi.com/api/v1/job/status/12345'
        job_result = self.service.fetch_results(status_url)
        
        self.assertIsInstance(job_result, SharpApiJob)
        self.assertEqual(job_result.get_id(), '12345')
        self.assertEqual(job_result.get_status(), SharpApiJobStatusEnum.SUCCESS.value)
        self.assertEqual(job_result.get_result_object(), {'categories': ['Video Games', 'Consoles']})
    
    @patch('sharpapi.sharp_api_service.requests.post')
    def test_generate_job_description(self, mock_post):
        mock_response = {'status_url': 'https://sharpapi.com/api/v1/job/status/67890'}
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        params = JobDescriptionParameters(name='Software Engineer')
        status_url = self.service.generate_job_description(params)
        
        self.assertEqual(status_url, mock_response['status_url'])
        mock_post.assert_called_with(
            f'{self.service.api_base_url}{SharpApiJobTypeEnum.HR_JOB_DESCRIPTION["url"]}',
            headers=self.service.get_headers(),
            json=params.to_dict()
        )
    
    @patch('sharpapi.sharp_api_service.requests.get')
    def test_ping(self, mock_get):
        mock_response = {'ping': 'pong', 'timestamp': '2024-10-06T12:00:00Z'}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        response = self.service.ping()
        self.assertEqual(response, mock_response)
        mock_get.assert_called_with(f'{self.service.api_base_url}/ping', headers=self.service.get_headers(), params=None)
    
    @patch('sharpapi.sharp_api_service.requests.get')
    def test_quota(self, mock_get):
        mock_response = {
            'timestamp': '2024-10-06T12:00:00Z',
            'on_trial': False,
            'trial_ends': '2024-11-06T12:00:00Z',
            'subscribed': True,
            'current_subscription_start': '2024-10-01T12:00:00Z',
            'current_subscription_end': '2024-11-01T12:00:00Z',
            'subscription_words_quota': 100000,
            'subscription_words_used': 5000,
            'subscription_words_used_percentage': 5,
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        quota_info = self.service.quota()
        self.assertIsNotNone(quota_info)
        self.assertEqual(quota_info.subscription_words_used, 5000)
        mock_get.assert_called_with(f'{self.service.api_base_url}/quota', headers=self.service.get_headers(), params=None)
    
    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()

