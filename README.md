# Student Performance ML E2E Project 🚀

This repository provides an **end-to-end machine learning pipeline** for predicting student performance using modular coding, Pythonic best practices, and cloud-ready deployment. The project integrates **CI/CD pipelines** and cloud deployment, making it suitable for production environments.

---

## Key Features 🌟

- **Modular Code Structure**: Clear separation of training, prediction, and utility modules.
- **Data Pipelines**: Streamlined training and prediction workflows.
- **CI/CD Integration**: Automated testing and deployment with GitHub Actions.
- **Cloud Deployment**: Ready-to-deploy over cloud services like AWS, GCP, or Azure.
- **Pythonic Standards**: Clean and well-documented code.

---

## How to Run 🛠️

Follow the steps below to clone, set up, and run the project.

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/therealmanraj/students-Performance-ML-E2E-Project.git
cd students-Performance-ML-E2E-Project
```

---

### **Step 2: Set Up the Environment**

#### For Mac/Linux (Python 3.11+ Recommended):

Ensure you have Python installed. Use `python3` and `pip3`.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verify the Python version
python --version
```

#### For Windows:

Use the same steps but replace the activation command with:

```bash
venv\Scripts\activate
```

---

### **Step 3: Install Requirements**

Install all the dependencies listed in the `requirements.txt` file.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### **Step 4: Configure CI/CD (Optional)**

1. Update **GitHub Actions** workflow with your cloud credentials.
2. Push your changes to trigger automated testing and deployment.

---

### **Step 5: Run the Project**

You can execute the pipeline using the main script.

```bash
python main.py
```

---

### **Step 6: Access Local Deployment**

The project runs a server locally. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Deployment 🌐

The project is ready to deploy on any cloud provider. Follow these steps:

1. Update your `config.py` with appropriate cloud settings.
2. Integrate deployment scripts for AWS, GCP, or Azure.
3. Push to GitHub to trigger CI/CD workflows.

---

## Author 👨‍💻

**Manraj Singh**

- **LinkedIn**: [Manraj Singh](https://www.linkedin.com/in/therealmanraj/)
- **GitHub**: [therealmanraj](https://github.com/therealmanraj)

---

## License 📄

This project is licensed under the MIT License.
