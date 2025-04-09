# Certificate Generator 📜

[![Author](https://img.shields.io/badge/Author-Prince2347X-blue)](https://github.com/Prince2347X)
[![Vibe Coded](https://img.shields.io/badge/Vibe_Coded-✨-purple)](https://github.com/Prince2347X/certificate-generator)
[![Python](https://img.shields.io/badge/Python-3.12-yellow)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A Python-based certificate generation and distribution system created for [Code2X](https://konfhub.com/code2x) - A programming contest held at [Shri Shankaracharya Institute of Professional Management & Technology](https://ssipmt.edu.in/), organized by [Student Activity Centre (SAC, SSIPMT)](https://sac-ssipmt.web.app/).

## Features ✨

- Automated certificate generation from PDF template
- Dynamic font sizing based on participant name length
- Bulk certificate generation from CSV data
- Automated email distribution of certificates
- Custom font support
- Centralized text placement on certificates

## Prerequisites 📋

- Python 3.12 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - chardet
  - pillow
  - PyPDF2
  - reportlab

## Setup & Usage 🚀

1. Clone the repository
```bash
git clone https://github.com/yourusername/certificate-generator.git
cd certificate-generator
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Prepare your files:
   - Place your certificate template as `code2x_template.pdf`
   - Update `participants.csv` with participant details (Name, Email)
   - Ensure the font files are in the `font/` directory

4. Configure email settings:
   - Open `main.py`
   - Set your email credentials:
     ```python
     from_email = "your.email@gmail.com"
     from_password = "your-app-specific-password"
     ```
   > Note: For Gmail, you'll need to use an App Password. Enable 2FA and generate an App Password from your Google Account settings.

5. Run the script
```bash
python main.py
```

## Project Structure 📁

```
certificate-generator/
├── code2x_template.pdf    # Certificate template
├── main.py               # Main script
├── participants.csv      # Participant details
├── requirements.txt      # Python dependencies
├── certificates/         # Generated certificates
├── font/                # Custom fonts
└── utils/               # Utility functions
    ├── generate_certificate.py
    ├── calculate_font_size.py
    └── mail.py
```

## How It Works 🔧

1. Reads participant data from `participants.csv`
2. Generates certificates using the template and custom fonts
3. Dynamically adjusts font size based on name length
4. Places text in the center of designated areas
5. Saves generated certificates in the `certificates/` directory
6. Sends certificates to participants via email

## Contributing 🤝

Feel free to open issues and pull requests!

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Prince2347X](https://github.com/Prince2347X) for [SAC, SSIPMT](https://sac-ssipmt.web.app/)