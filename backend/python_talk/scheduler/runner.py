from apscheduler.schedulers.blocking import BlockingScheduler
from python_talk.scheduler.jobs import run_spider

def start_scheduler():
    """
    启动 APScheduler，每 5 分钟执行一次爬虫。
    """
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")

    scheduler.add_job(
        run_spider,
        trigger="interval",
        minutes=2,                # 每 5 分钟执行一次
        args=["booksbot", "manning"],  # project, spider
        id="booksbot_manning_5min",
        max_instances=1,
        coalesce=True,
    )

    print("Scheduler started. Waiting for jobs...")
    scheduler.start()


if __name__ == "__main__":
    start_scheduler()
