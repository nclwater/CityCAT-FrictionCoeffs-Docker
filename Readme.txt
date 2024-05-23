git clone https://github.com/nclwater/CityCAT-FrictionCoeffs
cmd
docker build -t friction-coeffs .
Run container in Docker Desktop. In Images find friction-coeffs. Click on the play button. Then "optional settings" and call "Container name" something like "friction-coeffs"
A new Container called "fraction-coeffs" is produced.
*** not needed as default **** Enivonment Variables DATA_PATH /data

The Dockerfile spefies that this reads script.py into the src folder and the data into the /data folder in the container. then python script.py is run.

The output is in the Docker container. to view output copy it to a local path
docker cp friction-coeffs:/data/outputs/FrictionCoeffs.txt ./FrictionCoeffs.txt


https://docs.docker.com/guides/walkthroughs/run-a-container/
https://docs.docker.com/reference/cli/docker/container/cp/


docker save -o friction-coeffs.tar friction-coeffs
compress friction-coeffs.tar to friction-coeffs.tar/gz using 7Zip add to achive


set DATA_PATH = 'C:\Users\steve\Documents\citycat\CityCAT-FrictionCoeffs-Docker'

docker system prune -a