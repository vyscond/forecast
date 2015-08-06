import os, re , yaml
from subprocess import call, check_call, CalledProcessError
from sys import argv
import forecast.log

FORECASTS_FOLDER = os.getcwd() + '/.forecasts'

def create_file(tag,content=''):
    path=os.cmd()
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path),exist_ok=True)
    f = open(path,'w')
    f.write(content)
    f.close()

def gen():
    
    if len(argv) == 3: # file provided
        filename = argv[2]
    else :
        print('using default forecasts.yaml')
        filename = 'forecast.yaml'
        #print("dude! it's: \"forecast read filename\" not \"forecast read\"")

    if os.path.isfile(filename):

        procfile = yaml.safe_load(open(filename))

        if not os.path.exists(FORECASTS_FOLDER):
            os.makedirs(FORECASTS_FOLDER,exist_ok=True)

        for tag in procfile.keys():
            print('building [{0}]'.format(tag))
            f = open(FORECASTS_FOLDER + '/'+tag+'.sh','w')
            f.write(procfile[tag]+'\n')
            f.close()

    else :
        print('no custom file was provided and default forecast.yaml is missing too! nothing to do :(')

def run():
    forecasts_folder = os.path.join(os.getcwd() , '.forecasts')
    if len(argv) == 2: # file provided
        forecastscript = os.path.join(FORECASTS_FOLDER,argv[1]+'.sh')
        if os.path.isfile(forecastscript):
            try :
                check_call(['sh',forecastscript] , env=os.environ.copy())
            except KeyboardInterrupt:
                log.error('quit process')
            except CalledProcessError :
                log.error('something bad happened')
    else :
        pass
def main():
    if len(argv) > 1 :
        if argv[1] in globals().keys() :
            globals()[argv[1]]()
        else :
            run()
    else :
        log.debug('[available commands]') 
        print( '\n'.join(os.listdir(FORECASTS_FOLDER)) ) 
