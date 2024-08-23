import torch
import torch.nn.functional

def harmless(x: torch.Tensor) -> torch.Tensor:
    return x