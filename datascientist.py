import syft as sy
from syft.grid.private_grid import PrivateGridNetwork
from syft.grid.clients.data_centric_fl_client import DataCentricFLClient
import torch as th
hook = sy.TorchHook(th)
bob = DataCentricFLClient(hook,'http://localhost:3000')
grid = PrivateGridNetwork(bob)
results = grid.search("#February", "#birth-records")
feb_records = results['Bob'][0]

def sum_column(dataset, column):
    sum_result = dataset[0][column].copy()
    for i in range(1, dataset.shape[0]):
        sum_result += dataset[i][column]
    return sum_result

weight_sum = sum_column(feb_records, 1)
avg_weight = weight_sum.get(user='Bob')/5

print(avg_weight)
