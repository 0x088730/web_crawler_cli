import argparse


def get_parsed_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--initial_url", 
        #nargs=1,  
        type=str,
        default = "https://blog.scrapinghub.com",
        help="Enter a start url (default: 'https://blog.scrapinghub.com')",
        #required=True
        )
    
    parser.add_argument(
        "-ad",
        "--allowed_domains", 
        nargs="+",  
        type=str,
        default = ["blog.scrapinghub.com"],
        help="Enter allowed domains (defualt: 'blog.scrapinghub.com')",
        #required=True
        )

    parser.add_argument(
        "-d",
        "--depth", 
        type=int,
        default=1,
        help="Enter the depth, aka number of sites to crawl (default: 1)"
        #required=True
        )
   

    # parse the command line
    args = parser.parse_args()

    # Pack up the args to a neat lil' dictionary
    args = {
        'initial_url': str(args.initial_url),
        'allowed_domains': list(args.allowed_domains),
        'depth': int(args.depth)
        }
    
    return args
