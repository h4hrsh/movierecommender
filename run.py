import pickle
import numpy as np
import difflib
import streamlit as st

with open('C:/Users/harsh/OneDrive/Desktop/heroku/movies.sav','rb') as f:
	allmovie=pickle.load(f)
with open('C:/Users/harsh/OneDrive/Desktop/heroku/movierec.sav', 'rb') as f:
	model=pickle.load(f)


def movielist(mov,n=5):
	mymov=difflib.get_close_matches(mov,allmovie)[0]

	# finding the index of the movie with title
	idx=0
	for i in range(len(allmovie)):
		if allmovie[i]==mymov:
			idx=i
			break

	sim_score=list(enumerate(model[idx]))
	sorted_similar_movies = sorted(sim_score, key = lambda x:x[1], reverse = True)

	soln=[]
	for i in range(n):
		soln.append(allmovie[sorted_similar_movies[i][0]])
	
	ans=''
	for x in soln:
		ans=ans+x+'\n\n'
	return ans

def main():
	st.title('Movie prediction App\n Made with love')
	movie=st.text_input('Enter the movie')
	n=st.slider('Number of movies you want',min_value=0,max_value=10)

	reccomended=''
	if st.button('Movie list'):
		reccomended=movielist(movie,int(n))
		st.balloons()
	
	st.success(reccomended)


if __name__=='__main__':
	main()
	print(movielist('ironman',3))
	