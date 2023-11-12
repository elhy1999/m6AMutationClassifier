# Welcome to `/deployment`!
This guide will cover how you can use our model to make predictions on new datasets. For student testers of DSA4266, you may read **1. Docker** for context. However, only **2. Using AWS EC2** will be relevant to reproduce our model on AWS EC2.

## 1. Docker

A Docker image which contains the trained model has been deployed on Docker Hub [here](https://hub.docker.com/repository/docker/elhy1999/quantrf-bagm6a/general). Hence, while you can build the Docker image using the Dockerfile within this folder,
there isn't a need to as you can pull the image from the public registry. To pull the Docker image and spin off a container called `model_container`, simply start Docker Desktop and run the following command from a Unix or Windows terminal:

```bash
docker run -it --name model_container --entrypoint bash elhy1999/quantrf-bagm6a:latest
```

After running the command, you will be brought into the terminal of the container. Your current working directory is set to `/src/RF/`. **Note that the root directory of the container contains all the files and folders in this `/deployment` directory.**
Within the `/data/raw/` directory, you will find `dataset2.json`. We shall make predictions on this very dataset to demonstrate how predictions can be made. To do that, simply run the following command while you are in the `/src/RF/` directory:

```bash
python3 RF_testing_pipeline.py --test_path ./../../data/raw/dataset2.json
```

Note that `dataset2.json` is the path of the test dataset in the command above. If you wish to make predictions on your own datasets, you may copy other datasets into this Docker container and modify the `--test_path` argument to the path of your custom dataset.

After the command above has finished execution, you should see the path where the predictions have been written to.

## 2. Using AWS EC2

![image](https://github.com/leontanwh/teamrc4dsa/blob/main/resources/EC2%20Pipeline.png)


**This section is particularly relevant for student testers for DSA4266. Please use the Ubuntu 20 04 Large (m6a.large or larger) instance.** A video demonstration of this entire section can be found [here](https://youtu.be/cgdmauyna_s). The YouTube tutorial runs some lines of code on the command line. For your convenience, you can find these commands in the `Commands to Run (for DSA4266 Student Testers).txt` file in this directory!

Since the project will be evaluated using AWS EC2, you will first need to install Docker into your AWS instance. To do this, you can simply copy the `docker_installation.sh` script found within this `/deployment` folder into your EC2 instance using the `scp`
command. An example is given below:

```bash
scp -i 'path/to/pem/file' ./docker_installation.sh ubuntu@XX.XXX.XX.XXX:~/
```

Note that you will have to change `XX.XXX.XX.XXX` to the IP address of your EC2 instance, which you can find here:

![image](https://github.com/leontanwh/teamrc4dsa/blob/main/resources/Research%20Gateway%20SS.png)

After this is completed, `ssh` into your EC2 instance. You should be able to find `docker_installation.sh` in your home directory (`~`). Next, run the following commands:

```bash
sudo apt-get update
sudo apt install dos2unix
dos2unix docker_installation.sh

chmod +x docker_installation.sh # This makes the .sh script into an executable
./docker_installation.sh # This runs the script to install Docker into your EC2 instance
```

Now that we have Docker installed, run the following command to pull our team's Docker image from the public registry:

```bash
sudo docker run -it --name model_container --entrypoint bash elhy1999/quantrf-bagm6a:latest
```

Your terminal should now be within the Docker container. To make predictions on the `dataset2.json` dataset, run:

```bash
python3 RF_testing_pipeline.py --test_path ./../../data/raw/dataset2.json
```

After the command above has finished execution, you should see the path where the predictions have been written to.

## 3. FAQ

**Q: Why are there more `src`, `data`, and `model` folders within this `/deployment` directory?**

A: The `/deployment/src` directory is the folder that is copied into the Docker container, whereas the `/src` directory is the folder that consists of all the scripts we ran, some of which ended up not being used by the final model.

