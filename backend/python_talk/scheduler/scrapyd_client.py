import requests
from typing import Dict, Optional

class ScrapydClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def schedule(
        self,
        project: str,
        spider: str,
        settings: Optional[Dict] = None,
        args: Optional[Dict] = None,
    ):
        """
        调度一个 spider
        """
        data = {
            "project": project,
            "spider": spider,
        }

        if settings:
            for k, v in settings.items():
                data[f"setting_{k}"] = v

        if args:
            data.update(args)

        return requests.post(
            f"{self.base_url}/schedule.json",
            data=data,
            timeout=10,
        )
