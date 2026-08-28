## SageMaker

Amazon Web Services Amazon SageMaker is a managed machine learning platform on AWS that helps teams build, train, deploy, and operate ML and AI models without managing most of the underlying infrastructure.

Data
  ↓
Experimentation
  ↓
Training
  ↓
Model Registry
  ↓
Deployment
  ↓
Monitoring

Components:
- SageMaker Studio: Web IDE for ML teams: notebooks, experiments, pipelines
- Training Jobs: Managed distributed training
- Endpoints: Managed inference APIs. realtime inference, async inference, serverless inference
- Pipelines: Preprocess -> Train -> Evaluate -> Register -> Deploy
- Feature Store: Centralized ML features.
- JumpStart: Prebuilt models and templates.

SageMaker Advantages:
- Fully Managed Infrastructure
- AWS Integration
- Enterprise Security

### Training ML Models

Data scientists use Python, PyTorch, Scikit-learn to train ML models (fraud detection, forecasting).
__SageMaker spins up GPU/CPU clusters automatically__.

#### Fine-Tuning LLMs

### Hosting Models Behind APIs

After training: Model → Endpoint → REST API

### Inference: batch or real-time

## MLOps

