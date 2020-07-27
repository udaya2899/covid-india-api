def post_worker_init(worker):
    from app import start_thread
    start_thread()