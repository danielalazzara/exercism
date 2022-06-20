import random

def private_key(p):
    alice = random.randint(1, p)
    return alice

def public_key(p, g, private):
    p_key = (g ** private) % p
    return p_key


def secret(p, public, private):
    return (public ** private) % p
