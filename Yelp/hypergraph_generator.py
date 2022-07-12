import json
import numpy as np
import parsers

def save_food_hypergraph(write=True, print_process = False):
    food = parsers.get_food_business()
    review = parsers.load_review()
    users = parsers.load_users()

    # conver to np array for the sake of computational time,
    # np arrays are processed much faster than the "vanilla" arrays
    np_food_id = np.array(food['id'])
    np_review_business_id = np.array(review['business_id'])
    np_review_user_ids = np.array(review['user_id'])
    np_user_ids = np.array(users['user_id'])

    food_hypergraph = []
    if write:
        with open("restaurant_as_hyperedge.txt", 'w') as f:
            print("It takes really long to process all the restaurant data")
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
    food_businesses = parsers.get_food_business()

    if label == 'location':
        with open("location_as_label.txt", 'w') as f:
            for i in range(0, len(food_businesses['id'])):
                f.write(str(food_businesses['latitude'][i]))
                f.write(",")
                f.write(str(food_businesses['longitude'][i]))
                f.write('\n')
    elif label == 'city': 
        cities = sorted(list(set(food_businesses['city'])))
        with open('city_labels.txt', 'w') as f:
            for i in range(0, len(cities)):
                f.write(str(i)+": "+ cities[i]+'\n')

        with open('city_as_label.txt', 'w') as f:
            for i in range(0, len(food_businesses['id'])):
                f.write(str(cities.index(food_businesses['city'][i]))+'\n')

    elif label == 'state':
        states = sorted(list(set(food_businesses['state'])))
        with open('state_labels.txt', 'w') as f:
            for i in range(0, len(states)):
                f.write(str(i)+": "+ states[i]+'\n')
        with open('state_as_label.txt', 'w') as f:
            for i in range(0, len(food_businesses['id'])):
                f.write(str(states.index(food_businesses['state'][i]))+'\n')
    else:
        with open(label+"_as_label.txt",'w') as f:
            for i in food_businesses[label]:
                f.write(str(i))
                f.write('\n')


def main():
    pass

if __name__ == "__main__":
   save_food_hypergraph(print_process = True)
   food_hypergraph_labels(label = "location")
   food_hypergraph_labels(label = "city")
   food_hypergraph_labels(label = "state")