# python-ci-cd-docker

## Continuous Delivery (Concept)

The CI pipeline produces immutable Docker images tagged with the commit SHA.

In production:
- ECS: a new task definition references the new image tag
- EKS: the Deployment image is updated

Rollback is achieved by redeploying the previous known-good image.