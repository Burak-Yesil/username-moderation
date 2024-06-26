# Username Moderation System

## Overview
The Username Moderation System is a sophisticated tool designed to assist in the moderation of user-generated content on digital platforms. This system proactively identifies usernames that may carry hateful connotations or resemble the names of well-known personalities, which is essential for preventing impersonation and ensuring respectful community interactions. Additionally, it is equipped to detect and flag comments that contain hateful speech, further contributing to the maintenance of a positive and welcoming online environment.

## Features
- **Hateful Username Detection**: Employs machine learning algorithms to spot and flag usernames containing offensive or inappropriate content.
- **Celebrity Name Approximation**: Analyzes usernames to find close matches to famous individuals, such as flagging 'well smith' as resembling 'Will Smith'.
- **Hateful Comment Detection**: Scans user comments for hateful or toxic expressions to promote constructive and respectful discourse.
- **Streamlined Integration**: Can be easily incorporated into existing user management systems with minimal setup effort.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Git
- Python3
- pip (Python package installer)

### Installing

A step by step series of examples that tell you how to get a development environment running:

###Clone the repository
git clone https://github.com/Burak-Yesil/username-moderation.git

###Install the required dependencies using pip:
pip install -r requirements.txt

###Running the Application
Once the dependencies are installed, you can run the application with the following command:
python main.py
