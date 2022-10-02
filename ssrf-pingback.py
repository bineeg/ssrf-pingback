#! /usr/bin/env python3
from optparse import OptionParser
from time import sleep
import requests

poll_delay = None
url_file = ""
biid_req_url = ""
burp_collab_url = ""
urls = []


def parse_arguments():
    global url_file, biid_req_url, burp_collab_url, poll_delay
    usage = "\tUsage: ssrf-pingback.py --uf url_file --biid biid_req_url --pdelay poll_delay \n\tfor more try help -h"

    parser = OptionParser(
        usage=usage)

    # add options
    parser.add_option('--uf', dest='url_file',
                      type='string',
                      help='specify the url file name',)
    parser.add_option('--biid', dest='biid_req_url',
                      type='string',
                      help='specify the biid url',)
    parser.add_option('--pdelay', dest='poll_delay',
                      type='float',
                      help='time delay between each poll',)

    (options, args) = parser.parse_args()
    if (options.url_file == None):
        print(parser.usage)
        exit(0)
    else:
        url_file = options.url_file

    if options.poll_delay is not None:
        poll_delay = options.poll_delay
    else:
        poll_delay = 1
    if (options.biid_req_url == None):
        print(parser.usage)
        exit(0)
    else:
        biid_req_url = options.biid_req_url


class bcolors:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def urls_load():
    global url_file
    try:
        f = open(url_file, "r")
        urls = f.read().split('\n')
        print('Checking urls\n')
        for i in urls:
            if len(i.rstrip()) > 1:
                request_handler(i)
    except Exception as e:
        print("Exception : "+str(e))


def request_handler(req):
    global urls

    re = requests.get(url=req)
    sleep(poll_delay)
    poll_req = requests.get(biid_req_url)
    if(len(poll_req.text) > 2):
        urls.append(req)


if __name__ == "__main__":

    print(bcolors.OKBLUE + bcolors.BOLD +
          '\n\tSSRF PING BACK\n'+bcolors.ENDC+bcolors.ENDC)
    parse_arguments()
    urls_load()
    if(len(urls)) >= 1:
        print('\n[!] Got ping\n')
        for i in urls:
            print('\tURL %s' % (i))
    else:
        print('[-] No ping back')
