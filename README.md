# ObjectDetection-training
1. Download my docker image from dockerhub

   1a. docker pull hitenderoswal/tensorflow:latest if you want to train  
   1b. docker pull hitenderoswal/tensorflow:100ktrained if you want to continue training my 100k step model  
   1c. docker pull hitenderoswal/tensorflow:100kdeploy if you want to deploy the 100k model

2. Run the following command in cmd to run the container: 

   2a. docker run -i -t -p 8888:8888 --gpus all {name of image your downloaded}  
   2b. Optionally, if the docker vm is using too much memory, you can limit memory to 8gb and give it memory swap:  
   docker run -i -t -p 8888:8888 --gpus all -m 8000000000 --memory-swap -1 {name of image your downloaded}

3. Open the jupyter notebook using the link provided by docker. If it does not work, go to localhost:8888. If it asks for a password, enter the token from the end of the link to the jupyter notebook that commandline provided.

   4a. If you want to train, open TFtraining and start at the cell that says "START HERE"  
   4b. If you want to deploy, open TFDeploy and start from the first cell 
