# Opengeo

**Python for Everybody Capstone Project**

## Overview

Opengeo is a capstone project developed as part of the "Python for Everybody" course. This project demonstrates basic geospatial data processing using Python and SQLite alongside a simple HTML/JavaScript front-end for data visualization. It is intended as an educational tool to showcase techniques in handling and displaying geospatial information.

## Features

- **Geospatial Data Processing:** Uses Python scripts to parse, process, and store geospatial data in a SQLite database.
- **Simple Web Interface:** Provides an HTML page powered by JavaScript to view and interact with geospatial data.
- **Educational Purpose:** Developed as a capstone project to consolidate and demonstrate skills learned during the course.

## File Structure

- **My_work.py**  
  The main Python script that performs the geospatial data processing tasks.
- **mygeodumb.py**  
  A supporting Python module for geospatial data operations.
- **myopengeo.sqlite**  
  The SQLite database file that contains the processed geospatial data.
- **where.data**  
  A data file used as input for geospatial queries.
- **mywhere.js**  
  JavaScript code that handles the client-side interactions on the web page.
- **where.html**  
  The HTML file providing a simple user interface for displaying geospatial data.
- **README.md / README.txt**  
  Documentation files for the project.

## Requirements

- **Python 3.x**  
  Ensure that Python 3 is installed on your system.
- **SQLite**  
  Used for the geospatial database.
- **Web Browser**  
  To open and interact with the `where.html` page.

## Setup and Usage

1. **Clone the Repository:**

   Open a terminal and run:

   ```bash
   git clone https://github.com/Mosab2099/Opengeo.git
   cd Opengeo
   ```

2. **Set Up a Python Environment (Optional):**

   Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
   ```

3. **Run the Python Script:**

   Execute the main script to process the geospatial data:

   ```bash
   python My_work.py
   ```

4. **View the Web Interface:**

   Open the `where.html` file in your web browser to interact with the geospatial data through the front-end interface.

## Customization

- **Modifying the Scripts:**  
  You can update the Python scripts (`My_work.py` and `mygeodumb.py`) to add new features or customize the data processing logic.
- **Updating the Database:**  
  The SQLite database (`myopengeo.sqlite`) can be expanded or modified to include additional geospatial information.
- **Front-End Tweaks:**  
  The HTML (`where.html`) and JavaScript (`mywhere.js`) files can be customized to change the presentation or interaction of the geospatial data.

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

## License

This project is intended for educational purposes.  
*(Add specific license details here if applicable.)*

## Acknowledgments

- Developed as part of the Python for Everybody capstone project.
- Special thanks to the Python for Everybody community and Dr. Charles Severance for the inspiration and educational resources.

