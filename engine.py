import textwrap
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def process_csv():
    movies_data=pd.read_csv('movies.csv')

    #select relevant features
    selected_features=['genres','keywords','tagline','cast','director']
    
    print("\n")
    
    #replacing missing values with null string
    for i in selected_features:
        movies_data[i]=movies_data[i].fillna('')

    #combine features (Dimentionality reduc.)
    combined_features =movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']#+' '+movies_data['overview']

    # Add a new column 'combined_features' to the DataFrame
    movies_data['combined_features'] = combined_features

    # Write the DataFrame to a new CSV file, including the 'combined_features' column
    movies_data.to_csv('movies_with_combined_features.csv', index=False)


def exe():
    #convert text data to feature vectors
    movies_data=pd.read_csv('movies_with_combined_features.csv')
    combined_features=movies_data['combined_features']
    vectorizer=TfidfVectorizer()
    feature_vectors=vectorizer.fit_transform(combined_features)
    # print(feature_vectors)
    # print("\n")

    #getting similarity score using cosine similarity
    similarity=cosine_similarity(feature_vectors)
    # print(similarity)
    # print("\n")
    # print(similarity.shape)
    # print("\n")

    #input from user
    movie_name=input('Enter movie name? ')

    #creating list with all movie names given in dataset
    titles=movies_data['title'].tolist()

    #find match for movie name entered by user
    matchNames=difflib.get_close_matches(movie_name,titles)
    # print(matchNames)

    selected_match=matchNames[0]
    # print(selected_match)

    #find index of selected match
    index=movies_data[movies_data.title==selected_match]['index'].values[0]
    #print(index)

    #getting list of similar movies
    score=list(enumerate(similarity[index]))
    # print(score)

    #sorting based on score
    sorted_similar_movies=sorted(score,key= lambda x:x[1], reverse=True)

    #display top n movies after rematching index with titles
    print("\nSuggested Movies-> \n")
    c=1
    for i in sorted_similar_movies:
        index=i[0]
        movie_title=movies_data[movies_data.index==index]['title'].values[0]
        movie_description=movies_data[movies_data.index==index]['overview'].values[0]
        movie_release=movies_data[movies_data.index==index]['release_date'].values[0]
        movie_cast=movies_data[movies_data.index==index]['cast'].values[0]
        movie_director=movies_data[movies_data.index==index]['director'].values[0]
        if(c<=5):
            print(c, ".", movie_title)
            print('\nDescription: ',(textwrap.fill(movie_description, width=70)))
            print('\nRelease:       ',movie_release)
            print('Cast:          ',movie_cast)
            print('Director:      ',movie_director)
            print('\n')
            c+=1
        else:
            break

def main():
    x='y'
    while(x=='y' or x=='Y'):

        print("Press 1-> Process CSV file")
        print("Press 2-> Execute")

        c=int(input("Choice : "))
        print()

        if(c==1):
            process_csv()
        elif(c==2):
            exe()
        else:
            print("Choice invalid\n")

        x=input("do you want to continue ?(y/n) ")
        x=x[0]
        print()

if __name__=="__main__":
    main()