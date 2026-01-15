# Alynos BioTech SuperSystem

![Alynos BioTech SuperSystem](media/og_image/og_image.webp)

Alynos BioTech SuperSystem is a comprehensive Django-based web application designed for biotech and healthcare organizations. It integrates medical services, department management, appointment scheduling, and an e-commerce platform for medical products.

## Features

- **Department Management**: Detailed profiles and listings for various medical and research departments.
- **Doctor Profiles**: Comprehensive doctor information including education, skills, and areas of expertise.
- **Appointment System**: Streamlined scheduling for medical appointments.
- **E-commerce Platform**:
  - Product catalog with detailed information.
  - Shopping cart functionality.
  - Checkout and integrated payment processing.
- **Blog Section**: Insightful articles and news with sidebar and single-post views.
- **Contact & Messaging**: Built-in contact forms and message confirmation systems.
- **Responsive Design**: Modern UI templates for a seamless user experience.

## Tech Stack

- **Backend**: Python 3, Django 4.2.6
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, JavaScript (with jQuery, Bootstrap, and Slick Carousel)
- **Media Management**: Integrated file handling for product, doctor, and department images.

## Project Structure

- `Alynos_BioTech_SuperSystem/`: Core Django project configuration.
- `System_App/`: Main application logic, including models, views, and business logic.
- `templates/`: HTML templates for the entire system.
- `media/`: User-uploaded images for products, doctors, and departments.
- `static/`: CSS, JavaScript, and third-party plugins.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Alynos-Website-Final-Emobillis-Project
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   *(Note: Ensure you have Django 4.2.6 installed. If a requirements.txt is not present, you can install the core package)*
   ```bash
   pip install django pillow
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Interface**: Access the Django admin at `http://127.0.0.1:8000/admin/` to manage doctors, departments, and products.
- **Public Site**: Browse services, book appointments, and purchase products through the main navigation.

---
Developed as part of the Emobillis Project.
