
import csv
from models import db, Episode, Guest, Appearance

def import_episodes(file_path):
    with open(file_path, 'r') as csvfile:
        episode_reader = csv.DictReader(csvfile)
        for episode in episode_reader:
            db.session.add(Episode(**episode))
            db.session.commit()
            print(f"Added episode: {episode['date']} - {episode['number']}")