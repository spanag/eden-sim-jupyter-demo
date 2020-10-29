FROM spanagiotou/eden-sim-jupyter-demo:latest
MAINTAINER Sotirios Panagiotou <spanagiotou@erasmusmc.nl>

WORKDIR $WORK_HOME

#  so NB_USER can edit them
COPY --chown=${NB_USER}:users ./ $WORK_HOME


CMD ["start-notebook.sh"]
