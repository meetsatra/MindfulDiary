import random
from nltk.sentiment import SentimentIntensityAnalyzer

# import nltk
# nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

positive_quotes = [
    "Every day is a new beginning. Seize the opportunity and make the most of it.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "You are capable of amazing things. Keep pushing forward and striving for greatness.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do. Keep pursuing your passion.",
    "Your positive action combined with positive thinking results in success. Stay positive and focused.",
]

negative_quotes = [
    "Remember, tough times never last, but tough people do. Stay strong and resilient. Tomorrow is a new day, filled with possibilities.",
    "Don't let the fear of losing be greater than the excitement of winning. Keep moving forward, and tomorrow will bring new opportunities for success.",
    "Challenges make you stronger. Embrace them and use them as opportunities for growth. Tomorrow is a chance to apply the lessons you've learned today.",
    "Remember, difficult roads often lead to beautiful destinations. Keep going and don't give up. Tomorrow is a fresh start, another step towards your goals.",
    "You are not alone in this. Reach out for support when you need it. You've got this! Tomorrow is a new day, and you have the strength to overcome any obstacle.",
    "Stay patient and trust your journey. Good things take time. Tomorrow holds the promise of progress and new beginnings.",
]

neutral_quotes = [
    "Take a deep breath and enjoy the present moment. Find joy in the little things around you.",
    "Sometimes the best thing you can do is not think, not wonder, not imagine, not obsess. Just breathe and have faith.",
    "Embrace the uncertainty and let go of the need for control. Trust that everything will work out.",
    "Life is a balance of holding on and letting go. Find the peace within the chaos.",
    "Remember to take care of yourself. Your well-being is important. Practice self-care and self-compassion.",
    "Stay present and mindful. Focus on what you can control and let go of what you can't.",
]

def process_description(desc):
    sentiment = give_sentiments(desc)
    if sentiment == 'Positive':
        return random.choice(positive_quotes)
    elif sentiment == 'Neutral':
        return random.choice(neutral_quotes)
    else:  # Negative sentiment
        return random.choice(negative_quotes)
    
    

def give_sentiments(desc):
    sentiment_score = sia.polarity_scores(desc)

    # Interpret the sentiment score
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
        return 'Neutral'
    else:
        return 'Negative'