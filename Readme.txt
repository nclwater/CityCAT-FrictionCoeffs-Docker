git clone https://github.com/nclwater/CityCAT-FrictionCoeffs
cmd
docker build -t friction-coeffs .
Run container in Docker Desktop. In Images find friction-coeffs. Click on the play button. Then "optional settings" and call "Container name" something like "friction-coeffs"
A new Container called "fraction-coeffs" is produced.

The Dockerfile spefies that this reads everything into the /apt folder in the container. then python script.py is run.

The output is in the Docker container. to view output copy it to a local path
docker cp friction-coeffs:/app/FrictionCoeffs.txt ./FrictionCoeffs.txt


https://docs.docker.com/guides/walkthroughs/run-a-container/
https://docs.docker.com/reference/cli/docker/container/cp/
