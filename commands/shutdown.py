import click
import os

# from .env import PASSWD

@click.command()
def shutdown():
    '''Command to shut down your PC'''
    if os.name == 'nt':
        # Shutdown the Windows system in 5 seconds
        os.system('shutdown /s /t 5')
    if os.name == 'posix':
        # Shutdown the Linux system immediately
        os.system('sudo systemctl poweroff')
        # os.system(PASSWD)

@click.command()
def hibernate():
    if os.name == 'nt':
        # Hibernate the Windows system
        os.system('shutdown /h')
    if os.name == 'posix':
        pass

@click.command()
def restart():
    if os.name == 'nt':
        # Restart the Windows system
        os.system('shutdown /r')
    if os.name == 'posix':
        pass

@click.command()
@click.option('--process', prompt='PID:', help='Process to be killed')
def taskkill(pid):
    if os.name == 'nt':
        # Restart the Windows system
        os.system('taskkill /pid %d' % pid)
    if os.name == 'posix':
        pass
    