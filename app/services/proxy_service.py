def parse_proxy(proxy_str):
    if not proxy_str:
        return None
    host, port = proxy_str.split(":")
    return ("socks5", host, int(port))
