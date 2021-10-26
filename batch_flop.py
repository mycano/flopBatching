"""
This file is used to masure the flop with different batching size.
In the experiment, we can know that it is a linear function between batching size and flop.
"""
import torch
from torchvision import models
from thop import profile
import math
import matplotlib.pyplot as plt


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

    FLOPS_BATCH = []
    for i in range(1, 20):
        inputs = torch.randn(i, 3, 224, 224)
        flops, _ = profile(net, inputs=(inputs, ))
        FLOPS_BATCH.append(flops / math.pow(10, 6))
    print(FLOPS_BATCH)

    plt.plot(FLOPS_BATCH)
    plt.show()

    with open("batch_flop.txt", "a+") as f:
        f.write("{} flop in different batches: {}\n".format(model_name[model_id], FLOPS_BATCH))

if __name__ == "__main__":
    for model_id in range(1, len(model_name)+1):
        measure(model_id)