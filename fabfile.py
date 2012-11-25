from fabric.api import task, env
#from butter import drush, deploy, drupal


# Host settings
@task
def qa():
    """
    The qa server definition
    """
    env.config_file = 'config.production.py'
    env.hosts = ['ombu@d2.ombuweb.com:34165']
    env.host_type = 'qa'
    env.user = 'ombu'
    env.host_webserver_user = 'www-data'
    env.host_site_path = '/mnt/main/qa/qa2'


@task
def push(ref='origin/master'):
    """
    Deploy a commit to a host
    """
    from fabric.api import local, run, cd
    from fabric.contrib.project import rsync_project
    local('pelican -s %s -d' % env.config_file)
    with cd(env.host_site_path):
        run('rm -rf public && mkdir public')
    rsync_project(
        remote_dir=env.host_site_path + '/public',
        local_dir='output/'
    )
    with cd(env.host_site_path):
        run('chown -R ombu:www-data public && chmod -R 02750 public')
