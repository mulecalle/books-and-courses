export OPENAI_API_KEY=""

all: init

install:
	 brew install kind && \
 	 brew install kubectl && \
 	 brew install helm && \
 	 brew install kagent

kind-init:
	kind create cluster --wait 5m --name kagent

kagent-install:
	kagent install --profile demo && \
	kagent install --profile demo

kagent-dashboard:
	kagent dashboard

# https://kagent.dev/docs/kagent/supported-providers/ollama
kagent-ollama:
	kubectl create ns ollama
	kubectl apply -f ollama-service.yaml && \
	kubectl apply -f ollama-deployment.yaml && \
	kubectl apply -f ollama-modelConfig.yaml
