FROM spanagiotou/eden-sim-jupyter-demo:latest
MAINTAINER Sotirios Panagiotou <spanagiotou@erasmusmc.nl>

WORKDIR $HOME

COPY * ./

CMD ["start-notebook.sh"]
