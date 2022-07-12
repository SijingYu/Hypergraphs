import json
import numpy as np

def load_review():
    reviews = []
    with open('raw-data/Yelp/yelp_academic_dataset_review.json') as f:
        for line in f:
            reviews.append(json.loads(line))

    new_reviews = {'review_id': [], 
        'user_id': [], 
        'business_id': [], 
        'stars': [], 
        'useful': [], 
        'funny': [], 
        'cool': [], 
        'text': [], 
        'date': []}

    for rev in reviews:
        new_reviews['review_id'].append(rev['review_id'])
        new_reviews['user_id'].append(rev['user_id'])
        new_reviews['business_id'].append(rev['business_id'])
        new_reviews['stars'].append(rev['stars'])
        new_reviews['useful'].append(rev['useful'])
        new_reviews['funny'].append(rev['funny'])
        new_reviews['cool'].append(rev['cool'])
        new_reviews['text'].append(rev['text'])
        new_reviews['date'].append(rev['date'])

    return new_reviews


def load_business():
    businesses = []
    with open('raw-data/Yelp/yelp_academic_dataset_business.json') as f:
        for line in f:
            businesses.append(json.loads(line))


    new_businesses = {
        "business_id": [],
        'name': [],
        'address': [],
        'city': [],
        'state': [],
        'postal_code': [],
        'latitude': [],
        'longitude': [],
        'stars': [],
        'review_count': [],
        'is_open': [],
        'attributes': [],
        'categories': [],
        'hours': []
    }

    for bus in businesses:
        new_businesses['business_id'].append(bus['business_id'])
        new_businesses['name'].append(bus['name'])
        new_businesses['address'].append(bus['address'])
        new_businesses['city'].append(bus['city'])
        new_businesses['state'].append(bus['state'])
        new_businesses['postal_code'].append(bus['postal_code'])
        new_businesses['latitude'].append(bus['latitude'])
        new_businesses['longitude'].append(bus['longitude'])
        new_businesses['stars'].append(bus['stars'])
        new_businesses['review_count'].append(bus['review_count'])
        new_businesses['is_open'].append(bus['is_open'])
        new_businesses['attributes'].append(bus['attributes'])
        new_businesses['categories'].append(bus['categories'])
        new_businesses['hours'].append(bus['hours'])

    return new_businesses


def load_users():
    users = []
    with open('raw-data/Yelp/yelp_academic_dataset_user.json') as f:
        for line in f:
            users.append(json.loads(line))

    new_users ={
    'user_id': [],
    'name': [],
    'review_count': [],
    'yelping_since': [],
    'useful': [],
    'funny': [],
    'cool': [],
    'elite': [],
    'friends':[]}

    for user in users:
        new_users['user_id'].append(user['user_id'])
        new_users['name'].append(user['name'])
        new_users['review_count'].append(user['review_count'])
        new_users['yelping_since'].append(user['yelping_since'])
        new_users['useful'].append(user['useful'])
        new_users['funny'].append(user['funny'])
        new_users['cool'].append(user['cool'])
        new_users['elite'].append(user['elite'])
        new_users['friends'].append(user['friends'])

    return new_users

def get_food_business():
    business = load_business()
    food = {
        'original_index': [],
        'id': [],
        'latitude': [],
        'longitude': [],
        'name': [],
        'address': [],
        'city': [],
        'state': [],
        'postal_code': [],
        'latitude': [],
        'longitude': [],
        'stars': [],
        'review_count': [],
        'is_open': [],
        'attributes': [],
        'categories': [],
        'hours': []
    }

    for i in range(0,len(business['categories'])):
        if (not business['categories'][i] == None) and ("food" in business['categories'][i].lower() or "restaurant" in business['categories'][i].lower()):
            food['original_index'].append(i)
            food['id'].append(business['business_id'][i])
            food['latitude'].append(business['latitude'][i])
            food['longitude'].append(business['latitude'][i])
            food['name'].append(business['name'][i])
            food['address'].append(business['address'][i])
            food['city'].append(business['city'][i])
            food['state'].append(business['state'][i])
            food['postal_code'].append(business['postal_code'][i])
            food['stars'].append(business['stars'][i])
            food['review_count'].append(business['review_count'][i])
            food['is_open'].append(business['is_open'][i])
            food['attributes'].append(business['attributes'][i])
            food['categories'].append(business['categories'][i])
            food['hours'].append(business['hours'][i])
    return food

def main():
    pass

if __name__ == "__main__":
    users = load_users()
    with open('user_ids.txt', 'w') as f:
        for i in range(0, len(users['user_id'])):
            f.write(str(i)+": "+ users['user_id'][i] +'\n')

    food = get_food_business()
    with open('food_business.txt', 'w') as f:
        for i in range(0, len(food['id'])):
            f.write(str(i)+": "+ food['id'][i] +'\n')
