# upgrade-example
An API Endpoint and test application that can be upgraded live

## How to build Docker Image

***NOTE Docker is a depencency***

1. From the root of the repo run the following command.

```shell
docker build -f dockerfiles/api.Dockerfile -t pwalters1122/simple-flask-api:v1 .
```

Replace 'pwalters1122/simple-flask-api' with the name of the image that you want to create. Also, replace 'v1' with whatever tag you want to put on the image, it's best to create a new image every time to avoid overwriting an unprotected previous image.

2. To push the image run the following command.

```shell
docker push pwalters1122/simple-flask-api:v1
```

Remember to change the image name to whatever you built.

## To Test Endpoint

1. Start all the Kubernetes services using.

```shell
kubectl apply -R -f manifests
```

2. Make sure the services start using.

```shell
kubectl get all
```

One the deployment pods state is running you can move into the next step.

3. Start a test

```shell
python python/client.py --url http://localhost:31000/ --sec 600000
```

Pass your URL, I found 600000 seconds to be more than enough. Once you are receiving responses. Change the [api.yml](./manifests/api.yaml) image from 'pwalters1122/simple-flask-api:v1' to 'pwalters1122/simple-flask-api:v2' and then run the following command.

```shell
kubectl apply -R -f manifests
```

This will deploy the new version of the service. This will deploy the new endpoint, it will attempt to spin up a new pod and then internally switch the service endpoint over to it only after the new pod is successfully up and running.