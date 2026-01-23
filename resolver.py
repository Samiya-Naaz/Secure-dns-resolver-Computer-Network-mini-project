import socket
import time

# Simple cache dictionary: { query: (result, expiry_time) }
dns_cache = {}
CACHE_TTL = 60  # seconds

def get_from_cache(query):
    if query in dns_cache:
        result, expiry = dns_cache[query]
        if time.time() < expiry:
            print(f"[CACHE HIT] {query}")
            return result
        else:
            print(f"[CACHE EXPIRED] {query}")
            del dns_cache[query]
    return None

def add_to_cache(query, result):
    dns_cache[query] = (result, time.time() + CACHE_TTL)

def recursive_dns_lookup(domain):
    cached = get_from_cache(domain)
    if cached:
        return cached

    try:
        result = socket.gethostbyname(domain)
        add_to_cache(domain, result)
        return result
    except socket.gaierror:
        return "Domain not found."

def reverse_dns_lookup(ip):
    cached = get_from_cache(ip)
    if cached:
        return cached

    try:
        result = socket.gethostbyaddr(ip)[0]
        add_to_cache(ip, result)
        return result
    except socket.herror:
        return "Hostname not found."

