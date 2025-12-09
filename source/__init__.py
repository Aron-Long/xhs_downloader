from .CLI import cli
try:
    from .TUI import XHSDownloader
except ImportError:
    XHSDownloader = None
from .application import XHS
from .module import Settings

__all__ = [
    "XHS",
    "XHSDownloader",
    "cli",
    "Settings",
]
