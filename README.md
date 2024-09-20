# budget-app
## how to start in Docker
First, build an image
```commandline
docker build --platform linux/amd64 -t budget_app .
```
Next we run an image
```commandline
docker run --platform linux/amd64 --rm -it -p 80:8000 budget_app
```
Use Ngrok as DNS 
```commandline
ngrok http http://localhost:80
```
