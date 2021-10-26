"""
when the arrival task is fix. For example, the total number of requests is 100.
This function is used to measure the total execution time with different batching size.
"""
import torch
from torchvision import models
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

total_num_request = 100
max_batch_size = 10

model_name = ["None", "ResNet34", "VGG16", "AlexNet"]


def measure(model_id):
    net = None
    if model_id == 1:
        net = models.resnet34()
    elif model_id == 2:
        net = models.vgg16()
    elif model_id == 3:
        net = models.alexnet()
    if net is None:
        print("error model id...........")
        return
    measure_time = []

    for batch_size in range(1, max_batch_size+1):
        queue_list = []
        for _ in range(batch_size, total_num_request, batch_size):
            queue_list.append(batch_size)
        if sum(queue_list) != total_num_request:
            queue_list.append(total_num_request - sum(queue_list))
        start_time = time.time()
        for ele in tqdm(queue_list, desc="batch_size: {}".format(batch_size)):
            x = torch.randn((ele, 3, 224, 224))
            net(x)
        end_time = time.time()
        measure_time.append(end_time-start_time)

    plt.plot(measure_time)
    plt.show()
    print("measure_time: ", measure_time)
    with open("batch_time_with_input.txt", "a+") as f:
        f.write("{}, total_request_num={}, batching_time={}\n".format(model_name[model_id], total_num_request, measure_time))

if __name__ == "__main__":
    for model_id in range(1, len(model_name)+1):
        measure(model_id)