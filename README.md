# SharpAPI Python Client SDK

🚀 Automate workflows with AI-powered API

## Leverage AI API to streamline workflows in E-Commerce, Marketing, Content Management, HR Tech, Travel, and more.

[![Version](https://img.shields.io/pypi/v/sharpapi-python-client.svg)](https://pypi.org/project/sharpapi-python-client/)
[![License](https://img.shields.io/pypi/l/sharpapi-python-client.svg)](https://github.com/yourusername/sharpapi-python-client/blob/main/LICENSE)

#### Save time on repetitive content analysis and generation tasks that your app users perform daily.

See more at [SharpAPI.com Website »](https://sharpapi.com/)

## Requirements

- Python >= 3.6


## Installation

```bash
pip install sharpapi-python-client


## What can it do for you?

- **E-commerce**
  - Generate engaging product introductions.
  - Create personalized thank-you emails.
  - Streamline product categorization.
  - Perform sentiment analysis on product reviews.

- **Content & Marketing Automation**
  - Translate text for a global audience.
  - Paraphrase and proofread any text.
  - Detect spam content.
  - Extract contact information.
  - Summarize content and generate keywords/tags.
  - Generate SEO meta tags.

- **HR Tech**
  - Generate job descriptions.
  - Identify related job positions and skills.
  - Parse and extract information from resumes.

- **Travel, Tourism & Hospitality**
  - Analyze sentiment in travel reviews.
  - Categorize tours, activities, and hospitality products.

## Usage

### Simple Example

```python
from sharpapi.sharp_api_service import SharpApiService

sharp_api = SharpApiService('YOUR_SHARP_API_KEY')

try:
    status_url = sharp_api.product_categories(
        'Lenovo Chromebook Laptop (2023), 14" FHD Touchscreen Slim 3, 8-Core MediaTek Kompanio 520 CPU, 4GB RAM, 128GB Storage',
        language='German',  # optional
        max_quantity=400,  # optional
        voice_tone='Neutral',  # optional
        context='Optional current e-store categories'  # optional
    )

    result_sharp_api_job = sharp_api.fetch_results(status_url)
    print(result_sharp_api_job.get_result_json())
except Exception as e:
    print(e)
```

## Documentation
For detailed usage and API methods, please refer to the [SharpAPI Documentation](https://sharpapi.com/documentation).

## Changelog
Please see CHANGELOG for more information on what has changed recently.

## License
The MIT License (MIT). Please see License File for more information.
