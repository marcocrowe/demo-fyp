from bs4 import BeautifulSoup


def parse_course_modules(html_content, output_file="course_modules.csv"):
    """
    Parses course modules from the HTML content and writes the details to a CSV file.

    Args:
    - html_content (str): The HTML content as a string.
    - output_file (str): The file name for the CSV output (default is 'course_modules.csv').

    CSV Columns: Year, Semester, Title, Credits, Description.
    """
    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the section with Course Modules
    course_modules_section = soup.find("h3", string="Course Modules")
    if not course_modules_section:
        print("Course Modules section not found.")
        return

    # Find the parent container of the Course Modules section
    course_modules_container = course_modules_section.find_next(
        "div", class_="accordion"
