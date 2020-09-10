FROM python 
#
ADD ./bin/calc_401k_contrib.py /usr/bin/
RUN chmod +x /usr/bin/calc_401k_contrib.py
#
## ADD ./bin/run-calc_401k_contrib.py /usr/bin/run-calc_401k_contrib.py
## RUN chmod +x /usr/bin/run-calc_401k_contrib.py
#
CMD ["/usr/bin/calc_401k_contrib.py"]
