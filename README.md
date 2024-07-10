**Iris Flower Classification Web App**
This project implements a web application using Flask for predicting the species of Iris flowers based on their sepal and petal dimensions. It utilizes a pre-trained K-Nearest Neighbors (KNN) model to make accurate predictions.

**Features**
Input Fields: Enter sepal length, sepal width, petal length, and petal width of an Iris flower.
Prediction: Click the "Predict" button to instantly see the predicted species of the flower.
Simple Interface: Clean and intuitive interface designed using HTML and CSS.
**Technologies Used**
Python: Language used for backend logic and model handling.
Flask: Micro web framework used to develop the web application.
HTML/CSS: Frontend design and structure.
Scikit-learn: Machine learning library for KNN model training and predictions.
Joblib: Library used to serialize the trained KNN model.
Directory Structure
app.py: Main Flask application file containing the server-side logic.
knn_model.pkl: Pre-trained KNN model file stored in pickle format.
templates/: Directory containing HTML templates for rendering pages.
**Usage**
Enter numerical values for sepal length, sepal width, petal length, and petal width.
Click "Predict" to see the predicted Iris flower species displayed on the screen.
