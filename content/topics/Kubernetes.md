#### Setup

| <center>Tool</center> | <center>Installation</center> | <center>Description</center> |
| -------- | -------- | -------- |
| Docker & kubectl | <center><a href="https://docs.docker.com/desktop/install/windows-install/"><img src="https://img.icons8.com/?size=100&id=1349&format=png&color=000000" alt="Docker" width="30" height="30"></a></center>| Docket Desktop is a great way to get a local development cluster on your Mac or Windows laptop. It automatically installs and configures `kubectl` and you get a GUI that simplifies common operations such as switching between kubectl contexts. *Note*: enable Kubernetes in Preferences.|
| K3d| Via brew (macOs) or choco (Windows) | great tool for creating multi-node Kubernetes clusters on your laptop.|
| KinD| Via brew (macOs) or choco (Windows) | great way to create multi-node clusters.|

#### Terminologies

| <center>Term</center> | <center>Description</center> |
| -------- | -------- | 
| Kubernetes (K8s)| it is a cluster to run application on and an orchestrator of cloud-native microservices apps|
| orchestrator| takes care of deploying and managing apps.|
| could-native app| application that meets cloud-like demands of auto-scaling, auto-healing, rolling updates, etc.|
| microservices app| is built from lots of small, specialised, independent parts that work together to form a meaningful application.|
| Pod| the atomic unit of scheduling in K8s, i.e. app always run inside Pods|


#### Workflow

Before deployment:
1. Design and write application as small independent microservices in your favorite languages.
2. Package each microservices as its own container.
3. Wrap each container in a Kubernetes Pod.
4. Deploy Pods to the cluster via higher-level controllers such as Deployments, DaemonSets, StatefulSets, CronJobs etc.

In Kubernetes, a declarative model works like this:
1. Declare the desired state of an application microservice in a manifest file (YAML)
2. Post it to the API server
3. Kubernetes stores it in the cluster store as the application's desired state
4. Kubernetes implement the desired state on the cluster
5. A controller makes sure the observed state of the application doesn't vary from the desired state

#### Code Snippets

| Command | Description |
| -------- | -------- |
| `kubectl get nodes`| See your cluster|
| `kubectl apply -f pod.yml`| Deploy Pods from a manifest file|
| `kubectl get pods --watch`| Watch Pods provisioning|
| `kubectl describe pods hello-pod`| Describe Pod|
| `kubectl logs multipod --container syncer`| Pull logs from the syncer container|
| `kubectl exec hello-pod -- ps`| Run commands in Pods|
| `kubectl delete pod hello-pod`| Delete Pod|
| `k3d cluster create tkb --servers 1 --agents 3 --image rancher/k3s:latest`| Create a 4-node K3d cluster called tkb|
| `k3d cluster list`| See your cluster|
| `kind create cluster --config=kind.yml`| Create a cluster |
| `kind get clusters`| See your cluster|

#### Resources

| <center>Resource</center> | <center>URL</center> |
| -------- | -------- | 
| The K8s Book (Nigel Poulton) | <center><a href="https://github.com/nigelpoulton/TheK8sBook/"><img src="https://img.icons8.com/?size=100&id=YsPdguLCFOMH&format=png&color=000000" alt="GitHub" width="30" height="30"></a></center>|