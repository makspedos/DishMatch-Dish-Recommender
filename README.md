# DishMatch: Dish Recommender System

DishMatch is a recommendation system that suggests dishes based on user preferences.
By leveraging machine learning techniques, specifically the Apriori algorithm from MLxtend, the system identifies patterns in user behavior to provide highly relevant dish recommendations.
## Features

- **Personalized Recommendations**: Provides dish recommendations based on user browsing and preferences.
- **Apriori Algorithm**: Uses association rule learning to find patterns in user-selected dishes.
- **External API Integration**: Utilizes the Spoonacular API for fetching additional dish-related data.
- **Intuitive Interface**: A user-friendly web interface for interaction.

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/makspedos/DishMatch-Dish-Recommender.git
   cd DishMatch-Dish-Recommender
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Project Structure

- `app.py`: Main application file handling routes and logic.
- `database.py`: Handles interactions with the database.
- `culinary/`: Contains routes, api fetches and overall page logic. 
- `static/`: Stores static assets such as CSS and images.
- `templates/`: HTML templates for the front-end.
- `tests/`: Test cases for validating the functionality.

## Technologies Used

- **Python**: Core language for backend development.
- **Flask**: Web framework for building the application.
- **Spoonacular API**: External API service used for fetching dish-related data.
- **MLxtend (Apriori Algorithm)**: Used for association rule learning in recommendations.
- **MongoDB**: NoSQL database used for storing user preferred ingredients and based on it recommendations.
- **Pytest**: Testing framework used for unit testing the application.
- **HTML/CSS**: For front-end design.
