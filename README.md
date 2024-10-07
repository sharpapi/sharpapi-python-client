![SharpAPI GitHub cover](https://sharpapi.com/sharpapi-github-php-bg.jpg)

# SharpAPI Python Client SDK

🚀 **Automate Workflows with AI-Powered API**

## Leverage AI API to Streamline Workflows in E-Commerce, Marketing, Content Management, HR Tech, Travel, and More.

[![PyPI Version](https://img.shields.io/pypi/v/sharpapi-python-client.svg)](https://pypi.org/project/sharpapi-python-client/)
[![License](https://img.shields.io/pypi/l/sharpapi-python-client.svg)](https://github.com/sharpapi/sharpapi-python-client/blob/main/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sharpapi-python-client.svg)](https://pypi.org/project/sharpapi-python-client/)
[![Python Version](https://img.shields.io/pypi/pyversions/sharpapi-python-client.svg)](https://www.python.org/downloads/)

#### Save time on repetitive content analysis and generation tasks that your app users perform daily.
**SharpAPI Python Client SDK** enables developers to integrate advanced artificial intelligence capabilities into their Python applications. This SDK simplifies interaction with the SharpAPI services, providing a seamless way to leverage AI for various use cases.


Visit the [SharpAPI.com Website »](https://sharpapi.com/) for more information.

---

## 📚 Table of Contents

- [📦 Installation](#-installation)
- [🔧 Configuration](#-configuration)
- [💡 Features](#-features)
- [💻 Usage](#-usage)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📞 Contact](#-contact)

---

## 📦 Installation

You can install the SharpAPI Python Client SDK via **PyPI** using `pip`:

```bash
pip install sharpapi-python-client
```

Alternatively, if you prefer using **Poetry** for dependency management, you can add it to your project:

```bash
poetry add sharpapi-python-client
```

---

## 🔧 Configuration

### 1. **Obtain Your SharpAPI API Key**

Sign up at [SharpAPI.com](https://sharpapi.com/) to obtain your API key.

### 2. **Set Up Environment Variables**

Create a `.env` file in your project's root directory to securely store your API key:

```env
SHARP_API_KEY=your_sharpapi_api_key_here
```

Ensure that `.env` is included in your `.gitignore` to prevent accidental exposure of your API key.

### 3. **Loading Environment Variables**

The SDK uses `python-dotenv` to load environment variables. Ensure that your application initializes the environment variables before using the SDK:

```python
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file
```

---

## 💡 Features

The **SharpAPI Python Client SDK** offers a comprehensive suite of AI-powered tools to enhance various aspects of your applications:

### **E-Commerce**
- **Generate Engaging Product Introductions**
- **Create Personalized Thank-You Emails**
- **Streamline Product Categorization**
- **Perform Sentiment Analysis on Product Reviews**

### **Content & Marketing Automation**
- **Translate Text for a Global Audience**
- **Paraphrase and Proofread Any Text**
- **Detect Spam Content**
- **Extract Contact Information**
- **Summarize Content and Generate Keywords/Tags**
- **Generate SEO Meta Tags**

### **HR Tech**
- **Generate Job Descriptions**
- **Identify Related Job Positions and Skills**
- **Parse and Extract Information from Resumes**

### **Travel, Tourism & Hospitality**
- **Analyze Sentiment in Travel Reviews**
- **Categorize Tours, Activities, and Hospitality Products**

---

## 💻 Usage

### 🛠 **Basic Example**

```python
from sharpapi import SharpApiService

# Initialize the SharpApiService with your API key
sharp_api = SharpApiService(api_key='YOUR_SHARP_API_KEY')

try:
    # Example: Generate Product Categories
    status_url = sharp_api.product_categories(
        product_name='Lenovo Chromebook Laptop (2023), 14" FHD Touchscreen Slim 3, 8-Core MediaTek Kompanio 520 CPU, 4GB RAM, 128GB Storage',
        language='German',  # Optional
        max_quantity=400,   # Optional
        voice_tone='Neutral',  # Optional
        context='Optional current e-store categories'  # Optional
    )

    # Fetch and print the results
    result_sharp_api_job = sharp_api.fetch_results(status_url)
    print(result_sharp_api_job.get_result_json())
except Exception as e:
    print(f"An error occurred: {e}")
```

### 🛠 **Advanced Example: Parsing a Resume**

```python
from sharpapi import SharpApiService

# Initialize the SharpApiService with your API key
sharp_api = SharpApiService(api_key='YOUR_SHARP_API_KEY')

try:
    # Parse Resume
    status_url = sharp_api.parse_resume(
        file_path='path/to/sample_resume.pdf',
        language='English'  # Optional
    )

    # Fetch and print the parsed resume data
    parsed_resume = sharp_api.fetch_results(status_url)
    print(parsed_resume.get_result_json())
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## 🧪 Testing

This project uses Python's built-in `unittest` framework for testing.

### **Running Tests**

Ensure that you are in the project's root directory and that all dependencies are installed via Poetry or `pip`.

#### **Using Poetry:**

1. **Activate Poetry Shell:**

    ```bash
    poetry shell
    ```

2. **Run Tests:**

    ```bash
    python -m unittest discover tests
    ```

#### **Using pip and Virtual Environment:**

1. **Activate Your Virtual Environment:**

    ```bash
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Run Tests:**

    ```bash
    python -m unittest discover tests
    ```

---

### **Key Components:**

- **`src/sharpapi/`**: Contains the main SDK code.
  - **`dto/`**: Data Transfer Objects for handling request and response data.
  - **`enums/`**: Enumerations for standardized values across the SDK.
  - **`sharp_api_service.py`**: Core service class to interact with SharpAPI endpoints.
- **`tests/`**: Contains unit tests for the SDK using Python's `unittest` framework.
- **`pyproject.toml`**: Configuration file managed by Poetry for dependencies and packaging.
- **`LICENSE`**: Licensing information.
- **`README.md`**: Project documentation.
- **`venv/`**: Virtual environment directory (should be excluded from version control).

---

## 🤝 Contributing

Contributions are welcome! Whether you're reporting a bug, suggesting an enhancement, or submitting a pull request, your input is valuable to us.

### **How to Contribute:**

1. **Fork the Repository**

    Click the [Fork](https://github.com/sharpapi/sharpapi-python-client/fork) button at the top-right corner of the repository page.

2. **Clone Your Fork**

    ```bash
    git clone https://github.com/yourusername/sharpapi-python-client.git
    cd sharpapi-python-client
    ```

3. **Create a New Branch**

    ```bash
    git checkout -b feature/YourFeatureName
    ```

4. **Make Your Changes**

    Implement your feature or fix. Ensure that your code adheres to the project's coding standards.

5. **Run Tests**

    Ensure all tests pass before committing your changes.

    ```bash
    poetry shell
    python -m unittest discover tests
    ```

6. **Commit Your Changes**

    ```bash
    git commit -m "Add feature XYZ"
    ```

7. **Push to Your Fork**

    ```bash
    git push origin feature/YourFeatureName
    ```

8. **Create a Pull Request**

    Navigate to the original repository and click on "Compare & pull request." Provide a clear description of your changes.

### **Coding Standards:**

- Follow [PEP 8](https://pep8.org/) style guidelines.
- Write clear and concise docstrings for all modules, classes, and methods.
- Ensure that all new features are accompanied by corresponding unit tests.

---

## 📄 License

This project is licensed under the [MIT License](https://github.com/sharpapi/sharpapi-python-client/blob/main/LICENSE).

---

## 📞 Contact

For any questions, support, or inquiries, feel free to reach out:

- **Email**: [contact@sharpapi.com](mailto:contact@sharpapi.com)
- **Website**: [https://sharpapi.com](https://sharpapi.com/)
- **GitHub**: [https://github.com/sharpapi/sharpapi-python-client](https://github.com/sharpapi/sharpapi-python-client)

---

## 📝 Changelog

Please see [CHANGELOG.md](https://github.com/sharpapi/sharpapi-python-client/blob/main/CHANGELOG.md) for more information on what has changed recently.

---

## 📚 Documentation

For detailed usage and API methods, please refer to the [SharpAPI Documentation](https://sharpapi.com/documentation).

---

## 🧰 Additional Resources

- **Poetry Documentation**: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- **Python `unittest` Documentation**: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
- **SharpAPI Documentation**: [https://sharpapi.com/documentation](https://sharpapi.com/documentation)

---
## Social Media

🚀 For the latest news, tutorials, and case studies, don't forget to follow us on:
- [SharpAPI X (formerly Twitter)](https://x.com/SharpAPI)
- [SharpAPI YouTube](https://www.youtube.com/@SharpAPI)
- [SharpAPI Vimeo](https://vimeo.com/SharpAPI)
- [SharpAPI LinkedIn](https://www.linkedin.com/products/a2z-web-ltd-sharpapicom-automate-with-aipowered-api/)
- [SharpAPI Facebook](https://www.facebook.com/profile.php?id=61554115896974)

---

Happy Coding! 🚀
