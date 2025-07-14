import praw
import ollama
import os
from reddit_config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def extract_username(url):
    return url.strip("/").split("/")[-1]

def get_user_data(username):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    user = reddit.redditor(username)
    content = []

    for post in user.submissions.new(limit=20):
        content.append("Post Title: " + post.title)
        content.append("Post Body: " + post.selftext)
        content.append("")

    for comment in user.comments.new(limit=20):
        content.append("Comment: " + comment.body)
        content.append("")

    return "\n".join(content)

def generate_persona(content, username):
    prompt = f"""
        Hi, I want you to generate a detailed user persona based on a Reddit user's posts and comments.
        
        Use the structure below. For each section, include a short quote or comment from the user that supports your conclusion. Keep it simple, human-readable, and use bullet points or short paragraphs.
        
        ### 1. User Details
        - **Username**: u/{username}
        - **Age**: (guess if possible)
        - **Occupation / Role**: (guess based on their content)
        - **Location**: (if mentioned or guessable)
        - **Tier**: (Urban/Rural/Tier 1/2/3 if possible)
        - **Marital/Relationship Status**: (if guessable)
        
        ### 2. Behavior and Habits
        - What the user frequently talks about or does online
        - How active they are on Reddit
        - What kind of language or tone they use
        - Cite 1–2 comments or post snippets
        
        ### 3. Frustrations / Pain Points
        - What annoys or bothers them
        - Things they complain about or struggle with
        - Include short quotes as evidence
        
        ### 4. Motivations
        - What drives them, interests them, or makes them excited
        - Why they engage in certain topics or communities
        - Add relevant quotes that show this
        
        ### 5. Personality Type
        - Introvert or extrovert?
        - Thinking or feeling oriented?
        - Intuitive or factual?
        - Perceiving or judging?
        - (You can guess this based on language, tone, openness)
        
        ### 6. Goals and Needs
        - What the user wants to achieve
        - What they are working on or asking about
        - Show this using their post/comment quotes
        
        Be sure to include actual quotes from the user's content to support each insight. Keep formatting clean and easy to read.
        
        Below is the user’s Reddit data:
        {content}
        """

    response = ollama.chat(
        model="gemma3:1b",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def save_persona(username, text):
    os.makedirs("personas", exist_ok=True)
    file_path = "personas/" + username + ".txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

if __name__ == "__main__":
    print("Enter Reddit Profile URL:")
    url = input().strip()
    username = extract_username(url)

    print("Fetching Reddit data...")
    data = get_user_data(username)

    print("Generating persona using Ollama...")
    persona = generate_persona(data, username)

    print("Saving persona to file...")
    save_persona(username, persona)

    print("File saved at: personas/" + username + ".txt")
