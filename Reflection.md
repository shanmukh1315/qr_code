# Reflection on Dockerizing the QR Code Generator Application

Completing this assignment helped me understand how containerization simplifies software deployment and ensures consistent environments across different systems. I learned how Docker encapsulates all dependencies within a lightweight image, allowing the QR Code Generator to run identically on any machine.

The key steps I followed included writing a secure Dockerfile using the python:3.12-slim-bullseye base image, setting up a non-root user (myuser), and creating dedicated folders for logs and generated QR codes. By using a minimal base image and the --no-cache-dir option during package installation, I was able to reduce image size and enhance security.

One of the challenges I faced was during the initial GitHub Actions build, where the requirements.txt contained local Anaconda paths. I resolved this by cleaning it to only include the required dependency qrcode[pil]. This fix allowed the CI workflow to build successfully.

The integration of GitHub Actions taught me the power of automation in DevOps. Every push now triggers a new build that verifies the Docker image, ensuring reliability and reproducibility. Pushing the final image to DockerHub (sc2764/qr-code-generator-app) made the application easily shareable.

Overall, this project improved my understanding of Docker fundamentals, CI/CD pipelines, and cloud-ready deployment strategies. I now feel confident in containerizing and automating the build process for Python-based applications.

## Links

- **GitHub Repository:** [https://github.com/shanmukh1315/qr_code](https://github.com/shanmukh1315/qr_code)
- **DockerHub Image:** [https://hub.docker.com/r/sc2764/qr-code-generator-app](https://hub.docker.com/r/sc2764/qr-code-generator-app)
