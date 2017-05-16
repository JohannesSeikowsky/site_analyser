from urlparse import urlparse # for py2, maybe upgrade?

def get_central_domain(url):
    parsed_obj = urlparse(url)
    all_domain_parts = parsed_obj.netloc.split(".")
    central_domain = all_domain_parts[-2] + "." + all_domain_parts[-1]
    return central_domain
