import urllib
import http.client

def send_rca(theRciUri, theTarget, theArguments={}):
    escapedArguments = urllib.parse.quote("&".join(list(map(lambda key, value: key + "=" + value,
                             theArguments.keys(),
                             theArguments.values()))))
    post_data = "target={target}&arguments={arguments}".format(target=theTarget,
                                                               arguments=escapedArguments)
    rci_uri = urllib.parse.urlparse(theRciUri)
    conn = http.client.HTTPConnection(rci_uri.netloc)
    conn.request("POST", rci_uri.path + "?" + post_data, post_data)
    response = conn.getresponse()
    raw_payload = response.read().decode('utf-8')
    conn.close()
    return response.status, raw_payload
