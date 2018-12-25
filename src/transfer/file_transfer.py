from src.transfer.transfer import Transfer


class FileTransfer(Transfer):

    def __init__(self, waittime, executions):
        super().__init__()
        self.waittime = waittime
        self.executions = executions
