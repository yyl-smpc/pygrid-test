from syft.grid.public_grid import PublicGridNetwork
import torch as th
hook = sy.TorchHook(th)
grid_address = "http://network:7000"
grid = PublicGridNetwork(hook, grid_address)
results = grid.search("#February", "#birth-records")
def sum_column(dataset, column):
    sum_result = dataset[0][column].copy()
    for i in range(1, dataset.shape[0]):
        sum_result += dataset[i][column]
    return sum_result

weight_sum = sum_column(feb_records, 1)
avg_weight = weight_sum.get(user='Bob')/5

print(weight_sum,avg_weight)
