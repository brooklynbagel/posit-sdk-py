import warnings

from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar

import requests

from .config import Config


T = TypeVar("T")


class Resource(ABC, dict):
    def __init__(self, config: Config, session: requests.Session, **kwargs):
        super().__init__(**kwargs)
        self.config: Config
        super().__setattr__("config", config)
        self.session: requests.Session
        super().__setattr__("session", session)

    def __getitem__(self, key):
        warnings.warn(
            f"__getitem__ for '{key}' does not support backwards compatibility. Consider using field based access instead: 'instance.{key}'",
            FutureWarning,
        )
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        warnings.warn(
            f"__setitem__ for '{key}' does not support backwards compatibility. Consider using field based access instead: 'instance.{key} = {value}",
            FutureWarning,
        )
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        warnings.warn(
            f"__delitem__ for '{key}' does not support backwards compatibility. Consider using field based access instead: 'del instance.{key}'",
            FutureWarning,
        )
        return super().__delitem__(key)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("cannot set attributes: use update() instead")


class Resources(ABC):
    def __init__(self, config: Config, session: requests.Session) -> None:
        self.config = config
        self.session = session
