import json
import numpy as np

def load_review():
    reviews = []
    with open('yelp_academic_dataset_review.json') as f:
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
    with open('yelp_academic_dataset_business.json') as f:
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
    with open('yelp_academic_dataset_user.json') as f:
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

def save_food_hypergraph(write=True, print_process = False):
    food = get_food_business()
    review = load_review()
    users = load_users()

    # conver to np array for the sake of computational time,
    # np arrays are processed much faster than the "vanilla" arrays
    np_food_id = np.array(food['id'])
    np_review_business_id = np.array(review['business_id'])
    np_review_user_ids = np.array(review['user_id'])
    np_user_ids = np.array(users['user_id'])

    food_hypergraph = []
    if write:
        with open("restaurant_as_hyperedge", 'w') as f:
            for i in range(0, len(food)):
                if i % 500 == 0 and print_process:
                    print("finished writing the ")
                    print(i)
                    print("th node")
                #index = review_business_ids.index(food_id[i])
                #indices = np.where(np_review_business_id==food_id[i])[0]
                indices = np.in1d(np_review_business_id,np_food_id[i]).nonzero()[0]
                #print(indices)
                #print(",".join(map(str, sorted((np_user_ids[:,None] == np_review_user_ids[indices]).argmax(axis=0)))))
                #print(i)
                #print(",".join(map(str, np.in1d(np_user_ids,np_review_user_ids[indices]).nonzero()[0])))
                #print(",".join(map(str, np_review_user_ids[indices])))
                #print("\n")
                #f.write(",".join(map(str, np_review_user_ids[indices])))
                #print(",".join(map(str, np.in1d(np_user_ids,np_review_user_ids[indices]).nonzero()[0])))
                # The following implementation turns out to be the fastest of all tried
                food_hypergraph.append(np.in1d(np_user_ids,np_review_user_ids[indices]).nonzero()[0])
                f.write(",".join(map(str, np.in1d(np_user_ids,np_review_user_ids[indices]).nonzero()[0])))
                f.write('\n')
    else:
        for i in range(0, len(food)):
            if i % 500 == 0 and print_process:
                print("finished the ")
                print(i)
                print("th node")
                indices = np.in1d(np_review_business_id,np_food_id[i]).nonzero()[0]
                food_hypergraph.append(np.in1d(np_user_ids,np_review_user_ids[indices]).nonzero()[0])
    
    return food_hypergraph

# all choices of labels: 'original_id', 'id', 'latitude', 'longitude', 'name', 'address', 'city', 'state',
#       'postal_code', 'stars', 'review_count', 'is_open', 'attributes', 'categories', 'hours'

def food_hypergraph_labels(label = "location", write = True):
    food_businesses = get_food_business()

    if label == 'location':
        with open("location_as_label", 'w') as f:
            for i in range(0, len(food_businesses['id'])):
                f.write(str(food_businesses['latitude'][i]))
                f.write(",")
                f.write(str(food_businesses['longitude'][i]))
                f.write('\n')
    elif label == 'city': 
        cities = sorted(list(set(food_businesses['city'])))
        with open('city_labels', 'w') as f:
            for i in range(0, len(cities)):
                f.write(str(i)+": "+ cities[i])

        with open('city_as_label', 'w') as f:
           for i in range(0, len(food_businesses['id'])):
               f.write(str(cities.index(food_businesses['city']))+'\n')
    elif label == 'state':
        states = sorted(list(set(food_businesses['state'])))
        with open('state_labels', 'w') as f:
            for i in range(0, len(states)):
                f.write(str(i)+": "+ states[i])
    else:
        with open(label+"_as_label",'w') as f:
            for i in food_businesses[label]:
                f.write(str(i))
                f.write('\n')

    