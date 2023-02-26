# ObjectDetection-training
1. Download my docker image from dockerhub: docker pull hitenderoswal/tensorflow
2. Run the following command in cmd to run the container: docker run -i -t -p 8888:8888 --gpus all tensorflow
  2a. Optionally, if the docker vm is using too much memory, you can limit memory to 8gb and give it memory swap: docker run -i -t -p 8888:8888 --gpus all -m 8000000000 --memory-swap -1 tensorflow
3. Open the jupyter notebook using the link provided by docker. If it does not work, go to localhost:8888. If it asks for a password, enter the token from the end of the link to the jupyter notebook that commandline provided.
4. Open TFtraining and go to the cell that says "START HERE"
5. Run the cell
6. Run the next cell to start the training
7. Wait for error
