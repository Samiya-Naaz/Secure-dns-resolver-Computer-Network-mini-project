# Secure DNS Resolver - Computer Networks Mini Project

## Overview
The **Secure DNS Resolver** is a mini-project designed for a Computer Networks course. It provides a secure and efficient way to resolve domain names to IP addresses, supporting multiple DNS protocols and optional GUI features.

## Features
- Resolves domain names securely
- Supports multiple DNS protocols (UDP, TCP)
- Optional GUI for user-friendly interaction
- Logs queries for debugging and monitoring

## Project Structure

- `cn_project/`
  - `main.py`               : Entry point of the resolver
  - `resolver/`             : Core resolver logic
    - `udp_resolver.py`    
    - `tcp_resolver.py`    
  - `gui/`                  : Optional GUI files
  - `requirements.txt`      : Project dependencies
  - `README.md`             : Project documentation

## Installation
1. **Clone the repository**:
```bash
git clone https://github.com/Samiya-Naaz/Secure-dns-resolver-Computer-Network-mini-project.git
Navigate to the project folder:
cd cn_project

Install dependencies (if using Python):
pip install -r requirements.txt

Usage:
Run the resolver via command line:
python main.py

Optional GUI (if implemented):
python gui/app.py

Future Enhancements
Implement caching for faster resolution
Add support for DNS-over-HTTPS (DoH)
Include logging and analytics dashboard

Author
Samiya Naaz

License
This project is licensed under the MIT License.

