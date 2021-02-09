import syft as sy
from syft.grid.clients.data_centric_fl_client import DataCentricFLClient
from syft.grid.clients.model_centric_fl_client import ModelCentricFLClient

import torch as th
hook = sy.TorchHook(th)
bob = "http://bob:5001"
hospital_datacluster = DataCentricFLClient(hook, bob)

data_description = """Description:
                        This data presents the monthly birth records.
                        
                        Columns:
                            Gender: 0 - Male, 1 - Female
                            Weight: in Kg
                            Height: in cm


                        Shape 5 * 3
                        """

monthly_birth_records = th.tensor([[1, 3.5, 47.3],
                                   [0, 3.7, 48.1],
                                   [0, 3.9, 50.0],
                                   [1, 4.1, 52.3],
                                   [0, 4.1, 49.7]
                                  ])

private_dataset = monthly_birth_records.private_tensor(allowed_users = ("Bob", "Ana", "Alice"))
private_dataset = private_dataset.tag("#February", "#birth-records").describe(data_description)
data_pointer = private_dataset.send(hospital_datacluster, user = "Bob")
