from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_synthetic_data(n=100):
    data = []
    for _ in range(n):
        post = fake.sentence(nb_words=12)
        name = fake.name()
        email = fake.email()
        engagement = random.choice(["Like", "Comment", "Share"])
        comment = fake.sentence(nb_words=10) if engagement == "Comment" else ""
        data.append([post, name, email, engagement, comment])
    df = pd.DataFrame(data, columns=["Post", "Engager", "Email", "EngagementType", "Comment"])
    return df