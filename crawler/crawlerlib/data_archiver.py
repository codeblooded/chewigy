from os import getcwd, path, mkdir
from datetime import datetime

class DataArchiver(object):
    def __init__(self):
        self.data_dir = self._create_data_directory()

    def write_file(self, path, contents=''):
        file = open(self.data_dir + '/' + path)
        file.write(contents)
        file.close()


    def _create_data_directory(self):
        """
        Create a data directory and a subdirectory for today's crawl. Return the
        subdirectory, so other files can be stored inside.

        The directories are created relative to the present directory:
        - data/
        - data/TIMESTAMP/
        """
        root_data_dir = getcwd() + '/data'
        today = datetime.now().strftime("%m_%d_%y__%H_%M_%S")
        today_data_dir = '{0}/{1}'.format(root_data_dir, today)

        if not path.exists(root_data_dir):
            mkdir(getcwd() + '/data/')

        if not path.exists(today_data_dir):
            mkdir(today_data_dir)
        
        return today_data_dir
    