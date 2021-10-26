# Introduction
This project is used to measure the flop and running time with different batching sizes.
Then, this project contains two python files, their function is as follows,
* batch_flop.py: This file is used to measure the flops with the change of batching sizes. In experiment, it is shown that flops is proportional to batching size.
* batch_with_input.py: This file is used to measure the total running time with the change of batching size when the number of requests is given. In the experiment, we set "total_num_request = 100", which means there are total 100 requests that needs to be executed.
# How to use?
Please use the following command with pip.
```python
pip install -r requirements.txt
```