#  Azure Feedback App (Flask + Terraform)

This is a collaborative DevOps project for deploying a simple feedback collection app using Flask on Azure App Service, with infrastructure provisioned via Terraform.

##  Project Description

The app allows users to submit feedback through a web form. All feedback is displayed in real time on the same page. The app is deployed using Azure App Service and configured via Infrastructure as Code using Terraform.

The project demonstrates:
- Azure Web App deployment using Infrastructure as Code (IaC)
- Basic full-stack web application structure
- Collaboration via GitHub and Azure

Key services used:
- Azure Resource Group
- Azure App Service Plan (Standard Tier)
- Azure App Service (Python Flask app)
- Azure Storage Account (for logging)
- Azure Application Insights (for monitoring)

---
## Project Structure
## 📁 Project Structure

- `feedback-app/`
  - `app/` — Flask application
    - `app.py` — Main Python app
    - `templates/`
      - `index.html` — HTML form for feedback
  - `terraform/` — Infrastructure as Code
    - `main.tf` — Terraform configuration
    - `variables.tf` — Variables for reusable config
    - `terraform.tfvars` — Actual values for the variables
    - `outputs.tf` — Output values like Web App URL
  - `screenshot.png` — Screenshot of working deployment
  - `README.md` — Project documentation

---
## Team Member Roles

- **Abdulqudus Balogun** – Worked on the **backend**, including:
  - Flask application setup
  - Feedback form logic
  - Terraform IaC deployment

- **Peter Kigathi** – Worked on the **frontend**, including:
  - HTML templates and styling
  - Frontend user interface improvements
---

## Instructions to Run the Code
## 🚀 Instructions to Run the App

### 🛠️ Prerequisites

- Python 3.x installed
- Flask installed (`pip install flask`)
- Azure CLI installed (for deployment)
- Terraform installed (for infrastructure provisioning)

---

### 💻 1. Clone the Repository


git clone https://github.com/codesyncAP/feedback-app.git
cd feedback-app

### Terraform Setup

1. Navigate to the Terraform folder:

   cd terraform
   

2. Initialize and deploy infrastructure:
   terraform init
   terraform apply

Deployed app is live at:
    https://web-feedback-app-500238341-a2.azurewebsites.net/


