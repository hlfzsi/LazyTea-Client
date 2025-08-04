import os

__version__ = "0.1.0a1"
__author__ = "hlfzsi"

os.environ["UIVERSION"] = __version__
os.environ["UIAUTHOR"] = __author__
os.environ["LOGLEVEL"] = "DEBUG"

if __name__ == "__main__":
    from LazyTea.main_window import run
    run()
