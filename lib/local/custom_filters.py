from random import choice
import time
import md5
from jinja2 import contextfilter

CF_DOMAINS = ['d1vq0q4bhrh1pl.cloudfront.net', 'd2pi1004d09op3.cloudfront.net']


@contextfilter
def cdn(context, path):
    """
    Returns a CDN link when building for production
    Returns a regular link otherwise
    """
    if context['BUILD_ENV'] == 'production':
        if path.find('?') == -1:
            bust = md5.new(str(time.time())).hexdigest()[:8]
            path = path + '?' + bust
        return 'http://' + choice(CF_DOMAINS) + '/' + path
    else:
        return '/' + path
