Pascal Triangle,docker,minikube

helm install airflow apache-airflow/airflow \
--debug \
--namespace airflow \
--create-namespace \
--set dags.gitSync.enabled=true \
--set dags.gitSync.repo=https://github.com/Michael-Bokov/airflow_trianglepascal.git \
--set dags.gitSync.branch=main \
--set dags.gitSync.subPath="/"

kubectl port-forward svc/airflow-webserver 8888:8080 --namespace airflow
