# 🔗 URL Shortener | Flask Project

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)

A minimalist and elegant URL shortening service built with Flask and styled with modern CSS.

## ✨ Features

- 🚀 Lightning fast URL shortening
- 🎨 Modern and responsive UI
- 🔒 Secure random URL generation
- 📱 Mobile-friendly design
- 🌐 Easy to deploy and use

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows**:
```bash
.\venv\Scripts\activate
```

**Unix/MacOS**:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install flask python-dotenv
```

## 🚀 Usage

1. Start the Flask server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Enter your long URL and click "Shorten URL" to get a shortened version!

## 📁 Project Structure

```
url-shortener/
│
├── main.py           # Main Flask application
├── templates/        # HTML templates
│   ├── index.html   # Home page
│   └── result.html  # Results page
├── .env             # Environment variables
└── README.md        # Project documentation
```

## 💻 Technologies Used

- **Flask**: Web framework
- **Python**: Programming language
- **HTML/CSS**: Frontend design
- **python-dotenv**: Environment management

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Known Issues

- URLs are stored in memory and will be lost when server restarts
- No duplicate URL checking implemented

## 🎯 Future Improvements

- [ ] Add persistent storage using database
- [ ] Implement user authentication
- [ ] Add URL analytics
- [ ] Custom URL slugs
- [ ] API endpoints for programmatic access

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```