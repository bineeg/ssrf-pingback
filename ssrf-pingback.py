#! /usr/bin/env python3
from optparse import OptionParser
from time import sleep
import requests

poll_delay = None
url_file = ""
biid_req_url = ""
urls = []
output_file = ""


def parse_arguments():
    global url_file, biid_req_url, poll_delay, output_file
    usage = "\tUsage: ssrf-pingback.py --uf url_file --biid biid_req_url --pdelay poll_delay [--outfile filename] \n\tfor more try help -h"

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
    parser.add_option('--outfile',  dest='out_file',
                      type='string',
                      help='output file name',)

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
    output_file = options.out_file if options.out_file != None else None


class bcolors:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'


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


def file_write(data):
    try:
        with open(output_file, 'w') as writer:
            writer.write(data)
            print(bcolors.WARNING+'\nOutput file : '+output_file+bcolors.ENDC)
    except Exception as e:
        print("Exception in file write "+str(e))


if __name__ == "__main__":

    print(bcolors.OKBLUE + bcolors.BOLD +
          '\n\tSSRF PING BACK\n'+bcolors.ENDC+bcolors.ENDC)
    parse_arguments()
    urls_load()
    buffer = ""
    if(len(urls)) >= 1:
        print('\n[!] Got ping\n')
        for i in urls:
            buffer += str(i)+'\n'
            print('\tURL %s' % (i))
        if output_file is not None:
            file_write(buffer)
    else:
        buffer='[-] No ping back'
        if output_file is not None:
            file_write(buffer)
        print(buffer)
