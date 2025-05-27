import random
import time

def chatbot():
    print("Hi there! I'm your chatbot. What would you like to chat about today?")

    # Categories and corresponding responses
    greetings = [
        "Hi there! How's it going?", 
        "Hey, hey! What's up?", 
        "Hello! How can I assist you today?",
        "Greetings, ready to chat?"
    ]
    
    goodbyes = [
        "Goodbye! Have a fabulous day ahead!", 
        "Bye-bye! Hope to chat again soon!",
        "Catch you later! Stay awesome!",
        "See ya! Don't forget to smile today!"
    ]
    
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the computer go to the doctor? It had a virus!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't programmers like nature? It has too many bugs!",
        "What do you call fake spaghetti? An impasta!"
    ]
    
    weather_comments = [
        "I can't feel the weather, but I bet it's sunny where you are!",
        "It's always a good day in my world! But I'm sure it's a great day outside!",
        "I can't check the weather, but I hope it's warm and cozy where you are!",
        "Imagine the weather is perfect... because it always is!"
    ]
    
    compliments = [
        "You're awesome! Keep being amazing!", 
        "You're a star! Don’t forget that!", 
        "You’ve got this! Keep shining!", 
        "Your energy is contagious! Keep it up!"
    ]
    
    random_thoughts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs!",
        "Imagine if cats could talk. What do you think they'd say?",
        "I wonder if ants have their own version of 'Monday blues'...",
        "Wouldn't it be cool if we could taste colors?"
    ]
    
    motivation = [
        "Believe in yourself! You’re capable of amazing things!",
        "Keep going, even when things get tough. You've got this!",
        "Success comes to those who are consistent. You’re doing great!",
        "Remember, every small step counts. You're closer to your goals than you think!"
    ]
    
    advice = [
        "Take a deep breath, everything will work out just fine!",
        "Sometimes, the best way to move forward is to take a break.",
        "It's okay to not have everything figured out right now. Take it one day at a time.",
        "Don’t be afraid to ask for help when you need it. We all need a little support."
    ]
    
    fun_facts = [
        "Did you know octopuses have three hearts?",
        "Bananas are berries, but strawberries aren't!",
        "The Eiffel Tower can grow by 6 inches in summer due to the expansion of the metal in heat!",
        "A group of flamingos is called a 'flamboyance'!"
    ]
    
    emotions = [
        "I'm feeling super excited today! How about you?",
        "Sometimes I feel a little overwhelmed, but I know it's okay to take things slow.",
        "I'm feeling pretty calm today. It's a peaceful kind of mood.",
        "Feeling adventurous today! Let's go explore new topics!"
    ]
    
    life_goals = [
        "What's one goal you're working towards right now?",
        "Remember, small progress is still progress!",
        "Don’t forget to enjoy the journey, not just the destination!",
        "Your dreams are valid. Keep going after them!"
    ]
    
    music = [
        "What's your favorite genre of music?",
        "I wish I could listen to music, but I can only appreciate it in words!",
        "Do you like to sing in the shower?",
        "Have you ever tried listening to classical music to relax?"
    ]
    
    hobbies = [
        "What do you like to do for fun in your free time?",
        "Do you enjoy reading books? If so, what genre?",
        "I heard some people love knitting. Do you have a hobby like that?",
        "What’s your favorite outdoor activity?"
    ]
    
    travel = [
        "If you could visit anywhere in the world, where would you go?",
        "I’d love to explore the world through your eyes! Tell me about your dream destination!",
        "Do you prefer the beach or the mountains when traveling?",
        "What's the most interesting place you've ever visited?"
    ]
    
    self_care = [
        "Remember to take care of yourself today. You deserve it!",
        "A good book and some tea can do wonders for the soul.",
        "It's okay to take a break and rest. Self-care is so important!",
        "Take a walk outside, breathe in the fresh air. Nature is the best healer!"
    ]
    
    books_and_movies = [
        "What's the best book you've read recently?",
        "Are you into movies or TV shows? What's your current favorite?",
        "If you could star in any movie, what role would you play?",
        "I love hearing about favorite books! Do you prefer fiction or nonfiction?"
    ]
    
    random_quotes = [
        "“The only way to do great work is to love what you do.” – Steve Jobs",
        "“Be the change that you wish to see in the world.” – Mahatma Gandhi",
        "“In the middle of every difficulty lies opportunity.” – Albert Einstein",
        "“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb"
    ]

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if 'bye' in user_input or 'exit' in user_input:
            print(random.choice(goodbyes))
            break
        
        # Random greeting
        elif any(greet in user_input for greet in ["hello", "hi", "hey", "greetings"]):
            print(random.choice(greetings))

        # Asking about how the chatbot is
        elif 'how are you' in user_input:
            print("Chatbot: I'm feeling fabulous, thank you! How about you?")

        # Asking about chatbot's name
        elif 'name' in user_input:
            print("Chatbot: I’m Chatty the Bot! What should I call you?")

        # Random joke
        elif 'joke' in user_input:
            print("Chatbot: Ready for some fun? Here comes a joke!")
            time.sleep(2)  # Adding a small delay for effect
            print(random.choice(jokes))

        # Asking about weather
        elif 'weather' in user_input:
            print(random.choice(weather_comments))

        # Complimenting the user
        elif 'love' in user_input:
            print("Chatbot: Love is in the air! It's beautiful, isn't it? Who or what do you love?")

        elif 'help' in user_input:
            print("Chatbot: I'm here to chat, crack jokes, share weather thoughts, and spread good vibes! Just ask me anything!")

        # Compliments for the user
        elif 'awesome' in user_input or 'good' in user_input:
            print(random.choice(compliments))

        # Random thoughts
        elif 'thoughts' in user_input or 'think' in user_input:
            print(random.choice(random_thoughts))

        # Motivation
        elif 'motivated' in user_input or 'motivation' in user_input:
            print(random.choice(motivation))

        # Life advice
        elif 'advice' in user_input:
            print(random.choice(advice))

        # Fun facts
        elif 'fact' in user_input or 'facts' in user_input:
            print(random.choice(fun_facts))

        # Discussing emotions
        elif 'feel' in user_input or 'emotion' in user_input:
            print(random.choice(emotions))

        # Life goals
        elif 'goals' in user_input:
            print(random.choice(life_goals))

        # Discussing music
        elif 'music' in user_input:
            print(random.choice(music))

        # Hobbies
        elif 'hobby' in user_input:
            print(random.choice(hobbies))

        # Travel
        elif 'travel' in user_input:
            print(random.choice(travel))

        # Self-care
        elif 'care' in user_input:
            print(random.choice(self_care))

        # Books and Movies
        elif 'book' in user_input or 'movie' in user_input:
            print(random.choice(books_and_movies))

        # Random quote
        elif 'quote' in user_input:
            print(random.choice(random_quotes))
        
        else:
            print("Chatbot: Hmm, that's a tricky one! Let me think... Maybe try asking something else?")

if __name__ == "__main__":
    chatbot()