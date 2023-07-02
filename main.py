import args
import storage
from naive_crawler import NaiveCrawler

if __name__ == "__main__":
    SAVEPATH = "crawler_state"
    database = storage.Memento(SAVEPATH)

    params = args.get_parsed_args()
    params["database"] = database

    lil_spidey = NaiveCrawler(**params)
    lil_spidey.initium()