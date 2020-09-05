import os

c = get_config()

c.JupyterHub.spawner_class = 'jhub.SwarmSpawner'

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.base_url = '/base_url'

# First pulls can be really slow, so let's give it a big timeout
c.SwarmSpawner.start_timeout = 60 * 15

c.SwarmSpawner.jupyterhub_service_name = 'jupyter-service_jupyterhub'

c.SwarmSpawner.networks = ["jupyter-service_default"]

# The path at which the notebook will start
#notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
#c.DockerSpawner.notebook_dir = notebook_dir

home_dir = "/home/jovyan/work"

#mounts = [{"type": "volume", "source": "", "target": home_dir}]

mounts = [{'type' : 'bind',
        'source' : '/opt/share/{username}',
        'target' : '/home/jovyan/work',}]

# 'args' is the command to run inside the service
c.SwarmSpawner.container_spec = {
    "env": {"JUPYTER_ENABLE_LAB": "1",
    "NOTEBOOK_DIR": home_dir },
    "mounts": mounts,
}

# Before the user can select which image to spawn,
# user_options has to be enabled
c.SwarmSpawner.use_user_options = True

# Available docker images the user can spawn
c.SwarmSpawner.dockerimages = [
    {'image': 'jupyter/base-notebook:latest',
     'name': 'Basic Python Notebook'}
]

# Authenticator, all users can use the default password. Only for dev/test
#c.JupyterHub.authenticator_class = 'jhubauthenticators.DummyAuthenticator'
#c.DummyAuthenticator.password = 'password'

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.admin_users = {'admin'}
