from .scrapyd_client import ScrapydClient

scrapyd = ScrapydClient("http://scrapyd:6800")

def run_spider(project, spider, **kwargs):
    return scrapyd.schedule(
        project=project,
        spider=spider,
        args=kwargs,
    )
