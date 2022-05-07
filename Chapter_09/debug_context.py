import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# デフォルトをINFOレベルとし、DEBUGレベルのログは無視する
logger.setLevel(logging.INFO)

@contextmanager
def debug_context():
    level = logger.level

    try:
        # ログレベルを変更する
        logger.setLevel(logging.DEBUG)
        yield
    
    finally:
        logger.setLevel(level)

def main():
    logger.info("before: info log")
    logger.debug("before: debug log")

    # DEBUGログを見たい処理をwithブロック内で実行する
    with debug_context():
        logger.info("inside the block: info log")
        logger.debug("inside the block: debug log")

    logger.info("after: info log")
    logger.debug("after: debug log")

if __name__ == "__main__":
    main()
