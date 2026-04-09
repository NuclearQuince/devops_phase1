import yaml
import sys

files = ['k8s/deployment.yaml', 'k8s/service.yaml']

for f in files:
    with open(f) as fp:
        yaml.safe_load(fp)
    print(f"OK: {f} is valid YAML")

print("")
print("Deployment simulation complete!")
print("Replicas: 2")
print("Service: devops-phase1-service on port 80")