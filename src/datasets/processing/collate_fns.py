import torch
import numpy as np

class DBNetCollateFN:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, batch):
        data_dict = {}
        to_tensor_keys = []
        
        for sample in batch:
            for k, v in sample.items():
                if k not in data_dict:
                    data_dict[k] = []
                    
                if isinstance(v, (np.ndarray, torch.Tensor)):
                    if k not in to_tensor_keys:
                        to_tensor_keys.append(k)

                data_dict[k].append(v)
                
        for k in to_tensor_keys:
            data_dict[k] = torch.stack(data_dict[k], 0)
            
        return data_dict