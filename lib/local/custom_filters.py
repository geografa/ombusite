from random import choice

CF_DOMAINS = ['d1vq0q4bhrh1pl.cloudfront.net', 'd2pi1004d09op3.cloudfront.net']


def cdn(text):
    if text[0] != '/':
        text = '/' + text
    return 'http://' + choice(CF_DOMAINS) + text
