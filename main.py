import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset (use the correct file path)
data = pd.read_csv("election_project11.csv")

# Display the first few rows of the data for debugging
st.write("Dataset Preview:")
st.write(data)  # Check the structure of the data

# Add dropdown for selecting a question
questions = [
    "Which party won the most elections?",
    "What is the total number of votes in each state?",
    "Which candidate received the highest number of votes?",
    "What is the voter turnout in each state?",
    "Which party had the highest vote share in each state?",
    "What is the total number of votes received by each party?",
    "Which party won in the most states?",
    "What percentage of the total votes did each party receive?",
    "How many candidates from each party contested in the election?",
    "What is the average margin of victory for each party?",
    "What is the percentage of votes for the winning party in each state?",
    "What is the total number of votes in each region?",
    "How many parties contested in the election?",
    "Which party had the highest vote share overall?",
    "How many seats did each party win?",
    "What is the gender distribution of the candidates?",
    "Which party had the highest increase in vote share compared to the previous election?",
    "How many states did each candidate win?",
    "What is the total number of valid votes across all states?",
    "What is the average number of votes per candidate?"
]

selected_question = st.selectbox("Select a Question", questions)

# Now, we'll add different visualizations for each selected question
if selected_question == "Which party won the most elections?":
    st.write("Which party won the most elections?")
    if "Result" in data.columns and "Party" in data.columns:
        party_wins = data[data['Result'] == 'Won'].groupby('Party').size().sort_values(ascending=False)
        st.write(party_wins)
        
        # Create bar plot
        plt.figure(figsize=(12, 8))
        sns.barplot(x=party_wins.index, y=party_wins.values, palette="viridis")
        plt.title("Party Wins")
        plt.xlabel("Party")
        plt.ylabel("Number of Wins")
        plt.xticks(rotation=45)
        st.pyplot(plt)  # Ensure the plot renders in Streamlit

elif selected_question == "What is the total number of votes in each state?":
    st.write("Total Votes in Each State")
    if "State" in data.columns and "Total Votes" in data.columns:
        state_votes = data.groupby("State")["Total Votes"].sum().sort_values(ascending=False)
        st.write(state_votes)
        
        # Create bar plot
        plt.figure(figsize=(12, 8))
        sns.barplot(x=state_votes.index, y=state_votes.values, palette="viridis")
        plt.title("Total Votes by State")
        plt.xlabel("State")
        plt.ylabel("Total Votes")
        plt.xticks(rotation=45)
        st.pyplot(plt)  # Ensure the plot renders in Streamlit

elif selected_question == "Which candidate received the highest number of votes?":
    st.write("Candidate with Highest Votes")
    if "Candidate" in data.columns and "Total Votes" in data.columns:
        highest_votes = data.loc[data['Total Votes'].idxmax()]
        st.write(highest_votes)
        st.write(f"The candidate with the highest votes is {highest_votes['Candidate']} with {highest_votes['Total Votes']} votes.")
        
        # Create bar plot for highest votes
        plt.figure(figsize=(12, 8))
        sns.barplot(x=[highest_votes['Candidate']], y=[highest_votes['Total Votes']], palette="viridis")
        plt.title("Highest Votes Received by a Candidate")
        plt.xlabel("Candidate")
        plt.ylabel("Votes")
        st.pyplot(plt)  # Ensure the plot renders in Streamlit

# More questions can be added similarly...