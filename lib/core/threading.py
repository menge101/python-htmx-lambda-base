from mypy_boto3_dynamodb.client import DynamoDBClient
from mypy_boto3_dynamodb.service_resource import Table
from threading import Event, Thread
from typing import Any, Callable, Mapping, NewType

ConnectionThreadResultType = NewType("ConnectionThreadResultType", tuple[str, DynamoDBClient, Table])


class ThreadException(BaseException):
    pass


class ThreadExit(SystemExit):
    pass


class ReturningThread(Thread):
    def __init__(
        self,
        target: Callable,
        name: str | None = None,
        args: tuple = (),
        kwargs: Mapping | None = None,
        *,
        daemon: bool | None = None,
    ):
        # The following four lines are all attributes of the super class but for inexplicable reasons
        # are not being found by code analyzers.  Setting them here to the same initial values the super init
        # should set them to, and calling super init afterward so it can do its thing without these doing anything.
        self._target = target
        self._args = args or []
        self._kwargs = kwargs or {}
        self._started = Event()
        super().__init__(
            group=None,
            target=target,
            name=name,
            args=args,
            kwargs=kwargs,
            daemon=daemon,
        )
        self.return_value: Any | None = None
        self.exception: Exception | None = None

    def run(self):
        try:
            if self._target is not None:
                try:
                    self.return_value = self._target(*self._args, **self._kwargs)
                except Exception as e:
                    self.exception = e
        finally:
            del self._target, self._args, self._kwargs

    def join(self, *args) -> Any | None:
        if self.exception is not None:
            raise self.exception
        super().join(*args)
        return self.return_value

    def start_safe(self):
        if not self._started.is_set():
            self.start()

    def stop(self):
        raise ThreadExit(0)
