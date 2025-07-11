# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on movie features like genres, keywords, cast, director, and tagline using machine learning techniques.

## 🎬 Overview

This project implements a movie recommendation system using **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization and **cosine similarity** to find and recommend movies similar to a user's input. The system analyzes movie metadata to create feature vectors and calculates similarity scores between movies.

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on movie features rather than user ratings
- **Fuzzy String Matching**: Handles typos and partial movie names using `difflib`
- **Comprehensive Movie Information**: Displays movie title, description, release date, cast, and director
- **Interactive CLI**: User-friendly command-line interface
- **Data Processing Pipeline**: Separate preprocessing and execution phases

## 🛠️ Technology Stack

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **scikit-learn**: TF-IDF vectorization and cosine similarity
- **numpy**: Numerical computations
- **difflib**: Fuzzy string matching for movie names

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── engine.py              # Main application with recommendation logic
├── movies.csv             # Dataset containing movie information
├── feature_vector.csv     # Pre-computed feature vectors (if available)
└── README.md              # Project documentation
```

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Movie-Recommendation-System
   ```

2. **Install required dependencies**
   ```bash
   pip install pandas scikit-learn numpy
   ```

3. **Run the application**
   ```bash
   python engine.py
   ```

## 💻 Usage

The application provides two main options:

### Option 1: Process CSV File
- Preprocesses the movie dataset
- Combines movie features (genres, keywords, tagline, cast, director)
- Creates a new CSV file with combined features
- **Run this first** before getting recommendations

### Option 2: Execute Recommendation
- Takes user input for a movie name
- Finds the closest match using fuzzy string matching
- Calculates similarity scores with other movies
- Returns top 5 similar movie recommendations

### Example Workflow:
```
Press 1-> Process CSV file
Press 2-> Execute
Choice : 1

[Processing movies dataset...]

do you want to continue ?(y/n) y

Press 1-> Process CSV file
Press 2-> Execute  
Choice : 2

Enter movie name? Avatar

Suggested Movies-> 

1 . Avatar
Description: In the 22nd century, a paraplegic Marine is dispatched to the moon 
            Pandora on a unique mission, but becomes torn between following orders 
            and protecting an alien civilization.
Release:        2009-12-10
Cast:           Sam Worthington Zoe Saldana Sigourney Weaver Stephen Lang Michelle Rodriguez
Director:       James Cameron

[... 4 more similar movies ...]
```

## 🔧 How It Works

### 1. Data Preprocessing (`process_csv()`)
- Loads movie data from `movies.csv`
- Selects relevant features: genres, keywords, tagline, cast, director
- Fills missing values with empty strings
- Combines all features into a single text string
- Saves processed data to `movies_with_combined_features.csv`

### 2. Feature Vectorization (`exe()`)
- Uses **TF-IDF Vectorizer** to convert text features into numerical vectors
- Creates a matrix where each movie is represented by its feature importance scores

### 3. Similarity Calculation
- Computes **cosine similarity** between all movie pairs
- Cosine similarity measures the angle between feature vectors (0 = no similarity, 1 = identical)

### 4. Recommendation Generation
- Finds user's input movie using fuzzy string matching
- Retrieves similarity scores for that movie with all others
- Sorts movies by similarity score in descending order
- Returns top 5 most similar movies with detailed information

## 📊 Dataset Information

The system expects a CSV file with the following columns:
- `title`: Movie title
- `genres`: Movie genres
- `keywords`: Associated keywords
- `tagline`: Movie tagline
- `cast`: Main cast members
- `director`: Movie director
- `overview`: Movie description
- `release_date`: Release date
- `index`: Unique identifier

## 🎯 Algorithm Details

### TF-IDF (Term Frequency-Inverse Document Frequency)
- **Term Frequency (TF)**: How often a word appears in a document
- **Inverse Document Frequency (IDF)**: How rare or common a word is across all documents
- **TF-IDF Score**: TF × IDF - gives higher scores to words that are frequent in a document but rare across the corpus

### Cosine Similarity
- Measures the cosine of the angle between two vectors
- Range: [-1, 1], but for TF-IDF vectors: [0, 1]
- Formula: `cos(θ) = (A · B) / (||A|| × ||B||)`

## 🔮 Future Enhancements

- [ ] **Hybrid Filtering**: Combine content-based with collaborative filtering
- [ ] **Web Interface**: Create a web-based GUI using Flask/Django
- [ ] **Database Integration**: Replace CSV with a proper database
- [ ] **Advanced NLP**: Use word embeddings (Word2Vec, BERT) for better feature representation
- [ ] **User Profiles**: Add user preference learning
- [ ] **Rating Integration**: Include IMDb/user ratings in recommendations
- [ ] **API Development**: Create REST API for integration with other applications
- [ ] **Performance Optimization**: Implement caching and faster similarity search
- [ ] **Recommendation Explanations**: Show why specific movies were recommended

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- **Anish** - *Initial work*

## 🙏 Acknowledgments

- Movie dataset providers
- scikit-learn community for excellent documentation
- Contributors to the pandas and numpy libraries

---

**Note**: Make sure to run "Process CSV file" (Option 1) before attempting to get recommendations (Option 2) for the first time.
