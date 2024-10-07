import time
import requests
from urllib.parse import urlparse

from .dto.job_description_parameters import JobDescriptionParameters
from .dto.sharp_api_job import SharpApiJob
from .dto.sharp_api_subscription_info import SharpApiSubscriptionInfo
from .enums.sharp_api_job_status_enum import SharpApiJobStatusEnum
from .enums.sharp_api_job_type_enum import SharpApiJobTypeEnum


class SharpApiService:
    def __init__(self, api_key, api_base_url='https://sharpapi.com/api/v1', user_agent='SharpAPIPythonClient/1.2.0'):
        if not api_key:
            raise ValueError('API key is required.')
        self.api_key = api_key
        self.api_base_url = api_base_url
        self.user_agent = user_agent
        self.api_job_status_polling_interval = 10  # seconds
        self.use_custom_interval = False
        self.api_job_status_polling_wait = 180  # seconds

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json',
            'User-Agent': self.user_agent,
        }

    def make_request(self, method, url, data=None, file_path=None):
        full_url = f'{self.api_base_url}{url}'
        headers = self.get_headers()

        if method == 'POST':
            if file_path:
                files = {'file': open(file_path, 'rb')}
                response = requests.post(full_url, headers=headers, data=data, files=files)
            else:
                response = requests.post(full_url, headers=headers, json=data)
        else:
            response = requests.get(full_url, headers=headers, params=data)

        response.raise_for_status()
        return response.json()

    def parse_status_url(self, response):
        return response.get('status_url')

    def fetch_results(self, status_url):
        waiting_time = 0

        while True:
            response = requests.get(status_url, headers=self.get_headers())
            response.raise_for_status()
            response_data = response.json()
            job_status = response_data['data']['attributes']

            if job_status['status'] in [SharpApiJobStatusEnum.SUCCESS.value, SharpApiJobStatusEnum.FAILED.value]:
                break

            retry_after = int(response.headers.get('Retry-After', self.api_job_status_polling_interval))
            if self.use_custom_interval:
                retry_after = self.api_job_status_polling_interval

            waiting_time += retry_after
            if waiting_time >= self.api_job_status_polling_wait:
                break

            time.sleep(retry_after)

        data = response_data['data']
        url_parts = urlparse(status_url)
        segments = url_parts.path.strip('/').split('/')
        if len(segments) == 5:
            result = data['attributes']['result']
        else:
            result = data['attributes']['result']

        return SharpApiJob(
            id=data['id'],
            type=data['attributes']['type'],
            status=data['attributes']['status'],
            result=result or None
        )

    def ping(self):
        response = self.make_request('GET', '/ping')
        return response

    def quota(self):
        response = self.make_request('GET', '/quota')
        if 'timestamp' not in response:
            return None
        return SharpApiSubscriptionInfo(response)

    # Include all API methods here, following the structure:

    def parse_resume(self, file_path, language=None):
        data = {}
        if language:
            data['language'] = language
        response = self.make_request('POST', SharpApiJobTypeEnum.HR_PARSE_RESUME['url'], data, file_path)
        return self.parse_status_url(response)

    def generate_job_description(self, job_description_parameters):
        data = job_description_parameters.to_dict()
        response = self.make_request('POST', SharpApiJobTypeEnum.HR_JOB_DESCRIPTION['url'], data)
        return self.parse_status_url(response)

    def related_skills(self, skill_name, language=None, max_quantity=None):
        data = {'content': skill_name}
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        response = self.make_request('POST', SharpApiJobTypeEnum.HR_RELATED_SKILLS['url'], data)
        return self.parse_status_url(response)

    def related_job_positions(self, job_position_name, language=None, max_quantity=None):
        data = {'content': job_position_name}
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        response = self.make_request('POST', SharpApiJobTypeEnum.HR_RELATED_JOB_POSITIONS['url'], data)
        return self.parse_status_url(response)

    def product_review_sentiment(self, review):
        data = {'content': review}
        response = self.make_request('POST', SharpApiJobTypeEnum.ECOMMERCE_REVIEW_SENTIMENT['url'], data)
        return self.parse_status_url(response)

    def product_categories(self, product_name, language=None, max_quantity=None, voice_tone=None, context=None):
        data = {'content': product_name}
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.ECOMMERCE_PRODUCT_CATEGORIES['url'], data)
        return self.parse_status_url(response)

    def generate_product_intro(self, product_data, language=None, max_length=None, voice_tone=None):
        data = {'content': product_data}
        if language:
            data['language'] = language
        if max_length:
            data['max_length'] = max_length
        if voice_tone:
            data['voice_tone'] = voice_tone
        response = self.make_request('POST', SharpApiJobTypeEnum.ECOMMERCE_PRODUCT_INTRO['url'], data)
        return self.parse_status_url(response)

    def generate_thank_you_email(self, product_name, language=None, max_length=None, voice_tone=None, context=None):
        data = {'content': product_name}
        if language:
            data['language'] = language
        if max_length:
            data['max_length'] = max_length
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.ECOMMERCE_THANK_YOU_EMAIL['url'], data)
        return self.parse_status_url(response)

    def detect_phones(self, text):
        data = {'content': text}
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_DETECT_PHONES['url'], data)
        return self.parse_status_url(response)

    def detect_emails(self, text):
        data = {'content': text}
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_DETECT_EMAILS['url'], data)
        return self.parse_status_url(response)

    def detect_spam(self, text):
        data = {'content': text}
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_DETECT_SPAM['url'], data)
        return self.parse_status_url(response)

    def summarize_text(self, text, language=None, max_length=None, voice_tone=None, context=None):
        data = {'content': text}
        if language:
            data['language'] = language
        if max_length:
            data['max_length'] = max_length
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_SUMMARIZE['url'], data)
        return self.parse_status_url(response)

    def generate_keywords(self, text, language=None, max_quantity=None, voice_tone=None, context=None):
        data = {'content': text}
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_KEYWORDS['url'], data)
        return self.parse_status_url(response)

    def translate(self, text, language, voice_tone=None, context=None):
        data = {'content': text, 'language': language}
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_TRANSLATE['url'], data)
        return self.parse_status_url(response)

    def paraphrase(self, text, language=None, max_length=None, voice_tone=None, context=None):
        data = {'content': text}
        if language:
            data['language'] = language
        if max_length:
            data['max_length'] = max_length
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_PARAPHRASE['url'], data)
        return self.parse_status_url(response)

    def proofread(self, text):
        data = {'content': text}
        response = self.make_request('POST', SharpApiJobTypeEnum.CONTENT_PROOFREAD['url'], data)
        return self.parse_status_url(response)

    def generate_seo_tags(self, text, language=None, voice_tone=None):
        data = {'content': text}
        if language:
            data['language'] = language
        if voice_tone:
            data['voice_tone'] = voice_tone
        response = self.make_request('POST', SharpApiJobTypeEnum.SEO_GENERATE_TAGS['url'], data)
        return self.parse_status_url(response)

    def travel_review_sentiment(self, text):
        data = {'content': text}
        response = self.make_request('POST', SharpApiJobTypeEnum.TTH_REVIEW_SENTIMENT['url'], data)
        return self.parse_status_url(response)

    def tours_and_activities_product_categories(self, product_name, city=None, country=None, language=None, max_quantity=None, voice_tone=None, context=None):
        data = {'content': product_name}
        if city:
            data['city'] = city
        if country:
            data['country'] = country
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.TTH_TA_PRODUCT_CATEGORIES['url'], data)
        return self.parse_status_url(response)

    def hospitality_product_categories(self, product_name, city=None, country=None, language=None, max_quantity=None, voice_tone=None, context=None):
        data = {'content': product_name}
        if city:
            data['city'] = city
        if country:
            data['country'] = country
        if language:
            data['language'] = language
        if max_quantity:
            data['max_quantity'] = max_quantity
        if voice_tone:
            data['voice_tone'] = voice_tone
        if context:
            data['context'] = context
        response = self.make_request('POST', SharpApiJobTypeEnum.TTH_HOSPITALITY_PRODUCT_CATEGORIES['url'], data)
        return self.parse_status_url(response)

