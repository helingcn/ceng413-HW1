# ANSWERS

## 1. Order of the Dockerfile instructions
Docker builds images in layers and stores each completed layer in the build cache. When a change is made, the modified layer and all subsequent layers are rebuilt, while the previous layers are reused from the cache. In my Dockerfile, I arranged the steps so that the required packages are installed before copying the application files. This way, changes made to `app.py` did not affect the dependency layer, so the packages did not need to be installed again. When I rebuilt the image, the `pip install` step was marked as CACHED, and the build completed in 1.2 seconds. If I had copied the application code before installing the dependencies, even a small change in the code would have caused the packages to be reinstalled, increasing the image build time.

## 2. Data inside a removed container
Data created inside a container is stored in its ephemeral writable layer, which is deleted together with the container, so the data is lost when the container is removed. To prevent data loss, a Docker volume or an external database can be used. Keeping important application data outside the container is a more reliable approach. My application is stateless, meaning it does not store any data in files or a database. The `/time` endpoint calculates the current time for each request, while the `/` endpoint gets its message from an environment variable. Therefore, removing and recreating the container does not cause any data loss.

## 3. Why `latest` is a risk
In Docker, the `latest` tag does not represent a fixed version and can change when new images are released. Therefore, even if the Dockerfile remains unchanged, different images may be used over time, which can cause unexpected issues in the application. This negatively affects reproducibility, which means getting the same results every time the same process is repeated. To avoid these problems, I pinned the base image to `python:3.12-slim` and pinned the dependency version (`flask==3.1.2`) in the `requirements.txt` file. I also tagged my own Docker image as `ceng413-app:1.0` instead of using `latest`. This makes version tracking easier and helps create a more consistent and predictable environment.

## Use of AI assistant
I used an AI assistant to explain Docker concepts and to help me write the app code, Dockerfile and README. I wrote the answers in this file myself and the assistant reviewed them.
