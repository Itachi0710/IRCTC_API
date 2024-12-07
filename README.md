# IRCTC API

## Introduction

*IRCTC API* is a project designed to provide a set of APIs for managing IRCTC-related services. The platform allows users to query and manage train bookings, stations, and related information. It aims to enhance the user experience by providing efficient and reliable backend services for train-related data.

---

## Technology Stack

- *Frontend*: HTML, CSS, JavaScript (optional for user-facing interfaces)
- *Backend*: Django
- *Database*: MySQL
- *API Format*: REST

---

## Features

### 1. Train Booking
- Allows users to book tickets for available trains using IRCTC’s integrated data.
- Provides real-time availability of train seats and schedules.

### 2. Station Information
- Offers information about train stations, including station codes, location, and amenities.
- Provides real-time updates for station data.

### 3. User Authentication
- Implements user authentication and authorization with Django's built-in authentication system.
- Role-based access control to ensure secure access to sensitive data.

### 4. Real-Time Data Fetching
- Efficiently fetches real-time data such as train availability, schedules, and station information.
- Uses Django models to interact with MySQL for data management.

### 5. Secure Authentication
- Login and registration functionality to manage user accounts.
- Utilizes Django’s security features for password encryption and user data protection.

### 6. Scalability and Maintainability
- Structured backend for easy scaling and maintenance.
- Modular components allow future feature additions and improvements.

### 7. Comprehensive Documentation
- Clear and easy-to-follow documentation for developers to integrate with the API and extend its functionality.

---

## Screenshots

### 1. Added Train Page
![Added Train Page](https://github.com/Itachi0710/IRCTC_API/blob/main/addedtrain.png)

### 2. Booked History Page
![Booked History Page](https://github.com/Itachi0710/IRCTC_API/blob/main/booked%20history.png)

### 3. Book Seat Page
![Book Seat Page](https://github.com/Itachi0710/IRCTC_API/blob/main/bookseat.png)

### 4. Normal User Dashboard
![Normal User Dashboard](https://github.com/Itachi0710/IRCTC_API/blob/main/normal%20user.png)

### 5. No Train Available
![No Train Available](https://github.com/Itachi0710/IRCTC_API/blob/main/notrain.png)

### 6. Seat Booked Confirmation
![Seat Booked Confirmation](https://github.com/Itachi0710/IRCTC_API/blob/main/seatbooked.png)

### 7. Signup Page
![Signup Page](https://github.com/Itachi0710/IRCTC_API/blob/main/signup.png)

### 8. Superuser Dashboard
![Superuser Dashboard](https://github.com/Itachi0710/IRCTC_API/blob/main/superuser.png)

### 9. Trains Data Management
![Trains Data Management](https://github.com/Itachi0710/IRCTC_API/blob/main/trains%20data.png)

### 10. Users Data Management
![Users Data Management](https://github.com/Itachi0710/IRCTC_API/blob/main/uersdata.png)

---

## Installation

Follow the steps below to set up the project locally:

1. *Clone the repository:*

    bash
    git clone https://github.com/ltachi0710/IRCTC_API.git
    cd IRCTC_API
    

2. *Install the required dependencies:*

    bash
    pip install -r requirements.txt
    

3. *Set up the database:*
    - Configure the database settings in settings.py (e.g., set DATABASES configuration to your MySQL instance).
    - Make sure MySQL server is running and create the database if not already created.

4. *Run migrations:*

    bash
    python manage.py migrate
    

5. *Start the development server:*

    bash
    python manage.py runserver
    

6. *Access the API:*
    - Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the backend API.

---

## Usage

- *Train Booking API:* Allows users to check train availability and book tickets.
- *Station Info API:* Retrieve detailed information about train stations.
- *Authentication:* Register and log in users to provide personalized services.

---

## Contribution Guidelines

Contributions to the IRCTC API project are welcome! To contribute:

1. *Fork the repository.*
2. *Create a feature branch:*

    bash
    git checkout -b feature-name
    

3. *Commit your changes:*

    bash
    git commit -m "Feature description"
    

4. *Push to the branch:*

    bash
    git push origin feature-name
    

5. *Open a Pull Request* for review.

Please ensure your contributions follow the project’s coding standards and include relevant tests where applicable.

---

## License

This project is licensed under the terms of the MIT License.

---

## Contact

For further information or inquiries, feel free to contact the project maintainer:

- *Name:* Aniket Shrivastava 
- *Email:* [aniket.shrivastava0202@gmail.com]
