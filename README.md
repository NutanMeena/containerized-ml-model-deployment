## 🧠 Model Description

- A simple **TensorFlow regression model**
- Trained using `train_model.py`
- Saved as `my_model.h5`
- Loaded during inference inside the Docker container

---

## 🐳 Run with Docker

### 🔹 Build Docker Image
```bash
docker build -t tensorflow-model .
🔹 Run Container
docker run tensorflow-model
🐳 Run with Docker Compose
docker compose up --build
🔗 API available at:
http://localhost:8000
🔌 API Usage
🔹 Health Check
GET /
🔹 Prediction Endpoint
POST /predict
📥 Sample Request Body
{
  "input": 10
}
📤 Sample Response
{
  "prediction": 13.55
}
☸️ Run with Kubernetes
🔹 Apply Kubernetes Manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
🔹 Check Service Status
kubectl get svc
