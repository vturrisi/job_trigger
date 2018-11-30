import os.path
from functools import partial
from itertools import repeat
from multiprocessing import Pool
from io import StringIO
from subprocess import Popen, PIPE
import subprocess


class ShellExecutor:
    '''
    Schedule and launches multiple processes for execution

    args:
    - jobs_file: text file containing one command per line

    - max_jobs: number of jobs to run in parallel.
      Use -1 to select max number of cores available

    - return_outputs: whether to return ouputs (output and error) of each process

    Example of execution:
    test.txt = "echo 1
                echo 2
                echo 3
                echo 4
                echo 5"

    e = ShellExecutor('text.txt', return_outputs=True)
    outputs, errors = e.execute()
    '''

    def __init__(self, jobs_file, max_jobs=-1, return_outputs=False):
        assert os.path.isfile(jobs_file)

        self.commands = []
        with open(jobs_file) as f:
            for command in f:
                command = command.strip()
                self.commands.append(command)

        if max_jobs == -1:
            self.pool = Pool()
        else:
            self.pool = Pool(max_jobs)
        self.return_outputs = return_outputs


    def execute(self):
        partial_func = partial(subprocess.run, shell=True,
                               capture_output=self.return_outputs)

        r = self.pool.map(partial_func, self.commands)

        if self.return_outputs:
            outs, errors = zip(*[(output.stdout.decode(),
                                output.stderr.decode())
                                for output in r])
            return outs, errors
