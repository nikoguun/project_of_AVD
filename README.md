# README - Data Analyzer Project

## Project Overview
The **Data Analyzer** project is a web application built with Django to enable users to upload CSV files, analyze their contents, and visualize the data through various plots. This project is designed for ease of use and supports basic statistical calculations, filtering, and graphical visualization.

---

## Features
1. **File Upload**
   - Users can upload CSV files using a form.
   - Uploaded data is processed and stored in the session for further analysis.

2. **Data Display and Statistics**
   - Displays the contents of the uploaded CSV file in a tabular format.
   - Allows filtering by row index or column name.
   - Provides basic statistical measures, including:
     - Mean
     - Median
     - Variance
     - Standard Deviation
     - Minimum and Maximum values

3. **Data Visualization**
   - Supports multiple plot types for visualizing numerical data:
     - Histogram
     - Line Plot
     - Scatter Plot
     - Boxplot
     - Heatmap
     - Pairplot
   - Interactive visualizations are rendered using Plotly.

---

## Technologies Used
### Backend:
- Django Framework
- Python Libraries:
  - `csv`: For handling CSV file operations
  - `numpy`: For numerical computations
  - `pandas`: For data manipulation
  - `plotly`: For interactive visualizations
  - `matplotlib` and `seaborn`: For static plots

### Frontend:
- Django Templates for rendering HTML pages

---

## Installation and Setup

### Prerequisites
1. Python 3.8 or above
2. Django 4.0 or above
3. Virtual environment tools (e.g., `venv` or `conda`)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd data-analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## File Structure
```
data_analyzer/
├── templates/
│   ├── data_analyzer/
│   │   ├── upload.html
│   │   ├── display.html
│   │   └── visualize.html
├── static/
│   └── css/
├── views.py
├── forms.py
├── urls.py
└── models.py
```

---

## How to Use

1. **Upload a CSV File:**
   - Navigate to the upload page.
   - Select a CSV file and submit the form.

2. **View and Analyze Data:**
   - After uploading, view the contents of the CSV file.
   - Filter rows by index or extract specific column data.
   - Perform statistical calculations on numeric columns.

3. **Visualize Data:**
   - Choose the type of plot (e.g., histogram, scatter).
   - Select the column(s) to visualize.
   - Generate and interact with the plots.

---

## Error Handling
- If an invalid file is uploaded, the user is notified via a message.
- Non-numeric columns are excluded from statistical calculations and certain visualizations.
- Errors during data processing or visualization are gracefully handled, displaying informative messages.

---

## Future Enhancements
1. Add support for more file formats (e.g., Excel).
2. Include more advanced visualization options.
3. Implement user authentication for managing file uploads securely.
4. Improve responsiveness of the frontend for mobile devices.

---

## Contributors
- SOUFIANE mohtadi(Developer)

---



