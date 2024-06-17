#### Code Snippets

| Command | Description |
| -------- | -------- |
| `docker pull NAME[:TAG]`| Pull image from container registry DockerHub to local with NAME is the image name.|
| `docker push NAME[:TAG]`| Push image from local to container registry DockerHub with NAME is the image name.|
| `docker build NAME[:TAG] PATH`| Build the image with Dockerfile can be found in `PATH`.|
| `docker tag SOURCE_IMAGE[:TAG] TARGET_IAMGE[:TAG]`| Commit or "rename" the existing image with container registry before you push it.|
| `docker run -it --rm NAME[:TAG]`| Execute the container and enter its terminal. Container to be removed right after the session ends.|
| `docker run -it --rm -v MOUNTED_HOST_DIR NAME[:TAG]`| Execute the container and enter its terminal. Container to be removed right after the session ends. Bind mount a volumn to host so data change to be saved.|
| `docker run -it CONTAINER-ID`| Execute the container and have it running in the back ground.|
| `docker images`| List out images in the local.|
| `docker ps`| List out running containers in the local.|

#### Resources

| <center>Resource</center> | <center>URL</center> |
| -------- | -------- |
| docker-ds-training | <center><a href="https://github.com/hovinh/docker-ds-training"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="30" height="30"></a></center>|