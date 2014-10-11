from fabric.api import *

@task(default=True)
def test():
    local('nosetests')