FROM spanagiotou/eden-sim-jupyter-demo:latest
MAINTAINER Sotirios Panagiotou <spanagiotou@erasmusmc.nl>

WORKDIR $WORK_HOME

COPY ./ $WORK_HOME

CMD ["start-notebook.sh"]
