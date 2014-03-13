from collections import Counter
import random
import string
import time
import pdb
import dis

alphabet = string.lowercase

possible_users = ['alice', 'jim', 'john', 'bob', 'peter']
real_users = {'bob':'password', 'jimmy':'foobar', 'roger':'p4assword'}

NUM_USERS = 1000

def random_string(len=10):
    return ''.join([random.choice(alphabet) for x in xrange(0, len)])


def login(username, password, users):
    """This is our target."""
    if username in users:
        if password == users[username]:
            return True
    return False


def attack_users(users, possible_users, num_attempts=1000):
    """You don't need many attempts because the comparison and dictionary check
    produces large timing differentials.
    """

    stats = Counter()
    trys = num_attempts
    
    #print "Enumerating the username from this list of possible candidates", possible_users

    for x in xrange(0, trys):
        for user in possible_users:

            start = time.time()
            login(user, 'thiscanbeanything', users)
            end = time.time()

            took = end - start
            stats[user] += took
            
    
    print stats
    our_guess = max(stats, key=stats.get)
    print "We think there could be a user called", our_guess

    return our_guess



def generate_fake_users(how_many):
    # Generate a bunch of fake users.
    users = dict()
    for fake_user in xrange(0, how_many):
        users[random_string(10)] = random_string(10)
    return users


if __name__ == '__main__':
    users = generate_fake_users(NUM_USERS)
    for x in xrange(NUM_USERS):
        possible_users.append(random_string(10))
    users.update(real_users)
    attack_users(users, possible_users)
